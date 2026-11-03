export default {
 async fetch(request, env) {
  const url = new URL(request.url);
  if (url.pathname === "/api/mentor") {
   const headers = {"Content-Type":"application/json; charset=utf-8","Cache-Control":"no-store"};
   const reply = (data,status=200) => new Response(JSON.stringify(data),{status,headers});
   if (request.method !== "POST") return reply({error:"Method not allowed."},405);
   if (!env.GEMINI_API_KEY) return reply({error:"The AI Mentor is not configured yet. Please check the GEMINI_API_KEY secret in Cloudflare."},503);
   try {
    const body = await request.json();
    const question = String(body.question || "").trim().slice(0,1200);
    const language = body.language === "pa" ? "Punjabi" : "English";
    if (!question) return reply({error:"A question is required."},400);

    const systemPrompt = "You are SEHAT SAATHI, a health-awareness educator for students and families. Reply in simple " + language + ". Answer directly in 40–70 words. Use short sentences. Cover general health, hygiene, sanitation, nutrition and healthy habits only. Do not diagnose, prescribe medicines, or give supplement doses. For personal symptoms or treatment decisions, recommend a qualified healthcare professional; for emergencies, advise local emergency services. Never request identifying or private medical information. If off-topic, politely redirect to health awareness.";

    // One fast, non-reasoning model. Stream tokens immediately; avoid serial fallback waits.
    const upstream = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:streamGenerateContent?alt=sse", {
      method:"POST",
      headers:{"Content-Type":"application/json","x-goog-api-key":env.GEMINI_API_KEY},
      body:JSON.stringify({
        systemInstruction:{parts:[{text:systemPrompt}]},
        contents:[{role:"user",parts:[{text:question}]}],
        generationConfig:{temperature:0.2,maxOutputTokens:220}
      })
    });

    if (!upstream.ok) {
      let detail={};
      try { detail=await upstream.json(); } catch (_) {}
      const status=upstream.status;
      const message=detail && detail.error && detail.error.message ? String(detail.error.message).slice(0,400) : "";
      const friendly=status===401 || status===403 ? "Gemini rejected the API key. Please check the Cloudflare GEMINI_API_KEY secret. " + message
        : status===429 ? "The AI Mentor is busy or the API limit was reached. Please try again shortly. " + message
        : status===404 ? "The selected Gemini model is unavailable for this API key. " + message
        : status===503 ? "Gemini is temporarily busy. Please try again shortly. " + message
        : "Gemini service error (HTTP " + status + "). " + message;
      return reply({error:friendly},502);
    }

    return new Response(upstream.body,{
      status:200,
      headers:{
        "Content-Type":"text/event-stream; charset=utf-8",
        "Cache-Control":"no-cache, no-transform",
        "X-Accel-Buffering":"no"
      }
    });
   } catch (e) {
    return reply({error:"Could not process the question. Please try again."},502);
   }
  }
  return env.ASSETS.fetch(request);
 }
};
