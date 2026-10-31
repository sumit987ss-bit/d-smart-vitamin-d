# SEHAT SAATHI – branded installable web app

This folder contains a Progressive Web App (PWA) shell with its own name, icon, manifest and standalone display mode. It embeds the current SEHAT SAATHI Streamlit application so the existing bilingual learning sections and configured AI Mentor remain available while the frontend migration is staged.

## Important architecture note

This first stage is a branded installable shell, **not yet a full removal of Streamlit**. The embedded learning app still runs at the Streamlit URL and needs internet access. A complete migration requires porting the existing Python features, session state, quiz logic and Gemini integration into a new web backend/frontend and testing them feature by feature.

## Publish using GitHub Pages

1. Open the repository settings on GitHub.
2. Go to **Pages** and choose **GitHub Actions** as the build/deployment source.
3. The workflow in `.github/workflows/deploy-pwa.yml` publishes this folder.
4. After the workflow succeeds, the PWA URL will be `https://sumit987ss-bit.github.io/d-smart-vitamin-d/` if Pages is enabled for this repository.
5. Open that URL in Chrome on Android, use the browser menu, then choose **Install app** or **Add to Home screen**. The exact wording depends on the browser version.

## Checks

- App name: SEHAT SAATHI – ਸਿਹਤ ਸਾਥੀ
- Short name: SEHAT SAATHI
- Icon: `icon.svg`
- Display: standalone
- Online/offline status shown in the shell
- The Streamlit iframe is deliberately not cached; the learning app and AI Mentor require internet.

If the app is published under a custom domain or a different Pages base path, update `start_url`, `scope`, and asset paths in `manifest.json` accordingly.