export default {
 async fetch(request, env) {
  const url = new URL(request.url);
  if (url.pathname === "/api/mentor") {
   const headers = {"Content-Type":"application/json; charset=utf-8","Cache-Control":"no-store"};
   const reply = (data,status=200) => new Response(JSON.stringify(data),{status,headers});
   if (request.method !== "POST") return reply({error:"Method not allowed."},405);
   if (!env.GEMINI_API_KEY) return reply({error:"The AI Mentor is not configured yet."},503);
   try {
    const body = await request.json();
    const question = String(body.question || "").trim().slice(0,1200);
    const language = body.language === "pa" ? "Punjabi" : "English";
    if (!question) return reply({error:"A question is required."},400);
    const prompt = "You are SEHAT SAATHI, a careful health, hygiene and sanitation education mentor for students and families. Answer in " + language + " using simple, respectful language. Give general educational information only; do not diagnose or prescribe medication. For personal symptoms, encourage consulting a qualified healthcare professional. For possible emergencies, advise contacting local emergency services. Do not ask for identifying details. If a question is unrelated to health, hygiene, sanitation or healthy habits, politely redirect. Question: " + question;
    const endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + encodeURIComponent(env.GEMINI_API_KEY);
    const response = await fetch(endpoint, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({contents:[{parts:[{text:prompt}]}],generationConfig:{temperature:0.35,maxOutputTokens:700}})
    });
    if (!response.ok) {
     let detail = {};
     try { detail = await response.json(); } catch (_) {}
     const status = response.status;
     const message = status === 400 ? "Gemini rejected the request. Check the model or request settings."
       : status === 401 || status === 403 ? "Gemini rejected the API key or the key does not have API access. Check Google AI Studio key restrictions and API access."
       : status === 404 ? "The configured Gemini model was not found or is unavailable for this key."
       : status === 429 ? "Gemini quota or rate limit reached. Check the Google AI Studio project quota."
       : "Gemini service error (HTTP " + status + "). Please check the Google AI Studio project and try again.";
     return reply({error:message},502);
    }
    const data = await response.json();
    const answer = (data.candidates || []).flatMap(c => c.content && c.content.parts ? c.content.parts : []).map(p => p.text || "").join("\n").trim();
    return answer ? reply({answer}) : reply({error:"No answer was returned. Please try again."},502);
   } catch (e) {
    return reply({error:"Could not process the question."},400);
   }
  }
  return env.ASSETS.fetch(request);
 }
};
