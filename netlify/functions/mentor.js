exports.handler = async function (event) {
  const headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS"
  };
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers, body: "" };
  if (event.httpMethod !== "POST") return { statusCode: 405, headers, body: JSON.stringify({ error: "Method not allowed" }) };
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) return { statusCode: 503, headers, body: JSON.stringify({ error: "Mentor is not configured yet." }) };
  try {
    const body = JSON.parse(event.body || "{}");
    const question = String(body.question || "").trim().slice(0, 1200);
    const language = body.language === "pa" ? "Punjabi" : "English";
    if (!question) return { statusCode: 400, headers, body: JSON.stringify({ error: "A question is required." }) };
    const prompt = [
      "You are SEHAT SAATHI, a careful health, hygiene and sanitation education mentor for students and families.",
      "Answer in " + language + ". Use simple, respectful language and concise bullet points where useful.",
      "Give general educational information only. Never diagnose, prescribe medication, recommend high-dose supplements, or claim certainty without evidence.",
      "For personal symptoms, encourage speaking to a qualified healthcare professional. For possible emergency symptoms, advise contacting local emergency services immediately.",
      "Do not ask for identifying details. If the question is unrelated to health, hygiene, sanitation or healthy habits, politely guide it back to those topics.",
      "Question: " + question
    ].join("\n\n");
    const response = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + encodeURIComponent(apiKey), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }],
        generationConfig: { temperature: 0.35, maxOutputTokens: 700 },
        safetySettings: [
          { category: "HARM_CATEGORY_HARASSMENT", threshold: "BLOCK_MEDIUM_AND_ABOVE" },
          { category: "HARM_CATEGORY_HATE_SPEECH", threshold: "BLOCK_MEDIUM_AND_ABOVE" },
          { category: "HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold: "BLOCK_MEDIUM_AND_ABOVE" },
          { category: "HARM_CATEGORY_DANGEROUS_CONTENT", threshold: "BLOCK_MEDIUM_AND_ABOVE" }
        ]
      })
    });
    if (!response.ok) {
      return { statusCode: 502, headers, body: JSON.stringify({ error: "The mentor service is temporarily unavailable." }) };
    }
    const data = await response.json();
    const answer = (data.candidates || []).flatMap(c => c.content && c.content.parts ? c.content.parts : []).map(p => p.text || "").join("\n").trim();
    if (!answer) return { statusCode: 502, headers, body: JSON.stringify({ error: "No answer was returned. Please try again." }) };
    return { statusCode: 200, headers, body: JSON.stringify({ answer }) };
  } catch (error) {
    return { statusCode: 400, headers, body: JSON.stringify({ error: "Could not process the question." }) };
  }
};