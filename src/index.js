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

    // Short, direct instructions reduce input overhead and keep answers useful on mobile.
    const prompt = "You are SEHAT SAATHI, a health-awareness educator for students and families. Reply in simple " + language + ". Answer the exact question directly in about 60–100 words, using short bullets when helpful. Cover general health, hygiene, sanitation, nutrition and healthy habits only. Do not diagnose, prescribe medicines, or give supplement doses. For personal symptoms or treatment decisions, recommend a qualified healthcare professional; for emergencies, advise local emergency services. Never request identifying or private medical information. If off-topic, politely redirect to health awareness.";

    // Start with the lightweight model and minimal reasoning for routine health-awareness Q&A.
    // Fall back only on temporary overload; never retry invalid keys or quota errors.
    const models = [
      {name:"gemini-3.5-flash-lite",thinking:"minimal"},
      {name:"gemini-3.6-flash",thinking:"low"},
      {name:"gemini-3.8-flash",thinking:"low"}
    ];
    let response = null;
    let lastOverloadMessage = "";
    for (let i = 0; i < models.length; i++) {
      response = await fetch("https://generativelanguage.googleapis.com/v1beta/interactions", {
        method: "POST",
        headers: {"Content-Type":"application/json","x-goog-api-key":env.GEMINI_API_KEY},
        body: JSON.stringify({
          model:models[i].name,
          input:"Question: " + question,
          system_instruction:prompt,
          generation_config:{thinking_level:models[i].thinking},
          store:false
        })
      });
      if (response.ok) break;
      if (response.status !== 503) break;
      let detail = {};
      try { detail = await response.clone().json(); } catch (_) {}
      lastOverloadMessage = detail && detail.error && detail.error.message ? String(detail.error.message).slice(0,350) : "Gemini is temporarily overloaded.";
    }
    if (!response || !response.ok) {
     let detail = {};
     try { detail = await response.json(); } catch (_) {}
     const status = response ? response.status : 503;
     const googleMessage = detail && detail.error && detail.error.message ? String(detail.error.message).slice(0,500) : "";
     const message = status === 400 ? "Gemini rejected the request. " + googleMessage
       : status === 401 || status === 403 ? "Gemini rejected the API key or this key does not have API access. Check the Cloudflare GEMINI_API_KEY secret. " + googleMessage
       : status === 404 ? "Gemini model or Interactions API was not found. Confirm that this API is available for your key. " + googleMessage
       : status === 429 ? "Gemini quota or rate limit reached. Please try again later. " + googleMessage
       : status === 503 ? "Gemini is temporarily overloaded across the available models. Please try again shortly. " + (googleMessage || lastOverloadMessage)
       : "Gemini service error (HTTP " + status + "). " + googleMessage;
     return reply({error:message},502);
    }
    const data = await response.json();
    const answerFromSteps = (data.steps || [])
      .filter(step => step && step.type === "model_output" && Array.isArray(step.content))
      .flatMap(step => step.content)
      .filter(part => part && part.type === "text")
      .map(part => part.text || "")
      .join("\n").trim();
    const answer = String(data.output_text || answerFromSteps || "").trim();
    // Some interactions can be marked incomplete if a generation limit is reached.
    // Return any usable text instead of making the student press Send repeatedly.
    if (answer) return reply({answer});
    if (data.status === "failed" || data.status === "cancelled") {
      return reply({error:"The AI Mentor could not complete this answer. Please try once more."},502);
    }
    return reply({error:"The AI Mentor returned no text this time. Please try once more."},502);
   } catch (e) {
    return reply({error:"Could not process the question. Please try again."},502);
   }
  }
  return env.ASSETS.fetch(request);
 }
};
