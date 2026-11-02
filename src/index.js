export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/mentor") {
      return new Response(JSON.stringify({ error: "The mentor service is being configured." }), {
        status: 503,
        headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" }
      });
    }
    return env.ASSETS.fetch(request);
  }
};
