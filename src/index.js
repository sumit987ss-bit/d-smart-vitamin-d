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
    const prompt = "You are SEHAT SAATHI, a careful health, hygiene and sanitation education mentor for students and families. Answer in " + language + " using simple, respectful language. Keep the answer clear and practical. Give general educational information only; do not diagnose, prescribe medicines, or recommend supplement doses. For personal symptoms or treatment decisions, encourage consulting a qualified healthcare professional. For possible emergencies, advise contacting local emergency services immediately. Do not ask for identifying details. Do not request names, addresses, phone numbers, or private medical records. If a question is unrelated to health, hygiene, sanitation or healthy habits, politely redirect to those topics. Question: " + question;
    // Try the preferred model first, then fall back on temporary overload (503) only.
    // Do not silently fall back for invalid keys, permissions, malformed requests, or quota errors.
    const models = ["gemini-3.8-flash","gemini-3.6-flash","gemini-3.5-flash-lite"];
    let response = null;
    let lastOverloadMessage = "";
    for (let i = 0; i < models.length; i++) {
      const makeRequest = () => fetch("https://generativelanguage.googleapis.com/v1beta/interactions", {
        method: "POST",
        headers: {"Content-Type":"application/json","x-goog-api-key":env.GEMINI_API_KEY},
        body: JSON.stringify({model:models[i],input:prompt,store:false})
      });
      response = await makeRequest();
      if (response.ok) break;
      if (response.status !== 503) break;
      let detail = {};
      try { detail = await response.clone().json(); } catch (_) {}
      lastOverloadMessage = detail && detail.error && detail.error.message ? String(detail.error.message).slice(0,350) : "Gemini is temporarily overloaded.";
      if (i < models.length - 1) await new Promise(resolve => setTimeout(resolve, 700));
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
       : status === 503 ? "Gemini is temporarily overloaded across the available fallback models. Please try again shortly. " + (googleMessage || lastOverloadMessage)
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
    if (data.status && data.status !== "completed") {
      return reply({error:"The AI Mentor did not finish the response. Please try again."},502);
    }
    return answer ? reply({answer}) : reply({error:"Gemini returned no text answer. Please try again."},502);
   } catch (e) {
    return reply({error:"Could not process the question. Please try again."},400);
   }
  }
  return env.ASSETS.fetch(request);
 }
};
