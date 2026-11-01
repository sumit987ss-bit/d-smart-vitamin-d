# SEHAT SAATHI – independent bilingual health-learning app

This folder contains the standalone SEHAT SAATHI Progressive Web App (PWA). The current frontend is a native HTML/CSS/JavaScript app; it does **not** embed Streamlit and does not load the old Streamlit URL in an iframe.

## Features
- English and Punjabi interface
- Health basics, hygiene, sanitation and healthy habits
- Knowledge quiz with feedback and score
- Daily community challenge saved on the device
- Installable mobile-friendly interface and offline shell caching
- AI Health Mentor interface designed to use a secure server-side Gemini key

## Important: AI Mentor hosting
The frontend calls `/.netlify/functions/mentor`. Therefore, the AI Mentor works only when this repository is deployed to **Netlify** (or the frontend endpoint is changed to another compatible secure backend). GitHub Pages serves the static interface but does not run the Netlify function. On GitHub Pages, the rest of the learning app can work, but the AI Mentor will show a setup/unavailable message.

## Deploy the complete app with AI Mentor on Netlify
1. Open the official Netlify website: https://app.netlify.com/
2. Sign in and choose **Add new project → Import an existing project**.
3. Connect GitHub and select `sumit987ss-bit/d-smart-vitamin-d`, branch `main`.
4. Netlify should detect the committed `netlify.toml`. Confirm the publish directory is `pwa` and the functions directory is `netlify/functions`.
5. In the Netlify site dashboard, open **Site configuration → Environment variables** (menu wording may vary) and add:
   - Key: `GEMINI_API_KEY`
   - Value: your Gemini API key
   Never place the key in this repository, the frontend HTML, or a public message.
6. Trigger a deploy. Open the Netlify site URL and test the AI Mentor with both English and Punjabi questions.

## GitHub Pages preview
The independent frontend can also be previewed at:
https://sumit987ss-bit.github.io/d-smart-vitamin-d/

GitHub Pages does not execute `netlify/functions/mentor.js`; use the Netlify URL for the full app including AI.

## Install on Android
Open the deployed site in Chrome, open the browser menu, then select **Install app** or **Add to Home screen**. Exact wording depends on the browser.

## Safety and migration
- The Gemini key is read only from the backend environment variable.
- The mentor provides general educational information, not diagnosis or treatment.
- The original `app.py` is retained as a fallback while the independent app is tested.
- Do not retire the old app until the new deployment and mentor are verified end to end.
