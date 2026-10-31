import streamlit as st
st.set_page_config(
    page_title="SEHAT SAATHI | ਸਿਹਤ ਸਾਥੀ",
    page_icon="☀️",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        180deg, #eaf7ff 0%, #ffffff 55%, #f0fff4 100%
    );
}

.block-container {
    max-width: 800px;
    padding-top: 5.5rem !important;
    padding-bottom: 3rem;
}

h1 {
    color: #087f8c !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #176b5b !important;
}

.stButton > button {
    background: linear-gradient(
        90deg, #087f8c, #16a085
    );
    color: white;
    border: none;
    border-radius: 14px;
    min-height: 48px;
    font-weight: 700;
    width: 100%;
}

.stButton > button:hover {
    border: 2px solid #087f8c;
    color: #087f8c;
}

div[data-testid="stAlert"] {
    border-radius: 14px;
}

div[data-testid="stExpander"] {
    border-radius: 12px;
    border: 1px solid #cce8e4;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
language = st.selectbox(
    "Choose Language / ਭਾਸ਼ਾ ਚੁਣੋ",
    ["English", "ਪੰਜਾਬੀ"]
)

pa = language == "ਪੰਜਾਬੀ"

if pa:
    title = "ਸਿਹਤ, ਸਫ਼ਾਈ ਅਤੇ ਸੈਨਿਟੇਸ਼ਨ ਸਹਾਇਕ"
    intro = "ਸਿਹਤ, ਸਫ਼ਾਈ, ਸੈਨਿਟੇਸ਼ਨ ਅਤੇ ਚੰਗੀਆਂ ਆਦਤਾਂ ਰਾਹੀਂ ਤੰਦਰੁਸਤ ਭਾਰਤ ਵੱਲ ਕਦਮ ਵਧਾਓ।"
    notice = "ਇਹ ਸਿੱਖਿਆ ਲਈ ਹੈ। ਇਹ ਡਾਕਟਰੀ ਜਾਂਚ ਜਾਂ ਪੇਸ਼ੇਵਰ ਸਿਹਤ ਸਲਾਹ ਦਾ ਬਦਲ ਨਹੀਂ ਹੈ।"
else:
    title = "Smart Health, Hygiene & Sanitation"
    intro = "Explore health, hygiene, sanitation and healthy habits for a stronger, healthier India."
    notice = "This is an educational platform. It does not replace professional healthcare advice."

# ---------- MOBILE SCREEN NAVIGATION ----------
# Screen navigation preserves the existing feature code below.
ds_pages = ["Welcome", "Home", "About", "AI Assistant", "Hygiene", "Sanitation", "Healthy Habits", "Community Challenge", "Health"]

if "ds_page" not in st.session_state:
    st.session_state.ds_page = 0
if "ds_nav" not in st.session_state:
    st.session_state.ds_nav = ds_pages[0]

def _ds_sync_nav():
    st.session_state.ds_page = ds_pages.index(st.session_state.ds_nav)

def _ds_move_page(delta):
    new_page = max(0, min(len(ds_pages) - 1, st.session_state.ds_page + delta))
    st.session_state.ds_page = new_page
    st.session_state.ds_nav = ds_pages[new_page]

def _ds_go_to_page(page_name):
    if page_name in ds_pages:
        st.session_state.ds_page = ds_pages.index(page_name)
        st.session_state.ds_nav = page_name

st.markdown("""
<style>
div[data-testid="stSelectbox"] { margin-bottom: 0.25rem; }
.ds-screen-caption { text-align: center; color: #087f8c; font-weight: 700; }
.ds-welcome {
    background: radial-gradient(circle at 50% 0%, #d7fff2 0%, #e8f5ff 36%, #f7fbff 72%, #ffffff 100%);
    border: 1px solid #c7e6e7; border-radius: 28px; padding: 30px 22px 28px;
    text-align: center; box-shadow: 0 14px 38px rgba(8, 127, 140, 0.12); overflow: hidden;
}
.ds-sun {
    width: 124px; height: 124px; border-radius: 50%; margin: 4px auto 20px;
    display: flex; align-items: center; justify-content: center; font-size: 66px;
    background: radial-gradient(circle at 35% 28%, #fff6b0, #ffc857 52%, #ff9b42 100%);
    box-shadow: 0 0 0 12px rgba(255, 202, 87, .15), 0 0 0 25px rgba(255, 202, 87, .08);
}
.ds-brand { font-size: clamp(36px, 9vw, 52px); line-height: 1.05; font-weight: 900; letter-spacing: 1.5px; color: #087f8c; margin: 6px 0 12px; }
.ds-welcome-sub { font-size: 20px; font-weight: 750; color: #176b5b; margin-bottom: 12px; }
.ds-welcome-copy { color: #3c5962; font-size: 15px; line-height: 1.6; }
.ds-pill-row { display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin-top:20px; }
.ds-pill { border:1px solid #c4e3df; background:rgba(255,255,255,.78); border-radius:999px; padding:7px 11px; color:#176b5b; font-size:12px; font-weight:700; }
</style>
""", unsafe_allow_html=True)



if st.session_state.ds_page == 0:
    # Welcome / splash screen. The actual app begins on the next screen.
    st.markdown(
        f"""
        <div class="ds-welcome">
          <div class="ds-sun">☀️</div>
          <div class="ds-brand">SEHAT SAATHI</div>
          <div class="ds-welcome-sub">{'ਸਿਹਤ, ਸਫ਼ਾਈ ਅਤੇ ਸੈਨਿਟੇਸ਼ਨ ਸਹਾਇਕ' if pa else 'Smart Health, Hygiene & Sanitation'}</div>
          <div class="ds-welcome-copy">
            {'ਸਿਹਤਮੰਦ ਨਾਗਰਿਕ • ਸਵੱਛ ਸਮਾਜ • ਵਿਕਸਿਤ ਭਾਰਤ' if pa else 'Healthy Citizens • Clean Communities • Viksit Bharat @2047'}
          </div>
          <div class="ds-pill-row">
            <span class="ds-pill">🌐 {'ਪੰਜਾਬੀ + English' if pa else 'Punjabi + English'}</span>
            <span class="ds-pill">📘 {'ਸਿੱਖੋ' if pa else 'Learn'}</span>
            <span class="ds-pill">🔬 {'ਵਿਗਿਆਨ' if pa else 'Science'}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")
    st.caption(
        "ਇੱਕ ਵਿਦਿਆਰਥੀ-ਕੇਂਦਰਿਤ ਸਿਹਤ ਜਾਗਰੂਕਤਾ ਪ੍ਰੋਜੈਕਟ"
        if pa else
        "A student-led science and health-awareness project"
    )
    _welcome_left, _welcome_mid, _welcome_right = st.columns([1, 5, 1])
    with _welcome_mid:
        st.button(
            "ਸ਼ੁਰੂ ਕਰੋ  →" if pa else "Enter SEHAT SAATHI  →",
            key="ds_start_app",
            on_click=_ds_move_page,
            args=(1,),
            type="primary",
            use_container_width=True
        )

if st.session_state.ds_page == 1:
    # Clean home screen: app introduction and health learning hub.
    
    st.title("☀️ SEHAT SAATHI")
    st.subheader(title)
    st.write(intro)
    st.markdown("### " + ("ਤੁਹਾਡਾ ਸਿਹਤ ਸਿੱਖਣ ਕੇਂਦਰ" if pa else "Your Health Learning Hub"))
    st.info("ਵਿਕਸਿਤ ਭਾਰਤ @2047 ਵੱਲ: ਸਿਹਤਮੰਦ ਨਾਗਰਿਕ, ਸਵੱਛ ਸਮਾਜ" if pa else "Towards Viksit Bharat @2047: Healthy citizens, clean communities and digital awareness.")
    _hub_cards = st.columns(4)
    _hub_items = [
        ("🧼", "Hygiene" if not pa else "ਨਿੱਜੀ ਸਫ਼ਾਈ", "Hygiene"),
        ("💧", "Sanitation" if not pa else "ਸੈਨਿਟੇਸ਼ਨ", "Sanitation"),
        ("🌱", "Healthy Habits" if not pa else "ਸਿਹਤਮੰਦ ਆਦਤਾਂ", "Healthy Habits"),
        ("❤️", "Health" if not pa else "ਸਿਹਤ", "Health"),
    ]
    for _i, (_icon, _label, _dest) in enumerate(_hub_items):
        with _hub_cards[_i]:
            st.markdown(
                f'<div style="background:#f2fbf8;border:1px solid #cce8e4;border-radius:16px;padding:14px 8px;text-align:center;min-height:105px"><div style="font-size:30px">{_icon}</div><b style="color:#176b5b">{_label}</b></div>',
                unsafe_allow_html=True
            )
            st.button(
                ("Explore" if not pa else "ਖੋਲ੍ਹੋ") + " →",
                key="ds_hub_" + str(_i),
                use_container_width=True,
                on_click=_ds_go_to_page,
                args=(_dest,)
            )
    st.button(
        "🇮🇳 Community Health Awareness Challenge →" if not pa else "🇮🇳 ਭਾਈਚਾਰਕ ਸਿਹਤ ਜਾਗਰੂਕਤਾ ਚੁਣੌਤੀ →",
        key="ds_community_home",
        use_container_width=True,
        on_click=_ds_go_to_page,
        args=("Community Challenge",)
    )
    st.info(notice)
    
    st.divider()
    

if st.session_state.ds_page == 2:
    # ================= VISUAL PROJECT & CREDITS SCREEN =================
    _credits_pa = language == "ਪੰਜਾਬੀ"

    st.markdown(
        """
        <style>
        .ds-credit-hero {
            background: radial-gradient(circle at 50% 0%, #fff2b8 0%, #e4fff5 32%, #e9f1ff 72%, #ffffff 100%);
            border: 1px solid #c9e7e3; border-radius: 24px; padding: 26px 18px;
            text-align: center; box-shadow: 0 10px 28px rgba(8, 127, 140, .10);
            margin: 4px 0 18px;
        }
        .ds-credit-sun {
            width: 82px; height: 82px; display: flex; align-items: center; justify-content: center;
            border-radius: 50%; margin: 0 auto 12px; font-size: 46px;
            background: linear-gradient(145deg, #fff7bd, #ffc857);
            box-shadow: 0 0 0 8px rgba(255, 200, 87, .16);
        }
        .ds-credit-title { color: #087f8c; font-size: 34px; line-height: 1.1; font-weight: 900; letter-spacing: 1px; margin: 4px 0 8px; }
        .ds-credit-sub { color: #24505a; font-size: 17px; font-weight: 750; margin: 0 0 9px; }
        .ds-credit-tag { display: inline-block; margin: 4px 3px; padding: 6px 10px; border-radius: 999px; background: rgba(255,255,255,.85); border: 1px solid #c6e4de; color: #176b5b; font-size: 12px; font-weight: 700; }
        .ds-credit-card { background: linear-gradient(145deg, #ffffff, #f3fbff); border: 1px solid #d6e8ed; border-radius: 17px; padding: 16px; min-height: 126px; margin-bottom: 10px; }
        .ds-credit-icon { font-size: 27px; margin-bottom: 5px; }
        .ds-credit-label { color: #087f8c; font-size: 12px; font-weight: 800; letter-spacing: .5px; text-transform: uppercase; margin-bottom: 5px; }
        .ds-credit-name { color: #203d49; font-size: 16px; font-weight: 800; line-height: 1.35; }
        .ds-credit-detail { color: #536c74; font-size: 13px; line-height: 1.5; margin-top: 4px; }
        .ds-credit-feature { background: #f1faf7; border: 1px solid #d3ece2; border-radius: 12px; padding: 10px 12px; margin: 6px 0; color: #24565b; }
        .ds-credit-footer { text-align: center; padding: 13px 8px; color: #527078; font-size: 12px; }
        </style>
        """,
        unsafe_allow_html=True
    )

    if _credits_pa:
        st.markdown(
            """
            <div class="ds-credit-hero">
              <div class="ds-credit-sun">☀️</div>
              <div class="ds-credit-title">SEHAT SAATHI</div>
              <div class="ds-credit-sub">AI ਸਿਹਤ, ਸਫ਼ਾਈ ਅਤੇ ਸੈਨਿਟੇਸ਼ਨ ਪਲੇਟਫਾਰਮ</div>
              <div><span class="ds-credit-tag">🔬 ਵਿਗਿਆਨ</span><span class="ds-credit-tag">💻 ਤਕਨਾਲੋਜੀ</span><span class="ds-credit-tag">💚 ਸਿਹਤ ਜਾਗਰੂਕਤਾ</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("### 🎯 ਪ੍ਰੋਜੈਕਟ ਦਾ ਉਦੇਸ਼")
        st.write("SEHAT SAATHI ਨਿੱਜੀ ਸਫ਼ਾਈ, ਸੁਰੱਖਿਅਤ ਪਾਣੀ, ਸੈਨਿਟੇਸ਼ਨ, ਕੂੜਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਸਿਹਤਮੰਦ ਰੋਜ਼ਾਨਾ ਆਦਤਾਂ ਬਾਰੇ ਦੋ-ਭਾਸ਼ਾਈ ਸਿੱਖਿਆ ਪਲੇਟਫਾਰਮ ਹੈ।")

        st.markdown("### 🤝 ਪ੍ਰੋਜੈਕਟ ਟੀਮ")
        _c1, _c2 = st.columns(2)
        with _c1:
            st.markdown('<div class="ds-credit-card"><div class="ds-credit-icon">👩‍🎓</div><div class="ds-credit-label">ਵਿਦਿਆਰਥਣ / Student Developer</div><div class="ds-credit-name">Pawandeep Kaur</div><div class="ds-credit-detail">ਜਮਾਤ 9ਵੀਂ</div></div>', unsafe_allow_html=True)
        with _c2:
            st.markdown('<div class="ds-credit-card"><div class="ds-credit-icon">👨‍🏫</div><div class="ds-credit-label">ਮਾਰਗਦਰਸ਼ਕ ਅਧਿਆਪਕ</div><div class="ds-credit-name">Sumitpal Singh Sodhi</div><div class="ds-credit-detail">Science Master</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="ds-credit-card"><div class="ds-credit-icon">🏫</div><div class="ds-credit-label">ਸਕੂਲ / School</div><div class="ds-credit-name">GSSS Bare Ke, Ferozepur</div><div class="ds-credit-detail">ਜ਼ਿਲ੍ਹਾ ਫਿਰੋਜ਼ਪੁਰ, ਪੰਜਾਬ</div></div>', unsafe_allow_html=True)

        st.markdown("### ✨ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ")
        for _feature in [
            "🌐 ਪੰਜਾਬੀ ਅਤੇ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਜਾਣਕਾਰੀ",
            "🧼 ਹੱਥਾਂ, ਮੂੰਹ, ਭੋਜਨ ਅਤੇ ਨਿੱਜੀ ਸਫ਼ਾਈ ਬਾਰੇ ਸਿੱਖਿਆ",
            "💧 ਸੁਰੱਖਿਅਤ ਪਾਣੀ, ਟਾਇਲਟ ਸਫ਼ਾਈ ਅਤੇ ਕੂੜਾ ਪ੍ਰਬੰਧਨ",
            "🌱 ਸਿਹਤਮੰਦ ਆਦਤਾਂ ਲਈ ਇੰਟਰਐਕਟਿਵ ਟ੍ਰੈਕਰ",
            "🇮🇳 ਭਾਈਚਾਰਕ ਸਿਹਤ ਜਾਗਰੂਕਤਾ ਚੁਣੌਤੀ",
            "🎯 ਵਿਕਸਿਤ ਭਾਰਤ @2047 ਵਿੱਚ ਯੋਗਦਾਨ",
            "🤖 ਸਿਹਤ, ਸਫ਼ਾਈ ਅਤੇ ਸੈਨਿਟੇਸ਼ਨ ਲਈ AI ਸਹਾਇਕ",
        ]:
            st.markdown(f'<div class="ds-credit-feature">{_feature}</div>', unsafe_allow_html=True)

        st.warning("ਮਹੱਤਵਪੂਰਨ: ਇਹ ਸਿਰਫ਼ ਵਿਦਿਅਕ ਜਾਗਰੂਕਤਾ ਲਈ ਹੈ। ਇਹ ਡਾਕਟਰੀ ਜਾਂਚ, ਨਿਦਾਨ, ਇਲਾਜ ਜਾਂ ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਦਾ ਬਦਲ ਨਹੀਂ ਹੈ।")
        st.markdown('<div class="ds-credit-footer">ਵਿਗਿਆਨ ਪ੍ਰਦਰਸ਼ਨੀ ਪ੍ਰੋਜੈਕਟ • ਅਕਾਦਮਿਕ ਸੈਸ਼ਨ 2026–27<br>ਗਿਆਨ • ਜਾਗਰੂਕਤਾ • ਬਿਹਤਰ ਸਿਹਤ</div>', unsafe_allow_html=True)

    else:
        st.markdown(
            """
            <div class="ds-credit-hero">
              <div class="ds-credit-sun">☀️</div>
              <div class="ds-credit-title">SEHAT SAATHI</div>
              <div class="ds-credit-sub">AI Health, Hygiene & Sanitation Platform</div>
              <div><span class="ds-credit-tag">🔬 Science</span><span class="ds-credit-tag">💻 Technology</span><span class="ds-credit-tag">💚 Health Awareness</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("### 🎯 Project Purpose")
        st.write("SEHAT SAATHI is a bilingual educational platform covering personal hygiene, safe water, sanitation, waste management and healthier everyday habits.")

        st.markdown("### 🤝 Project Team")
        _c1, _c2 = st.columns(2)
        with _c1:
            st.markdown('<div class="ds-credit-card"><div class="ds-credit-icon">👩‍🎓</div><div class="ds-credit-label">Student Developer</div><div class="ds-credit-name">Pawandeep Kaur</div><div class="ds-credit-detail">Class 9</div></div>', unsafe_allow_html=True)
        with _c2:
            st.markdown('<div class="ds-credit-card"><div class="ds-credit-icon">👨‍🏫</div><div class="ds-credit-label">Project Guide</div><div class="ds-credit-name">Sumitpal Singh Sodhi</div><div class="ds-credit-detail">Science Master</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="ds-credit-card"><div class="ds-credit-icon">🏫</div><div class="ds-credit-label">School</div><div class="ds-credit-name">GSSS Bare Ke, Ferozepur</div><div class="ds-credit-detail">District Ferozepur, Punjab, India</div></div>', unsafe_allow_html=True)

        st.markdown("### ✨ Key Features")
        for _feature in [
            "🌐 Bilingual learning: English and Punjabi",
            "🧼 Hand, oral, food and personal hygiene learning",
            "💧 Safe water, toilet hygiene and waste management",
            "🌱 Interactive healthy-habits tracker",
            "🇮🇳 Community Health Awareness Challenge",
            "🎯 Contribution to Viksit Bharat @2047",
            "🤖 AI assistant for health, hygiene and sanitation education",
        ]:
            st.markdown(f'<div class="ds-credit-feature">{_feature}</div>', unsafe_allow_html=True)

        st.warning("Important: SEHAT SAATHI is for education and awareness only. It does not replace medical testing, diagnosis, treatment, or professional medical advice.")
        st.markdown('<div class="ds-credit-footer">Science Exhibition Project • Academic Session 2026–27<br>Knowledge • Awareness • Better Health</div>', unsafe_allow_html=True)


if st.session_state.ds_page == 3:
    # ---------- GEMINI-POWERED AI HEALTH EDUCATION ASSISTANT ----------
    st.header(
        "🤖 SEHAT SAATHI AI Health Mentor"
        if not pa else
        "🤖 SEHAT SAATHI AI ਸਿਹਤ ਸਾਥੀ"
    )
    st.write(
        "Ask about general health, nutrition, physical activity, sleep, emotional wellbeing, hygiene, safe water and sanitation in simple language."
        if not pa else
        "ਆਮ ਸਿਹਤ, ਪੋਸ਼ਣ, ਸਰੀਰਕ ਸਰਗਰਮੀ, ਨੀਂਦ, ਮਾਨਸਿਕ ਤੰਦਰੁਸਤੀ, ਸਫ਼ਾਈ, ਸੁਰੱਖਿਅਤ ਪਾਣੀ ਅਤੇ ਸੈਨਿਟੇਸ਼ਨ ਬਾਰੇ ਸੌਖੀ ਭਾਸ਼ਾ ਵਿੱਚ ਸਵਾਲ ਪੁੱਛੋ।"
    )
    st.info(
        "Education only: the AI provides general information, not personal medical advice. Do not enter names, contact details, medical reports, or other private health information."
        if not pa else
        "ਸਿਰਫ਼ ਸਿੱਖਿਆ ਲਈ: AI ਆਮ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ, ਨਿੱਜੀ ਡਾਕਟਰੀ ਸਲਾਹ ਨਹੀਂ। ਨਾਮ, ਸੰਪਰਕ ਵੇਰਵੇ, ਮੈਡੀਕਲ ਰਿਪੋਰਟਾਂ ਜਾਂ ਹੋਰ ਨਿੱਜੀ ਸਿਹਤ ਜਾਣਕਾਰੀ ਨਾ ਦਰਜ ਕਰੋ।"
    )

    try:
        _ds_gemini_key = st.secrets.get("GEMINI_API_KEY", "")
    except Exception:
        _ds_gemini_key = ""

    if not _ds_gemini_key:
        st.warning(
            "The AI screen is added, but it is not connected yet. The app owner must add GEMINI_API_KEY in Streamlit app Settings → Secrets. Never put the key in app.py or a public GitHub file."
            if not pa else
            "AI ਸਕ੍ਰੀਨ ਜੋੜ ਦਿੱਤੀ ਗਈ ਹੈ, ਪਰ ਹਾਲੇ ਕਨੈਕਟ ਨਹੀਂ ਹੋਈ। ਐਪ ਦੇ ਮਾਲਕ ਨੂੰ Streamlit App Settings → Secrets ਵਿੱਚ GEMINI_API_KEY ਜੋੜਨਾ ਹੋਵੇਗਾ। API key ਨੂੰ app.py ਜਾਂ public GitHub ਫਾਈਲ ਵਿੱਚ ਕਦੇ ਨਾ ਲਿਖੋ।"
        )
    else:
        if "ds_ai_messages" not in st.session_state:
            st.session_state.ds_ai_messages = []
        if "ds_ai_question_count" not in st.session_state:
            st.session_state.ds_ai_question_count = 0

        _ds_ai_limit_reached = st.session_state.ds_ai_question_count >= 5
        with st.form("ds_ai_question_form", clear_on_submit=True):
            _ds_ai_prompt = st.text_input(
                "Your question / ਤੁਹਾਡਾ ਸਵਾਲ",
                max_chars=1000,
                key="ds_ai_question_text",
                placeholder=(
                    "Ask about health, hygiene or sanitation..."
                    if not pa else
                    "ਸਿਹਤ, ਸਫ਼ਾਈ ਜਾਂ ਸੈਨਿਟੇਸ਼ਨ ਬਾਰੇ ਸਵਾਲ ਪੁੱਛੋ..."
                ),
                disabled=_ds_ai_limit_reached
            )
            _ds_ai_send = st.form_submit_button(
                "Ask AI →" if not pa else "AI ਨੂੰ ਪੁੱਛੋ →",
                disabled=_ds_ai_limit_reached,
                use_container_width=True
            )

        if _ds_ai_limit_reached:
            st.caption(
                "Demo limit reached: 5 questions per session."
                if not pa else
                "ਡੈਮੋ ਸੀਮਾ ਪੂਰੀ ਹੋ ਗਈ: ਹਰ ਸੈਸ਼ਨ ਵਿੱਚ 5 ਸਵਾਲ।"
            )

        if _ds_ai_send and _ds_ai_prompt.strip():
            st.session_state.ds_ai_messages.append(
                {"role": "user", "content": _ds_ai_prompt.strip()}
            )
            st.session_state.ds_ai_question_count += 1

            _ds_history = st.session_state.ds_ai_messages[-8:]
            _ds_chat_context = "\\n".join(
                ("User: " if _m["role"] == "user" else "Assistant: ") + _m["content"]
                for _m in _ds_history
            )
            _ds_language_instruction = (
                "Answer in Punjabi (Gurmukhi script)." if pa
                else "Answer in clear, simple English."
            )
            _ds_system_instruction = (
                "You are SEHAT SAATHI, an AI health-education assistant for general health literacy, balanced nutrition, physical activity, sleep, emotional wellbeing, preventive health awareness, personal and food hygiene, safe drinking water, sanitation, waste management and healthy habits. "
                "Provide concise, evidence-informed educational explanations for school students and the public. "
                "Do not diagnose or interpret a personal medical case, "
                "or prescribe treatment. For personal medical concerns, medication questions, or ongoing symptoms, "
                "recommend discussing the matter with a qualified healthcare professional. Never request identifying "
                "or private health information. If a question is unrelated to general health, hygiene, sanitation or wellness education, "
                "politely explain the assistant's limited scope. Be transparent about uncertainty and do not invent facts. "
                + _ds_language_instruction
                + "\\nConversation so far:\\n" + _ds_chat_context
            )

            try:
                from google import genai
                _ds_client = genai.Client(api_key=_ds_gemini_key)
                with st.spinner(
                    "SEHAT SAATHI AI is preparing an answer..." if not pa
                    else "SEHAT SAATHI AI ਜਵਾਬ ਤਿਆਰ ਕਰ ਰਿਹਾ ਹੈ..."
                ):
                    _ds_response = _ds_client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=_ds_system_instruction
                    )
                _ds_answer = (_ds_response.text or "").strip()
                if not _ds_answer:
                    _ds_answer = (
                        "I couldn't generate a response just now. Please try a different question."
                        if not pa else
                        "ਇਸ ਵੇਲੇ ਜਵਾਬ ਤਿਆਰ ਨਹੀਂ ਹੋ ਸਕਿਆ। ਕਿਰਪਾ ਕਰਕੇ ਹੋਰ ਤਰੀਕੇ ਨਾਲ ਸਵਾਲ ਪੁੱਛੋ।"
                    )
            except Exception as _ds_error:
                _ds_answer = (
                    "The AI request failed (" + type(_ds_error).__name__ + "). Please check the API key, API access/quota, and Streamlit app logs."
                    if not pa else
                    "AI ਬੇਨਤੀ ਅਸਫਲ ਰਹੀ (" + type(_ds_error).__name__ + ")। API key, API ਪਹੁੰਚ/quota ਅਤੇ Streamlit app logs ਦੀ ਜਾਂਚ ਕਰੋ।"
                )

            st.session_state.ds_ai_messages.append(
                {"role": "assistant", "content": _ds_answer}
            )

        # Render conversation after processing the form so the latest answer appears immediately.
        for _ds_msg in st.session_state.ds_ai_messages:
            with st.chat_message(_ds_msg["role"]):
                st.markdown(_ds_msg["content"])

    st.caption(
        "AI-generated information may be incomplete or incorrect. Verify important health information with a qualified professional."
        if not pa else
        "AI ਤੋਂ ਮਿਲੀ ਜਾਣਕਾਰੀ ਅਧੂਰੀ ਜਾਂ ਗਲਤ ਹੋ ਸਕਦੀ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਸਿਹਤ ਜਾਣਕਾਰੀ ਦੀ ਪੁਸ਼ਟੀ ਯੋਗ ਸਿਹਤ ਮਾਹਿਰ ਨਾਲ ਕਰੋ।"
    )



# ---------- HEALTH, HYGIENE AND SANITATION LEARNING HUB ----------
if st.session_state.ds_page == 4:
    st.header("🧼 " + ("Hygiene Hub" if not pa else "ਨਿੱਜੀ ਸਫ਼ਾਈ ਕੇਂਦਰ"))
    st.write(
        "Small daily hygiene habits help reduce the spread of germs and support dignity and wellbeing."
        if not pa else
        "ਰੋਜ਼ਾਨਾ ਦੀਆਂ ਸਫ਼ਾਈ ਵਾਲੀਆਂ ਆਦਤਾਂ ਕੀਟਾਣੂਆਂ ਦੇ ਫੈਲਾਅ ਨੂੰ ਘਟਾਉਣ ਅਤੇ ਸਿਹਤ ਤੇ ਸਨਮਾਨ ਦੀ ਰੱਖਿਆ ਵਿੱਚ ਮਦਦ ਕਰਦੀਆਂ ਹਨ।"
    )
    _hygiene_topics = [
        (
            "👐 Handwashing" if not pa else "👐 ਹੱਥ ਧੋਣਾ",
            "Wet hands with clean running water, apply soap, scrub all hand surfaces for at least 20 seconds, rinse, and dry with a clean towel or air-dry. Wash before preparing or eating food and after using the toilet, coughing, sneezing, or handling waste."
            if not pa else
            "ਸਾਫ਼ ਵਗਦੇ ਪਾਣੀ ਨਾਲ ਹੱਥ ਗਿੱਲੇ ਕਰੋ, ਸਾਬਣ ਲਗਾਓ, ਹੱਥਾਂ ਦੇ ਸਾਰੇ ਹਿੱਸੇ ਘੱਟੋ-ਘੱਟ 20 ਸਕਿੰਟ ਰਗੜੋ, ਫਿਰ ਧੋ ਕੇ ਸਾਫ਼ ਤੌਲੀਏ ਨਾਲ ਸੁਕਾਓ ਜਾਂ ਹਵਾ ਵਿੱਚ ਸੁੱਕਣ ਦਿਓ। ਖਾਣਾ ਬਣਾਉਣ ਜਾਂ ਖਾਣ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਟਾਇਲਟ ਵਰਤਣ, ਖੰਘਣ, ਛਿੱਕਣ ਜਾਂ ਕੂੜਾ ਸੰਭਾਲਣ ਤੋਂ ਬਾਅਦ ਹੱਥ ਧੋਵੋ।"
        ),
        (
            "🦷 Oral hygiene" if not pa else "🦷 ਮੂੰਹ ਅਤੇ ਦੰਦਾਂ ਦੀ ਸਫ਼ਾਈ",
            "Brush teeth twice a day with fluoride toothpaste, clean between teeth when possible, and arrange dental care for persistent pain or bleeding."
            if not pa else
            "ਦਿਨ ਵਿੱਚ ਦੋ ਵਾਰ ਫਲੋਰਾਈਡ ਵਾਲੇ ਟੂਥਪੇਸਟ ਨਾਲ ਦੰਦ ਸਾਫ਼ ਕਰੋ। ਸੰਭਵ ਹੋਵੇ ਤਾਂ ਦੰਦਾਂ ਵਿਚਕਾਰ ਵੀ ਸਫ਼ਾਈ ਕਰੋ ਅਤੇ ਲਗਾਤਾਰ ਦਰਦ ਜਾਂ ਖੂਨ ਆਉਣ 'ਤੇ ਦੰਦਾਂ ਦੇ ਡਾਕਟਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।"
        ),
        (
            "🥗 Food hygiene" if not pa else "🥗 ਭੋਜਨ ਦੀ ਸਫ਼ਾਈ",
            "Wash hands and produce with safe water, keep raw foods separate from cooked foods, use clean utensils, and refrigerate perishable food promptly."
            if not pa else
            "ਹੱਥ ਅਤੇ ਫਲ-ਸਬਜ਼ੀਆਂ ਸੁਰੱਖਿਅਤ ਪਾਣੀ ਨਾਲ ਧੋਵੋ, ਕੱਚੇ ਅਤੇ ਪੱਕੇ ਭੋਜਨ ਨੂੰ ਵੱਖ ਰੱਖੋ, ਸਾਫ਼ ਬਰਤਨ ਵਰਤੋ ਅਤੇ ਜਲਦੀ ਖਰਾਬ ਹੋਣ ਵਾਲਾ ਭੋਜਨ ਸਮੇਂ ਸਿਰ ਫਰਿੱਜ ਵਿੱਚ ਰੱਖੋ।"
        ),
        (
            "🤧 Cough and sneeze etiquette" if not pa else "🤧 ਖੰਘਣ ਅਤੇ ਛਿੱਕਣ ਦੇ ਸਹੀ ਤਰੀਕੇ",
            "Cover coughs and sneezes with a tissue or your bent elbow, dispose of tissues safely, and clean your hands."
            if not pa else
            "ਖੰਘਣ ਜਾਂ ਛਿੱਕਣ ਵੇਲੇ ਟਿਸ਼ੂ ਜਾਂ ਮੁੜੀ ਹੋਈ ਕੂਹਣੀ ਵਰਤੋ, ਟਿਸ਼ੂ ਢੰਗ ਨਾਲ ਸੁੱਟੋ ਅਤੇ ਹੱਥ ਸਾਫ਼ ਕਰੋ।"
        ),
        (
            "🌸 Menstrual hygiene" if not pa else "🌸 ਮਹਾਵਾਰੀ ਦੌਰਾਨ ਸਫ਼ਾਈ",
            "Use clean menstrual products, change them as directed, wash hands before and after changing, and dispose of used products safely according to local facilities. Menstruation is normal and should be discussed without shame."
            if not pa else
            "ਸਾਫ਼ ਮਹਾਵਾਰੀ ਉਤਪਾਦ ਵਰਤੋ ਅਤੇ ਹਦਾਇਤਾਂ ਅਨੁਸਾਰ ਬਦਲੋ। ਉਤਪਾਦ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਬਾਅਦ ਹੱਥ ਧੋਵੋ ਅਤੇ ਵਰਤੇ ਉਤਪਾਦਾਂ ਦਾ ਸਥਾਨਕ ਸਹੂਲਤਾਂ ਅਨੁਸਾਰ ਸੁਰੱਖਿਅਤ ਨਿਪਟਾਰਾ ਕਰੋ। ਮਹਾਵਾਰੀ ਇੱਕ ਕੁਦਰਤੀ ਪ੍ਰਕਿਰਿਆ ਹੈ; ਇਸ ਬਾਰੇ ਬਿਨਾਂ ਝਿਜਕ ਗੱਲ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।"
        ),
    ]
    for _topic, _details in _hygiene_topics:
        with st.expander(_topic):
            st.write(_details)
    st.divider()
    st.subheader("🧠 " + ("Hygiene Quick Quiz" if not pa else "ਸਫ਼ਾਈ ਬਾਰੇ ਛੋਟਾ ਕਵਿਜ਼"))
    _hq = st.radio(
        "When is handwashing especially important?" if not pa else "ਹੱਥ ਕਦੋਂ ਧੋਣੇ ਖਾਸ ਤੌਰ 'ਤੇ ਜ਼ਰੂਰੀ ਹਨ?",
        [
            "Only in the morning" if not pa else "ਸਿਰਫ਼ ਸਵੇਰੇ",
            "Before eating and after using the toilet" if not pa else "ਖਾਣ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਟਾਇਲਟ ਤੋਂ ਬਾਅਦ",
            "Only when hands look dirty" if not pa else "ਸਿਰਫ਼ ਜਦੋਂ ਹੱਥ ਗੰਦੇ ਦਿਸਣ",
        ],
        key="ds_hygiene_quiz"
    )
    if st.button("Check answer" if not pa else "ਜਵਾਬ ਵੇਖੋ", key="ds_hygiene_check"):
        if _hq == ("Before eating and after using the toilet" if not pa else "ਖਾਣ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਟਾਇਲਟ ਤੋਂ ਬਾਅਦ"):
            st.success("Correct! Hands can carry germs even when they look clean." if not pa else "ਸਹੀ! ਹੱਥ ਸਾਫ਼ ਦਿਸਣ ਦੇ ਬਾਵਜੂਦ ਉਨ੍ਹਾਂ 'ਤੇ ਕੀਟਾਣੂ ਹੋ ਸਕਦੇ ਹਨ।")
        else:
            st.info("Try again: wash before eating and after using the toilet, among other important times." if not pa else "ਫਿਰ ਕੋਸ਼ਿਸ਼ ਕਰੋ: ਖਾਣ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਟਾਇਲਟ ਤੋਂ ਬਾਅਦ ਸਮੇਤ ਹੋਰ ਜ਼ਰੂਰੀ ਸਮਿਆਂ 'ਤੇ ਹੱਥ ਧੋਵੋ।")
    st.caption("SEHAT SAATHI provides education, not individual medical advice." if not pa else "SEHAT SAATHI ਸਿੱਖਿਆ ਦਿੰਦਾ ਹੈ, ਨਿੱਜੀ ਡਾਕਟਰੀ ਸਲਾਹ ਨਹੀਂ।")


if st.session_state.ds_page == 5:
    st.header("💧 " + ("Sanitation & Safe Water" if not pa else "ਸੈਨਿਟੇਸ਼ਨ ਅਤੇ ਸੁਰੱਖਿਅਤ ਪਾਣੀ"))
    st.write(
        "Clean surroundings, safe water, hygienic toilets and responsible waste handling help protect community health."
        if not pa else
        "ਸਾਫ਼ ਵਾਤਾਵਰਣ, ਸੁਰੱਖਿਅਤ ਪਾਣੀ, ਸਾਫ਼ ਟਾਇਲਟ ਅਤੇ ਕੂੜੇ ਦਾ ਢੰਗ ਨਾਲ ਪ੍ਰਬੰਧ ਸਮੁਦਾਇਕ ਸਿਹਤ ਦੀ ਰੱਖਿਆ ਕਰਦੇ ਹਨ।"
    )
    _san_topics = [
        (
            "🚰 Safe drinking water" if not pa else "🚰 ਸੁਰੱਖਿਅਤ ਪੀਣ ਵਾਲਾ ਪਾਣੀ",
            "Water that looks clear is not always safe. Use a reliable approved source; when safety is uncertain, follow local public-health advice on treatment. Store drinking water in a clean, covered, food-safe container and avoid dipping unwashed hands or cups into it."
            if not pa else
            "ਸਾਫ਼ ਦਿਸਣ ਵਾਲਾ ਪਾਣੀ ਹਮੇਸ਼ਾ ਸੁਰੱਖਿਅਤ ਨਹੀਂ ਹੁੰਦਾ। ਭਰੋਸੇਯੋਗ ਅਤੇ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਸਰੋਤ ਵਰਤੋ। ਜੇ ਪਾਣੀ ਦੀ ਸੁਰੱਖਿਆ ਬਾਰੇ ਸ਼ੱਕ ਹੋਵੇ ਤਾਂ ਸਥਾਨਕ ਸਿਹਤ ਵਿਭਾਗ ਦੀ ਸਲਾਹ ਅਨੁਸਾਰ ਇਲਾਜ ਕਰੋ। ਪੀਣ ਵਾਲਾ ਪਾਣੀ ਸਾਫ਼, ਢੱਕੇ ਹੋਏ ਅਤੇ ਭੋਜਨ ਲਈ ਸੁਰੱਖਿਅਤ ਬਰਤਨ ਵਿੱਚ ਰੱਖੋ।"
        ),
        (
            "🚽 Toilet hygiene" if not pa else "🚽 ਟਾਇਲਟ ਦੀ ਸਫ਼ਾਈ",
            "Use toilets safely, keep facilities as clean as possible, wash hands with soap afterwards, and report broken water supplies or sanitation facilities to a responsible adult or local authority."
            if not pa else
            "ਟਾਇਲਟ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਵਰਤੋ, ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ ਸਹੂਲਤਾਂ ਸਾਫ਼ ਰੱਖੋ, ਬਾਅਦ ਵਿੱਚ ਸਾਬਣ ਨਾਲ ਹੱਥ ਧੋਵੋ ਅਤੇ ਪਾਣੀ ਜਾਂ ਸਫ਼ਾਈ ਦੀ ਸਹੂਲਤ ਖਰਾਬ ਹੋਣ 'ਤੇ ਜ਼ਿੰਮੇਵਾਰ ਵੱਡੇ ਜਾਂ ਸਥਾਨਕ ਅਧਿਕਾਰੀ ਨੂੰ ਦੱਸੋ।"
        ),
        (
            "♻️ Waste segregation" if not pa else "♻️ ਕੂੜੇ ਦੀ ਵੱਖ-ਵੱਖ ਛਾਂਟ",
            "Separate wet/biodegradable waste, dry recyclable waste and household hazardous waste according to local collection rules. Do not burn mixed waste or handle sharp, chemical or medical waste without proper support."
            if not pa else
            "ਸਥਾਨਕ ਨਿਯਮਾਂ ਅਨੁਸਾਰ ਗਿੱਲਾ/ਜੈਵਿਕ ਕੂੜਾ, ਸੁੱਕਾ ਰੀਸਾਈਕਲ ਹੋਣ ਵਾਲਾ ਕੂੜਾ ਅਤੇ ਘਰੇਲੂ ਖਤਰਨਾਕ ਕੂੜਾ ਵੱਖ ਕਰੋ। ਮਿਲਿਆ-ਜੁਲਿਆ ਕੂੜਾ ਨਾ ਸਾੜੋ ਅਤੇ ਤਿੱਖੇ, ਰਸਾਇਣਕ ਜਾਂ ਮੈਡੀਕਲ ਕੂੜੇ ਨੂੰ ਸਹੀ ਸਹਾਇਤਾ ਤੋਂ ਬਿਨਾਂ ਨਾ ਛੂਹੋ।"
        ),
        (
            "🦟 Mosquito prevention" if not pa else "🦟 ਮੱਛਰਾਂ ਤੋਂ ਬਚਾਅ",
            "Remove or cover standing water where practical, keep water-storage containers covered, and follow local public-health advice. Do not enter drains or handle chemicals to control mosquitoes."
            if not pa else
            "ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ ਖੜ੍ਹਾ ਪਾਣੀ ਹਟਾਓ ਜਾਂ ਢੱਕੋ ਅਤੇ ਪਾਣੀ ਸੰਭਾਲਣ ਵਾਲੇ ਬਰਤਨ ਢੱਕ ਕੇ ਰੱਖੋ। ਸਥਾਨਕ ਸਿਹਤ ਵਿਭਾਗ ਦੀ ਸਲਾਹ ਮੰਨੋ। ਮੱਛਰਾਂ ਨੂੰ ਕਾਬੂ ਕਰਨ ਲਈ ਨਾਲਿਆਂ ਵਿੱਚ ਨਾ ਉਤਰੋ ਅਤੇ ਰਸਾਇਣ ਆਪਣੇ ਆਪ ਨਾ ਵਰਤੋ।"
        ),
        (
            "🏫 Clean school checklist" if not pa else "🏫 ਸਾਫ਼ ਸਕੂਲ ਦੀ ਜਾਂਚ-ਸੂਚੀ",
            "Look for accessible drinking water, usable and reasonably clean toilets, soap or another approved handwashing option, covered bins, and clear reporting of leaks or stagnant water. Report problems to staff; students should not handle sewage, sharps or unknown chemicals."
            if not pa else
            "ਪੀਣ ਵਾਲੇ ਪਾਣੀ, ਵਰਤਣਯੋਗ ਅਤੇ ਸਾਫ਼ ਟਾਇਲਟ, ਸਾਬਣ ਜਾਂ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਹੱਥ ਧੋਣ ਦੀ ਸਹੂਲਤ, ਢੱਕੇ ਕੂੜੇਦਾਨ ਅਤੇ ਲੀਕੇਜ ਜਾਂ ਖੜ੍ਹੇ ਪਾਣੀ ਦੀ ਜਾਂਚ ਕਰੋ। ਸਮੱਸਿਆ ਅਧਿਆਪਕਾਂ ਜਾਂ ਸਟਾਫ਼ ਨੂੰ ਦੱਸੋ; ਵਿਦਿਆਰਥੀ ਸੀਵਰੇਜ, ਤਿੱਖੀਆਂ ਚੀਜ਼ਾਂ ਜਾਂ ਅਣਜਾਣ ਰਸਾਇਣ ਨਾ ਸੰਭਾਲਣ।"
        ),
        (
            "🌍 Water conservation" if not pa else "🌍 ਪਾਣੀ ਦੀ ਬਚਤ",
            "Turn off taps when not needed, report leaks, and avoid wasting clean water. Never compromise drinking-water safety to save water."
            if not pa else
            "ਲੋੜ ਨਾ ਹੋਣ 'ਤੇ ਨਲ ਬੰਦ ਕਰੋ, ਲੀਕੇਜ ਦੀ ਸੂਚਨਾ ਦਿਓ ਅਤੇ ਸਾਫ਼ ਪਾਣੀ ਬਰਬਾਦ ਨਾ ਕਰੋ। ਪਾਣੀ ਬਚਾਉਣ ਲਈ ਪੀਣ ਵਾਲੇ ਪਾਣੀ ਦੀ ਸੁਰੱਖਿਆ ਨਾਲ ਸਮਝੌਤਾ ਨਾ ਕਰੋ।"
        ),
    ]
    for _topic, _details in _san_topics:
        with st.expander(_topic):
            st.write(_details)
    st.subheader("🗑️ " + ("Waste sorting activity" if not pa else "ਕੂੜਾ ਛਾਂਟਣ ਦੀ ਗਤੀਵਿਧੀ"))
    _waste_item = st.selectbox(
        "Choose an item" if not pa else "ਇੱਕ ਚੀਜ਼ ਚੁਣੋ",
        ["Vegetable peels", "Clean paper/cardboard", "Plastic bottle", "Used battery"],
        format_func=lambda x: (
            ({
                "Vegetable peels":"Vegetable peels — wet/biodegradable",
                "Clean paper/cardboard":"Clean paper/cardboard — dry recyclable",
                "Plastic bottle":"Plastic bottle — dry recyclable where accepted",
                "Used battery":"Used battery — household hazardous/e-waste collection"
            } if not pa else {
                "Vegetable peels":"ਸਬਜ਼ੀਆਂ ਦੇ ਛਿਲਕੇ — ਗਿੱਲਾ/ਜੈਵਿਕ ਕੂੜਾ",
                "Clean paper/cardboard":"ਸਾਫ਼ ਕਾਗਜ਼/ਗੱਤਾ — ਸੁੱਕਾ ਰੀਸਾਈਕਲ ਕੂੜਾ",
                "Plastic bottle":"ਪਲਾਸਟਿਕ ਬੋਤਲ — ਜਿੱਥੇ ਸਵੀਕਾਰ ਹੋਵੇ ਸੁੱਕਾ ਰੀਸਾਈਕਲ ਕੂੜਾ",
                "Used battery":"ਵਰਤੀ ਬੈਟਰੀ — ਖਤਰਨਾਕ/ਈ-ਕੂੜਾ ਇਕੱਠਾ ਕਰਨ ਵਾਲੀ ਥਾਂ"
            })[x]
        ),
        key="ds_waste_item"
    )
    _waste_explanations = {
        "Vegetable peels": ("Put in the wet/biodegradable stream if local collection supports it." if not pa else "ਜੇ ਸਥਾਨਕ ਪ੍ਰਬੰਧ ਹੋਵੇ ਤਾਂ ਗਿੱਲੇ/ਜੈਵਿਕ ਕੂੜੇ ਵਿੱਚ ਪਾਓ।"),
        "Clean paper/cardboard": ("Keep clean and dry for recycling where accepted." if not pa else "ਜਿੱਥੇ ਰੀਸਾਈਕਲ ਹੁੰਦਾ ਹੋਵੇ, ਸਾਫ਼ ਅਤੇ ਸੁੱਕਾ ਰੱਖੋ।"),
        "Plastic bottle": ("Empty it and follow local recycling rules." if not pa else "ਬੋਤਲ ਖਾਲੀ ਕਰੋ ਅਤੇ ਸਥਾਨਕ ਰੀਸਾਈਕਲ ਨਿਯਮ ਮੰਨੋ।"),
        "Used battery": ("Do not put batteries in ordinary mixed waste; use an approved collection point." if not pa else "ਬੈਟਰੀ ਆਮ ਮਿਲੇ-ਜੁਲੇ ਕੂੜੇ ਵਿੱਚ ਨਾ ਪਾਓ; ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਇਕੱਠਾ ਕਰਨ ਵਾਲੀ ਥਾਂ ਵਰਤੋ।"),
    }
    st.info(_waste_explanations[_waste_item])
    st.caption("Waste categories and collection systems vary by location." if not pa else "ਕੂੜੇ ਦੀਆਂ ਸ਼੍ਰੇਣੀਆਂ ਅਤੇ ਇਕੱਠਾ ਕਰਨ ਦੇ ਨਿਯਮ ਥਾਂ ਅਨੁਸਾਰ ਵੱਖ ਹੋ ਸਕਦੇ ਹਨ।")


if st.session_state.ds_page == 6:
    st.header("🌱 " + ("Healthy Habits Tracker" if not pa else "ਸਿਹਤਮੰਦ ਆਦਤਾਂ ਟ੍ਰੈਕਰ"))
    st.write(
        "Use this optional checklist as a learning reminder. It is not a health score or a test of personal cleanliness."
        if not pa else
        "ਇਸ ਵਿਕਲਪਿਕ ਸੂਚੀ ਨੂੰ ਸਿੱਖਣ ਲਈ ਯਾਦ ਦਿਹਾਨੀ ਵਜੋਂ ਵਰਤੋ। ਇਹ ਸਿਹਤ ਅੰਕ ਜਾਂ ਨਿੱਜੀ ਸਫ਼ਾਈ ਦੀ ਜਾਂਚ ਨਹੀਂ ਹੈ।"
    )
    _habits = [
        ("Wash hands with soap at important times", "ਮਹੱਤਵਪੂਰਨ ਸਮਿਆਂ 'ਤੇ ਸਾਬਣ ਨਾਲ ਹੱਥ ਧੋਣੇ"),
        ("Brush teeth morning and night", "ਸਵੇਰੇ ਅਤੇ ਰਾਤ ਦੰਦ ਸਾਫ਼ ਕਰਨੇ"),
        ("Choose safe drinking water", "ਸੁਰੱਖਿਅਤ ਪੀਣ ਵਾਲਾ ਪਾਣੀ ਚੁਣਨਾ"),
        ("Keep food and utensils clean", "ਭੋਜਨ ਅਤੇ ਬਰਤਨ ਸਾਫ਼ ਰੱਖਣੇ"),
        ("Put waste in the appropriate bin", "ਕੂੜਾ ਢੁੱਕਵੇਂ ਕੂੜੇਦਾਨ ਵਿੱਚ ਪਾਉਣਾ"),
        ("Save water and report leaks", "ਪਾਣੀ ਬਚਾਉਣਾ ਅਤੇ ਲੀਕੇਜ ਦੀ ਸੂਚਨਾ ਦੇਣੀ"),
    ]
    st.caption("Tick only what you did or learned today; missed items are reminders, not a reason for shame." if not pa else "ਅੱਜ ਕੀਤੇ ਜਾਂ ਸਿੱਖੇ ਕੰਮਾਂ 'ਤੇ ਹੀ ਨਿਸ਼ਾਨ ਲਗਾਓ; ਰਹਿ ਗਈਆਂ ਗੱਲਾਂ ਸਿਰਫ਼ ਯਾਦ ਦਿਹਾਨੀਆਂ ਹਨ, ਸ਼ਰਮ ਦਾ ਕਾਰਨ ਨਹੀਂ।")
    _done_habits = []
    for _i, (_en, _pa) in enumerate(_habits):
        _done_habits.append(st.checkbox(_pa if pa else _en, key="ds_habit_" + str(_i)))
    _habit_count = sum(_done_habits)
    st.progress(_habit_count / len(_habits))
    st.success(
        (str(_habit_count) + " of " + str(len(_habits)) + " learning reminders checked.")
        if not pa else
        (str(_habit_count) + " ਵਿੱਚੋਂ " + str(len(_habits)) + " ਸਿੱਖਣ ਵਾਲੀਆਂ ਯਾਦ ਦਿਹਾਨੀਆਂ ਚੁਣੀਆਂ।")
    )
    st.info(
        "Healthy environments also depend on access to clean water, soap, safe toilets and reliable waste services—not only individual choices."
        if not pa else
        "ਸਿਹਤਮੰਦ ਵਾਤਾਵਰਣ ਲਈ ਸਾਫ਼ ਪਾਣੀ, ਸਾਬਣ, ਸੁਰੱਖਿਅਤ ਟਾਇਲਟ ਅਤੇ ਕੂੜਾ ਪ੍ਰਬੰਧਨ ਦੀਆਂ ਸਹੂਲਤਾਂ ਵੀ ਲੋੜੀਂਦੀਆਂ ਹਨ; ਸਿਰਫ਼ ਨਿੱਜੀ ਆਦਤਾਂ ਕਾਫ਼ੀ ਨਹੀਂ।"
    )
    st.caption("Your checklist is kept only in this app session and is not a medical record." if not pa else "ਤੁਹਾਡੀ ਸੂਚੀ ਸਿਰਫ਼ ਇਸ ਐਪ ਸੈਸ਼ਨ ਵਿੱਚ ਰਹਿੰਦੀ ਹੈ ਅਤੇ ਇਹ ਮੈਡੀਕਲ ਰਿਕਾਰਡ ਨਹੀਂ ਹੈ।")



if st.session_state.ds_page == 7:
    st.header("🇮🇳 " + ("Community Health Awareness Challenge" if not pa else "ਭਾਈਚਾਰਕ ਸਿਹਤ ਜਾਗਰੂਕਤਾ ਚੁਣੌਤੀ"))
    st.write(
        "Take this short learning challenge, then encourage your classmates or family to discuss one practical action for a healthier, cleaner community."
        if not pa else
        "ਇਹ ਛੋਟੀ ਸਿੱਖਣ ਚੁਣੌਤੀ ਪੂਰੀ ਕਰੋ ਅਤੇ ਫਿਰ ਆਪਣੇ ਸਾਥੀਆਂ ਜਾਂ ਪਰਿਵਾਰ ਨਾਲ ਤੰਦਰੁਸਤ ਤੇ ਸਾਫ਼ ਭਾਈਚਾਰੇ ਲਈ ਇੱਕ ਅਮਲੀ ਕਦਮ ਬਾਰੇ ਗੱਲ ਕਰੋ।"
    )
    st.info(
        "Small actions, shared by many people, can support the Viksit Bharat @2047 vision."
        if not pa else
        "ਬਹੁਤ ਸਾਰੇ ਲੋਕਾਂ ਦੇ ਛੋਟੇ-ਛੋਟੇ ਕਦਮ ਵਿਕਸਿਤ ਭਾਰਤ @2047 ਦੇ ਸੁਪਨੇ ਨੂੰ ਮਜ਼ਬੂਤ ਕਰ ਸਕਦੇ ਹਨ।"
    )
    _community_questions = [
        ("Which action helps prevent the spread of many infections?", "Wash hands with soap", ["Share drinking cups", "Skip handwashing"], "ਕਿਹੜਾ ਕਦਮ ਕਈ ਇਨਫੈਕਸ਼ਨਾਂ ਦੇ ਫੈਲਾਅ ਨੂੰ ਰੋਕਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ?", "ਸਾਬਣ ਨਾਲ ਹੱਥ ਧੋਣੇ", ["ਇੱਕੋ ਗਿਲਾਸ ਸਾਂਝਾ ਕਰਨਾ", "ਹੱਥ ਨਾ ਧੋਣਾ"]),
        ("What should you do with a used battery?", "Take it to an approved collection point", ["Put it in wet waste", "Throw it into a drain"], "ਵਰਤੀ ਹੋਈ ਬੈਟਰੀ ਦਾ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ?", "ਇਸ ਨੂੰ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਇਕੱਠਾ ਕਰਨ ਵਾਲੀ ਥਾਂ ਦੇਣਾ", ["ਗਿੱਲੇ ਕੂੜੇ ਵਿੱਚ ਪਾਉਣਾ", "ਨਾਲੀ ਵਿੱਚ ਸੁੱਟਣਾ"]),
        ("Which is important for safer drinking water?", "Use a safe source and proper treatment", ["Assume all clear water is safe", "Store it in an uncovered container"], "ਸੁਰੱਖਿਅਤ ਪੀਣ ਵਾਲੇ ਪਾਣੀ ਲਈ ਕੀ ਜ਼ਰੂਰੀ ਹੈ?", "ਸੁਰੱਖਿਅਤ ਸਰੋਤ ਅਤੇ ਢੁੱਕਵਾਂ ਸ਼ੁੱਧੀਕਰਨ", ["ਸਾਫ਼ ਦਿਸਦੇ ਹਰ ਪਾਣੀ ਨੂੰ ਸੁਰੱਖਿਅਤ ਮੰਨਣਾ", "ਖੁੱਲ੍ਹੇ ਭਾਂਡੇ ਵਿੱਚ ਰੱਖਣਾ"]),
        ("Who helps create a cleaner community?", "Everyone, together", ["Only sanitation workers", "Only students"], "ਸਾਫ਼ ਭਾਈਚਾਰਾ ਬਣਾਉਣ ਵਿੱਚ ਕੌਣ ਯੋਗਦਾਨ ਪਾਉਂਦਾ ਹੈ?", "ਸਾਰੇ ਮਿਲ ਕੇ", ["ਸਿਰਫ਼ ਸਫ਼ਾਈ ਕਰਮਚਾਰੀ", "ਸਿਰਫ਼ ਵਿਦਿਆਰਥੀ"]),
        ("What is a useful school-community action?", "Share reliable health and hygiene awareness", ["Spread unverified health claims", "Ignore leaking taps"], "ਸਕੂਲ ਅਤੇ ਭਾਈਚਾਰੇ ਲਈ ਕਿਹੜਾ ਕਦਮ ਲਾਭਦਾਇਕ ਹੈ?", "ਭਰੋਸੇਯੋਗ ਸਿਹਤ ਅਤੇ ਸਫ਼ਾਈ ਜਾਗਰੂਕਤਾ ਸਾਂਝੀ ਕਰਨੀ", ["ਬਿਨਾਂ ਜਾਂਚੀਆਂ ਸਿਹਤ ਗੱਲਾਂ ਫੈਲਾਉਣੀਆਂ", "ਟਪਕਦੇ ਨਲਾਂ ਨੂੰ ਅਣਡਿੱਠਾ ਕਰਨਾ"]),
    ]
    _community_answers = []
    for _qi, _q in enumerate(_community_questions):
        _prompt = _q[3] if pa else _q[0]
        _correct = _q[4] if pa else _q[1]
        _wrong = _q[5] if pa else _q[2]
        _options = _wrong + [_correct]
        _community_answers.append(
            st.radio(
                _prompt,
                _options,
                index=None,
                key="ds_community_q_v2_" + str(_qi),
                help=("Select one answer." if not pa else "ਇੱਕ ਜਵਾਬ ਚੁਣੋ।")
            )
        )
    if st.button("Check my challenge" if not pa else "ਮੇਰੀ ਚੁਣੌਤੀ ਦੇ ਜਵਾਬ ਵੇਖੋ", type="primary", key="ds_community_check_v2"):
        if any(_answer is None for _answer in _community_answers):
            st.warning(
                "Please answer all five questions before checking your score."
                if not pa else
                "ਅੰਕ ਵੇਖਣ ਤੋਂ ਪਹਿਲਾਂ ਕਿਰਪਾ ਕਰਕੇ ਪੰਜੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦਿਓ।"
            )
        else:
            _score = sum(
                1 for _i, _answer in enumerate(_community_answers)
                if _answer == (_community_questions[_i][4] if pa else _community_questions[_i][1])
            )
            st.success(
                (f"You got {_score} out of 5. Keep learning and share one positive health action in your community!" if not pa else f"ਤੁਹਾਡੇ 5 ਵਿੱਚੋਂ {_score} ਜਵਾਬ ਸਹੀ ਹਨ। ਸਿੱਖਦੇ ਰਹੋ ਅਤੇ ਆਪਣੇ ਭਾਈਚਾਰੇ ਵਿੱਚ ਸਿਹਤ ਲਈ ਇੱਕ ਚੰਗਾ ਕਦਮ ਸਾਂਝਾ ਕਰੋ!")
            )
    st.markdown("### " + ("My community action" if not pa else "ਮੇਰਾ ਭਾਈਚਾਰਕ ਕਦਮ"))
    st.write(
        "Choose one realistic action: promote handwashing, keep drinking-water containers covered, use the correct waste bin, save water, or share trusted health information."
        if not pa else
        "ਇੱਕ ਅਮਲੀ ਕਦਮ ਚੁਣੋ: ਹੱਥ ਧੋਣ ਲਈ ਪ੍ਰੇਰਿਤ ਕਰਨਾ, ਪਾਣੀ ਦੇ ਭਾਂਡੇ ਢੱਕ ਕੇ ਰੱਖਣਾ, ਸਹੀ ਕੂੜੇਦਾਨ ਵਰਤਣਾ, ਪਾਣੀ ਬਚਾਉਣਾ ਜਾਂ ਭਰੋਸੇਯੋਗ ਸਿਹਤ ਜਾਣਕਾਰੀ ਸਾਂਝੀ ਕਰਨੀ।"
    )
    st.caption(
        "This is a learning activity. It does not collect or publish personal information."
        if not pa else
        "ਇਹ ਸਿੱਖਣ ਦੀ ਗਤੀਵਿਧੀ ਹੈ। ਇਹ ਨਿੱਜੀ ਜਾਣਕਾਰੀ ਇਕੱਠੀ ਜਾਂ ਪ੍ਰਕਾਸ਼ਿਤ ਨਹੀਂ ਕਰਦੀ।"
    )


if st.session_state.ds_page == 8:
    st.header("❤️ " + ("Health Learning Hub" if not pa else "ਸਿਹਤ ਸਿੱਖਿਆ ਕੇਂਦਰ"))
    st.write(
        "Build health literacy with reliable, age-appropriate information about the body, daily wellbeing and prevention. Good health is supported by personal choices as well as safe homes, schools and communities."
        if not pa else
        "ਸਰੀਰ, ਰੋਜ਼ਾਨਾ ਤੰਦਰੁਸਤੀ ਅਤੇ ਬਿਮਾਰੀਆਂ ਤੋਂ ਬਚਾਅ ਬਾਰੇ ਭਰੋਸੇਯੋਗ ਅਤੇ ਉਮਰ-ਅਨੁਕੂਲ ਜਾਣਕਾਰੀ ਨਾਲ ਸਿਹਤ ਦੀ ਸਮਝ ਵਧਾਓ। ਚੰਗੀ ਸਿਹਤ ਲਈ ਨਿੱਜੀ ਆਦਤਾਂ ਦੇ ਨਾਲ ਸੁਰੱਖਿਅਤ ਘਰ, ਸਕੂਲ ਅਤੇ ਭਾਈਚਾਰਾ ਵੀ ਜ਼ਰੂਰੀ ਹਨ।"
    )
    _health_topics = [
        (
            "🥗 Balanced nutrition" if not pa else "🥗 ਸੰਤੁਲਿਤ ਪੋਸ਼ਣ",
            "Eat a variety of foods such as vegetables, fruits, pulses, whole grains, nuts and suitable protein sources. Drink safe water and enjoy meals without skipping or following extreme diets. Food needs vary with age, activity, culture and health; no single food provides everything."
            if not pa else
            "ਸਬਜ਼ੀਆਂ, ਫਲ, ਦਾਲਾਂ, ਸਾਬਤ ਅਨਾਜ, ਮੇਵੇ ਅਤੇ ਢੁੱਕਵੇਂ ਪ੍ਰੋਟੀਨ ਵਾਲੇ ਵੱਖ-ਵੱਖ ਭੋਜਨ ਖਾਓ। ਸੁਰੱਖਿਅਤ ਪਾਣੀ ਪੀਓ ਅਤੇ ਖਾਣਾ ਛੱਡਣ ਜਾਂ ਬਹੁਤ ਸਖ਼ਤ ਡਾਇਟਾਂ ਦੀ ਥਾਂ ਸੰਤੁਲਿਤ ਭੋਜਨ ਚੁਣੋ। ਭੋਜਨ ਦੀ ਲੋੜ ਉਮਰ, ਸਰਗਰਮੀ, ਸੱਭਿਆਚਾਰ ਅਤੇ ਸਿਹਤ ਅਨੁਸਾਰ ਵੱਖ ਹੋ ਸਕਦੀ ਹੈ। ਕੋਈ ਇੱਕ ਭੋਜਨ ਸਾਰੇ ਪੋਸ਼ਕ ਤੱਤ ਨਹੀਂ ਦਿੰਦਾ।"
        ),
        (
            "🏃 Physical activity and movement" if not pa else "🏃 ਸਰੀਰਕ ਸਰਗਰਮੀ ਅਤੇ ਹਿਲਜੁਲ",
            "Regular enjoyable movement supports the heart, muscles, bones, mood and concentration. Walking, cycling, dancing, games and active play all count. Choose activities that are safe and suitable for your age and ability, take breaks, and avoid comparing your activity or body with others."
            if not pa else
            "ਨਿਯਮਿਤ ਅਤੇ ਮਨਪਸੰਦ ਸਰੀਰਕ ਸਰਗਰਮੀ ਦਿਲ, ਮਾਸਪੇਸ਼ੀਆਂ, ਹੱਡੀਆਂ, ਮਨੋਦਸ਼ਾ ਅਤੇ ਧਿਆਨ ਲਈ ਲਾਭਦਾਇਕ ਹੈ। ਤੁਰਨਾ, ਸਾਈਕਲ ਚਲਾਉਣਾ, ਨੱਚਣਾ, ਖੇਡਾਂ ਅਤੇ ਸਰਗਰਮ ਖੇਡਣਾ—ਸਭ ਗਿਣੇ ਜਾਂਦੇ ਹਨ। ਆਪਣੀ ਉਮਰ ਅਤੇ ਸਮਰੱਥਾ ਅਨੁਸਾਰ ਸੁਰੱਖਿਅਤ ਸਰਗਰਮੀ ਚੁਣੋ, ਵਿਚਕਾਰ ਆਰਾਮ ਕਰੋ ਅਤੇ ਆਪਣੀ ਤੁਲਨਾ ਹੋਰਾਂ ਨਾਲ ਨਾ ਕਰੋ।"
        ),
        (
            "😴 Sleep and rest" if not pa else "😴 ਨੀਂਦ ਅਤੇ ਆਰਾਮ",
            "A regular sleep routine helps learning, memory, mood and general wellbeing. Keep a calming bedtime routine, reduce bright screens close to bedtime when possible, and make the sleeping space comfortable and safe. If sleep problems persist and affect daily life, talk with a trusted adult and a healthcare professional."
            if not pa else
            "ਨਿਯਮਿਤ ਨੀਂਦ ਦੀ ਰੁਟੀਨ ਪੜ੍ਹਾਈ, ਯਾਦਦਾਸ਼ਤ, ਮਨੋਦਸ਼ਾ ਅਤੇ ਸਮੁੱਚੀ ਤੰਦਰੁਸਤੀ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਸੌਣ ਤੋਂ ਪਹਿਲਾਂ ਸ਼ਾਂਤ ਰੁਟੀਨ ਬਣਾਓ, ਸੰਭਵ ਹੋਵੇ ਤਾਂ ਸੌਣ ਦੇ ਨੇੜੇ ਤੇਜ਼ ਸਕ੍ਰੀਨ ਦੀ ਵਰਤੋਂ ਘਟਾਓ ਅਤੇ ਸੌਣ ਵਾਲੀ ਥਾਂ ਆਰਾਮਦਾਇਕ ਤੇ ਸੁਰੱਖਿਅਤ ਰੱਖੋ। ਜੇ ਨੀਂਦ ਦੀ ਸਮੱਸਿਆ ਲਗਾਤਾਰ ਰਹੇ ਅਤੇ ਰੋਜ਼ਾਨਾ ਜੀਵਨ ਪ੍ਰਭਾਵਿਤ ਕਰੇ ਤਾਂ ਭਰੋਸੇਯੋਗ ਵੱਡੇ ਅਤੇ ਸਿਹਤ ਮਾਹਿਰ ਨਾਲ ਗੱਲ ਕਰੋ।"
        ),
        (
            "🧠 Mental and emotional wellbeing" if not pa else "🧠 ਮਾਨਸਿਕ ਅਤੇ ਭਾਵਨਾਤਮਕ ਤੰਦਰੁਸਤੀ",
            "Feelings are a normal part of life. Talking with a trusted person, spending time with supportive people, taking breaks, enjoying hobbies and asking for help can support emotional wellbeing. If worry, sadness or stress feels difficult to manage, speak with a trusted adult, school counsellor or qualified professional."
            if not pa else
            "ਭਾਵਨਾਵਾਂ ਜੀਵਨ ਦਾ ਕੁਦਰਤੀ ਹਿੱਸਾ ਹਨ। ਭਰੋਸੇਯੋਗ ਵਿਅਕਤੀ ਨਾਲ ਗੱਲ ਕਰਨਾ, ਸਹਾਇਕ ਲੋਕਾਂ ਨਾਲ ਸਮਾਂ ਬਿਤਾਉਣਾ, ਆਰਾਮ ਕਰਨਾ, ਮਨਪਸੰਦ ਕੰਮ ਕਰਨਾ ਅਤੇ ਮਦਦ ਮੰਗਣਾ ਭਾਵਨਾਤਮਕ ਤੰਦਰੁਸਤੀ ਵਿੱਚ ਸਹਾਇਕ ਹੈ। ਜੇ ਚਿੰਤਾ, ਉਦਾਸੀ ਜਾਂ ਤਣਾਅ ਸੰਭਾਲਣਾ ਔਖਾ ਲੱਗੇ ਤਾਂ ਭਰੋਸੇਯੋਗ ਵੱਡੇ, ਸਕੂਲ ਕੌਂਸਲਰ ਜਾਂ ਯੋਗ ਮਾਹਿਰ ਨਾਲ ਗੱਲ ਕਰੋ।"
        ),
        (
            "🛡️ Preventing infections" if not pa else "🛡️ ਇਨਫੈਕਸ਼ਨਾਂ ਤੋਂ ਬਚਾਅ",
            "Handwashing, safe food and water, good ventilation, covering coughs and sneezes, and staying up to date with recommended vaccinations all help reduce infection risks. Follow current advice from qualified healthcare professionals and local public-health authorities."
            if not pa else
            "ਹੱਥ ਧੋਣਾ, ਸੁਰੱਖਿਅਤ ਭੋਜਨ ਅਤੇ ਪਾਣੀ, ਹਵਾਦਾਰੀ, ਖੰਘਣ-ਛਿੱਕਣ ਵੇਲੇ ਮੂੰਹ ਢੱਕਣਾ ਅਤੇ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੇ ਟੀਕਾਕਰਨ ਬਾਰੇ ਅਪਡੇਟ ਰਹਿਣਾ ਇਨਫੈਕਸ਼ਨ ਦੇ ਖਤਰੇ ਘਟਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਯੋਗ ਸਿਹਤ ਮਾਹਿਰਾਂ ਅਤੇ ਸਥਾਨਕ ਸਿਹਤ ਵਿਭਾਗ ਦੀ ਮੌਜੂਦਾ ਸਲਾਹ ਮੰਨੋ।"
        ),
        (
            "🩺 Check-ups and asking for help" if not pa else "🩺 ਸਿਹਤ ਜਾਂਚ ਅਤੇ ਮਦਦ ਲੈਣਾ",
            "Routine check-ups, dental care, vision checks and recommended vaccinations can support preventive health. Tell a trusted adult if you feel unwell or are worried about a health concern. Seek urgent help from an adult and local emergency services for severe or rapidly worsening symptoms. Do not self-diagnose or take medicines based only on app content."
            if not pa else
            "ਸਮੇਂ-ਸਮੇਂ 'ਤੇ ਸਿਹਤ ਜਾਂਚ, ਦੰਦਾਂ ਦੀ ਦੇਖਭਾਲ, ਨਜ਼ਰ ਦੀ ਜਾਂਚ ਅਤੇ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੇ ਟੀਕੇ ਰੋਕਥਾਮ ਵਾਲੀ ਸਿਹਤ ਸੰਭਾਲ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਜੇ ਤਬੀਅਤ ਠੀਕ ਨਾ ਹੋਵੇ ਜਾਂ ਕਿਸੇ ਸਿਹਤ ਸਮੱਸਿਆ ਦੀ ਚਿੰਤਾ ਹੋਵੇ ਤਾਂ ਭਰੋਸੇਯੋਗ ਵੱਡੇ ਨੂੰ ਦੱਸੋ। ਗੰਭੀਰ ਜਾਂ ਤੇਜ਼ੀ ਨਾਲ ਵਧ ਰਹੇ ਲੱਛਣਾਂ ਵਿੱਚ ਵੱਡੇ ਦੀ ਮਦਦ ਨਾਲ ਤੁਰੰਤ ਸਥਾਨਕ ਐਮਰਜੈਂਸੀ ਸੇਵਾ ਨਾਲ ਸੰਪਰਕ ਕਰੋ। ਸਿਰਫ਼ ਐਪ ਦੀ ਜਾਣਕਾਰੀ ਦੇ ਆਧਾਰ 'ਤੇ ਆਪਣੀ ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ ਜਾਂ ਦਵਾਈ ਨਾ ਕਰੋ।"
        ),
        (
            "🌞 Everyday wellbeing and safety" if not pa else "🌞 ਰੋਜ਼ਾਨਾ ਤੰਦਰੁਸਤੀ ਅਤੇ ਸੁਰੱਖਿਆ",
            "Spend time outdoors safely, use sun protection appropriate to the conditions, keep your surroundings clean, avoid tobacco and vaping, and never use someone else's medicines. Ask a trusted adult or qualified professional when you are unsure about a health claim."
            if not pa else
            "ਬਾਹਰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸਮਾਂ ਬਿਤਾਓ, ਮੌਸਮ ਅਨੁਸਾਰ ਧੁੱਪ ਤੋਂ ਬਚਾਅ ਕਰੋ, ਆਲੇ-ਦੁਆਲੇ ਸਾਫ਼ ਰੱਖੋ, ਤੰਬਾਕੂ ਅਤੇ ਵੇਪਿੰਗ ਤੋਂ ਦੂਰ ਰਹੋ ਅਤੇ ਕਿਸੇ ਹੋਰ ਦੀ ਦਵਾਈ ਕਦੇ ਨਾ ਵਰਤੋ। ਸਿਹਤ ਬਾਰੇ ਕਿਸੇ ਗੱਲ 'ਤੇ ਸ਼ੱਕ ਹੋਵੇ ਤਾਂ ਭਰੋਸੇਯੋਗ ਵੱਡੇ ਜਾਂ ਯੋਗ ਮਾਹਿਰ ਤੋਂ ਪੁੱਛੋ।"
        ),
    ]
    for _topic, _details in _health_topics:
        with st.expander(_topic):
            st.write(_details)

    st.divider()
    st.subheader("💡 " + ("Health knowledge check" if not pa else "ਸਿਹਤ ਜਾਣਕਾਰੀ ਦੀ ਜਾਂਚ"))
    _health_q = st.radio(
        "Which is a helpful everyday approach to health?" if not pa else "ਰੋਜ਼ਾਨਾ ਸਿਹਤ ਲਈ ਕਿਹੜਾ ਤਰੀਕਾ ਲਾਭਦਾਇਕ ਹੈ?",
        [
            "Skip meals to stay healthy" if not pa else "ਤੰਦਰੁਸਤ ਰਹਿਣ ਲਈ ਖਾਣਾ ਛੱਡਣਾ",
            "Balance food, enjoyable movement, sleep and support" if not pa else "ਸੰਤੁਲਿਤ ਭੋਜਨ, ਮਨਪਸੰਦ ਸਰਗਰਮੀ, ਨੀਂਦ ਅਤੇ ਸਹਾਇਤਾ",
            "Take medicines without asking an adult or professional" if not pa else "ਵੱਡੇ ਜਾਂ ਮਾਹਿਰ ਨੂੰ ਪੁੱਛੇ ਬਿਨਾਂ ਦਵਾਈ ਲੈਣਾ",
        ],
        index=None,
        key="ds_health_quiz_v1"
    )
    if st.button("Check answer" if not pa else "ਜਵਾਬ ਵੇਖੋ", key="ds_health_check_v1"):
        if _health_q is None:
            st.warning("Choose an answer first." if not pa else "ਪਹਿਲਾਂ ਇੱਕ ਜਵਾਬ ਚੁਣੋ।")
        elif _health_q == ("Balance food, enjoyable movement, sleep and support" if not pa else "ਸੰਤੁਲਿਤ ਭੋਜਨ, ਮਨਪਸੰਦ ਸਰਗਰਮੀ, ਨੀਂਦ ਅਤੇ ਸਹਾਇਤਾ"):
            st.success("Correct! Health is supported by several connected habits and supportive environments." if not pa else "ਸਹੀ! ਸਿਹਤ ਕਈ ਆਪਸ ਵਿੱਚ ਜੁੜੀਆਂ ਆਦਤਾਂ ਅਤੇ ਸਹਾਇਕ ਵਾਤਾਵਰਣ ਨਾਲ ਮਜ਼ਬੂਤ ਹੁੰਦੀ ਹੈ।")
        else:
            st.info("Try again. Healthy routines include balanced meals, enjoyable activity, rest and asking for support." if not pa else "ਫਿਰ ਕੋਸ਼ਿਸ਼ ਕਰੋ। ਚੰਗੀ ਰੁਟੀਨ ਵਿੱਚ ਸੰਤੁਲਿਤ ਭੋਜਨ, ਮਨਪਸੰਦ ਸਰਗਰਮੀ, ਆਰਾਮ ਅਤੇ ਲੋੜ ਪੈਣ 'ਤੇ ਮਦਦ ਲੈਣਾ ਸ਼ਾਮਲ ਹੈ।")
    st.info(
        "Health information here is general education, not a diagnosis or treatment plan. For personal concerns, speak with a trusted adult and a qualified healthcare professional."
        if not pa else
        "ਇੱਥੇ ਦਿੱਤੀ ਸਿਹਤ ਜਾਣਕਾਰੀ ਆਮ ਸਿੱਖਿਆ ਲਈ ਹੈ, ਨਿਦਾਨ ਜਾਂ ਇਲਾਜ ਦੀ ਯੋਜਨਾ ਨਹੀਂ। ਨਿੱਜੀ ਚਿੰਤਾ ਲਈ ਭਰੋਸੇਯੋਗ ਵੱਡੇ ਅਤੇ ਯੋਗ ਸਿਹਤ ਮਾਹਿਰ ਨਾਲ ਗੱਲ ਕਰੋ।"
    )



# Bottom navigation appears after each functional screen.
if st.session_state.ds_page > 0:
    _nav_bottom_left, _nav_bottom_right = st.columns(2)
    with _nav_bottom_left:
        st.button(
            "← Back" if not pa else "← ਪਿੱਛੇ",
            key="ds_bottom_back",
            disabled=st.session_state.ds_page == 0,
            on_click=_ds_move_page,
            args=(-1,),
            use_container_width=True
        )
    with _nav_bottom_right:
        st.button(
            "Next →" if not pa else "ਅੱਗੇ →",
            key="ds_bottom_next",
            disabled=st.session_state.ds_page == len(ds_pages) - 1,
            on_click=_ds_move_page,
            args=(1,),
            use_container_width=True
        )