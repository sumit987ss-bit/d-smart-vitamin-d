import streamlit as st
st.set_page_config(
    page_title="D-SMART",
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
    title = "ਵਿਟਾਮਿਨ D ਜਾਗਰੂਕਤਾ ਸਹਾਇਕ"
    intro = "ਆਪਣੀ ਸਿਹਤ ਬਾਰੇ ਸਿੱਖੋ ਅਤੇ ਵਿਟਾਮਿਨ D ਨੂੰ ਸਮਝੋ।"
    notice = (
        "ਇਹ ਸਿੱਖਿਆ ਲਈ ਹੈ। ਇਹ ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ ਨਹੀਂ ਕਰਦਾ "
        "ਅਤੇ ਡਾਕਟਰੀ ਸਲਾਹ ਦਾ ਬਦਲ ਨਹੀਂ ਹੈ।"
    )
    heading = "ਵਿਟਾਮਿਨ D ਜਾਗਰੂਕਤਾ ਪ੍ਰਸ਼ਨਾਵਲੀ"
    age_label = "ਤੁਹਾਡੀ ਉਮਰ (ਸਾਲ)"
    sun_label = "ਤੁਸੀਂ ਦਿਨ ਵੇਲੇ ਬਾਹਰ ਕਿੰਨੀ ਵਾਰ ਜਾਂਦੇ ਹੋ?"
    sun_options = ["ਰੋਜ਼ਾਨਾ", "ਹਫ਼ਤੇ ਵਿੱਚ ਕਈ ਵਾਰ", "ਬਹੁਤ ਘੱਟ"]
    food_label = "ਤੁਸੀਂ ਵਿਟਾਮਿਨ D ਵਾਲੇ ਭੋਜਨ ਕਿੰਨੀ ਵਾਰ ਖਾਂਦੇ ਹੋ?"
    food_options = ["ਅਕਸਰ", "ਕਦੇ-ਕਦੇ", "ਬਹੁਤ ਘੱਟ", "ਪਤਾ ਨਹੀਂ"]
    concern_label = "ਕੀ ਤੁਹਾਨੂੰ ਹੱਡੀਆਂ ਜਾਂ ਮਾਸਪੇਸ਼ੀਆਂ ਬਾਰੇ ਚਿੰਤਾ ਹੈ?"
    concern_options = ["ਨਹੀਂ", "ਹਾਂ", "ਪੱਕਾ ਨਹੀਂ"]
    test_label = "ਕੀ ਤੁਸੀਂ ਵਿਟਾਮਿਨ D ਦਾ ਖੂਨ ਟੈਸਟ ਕਰਵਾਇਆ ਹੈ?"
    test_options = ["ਹਾਂ", "ਨਹੀਂ", "ਪਤਾ ਨਹੀਂ"]
    button = "ਮੇਰੀ ਜਾਗਰੂਕਤਾ ਗਾਈਡ ਦਿਖਾਓ"
    result_title = "ਤੁਹਾਡੀ ਸਿੱਖਣ ਲਈ ਗਾਈਡ"
    sun_advice = (
        "ਸੁਰੱਖਿਅਤ ਧੁੱਪ ਅਤੇ ਦਿਨ ਦੀ ਰੌਸ਼ਨੀ ਬਾਰੇ ਸਿੱਖੋ। "
        "ਲੋੜੀਂਦੀ ਧੁੱਪ ਹਰ ਵਿਅਕਤੀ ਲਈ ਵੱਖਰੀ ਹੋ ਸਕਦੀ ਹੈ।"
    )
    food_advice = (
        "ਵਿਟਾਮਿਨ D ਦੇ ਸਰੋਤਾਂ ਵਿੱਚ ਚਰਬੀ ਵਾਲੀ ਮੱਛੀ, "
        "ਅੰਡੇ ਦੀ ਜ਼ਰਦੀ ਅਤੇ ਵਿਟਾਮਿਨ D ਮਿਲਾਇਆ ਭੋਜਨ ਸ਼ਾਮਲ ਹਨ।"
    )
    health_advice = (
        "ਹੱਡੀਆਂ ਜਾਂ ਮਾਸਪੇਸ਼ੀਆਂ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਦੇ ਕਈ ਕਾਰਨ ਹੋ ਸਕਦੇ ਹਨ। "
        "ਸਿਹਤ ਮਾਹਿਰ ਨਾਲ ਸਲਾਹ ਕਰੋ।"
    )
    test_advice = (
        "ਹਰ ਵਿਅਕਤੀ ਲਈ ਖੂਨ ਟੈਸਟ ਜ਼ਰੂਰੀ ਨਹੀਂ ਹੁੰਦਾ। "
        "ਸਿਹਤ ਮਾਹਿਰ ਦੱਸ ਸਕਦਾ ਹੈ ਕਿ ਟੈਸਟ ਦੀ ਲੋੜ ਹੈ ਜਾਂ ਨਹੀਂ।"
    )
    report_advice = (
        "ਰਿਪੋਰਟ ਨੂੰ ਸਮਝਣ ਲਈ ਸਿਹਤ ਮਾਹਿਰ ਦੀ ਸਲਾਹ ਲਵੋ।"
    )
    safe_end = (
        "ਇਹ ਪ੍ਰਸ਼ਨਾਵਲੀ ਸਿਰਫ਼ ਜਾਗਰੂਕਤਾ ਲਈ ਹੈ। "
        "ਇਹ ਤੁਹਾਡੇ ਵਿਟਾਮਿਨ D ਦੇ ਪੱਧਰ ਦੀ ਪੁਸ਼ਟੀ ਨਹੀਂ ਕਰਦੀ।"
    )
    learn_title = "ਵਿਟਾਮਿਨ D ਬਾਰੇ ਜਾਣੋ"
    why_title = "ਵਿਟਾਮਿਨ D ਕਿਉਂ ਜ਼ਰੂਰੀ ਹੈ?"
    why_text = (
        "ਵਿਟਾਮਿਨ D ਸਰੀਰ ਨੂੰ ਕੈਲਸ਼ੀਅਮ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ "
        "ਅਤੇ ਹੱਡੀਆਂ ਤੇ ਮਾਸਪੇਸ਼ੀਆਂ ਦੀ ਸਿਹਤ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ।"
    )
    sources_title = "ਵਿਟਾਮਿਨ D ਦੇ ਭੋਜਨ ਸਰੋਤ"
    sources_text = (
        "ਚਰਬੀ ਵਾਲੀ ਮੱਛੀ, ਅੰਡੇ ਦੀ ਜ਼ਰਦੀ ਅਤੇ ਵਿਟਾਮਿਨ D ਮਿਲਾਇਆ "
        "ਭੋਜਨ ਇਸ ਦੇ ਸਰੋਤ ਹਨ।"
    )
    symptoms_title = "ਕੀ ਲੱਛਣਾਂ ਨਾਲ ਕਮੀ ਦੀ ਪੁਸ਼ਟੀ ਹੋ ਸਕਦੀ ਹੈ?"
    symptoms_text = (
        "ਨਹੀਂ। ਸਿਰਫ਼ ਲੱਛਣਾਂ ਨਾਲ ਵਿਟਾਮਿਨ D ਦੀ ਕਮੀ ਦੀ ਪੁਸ਼ਟੀ ਨਹੀਂ ਹੁੰਦੀ। "
        "ਲੋੜ ਪੈਣ 'ਤੇ ਡਾਕਟਰੀ ਜਾਂਚ ਅਤੇ ਖੂਨ ਟੈਸਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।"
    )
else:
    title = "Your Vitamin D Awareness Assistant"
    intro = "Learn about Vitamin D and make informed health choices."
    notice = (
        "This is an educational tool. It cannot diagnose deficiency "
        "or replace professional medical advice."
    )
    heading = "Your Vitamin D Awareness Check"
    age_label = "Your age (years)"
    sun_label = "How often are you outdoors in daylight?"
    sun_options = ["Daily", "Several days a week", "Rarely"]
    food_label = "How often do you eat Vitamin D-containing foods?"
    food_options = ["Often", "Sometimes", "Rarely", "Not sure"]
    concern_label = "Any concerns about bone or muscle health?"
    concern_options = ["No particular concern", "Yes, I have concerns", "Not sure"]
    test_label = "Have you had a Vitamin D blood test?"
    test_options = ["Yes", "No", "Not sure"]
    button = "Get My Awareness Guidance"
    result_title = "Your Learning Guide"
    sun_advice = (
        "Learn about safe daylight exposure. Requirements vary "
        "depending on several personal and environmental factors."
    )
    food_advice = (
        "Sources include oily fish, egg yolks and foods fortified "
        "with Vitamin D."
    )
    health_advice = (
        "Bone or muscle concerns can have many causes. "
        "Consult a healthcare professional."
    )
    test_advice = (
        "A blood test is not necessary for everyone. "
        "A healthcare professional can advise whether it is appropriate."
    )
    report_advice = (
        "Ask a healthcare professional to interpret your report "
        "in the context of your health."
    )
    safe_end = (
        "This questionnaire provides awareness guidance only. "
        "It cannot determine your Vitamin D level."
    )
    learn_title = "Learn About Vitamin D"
    why_title = "Why is Vitamin D important?"
    why_text = (
        "Vitamin D helps your body absorb calcium and supports "
        "healthy bones and muscles."
    )
    sources_title = "Food sources of Vitamin D"
    sources_text = (
        "Sources include oily fish, egg yolks and foods fortified "
        "with Vitamin D."
    )
    symptoms_title = "Can symptoms confirm deficiency?"
    symptoms_text = (
        "No. Symptoms alone cannot confirm deficiency. "
        "Clinical assessment and, when appropriate, a blood test are used."
    )


# ---------- MOBILE SCREEN NAVIGATION ----------
# Screen navigation preserves the existing feature code below.
ds_pages = ["Welcome", "Home", "Awareness", "Learn", "Report", "Converter", "Quiz", "About", "AI Assistant", "Impact Lab"]

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

if st.session_state.ds_page > 0:
    st.selectbox(
        "Go to screen / ਸਕ੍ਰੀਨ ਚੁਣੋ",
        ds_pages[1:],
        key="ds_nav",
        on_change=_ds_sync_nav
    )
    _nav_left, _nav_right = st.columns(2)
    with _nav_left:
        st.button(
            "← Back" if not pa else "← ਪਿੱਛੇ",
            key="ds_top_back",
            disabled=st.session_state.ds_page <= 1,
            on_click=_ds_move_page,
            args=(-1,),
            use_container_width=True
        )
    with _nav_right:
        st.button(
            "Next →" if not pa else "ਅੱਗੇ →",
            key="ds_top_next",
            disabled=st.session_state.ds_page == len(ds_pages) - 1,
            on_click=_ds_move_page,
            args=(1,),
            use_container_width=True
        )
    st.caption(
        f"Screen {st.session_state.ds_page} of {len(ds_pages) - 1}"
        if not pa else
        f"ਸਕ੍ਰੀਨ {st.session_state.ds_page} / {len(ds_pages) - 1}"
    )
    st.divider()


if st.session_state.ds_page == 0:
    # Welcome / splash screen. The actual app begins on the next screen.
    st.markdown(
        f"""
        <div class="ds-welcome">
          <div class="ds-sun">☀️</div>
          <div class="ds-brand">D-SMART</div>
          <div class="ds-welcome-sub">{'ਵਿਟਾਮਿਨ D ਜਾਗਰੂਕਤਾ ਸਹਾਇਕ' if pa else 'Vitamin D Awareness Assistant'}</div>
          <div class="ds-welcome-copy">
            {'ਵਿਗਿਆਨ ਅਤੇ ਤਕਨਾਲੋਜੀ ਰਾਹੀਂ ਸਿਹਤ ਬਾਰੇ ਸਿੱਖੋ।' if pa else 'A brighter way to learn about Vitamin D, understand reports, and build health awareness.'}
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
            "ਸ਼ੁਰੂ ਕਰੋ  →" if pa else "Start D-SMART  →",
            key="ds_start_app",
            on_click=_ds_move_page,
            args=(1,),
            type="primary",
            use_container_width=True
        )

if st.session_state.ds_page == 1:
    # Clean home screen: app introduction and Science Exhibition Mode.
    
    st.title("☀️ D-SMART")
    st.subheader(title)
    st.write(intro)
    st.info(notice)
    
    # ---------- SCIENCE EXHIBITION MODE ----------
    
    with st.expander(
        "🏆 Science Exhibition Mode" if not pa
        else "🏆 ਵਿਗਿਆਨ ਪ੍ਰਦਰਸ਼ਨੀ ਮੋਡ",
        expanded=False
    ):
        if not pa:
            st.subheader("The Problem")
            st.write(
                "Many people hear about Vitamin D but may not understand "
                "its role, food sources, laboratory units, or the limits "
                "of interpreting a blood test."
            )
    
            st.subheader("Our Solution")
            st.write(
                "D-SMART is a bilingual educational assistant that "
                "provides awareness guidance, explains Vitamin D report "
                "units, and tests learning through an interactive quiz."
            )
    
            st.subheader("How It Works")
            st.markdown(
                "1. Select English or Punjabi.\n"
                "2. Complete the awareness questionnaire.\n"
                "3. Explore Vitamin D learning resources.\n"
                "4. Enter a report value and its unit for an educational explanation.\n"
                "5. Complete the quiz and review the answers."
            )
    
            st.subheader("What Makes It Useful?")
            st.write(
                "It brings bilingual health education, unit conversion, "
                "report-reading awareness, and interactive learning "
                "together in one simple app."
            )
    
            st.subheader("Important Limitation")
            st.warning(
                "D-SMART does not diagnose Vitamin D deficiency, "
                "automatically read report images, or prescribe supplements. "
                "Its explanations are educational and should be discussed "
                "with a healthcare professional when needed."
            )
    
            st.subheader("Live Demonstration")
            st.markdown(
                "1. Switch between English and Punjabi.\n"
                "2. Complete the awareness questionnaire.\n"
                "3. Convert a sample report value between ng/mL and nmol/L.\n"
                "4. Try the quiz and show the answer explanations."
            )
    
        else:
            st.subheader("ਸਮੱਸਿਆ")
            st.write(
                "ਕਈ ਲੋਕ ਵਿਟਾਮਿਨ D ਬਾਰੇ ਸੁਣਦੇ ਹਨ, ਪਰ ਇਸ ਦੀ ਮਹੱਤਤਾ, "
                "ਭੋਜਨ ਸਰੋਤਾਂ, ਲੈਬ ਰਿਪੋਰਟ ਦੀਆਂ ਇਕਾਈਆਂ ਅਤੇ ਨਤੀਜਿਆਂ "
                "ਨੂੰ ਸਮਝਣ ਦੀਆਂ ਸੀਮਾਵਾਂ ਬਾਰੇ ਪੂਰੀ ਜਾਣਕਾਰੀ ਨਹੀਂ ਰੱਖਦੇ।"
            )
    
            st.subheader("ਸਾਡਾ ਹੱਲ")
            st.write(
                "D-SMART ਇੱਕ ਦੋ-ਭਾਸ਼ਾਈ ਸਿੱਖਿਆ ਸਹਾਇਕ ਹੈ ਜੋ "
                "ਵਿਟਾਮਿਨ D ਬਾਰੇ ਜਾਗਰੂਕਤਾ, ਰਿਪੋਰਟ ਦੀਆਂ ਇਕਾਈਆਂ ਦੀ "
                "ਵਿਆਖਿਆ ਅਤੇ ਇੰਟਰਐਕਟਿਵ ਕਵਿਜ਼ ਰਾਹੀਂ ਸਿੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।"
            )
    
            st.subheader("ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ?")
            st.markdown(
                "1. ਪੰਜਾਬੀ ਜਾਂ ਅੰਗਰੇਜ਼ੀ ਚੁਣੋ।\n"
                "2. ਜਾਗਰੂਕਤਾ ਪ੍ਰਸ਼ਨਾਵਲੀ ਭਰੋ।\n"
                "3. ਵਿਟਾਮਿਨ D ਬਾਰੇ ਜਾਣਕਾਰੀ ਪੜ੍ਹੋ।\n"
                "4. ਰਿਪੋਰਟ ਦਾ ਮੁੱਲ ਅਤੇ ਇਕਾਈ ਦਰਜ ਕਰਕੇ ਸਿੱਖਿਆ ਲਈ ਵਿਆਖਿਆ ਵੇਖੋ।\n"
                "5. ਕਵਿਜ਼ ਹੱਲ ਕਰੋ ਅਤੇ ਸਹੀ ਜਵਾਬਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।"
            )
    
            st.subheader("ਇਸ ਦੀ ਵਿਸ਼ੇਸ਼ਤਾ")
            st.write(
                "ਇਹ ਇੱਕੋ ਐਪ ਵਿੱਚ ਪੰਜਾਬੀ ਅਤੇ ਅੰਗਰੇਜ਼ੀ ਸਿਹਤ ਸਿੱਖਿਆ, "
                "ਇਕਾਈ ਬਦਲਣ ਦੀ ਸਹੂਲਤ ਅਤੇ ਇੰਟਰਐਕਟਿਵ ਸਿੱਖਣ ਦਾ ਅਨੁਭਵ ਦਿੰਦਾ ਹੈ।"
            )
    
            st.subheader("ਮਹੱਤਵਪੂਰਨ ਸੀਮਾ")
            st.warning(
                "D-SMART ਵਿਟਾਮਿਨ D ਦੀ ਕਮੀ ਦੀ ਪਛਾਣ ਨਹੀਂ ਕਰਦਾ, "
                "ਰਿਪੋਰਟ ਦੀ ਤਸਵੀਰ ਆਪਣੇ ਆਪ ਨਹੀਂ ਪੜ੍ਹਦਾ ਅਤੇ ਸਪਲੀਮੈਂਟ "
                "ਦੀ ਖੁਰਾਕ ਨਹੀਂ ਦੱਸਦਾ। ਲੋੜ ਪੈਣ 'ਤੇ ਸਿਹਤ ਮਾਹਿਰ ਨਾਲ ਸਲਾਹ ਕਰੋ।"
            )
    
            st.subheader("ਲਾਈਵ ਪ੍ਰਦਰਸ਼ਨ")
            st.markdown(
                "1. ਪੰਜਾਬੀ ਅਤੇ ਅੰਗਰੇਜ਼ੀ ਬਦਲ ਕੇ ਦਿਖਾਓ।\n"
                "2. ਜਾਗਰੂਕਤਾ ਪ੍ਰਸ਼ਨਾਵਲੀ ਭਰੋ।\n"
                "3. ਨਮੂਨਾ ਰਿਪੋਰਟ ਦੀ ਇਕਾਈ ਬਦਲ ਕੇ ਦਿਖਾਓ।\n"
                "4. ਕਵਿਜ਼ ਹੱਲ ਕਰਕੇ ਸਹੀ ਜਵਾਬਾਂ ਦੀ ਵਿਆਖਿਆ ਦਿਖਾਓ।"
            )
    st.divider()
    

if st.session_state.ds_page == 2:
    st.header(heading)
    
    age = st.number_input(
        age_label, min_value=1, max_value=120, value=18
    )
    
    
    sunlight = st.selectbox(sun_label, sun_options)
    food = st.selectbox(food_label, food_options)
    concern = st.selectbox(concern_label, concern_options)
    tested = st.radio(test_label, test_options)
    
    
    if st.button(button, type="primary"):
        st.subheader(result_title)
    
        # Daylight guidance
        if sunlight == sun_options[2]:
            st.write(sun_advice)
        elif sunlight == sun_options[1]:
            st.write(
                "Consider learning more about safe daylight exposure "
                "and how individual needs can differ."
                if not pa else
                "ਸੁਰੱਖਿਅਤ ਧੁੱਪ ਅਤੇ ਦਿਨ ਦੀ ਰੌਸ਼ਨੀ ਬਾਰੇ ਹੋਰ ਜਾਣੋ। "
                "ਹਰ ਵਿਅਕਤੀ ਦੀ ਲੋੜ ਵੱਖਰੀ ਹੋ ਸਕਦੀ ਹੈ।"
            )
    
        # Food guidance
        if food in food_options[2:]:
            st.write(food_advice)
        elif food == food_options[1]:
            st.write(
                "Explore food sources of Vitamin D and check whether "
                "foods fortified with Vitamin D are available to you."
                if not pa else
                "ਵਿਟਾਮਿਨ D ਵਾਲੇ ਭੋਜਨ ਸਰੋਤਾਂ ਬਾਰੇ ਜਾਣੋ ਅਤੇ ਵੇਖੋ ਕਿ "
                "ਵਿਟਾਮਿਨ D ਮਿਲਾਇਆ ਭੋਜਨ ਉਪਲਬਧ ਹੈ ਜਾਂ ਨਹੀਂ।"
            )
    
        # Age-aware educational note
        if age < 18:
            st.info(
                "If you have health concerns, discuss them with a parent "
                "or trusted adult and a healthcare professional."
                if not pa else
                "ਜੇ ਸਿਹਤ ਬਾਰੇ ਚਿੰਤਾ ਹੈ, ਤਾਂ ਮਾਪਿਆਂ ਜਾਂ ਭਰੋਸੇਯੋਗ ਵੱਡੇ "
                "ਅਤੇ ਸਿਹਤ ਮਾਹਿਰ ਨਾਲ ਗੱਲ ਕਰੋ।"
            )
    
        # Health concerns
        if concern == concern_options[1]:
            st.warning(health_advice)
        elif concern == concern_options[2]:
            st.write(
                "If you are unsure, a healthcare professional can help "
                "you decide whether any assessment is needed."
                if not pa else
                "ਜੇ ਤੁਹਾਨੂੰ ਪੱਕਾ ਪਤਾ ਨਹੀਂ, ਤਾਂ ਸਿਹਤ ਮਾਹਿਰ ਦੱਸ ਸਕਦਾ ਹੈ "
                "ਕਿ ਜਾਂਚ ਦੀ ਲੋੜ ਹੈ ਜਾਂ ਨਹੀਂ।"
            )
    
        # Testing guidance
        if tested == test_options[1] or tested == test_options[2]:
            st.write(test_advice)
        elif tested == test_options[0]:
            st.write(report_advice)
    
        st.success(safe_end)
    
    st.divider()
    

if st.session_state.ds_page == 3:
    st.header(learn_title)
    
    with st.expander(why_title):
        st.write(why_text)
    
    with st.expander(sources_title):
        st.write(sources_text)
    
    with st.expander(symptoms_title):
        st.write(symptoms_text)
    
    st.caption("D-SMART | Science Exhibition Project")
    
    st.divider()
    
    

if st.session_state.ds_page == 4:
    # ---------- D-SMART REPORT ASSISTANT ----------
    
    st.divider()
    
    st.header(
        "🧪 Vitamin D Report Assistant"
        if not pa else
        "🧪 ਵਿਟਾਮਿਨ D ਰਿਪੋਰਟ ਸਹਾਇਕ"
    )
    
    st.write(
        "Choose how you want to understand your report."
        if not pa else
        "ਚੁਣੋ ਕਿ ਤੁਸੀਂ ਆਪਣੀ ਰਿਪੋਰਟ ਕਿਵੇਂ ਸਮਝਣਾ ਚਾਹੁੰਦੇ ਹੋ।"
    )
    
    mode = st.radio(
        "Report option / ਰਿਪੋਰਟ ਦਾ ਵਿਕਲਪ",
        [
            "I know the unit",
            "I don't know the unit",
            "I have a report photo"
        ] if not pa else [
            "ਮੈਨੂੰ ਇਕਾਈ ਪਤਾ ਹੈ",
            "ਮੈਨੂੰ ਇਕਾਈ ਪਤਾ ਨਹੀਂ",
            "ਮੇਰੇ ਕੋਲ ਰਿਪੋਰਟ ਦੀ ਫੋਟੋ ਹੈ"
        ],
        key="report_mode"
    )
    
    # Reference framework used for educational explanations.
    # ng/mL: below 12 = deficiency risk;
    # 12 to below 20 = may be inadequate for some;
    # 20 or above = adequate for most, under NIH guidance.
    
    def explain_vitamin_d(value_ng, punjabi=False):
        if value_ng < 12:
            if punjabi:
                st.error(
                    "ਨਤੀਜਾ 12 ng/mL ਤੋਂ ਘੱਟ ਹੈ। "
                    "ਇਹ ਵਿਟਾਮਿਨ D ਦੀ ਕਮੀ ਦੇ ਵਧੇ ਹੋਏ ਜੋਖਮ ਨਾਲ ਜੁੜਿਆ ਹੈ। "
                    "ਡਾਕਟਰੀ ਸਲਾਹ ਲਵੋ।"
                )
            else:
                st.error(
                    "Below 12 ng/mL: associated with increased "
                    "risk of Vitamin D deficiency. Seek medical advice."
                )
    
            st.write(
                f"{12 - value_ng:.1f} ng/mL below the "
                "12 ng/mL reference point."
                if not punjabi else
                f"12 ng/mL ਦੇ ਹਵਾਲਾ ਬਿੰਦੂ ਤੋਂ "
                f"{12 - value_ng:.1f} ng/mL ਘੱਟ।"
            )
    
        
        elif value_ng < 20:
            if punjabi:
                st.warning(
                    "ਨਤੀਜਾ 12 ਤੋਂ 20 ng/mL ਦੇ ਵਿਚਕਾਰ ਹੈ। "
                    "ਇਹ ਕੁਝ ਲੋਕਾਂ ਲਈ ਨਾਕਾਫ਼ੀ ਹੋ ਸਕਦਾ ਹੈ। "
                    "ਆਪਣੀ ਰਿਪੋਰਟ ਦੀ ਹਵਾਲਾ ਸੀਮਾ ਅਤੇ ਸਿਹਤ ਬਾਰੇ "
                    "ਸਿਹਤ ਮਾਹਿਰ ਨਾਲ ਸਲਾਹ ਕਰੋ।"
                )
            else:
                st.warning(
                    "Between 12 and 20 ng/mL: may be inadequate "
                    "for some people. Discuss the result with a "
                    "healthcare professional."
                )
    
            st.write(
                f"{20 - value_ng:.1f} ng/mL below the "
                "20 ng/mL reference point used for adequacy "
                "in most people."
                if not punjabi else
                f"ਬਹੁਤੇ ਲੋਕਾਂ ਲਈ ਵਰਤੇ ਜਾਂਦੇ 20 ng/mL ਦੇ "
                f"ਹਵਾਲਾ ਬਿੰਦੂ ਤੋਂ {20 - value_ng:.1f} ng/mL ਘੱਟ।"
            )
    
        else:
            if punjabi:
                st.success(
                    "ਇਹ ਨਤੀਜਾ NIH ਦੇ ਹਵਾਲਾ ਢਾਂਚੇ ਅਨੁਸਾਰ "
                    "ਬਹੁਤੇ ਲੋਕਾਂ ਲਈ ਕਾਫ਼ੀ ਮੰਨੇ ਜਾਂਦੇ ਪੱਧਰ 'ਤੇ ਹੈ। "
                    "ਆਪਣੀ ਲੈਬ ਦੀ ਹਵਾਲਾ ਸੀਮਾ ਵੀ ਵੇਖੋ।"
                )
            else:
                st.success(
                    "This is within the level considered adequate "
                    "for most people under the NIH framework. "
                    "Also check your laboratory's reference range."
                )
    
        st.caption(
            "Educational interpretation only. Reference thresholds "
            "vary, and this tool cannot diagnose a medical condition."
            if not punjabi else
            "ਇਹ ਸਿਰਫ਼ ਸਿੱਖਿਆ ਲਈ ਹੈ। ਹਵਾਲਾ ਸੀਮਾਵਾਂ ਵੱਖਰੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ; "
            "ਇਹ ਸਾਧਨ ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ ਨਹੀਂ ਕਰਦਾ।"
        )
    
    
    if mode in ["I know the unit", "ਮੈਨੂੰ ਇਕਾਈ ਪਤਾ ਹੈ"]:
    
        unit = st.selectbox(
            "Report unit / ਰਿਪੋਰਟ ਦੀ ਇਕਾਈ",
            ["ng/mL", "nmol/L"],
            key="known_unit"
        )
    
        value = st.number_input(
            "Enter the reported value / ਰਿਪੋਰਟ ਦਾ ਮੁੱਲ",
            min_value=0.0,
            max_value=1000.0,
            value=20.0,
            step=0.1,
            key="known_value"
        )
    
        if st.button(
            "Explain My Result" if not pa else "ਮੇਰੀ ਰਿਪੋਰਟ ਸਮਝਾਓ",
            key="known_explain"
        ):
            value_ng = value if unit == "ng/mL" else value / 2.5
    
            st.subheader(
                "Your result" if not pa else "ਤੁਹਾਡਾ ਨਤੀਜਾ"
            )
    
            st.write(f"{value_ng:.1f} ng/mL")
            st.write(f"{value_ng * 2.5:.1f} nmol/L")
    
            explain_vitamin_d(value_ng, pa)
    
    
    elif mode in ["I don't know the unit", "ਮੈਨੂੰ ਇਕਾਈ ਪਤਾ ਨਹੀਂ"]:
    
        unknown_value = st.number_input(
            "Enter the number shown / ਰਿਪੋਰਟ ਵਿੱਚ ਦਿੱਤਾ ਅੰਕ ਲਿਖੋ",
            min_value=0.0,
            max_value=1000.0,
            value=20.0,
            step=0.1,
            key="unknown_value"
        )
    
        if st.button(
            "Compare Both Possibilities" if not pa
            else "ਦੋਵੇਂ ਸੰਭਾਵਨਾਵਾਂ ਵੇਖੋ",
            key="unknown_compare"
        ):
            st.subheader(
                "Possible interpretations" if not pa
                else "ਸੰਭਾਵਿਤ ਵਿਆਖਿਆਵਾਂ"
            )
            st.info(
                "These are two possibilities, not a way to identify "
                "the actual unit. Check the report before relying on either."
                if not pa else
                "ਇਹ ਦੋ ਸੰਭਾਵਨਾਵਾਂ ਹਨ, ਅਸਲ ਇਕਾਈ ਦੀ ਪਛਾਣ ਨਹੀਂ। "
                "ਕਿਸੇ ਨਤੀਜੇ 'ਤੇ ਭਰੋਸਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਰਿਪੋਰਟ ਵੇਖੋ।"
            )
            st.markdown("### Possibility A: ng/mL")
            st.write(
                f"{unknown_value:.1f} ng/mL = "
                f"{unknown_value * 2.5:.1f} nmol/L"
            )
            explain_vitamin_d(unknown_value, pa)
    
            st.markdown("### Possibility B: nmol/L")
            value_as_ng = unknown_value / 2.5
            st.write(
                f"{unknown_value:.1f} nmol/L = "
                f"{value_as_ng:.1f} ng/mL"
            )
            explain_vitamin_d(value_as_ng, pa)
    
    
    else:
    
        st.subheader(
            "Upload a report image" if not pa
            else "ਰਿਪੋਰਟ ਦੀ ਤਸਵੀਰ ਅਪਲੋਡ ਕਰੋ"
        )
    
        st.warning(
            "For privacy, use a sample report or hide your name, "
            "date of birth, address, patient ID and other personal details."
            if not pa else
            "ਨਿੱਜਤਾ ਲਈ ਨਮੂਨਾ ਰਿਪੋਰਟ ਵਰਤੋ ਜਾਂ ਆਪਣਾ ਨਾਮ, "
            "ਜਨਮ ਮਿਤੀ, ਪਤਾ, ਮਰੀਜ਼ ID ਅਤੇ ਹੋਰ ਨਿੱਜੀ ਜਾਣਕਾਰੀ ਲੁਕਾਓ।"
        )
    
        uploaded_report = st.file_uploader(
            "Choose report image / ਰਿਪੋਰਟ ਦੀ ਤਸਵੀਰ ਚੁਣੋ",
            type=["png", "jpg", "jpeg"],
            key="report_image"
        )
    
        if uploaded_report is not None:
            st.image(
                uploaded_report,
                caption=(
                    "Report preview — values are not read automatically yet."
                    if not pa else
                    "ਰਿਪੋਰਟ ਦੀ ਝਲਕ — ਅਜੇ ਮੁੱਲ ਆਪਣੇ ਆਪ ਨਹੀਂ ਪੜ੍ਹੇ ਜਾਂਦੇ।"
                ),
                use_container_width=True
            )
    
            st.info(
                "Automatic report reading is our next development step. "
                "For now, select a known unit or enter the number manually."
                if not pa else
                "ਰਿਪੋਰਟ ਨੂੰ ਆਪਣੇ ਆਪ ਪੜ੍ਹਨ ਦੀ ਸਹੂਲਤ ਅਗਲਾ ਕਦਮ ਹੈ। "
                "ਫਿਲਹਾਲ ਇਕਾਈ ਚੁਣੋ ਜਾਂ ਅੰਕ ਖੁਦ ਦਰਜ ਕਰੋ।"
            )
    st.divider()
    
    

if st.session_state.ds_page == 5:
    # ---------- LIVE VITAMIN D UNIT CONVERTER ----------
    
    st.divider()
    
    st.header(
        "🔄 Live Vitamin D Unit Converter"
        if not pa else
        "🔄 ਵਿਟਾਮਿਨ D ਇਕਾਈ ਬਦਲਣ ਵਾਲਾ ਕੈਲਕੁਲੇਟਰ"
    )
    
    st.write(
        "Enter a sample value and see its converted value instantly."
        if not pa else
        "ਕੋਈ ਮੁੱਲ ਦਰਜ ਕਰੋ ਅਤੇ ਉਸ ਦੀ ਬਦਲੀ ਹੋਈ ਇਕਾਈ ਤੁਰੰਤ ਵੇਖੋ।"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        converter_value = st.number_input(
            "Enter value" if not pa else "ਮੁੱਲ ਦਰਜ ਕਰੋ",
            min_value=0.0,
            max_value=1000.0,
            value=20.0,
            step=0.1,
            key="live_converter_value"
        )
    
        converter_from = st.selectbox(
            "From unit" if not pa else "ਮੂਲ ਇਕਾਈ",
            ["ng/mL", "nmol/L"],
            key="live_converter_from"
        )
    
    with col2:
        converter_to = st.selectbox(
            "Convert to" if not pa else "ਬਦਲਣ ਵਾਲੀ ਇਕਾਈ",
            ["nmol/L", "ng/mL"],
            index=0,
            key="live_converter_to"
        )
    
    if converter_from == converter_to:
        converted_value = converter_value
    elif converter_from == "ng/mL":
        converted_value = converter_value * 2.5
    else:
        converted_value = converter_value / 2.5
    
    st.metric(
        label=(
            f"Converted value ({converter_to})"
            if not pa else
            f"ਬਦਲਿਆ ਮੁੱਲ ({converter_to})"
        ),
        value=f"{converted_value:.2f}"
    )
    
    st.caption(
        "Conversion: 1 ng/mL = 2.5 nmol/L."
        if not pa else
        "ਇਕਾਈ ਬਦਲਾਅ: 1 ng/mL = 2.5 nmol/L।"
    )
    
    st.info(
        "This calculator converts units only. It does not diagnose "
        "Vitamin D deficiency or determine whether a result is healthy."
        if not pa else
        "ਇਹ ਕੈਲਕੁਲੇਟਰ ਸਿਰਫ਼ ਇਕਾਈ ਬਦਲਦਾ ਹੈ। ਇਹ ਵਿਟਾਮਿਨ D ਦੀ ਕਮੀ "
        "ਦੀ ਪਛਾਣ ਜਾਂ ਨਤੀਜੇ ਦੇ ਸਿਹਤਮੰਦ ਹੋਣ ਦੀ ਪੁਸ਼ਟੀ ਨਹੀਂ ਕਰਦਾ।"
    )
    

if st.session_state.ds_page == 6:
    st.header(
        "🎯 Vitamin D Challenge Zone"
        if not pa else
        "🎯 ਵਿਟਾਮਿਨ D ਚੈਲੰਜ ਜ਼ੋਨ"
    )
    
    st.write(
        "Test your knowledge and earn points!"
        if not pa else
        "ਆਪਣੇ ਗਿਆਨ ਦੀ ਜਾਂਚ ਕਰੋ ਅਤੇ ਅੰਕ ਪ੍ਰਾਪਤ ਕਰੋ!"
    )
    
    questions = [
        {
            "q": "What does Vitamin D help the body absorb?",
            "pa": "ਵਿਟਾਮਿਨ D ਸਰੀਰ ਨੂੰ ਕੀ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ?",
            "options": ["Iron", "Calcium", "Sodium"],
            "options_pa": ["ਆਇਰਨ", "ਕੈਲਸ਼ੀਅਮ", "ਸੋਡੀਅਮ"],
            "answer": 1,
            "why": "Vitamin D helps the body absorb calcium.",
            "why_pa": "ਵਿਟਾਮਿਨ D ਸਰੀਰ ਨੂੰ ਕੈਲਸ਼ੀਅਮ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।"
        },
        {
            "q": "Which is a source of Vitamin D?",
            "pa": "ਵਿਟਾਮਿਨ D ਦਾ ਇੱਕ ਸਰੋਤ ਕਿਹੜਾ ਹੈ?",
            "options": ["Egg yolk", "Plain sugar", "Salt"],
            "options_pa": ["ਅੰਡੇ ਦੀ ਜ਼ਰਦੀ", "ਸਾਦੀ ਖੰਡ", "ਨਮਕ"],
            "answer": 0,
            "why": "Egg yolk contains Vitamin D.",
            "why_pa": "ਅੰਡੇ ਦੀ ਜ਼ਰਦੀ ਵਿੱਚ ਵਿਟਾਮਿਨ D ਹੁੰਦਾ ਹੈ।"
        },
        {
            "q": "Can symptoms alone confirm Vitamin D deficiency?",
            "pa": "ਕੀ ਸਿਰਫ਼ ਲੱਛਣਾਂ ਨਾਲ ਵਿਟਾਮਿਨ D ਦੀ ਕਮੀ ਦੀ ਪੁਸ਼ਟੀ ਹੋ ਸਕਦੀ ਹੈ?",
            "options": ["Yes", "No", "Always"],
            "options_pa": ["ਹਾਂ", "ਨਹੀਂ", "ਹਮੇਸ਼ਾ"],
            "answer": 1,
            "why": "Symptoms alone cannot confirm deficiency.",
            "why_pa": "ਸਿਰਫ਼ ਲੱਛਣਾਂ ਨਾਲ ਕਮੀ ਦੀ ਪੁਸ਼ਟੀ ਨਹੀਂ ਹੁੰਦੀ।"
        },
        {
            "q": "Which test measures Vitamin D status?",
            "pa": "ਵਿਟਾਮਿਨ D ਦਾ ਪੱਧਰ ਜਾਣਨ ਲਈ ਕਿਹੜਾ ਟੈਸਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ?",
            "options": [
                "25-hydroxyvitamin D blood test",
                "Eye test",
                "Hearing test"
            ],
            "options_pa": [
                "25-ਹਾਈਡ੍ਰੋਕਸੀ ਵਿਟਾਮਿਨ D ਖੂਨ ਟੈਸਟ",
                "ਅੱਖਾਂ ਦਾ ਟੈਸਟ",
                "ਸੁਣਨ ਦਾ ਟੈਸਟ"
            ],
            "answer": 0,
            "why": "The 25-hydroxyvitamin D blood test is commonly used.",
            "why_pa": "25-ਹਾਈਡ੍ਰੋਕਸੀ ਵਿਟਾਮਿਨ D ਦਾ ਖੂਨ ਟੈਸਟ ਆਮ ਤੌਰ 'ਤੇ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।"
        },
        {
            "q": "What should you do before taking high-dose supplements?",
            "pa": "ਵੱਧ ਖੁਰਾਕ ਵਾਲੇ ਸਪਲੀਮੈਂਟ ਲੈਣ ਤੋਂ ਪਹਿਲਾਂ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ?",
            "options": [
                "Take them without advice",
                "Seek professional advice",
                "Guess the dose"
            ],
            "options_pa": [
                "ਬਿਨਾਂ ਸਲਾਹ ਲੈਣਾ",
                "ਸਿਹਤ ਮਾਹਿਰ ਦੀ ਸਲਾਹ ਲੈਣਾ",
                "ਖੁਰਾਕ ਦਾ ਅੰਦਾਜ਼ਾ ਲਗਾਉਣਾ"
            ],
            "answer": 1,
            "why": "Professional advice helps avoid inappropriate dosing.",
            "why_pa": "ਸਿਹਤ ਮਾਹਿਰ ਦੀ ਸਲਾਹ ਗਲਤ ਖੁਰਾਕ ਤੋਂ ਬਚਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ।"
        }
    ]
    
    answers = []
    
    for i, question in enumerate(questions):
        q_text = question["pa"] if pa else question["q"]
        opts = question["options_pa"] if pa else question["options"]
    
        choice = st.radio(
            f"{i + 1}. {q_text}",
            opts,
            index=None,
            key=f"vitd_quiz_{i}"
        )
        answers.append(choice)
    
    if st.button(
        "Check My Score" if not pa else "ਮੇਰੇ ਅੰਕ ਦਿਖਾਓ",
        type="primary"
    ):
        if any(a is None for a in answers):
            st.warning(
                "Please answer all questions first."
                if not pa else
                "ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਸਾਰੇ ਪ੍ਰਸ਼ਨਾਂ ਦੇ ਜਵਾਬ ਦਿਓ।"
            )
        else:
            score = sum(
                answers[i] == (
                    questions[i]["options_pa"][questions[i]["answer"]]
                    if pa else
                    questions[i]["options"][questions[i]["answer"]]
                )
                for i in range(len(questions))
            )
    
            st.subheader(
                f"Your score: {score}/5"
                if not pa else
                f"ਤੁਹਾਡੇ ਅੰਕ: {score}/5"
            )
    
            st.progress(score / 5)
    
            if score == 5:
                st.balloons()
                st.success(
                    "Perfect score! Vitamin D Champion!"
                    if not pa else
                    "ਸ਼ਾਨਦਾਰ! ਤੁਸੀਂ ਵਿਟਾਮਿਨ D ਚੈਂਪੀਅਨ ਹੋ!"
                )
            elif score >= 3:
                st.success(
                    "Good work! Keep learning."
                    if not pa else
                    "ਬਹੁਤ ਵਧੀਆ! ਸਿੱਖਦੇ ਰਹੋ।"
                )
            else:
                st.info(
                    "Keep learning and try again."
                    if not pa else
                    "ਸਿੱਖਦੇ ਰਹੋ ਅਤੇ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।"
                )
    
            # Review answers for every completed quiz
            with st.expander(
                "📘 Review Answers & Explanations"
                if not pa else
                "📘 ਸਹੀ ਜਵਾਬ ਅਤੇ ਵਿਆਖਿਆ ਵੇਖੋ"
            ):
                for i, question in enumerate(questions):
                    correct = (
                        question["options_pa"][question["answer"]]
                        if pa else
                        question["options"][question["answer"]]
                    )
    
                    explanation = (
                        question["why_pa"] if pa else question["why"]
                    )
    
                    selected = answers[i]
    
                    if selected == correct:
                        st.success(
                            f"{i + 1}. {correct}"
                            if not pa else
                            f"{i + 1}. {correct} — ਸਹੀ ਜਵਾਬ"
                        )
                    else:
                        st.error(
                            f"{i + 1}. Correct answer: {correct}"
                            if not pa else
                            f"{i + 1}. ਸਹੀ ਜਵਾਬ: {correct}"
                        )
                        st.caption(
                            (
                                f"Your answer: {selected}"
                                if not pa else
                                f"ਤੁਹਾਡਾ ਜਵਾਬ: {selected}"
                            )
                        )
    
                    st.write(explanation)
    
    

if st.session_state.ds_page == 7:
    # ================= PROJECT CREDITS =================
    
    st.divider()
    
    with st.expander("🏫 About the Project & Credits | ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਜਾਣਕਾਰੀ", expanded=False):
    
        if language == "ਪੰਜਾਬੀ":
            st.markdown(
                """
                <div style="
                    background: linear-gradient(135deg, #e0f7f1, #e8f0ff);
                    padding: 24px;
                    border-radius: 18px;
                    text-align: center;
                    border: 1px solid #b8ded5;
                ">
                    <h1 style="color:#087e75; margin-bottom:5px;">
                        ☀️ D-SMART
                    </h1>
                    <h3 style="color:#244c58;">
                        ਵਿਟਾਮਿਨ D ਜਾਗਰੂਕਤਾ ਸਹਾਇਕ
                    </h3>
                    <p style="color:#435b62;">
                        ਵਿਗਿਆਨ • ਤਕਨਾਲੋਜੀ • ਸਿਹਤ ਜਾਗਰੂਕਤਾ
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
    
            st.markdown("### 🎯 ਪ੍ਰੋਜੈਕਟ ਦਾ ਉਦੇਸ਼")
            st.write(
                "D-SMART ਦਾ ਉਦੇਸ਼ ਵਿਟਾਮਿਨ D ਬਾਰੇ ਜਾਗਰੂਕਤਾ ਵਧਾਉਣਾ, "
                "ਵਰਤੋਂਕਾਰਾਂ ਨੂੰ ਸਿਹਤਮੰਦ ਆਦਤਾਂ ਬਾਰੇ ਸਿੱਖਿਆ ਦੇਣਾ ਅਤੇ "
                "ਵਿਟਾਮਿਨ D ਦੀ ਰਿਪੋਰਟ ਵਿੱਚ ਦਿੱਤੀ ਇਕਾਈ ਨੂੰ ਸਮਝਣ ਵਿੱਚ ਮਦਦ ਕਰਨਾ ਹੈ।"
            )
    
            st.markdown("### 👩‍🎓 ਵਿਦਿਆਰਥਣ")
            st.write("**Pawandeep Kaur**")
            st.write("ਜਮਾਤ: 9ਵੀਂ")
    
            st.markdown("### 👨‍🏫 ਮਾਰਗਦਰਸ਼ਕ ਅਧਿਆਪਕ")
            st.write("**Sumitpal Singh Sodhi**")
            st.write("ਅਹੁਦਾ: Science Master")
    
            st.markdown("### 🏫 ਸਕੂਲ")
            st.write("**GSSS Bare Ke, Ferozepur**")
            st.write("ਜ਼ਿਲ੍ਹਾ: Ferozepur, Punjab")
    
            st.markdown("### 💡 ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ")
            st.write("• ਪੰਜਾਬੀ ਅਤੇ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਜਾਣਕਾਰੀ")
            st.write("• ਵਿਟਾਮਿਨ D ਬਾਰੇ ਇੰਟਰਐਕਟਿਵ ਕਵਿਜ਼")
            st.write("• ਰਿਪੋਰਟ ਦੀ ਇਕਾਈ ਬਦਲਣ ਦੀ ਸਹੂਲਤ")
            st.write("• ਇਕਾਈ ਪਤਾ ਨਾ ਹੋਣ 'ਤੇ ਦੋਵੇਂ ਸੰਭਾਵਨਾਵਾਂ ਦੀ ਵਿਆਖਿਆ")
            st.write("• ਰਿਪੋਰਟ ਦੀ ਤਸਵੀਰ ਅਪਲੋਡ ਕਰਨ ਦੀ ਸਹੂਲਤ")
    
            st.info(
                "ਇਹ ਵਿਦਿਅਕ ਜਾਗਰੂਕਤਾ ਐਪ ਹੈ। ਇਹ ਡਾਕਟਰੀ ਜਾਂਚ, "
                "ਨਿਦਾਨ ਜਾਂ ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਦਾ ਬਦਲ ਨਹੀਂ ਹੈ।"
            )
    
        else:
            st.markdown(
                """
                <div style="
                    background: linear-gradient(135deg, #e0f7f1, #e8f0ff);
                    padding: 24px;
                    border-radius: 18px;
                    text-align: center;
                    border: 1px solid #b8ded5;
                ">
                    <h1 style="color:#087e75; margin-bottom:5px;">
                        ☀️ D-SMART
                    </h1>
                    <h3 style="color:#244c58;">
                        Vitamin D Awareness Assistant
                    </h3>
                    <p style="color:#435b62;">
                        Science • Technology • Health Awareness
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
    
            st.markdown("### 🎯 About the Project")
            st.write(
                "D-SMART aims to improve awareness about Vitamin D, "
                "educate users about healthy habits, and help them understand "
                "the units used in Vitamin D laboratory reports."
            )
    
            st.markdown("### 👩‍🎓 Student Developer")
            st.write("**Pawandeep Kaur**")
            st.write("Class: 9")
    
            st.markdown("### 👨‍🏫 Guided By")
            st.write("**Sumitpal Singh Sodhi**")
            st.write("Designation: Science Master")
    
            st.markdown("### 🏫 School Details")
            st.write("**GSSS Bare Ke, Ferozepur**")
            st.write("District: Ferozepur, Punjab")
    
            st.markdown("### 💡 Key Features")
            st.write("• Bilingual support: English and Punjabi")
            st.write("• Interactive Vitamin D awareness quiz")
            st.write("• Vitamin D unit conversion")
            st.write("• Explanation of results when the unit is unknown")
            st.write("• Laboratory report photo upload and preview")
    
            st.info(
                "D-SMART is an educational awareness tool. It does not "
                "replace professional medical advice, diagnosis, or treatment."
            )
    
        st.caption("Science Exhibition Project | Academic Session 2026–27")
    


if st.session_state.ds_page == 8:
    # ---------- GEMINI-POWERED AI HEALTH EDUCATION ASSISTANT ----------
    st.header(
        "🤖 D-SMART AI Assistant"
        if not pa else
        "🤖 D-SMART AI ਸਹਾਇਕ"
    )
    st.write(
        "Ask general questions about Vitamin D and receive a response generated by an AI model."
        if not pa else
        "ਵਿਟਾਮਿਨ D ਬਾਰੇ ਆਮ ਸਵਾਲ ਪੁੱਛੋ ਅਤੇ AI ਮਾਡਲ ਤੋਂ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰੋ।"
    )
    st.info(
        "Education only: the AI cannot diagnose a condition, interpret your personal case, or recommend supplement doses. Do not enter names, contact details, report photos, or other private health information."
        if not pa else
        "ਸਿਰਫ਼ ਸਿੱਖਿਆ ਲਈ: AI ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ, ਨਿੱਜੀ ਮੈਡੀਕਲ ਕੇਸ ਦੀ ਵਿਆਖਿਆ ਜਾਂ ਸਪਲੀਮੈਂਟ ਦੀ ਖੁਰਾਕ ਨਹੀਂ ਦੱਸਦਾ। ਨਾਮ, ਸੰਪਰਕ ਵੇਰਵੇ, ਰਿਪੋਰਟ ਦੀਆਂ ਤਸਵੀਰਾਂ ਜਾਂ ਨਿੱਜੀ ਸਿਹਤ ਜਾਣਕਾਰੀ ਨਾ ਦਰਜ ਕਰੋ।"
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
                    "Ask a Vitamin D question..."
                    if not pa else
                    "ਵਿਟਾਮਿਨ D ਬਾਰੇ ਸਵਾਲ ਪੁੱਛੋ..."
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
                "You are D-SMART, an AI health-education assistant focused on general Vitamin D science. "
                "Provide concise, evidence-informed educational explanations for school students and the public. "
                "Do not diagnose, estimate an individual's Vitamin D status, interpret a personal medical case, "
                "prescribe treatment, or recommend supplement doses. Do not claim symptoms alone prove deficiency. "
                "For personal lab results, medication/supplement questions, pregnancy, children, or ongoing symptoms, "
                "recommend discussing the matter with a qualified healthcare professional. Never request identifying "
                "or private health information. If a question is unrelated to Vitamin D or general health education, "
                "politely explain the assistant's limited scope. Be transparent about uncertainty and do not invent facts. "
                + _ds_language_instruction
                + "\\nConversation so far:\\n" + _ds_chat_context
            )

            try:
                from google import genai
                _ds_client = genai.Client(api_key=_ds_gemini_key)
                with st.spinner(
                    "D-SMART AI is preparing an answer..." if not pa
                    else "D-SMART AI ਜਵਾਬ ਤਿਆਰ ਕਰ ਰਿਹਾ ਹੈ..."
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


if st.session_state.ds_page == 9:
    # ---------- D-SMART IMPACT LAB: PRE-TEST, LEARN, POST-TEST, REPORT ----------
    st.header("📊 D-SMART Impact Lab" if not pa else "📊 D-SMART ਪ੍ਰਭਾਵ ਲੈਬ")
    st.write(
        "Measure what you learn about Vitamin D. This activity checks awareness, not anyone's Vitamin D level."
        if not pa else
        "ਵਿਟਾਮਿਨ D ਬਾਰੇ ਆਪਣੀ ਸਿੱਖਿਆ ਵਿੱਚ ਤਬਦੀਲੀ ਮਾਪੋ। ਇਹ ਗਤੀਵਿਧੀ ਜਾਗਰੂਕਤਾ ਜਾਂਚਦੀ ਹੈ, ਕਿਸੇ ਦਾ ਵਿਟਾਮਿਨ D ਪੱਧਰ ਨਹੀਂ।"
    )
    st.info(
        "Privacy: this demo stores results only in the current app session. It does not ask for your name or save a public record."
        if not pa else
        "ਨਿੱਜਤਾ: ਇਸ ਡੈਮੋ ਦੇ ਨਤੀਜੇ ਸਿਰਫ਼ ਮੌਜੂਦਾ ਸੈਸ਼ਨ ਵਿੱਚ ਰਹਿੰਦੇ ਹਨ। ਇਹ ਨਾਮ ਨਹੀਂ ਪੁੱਛਦਾ ਅਤੇ ਜਨਤਕ ਰਿਕਾਰਡ ਨਹੀਂ ਬਣਾਉਂਦਾ।"
    )

    _impact_questions = [
        {
            "en": "What is one important role of Vitamin D?",
            "pa": "ਵਿਟਾਮਿਨ D ਦਾ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਕੰਮ ਕੀ ਹੈ?",
            "opts": ["It helps the body absorb calcium", "It replaces all other vitamins", "It directly cures every illness"],
            "opts_pa": ["ਇਹ ਸਰੀਰ ਨੂੰ ਕੈਲਸ਼ੀਅਮ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ", "ਇਹ ਸਾਰੇ ਹੋਰ ਵਿਟਾਮਿਨਾਂ ਦੀ ਥਾਂ ਲੈਂਦਾ ਹੈ", "ਇਹ ਹਰ ਬਿਮਾਰੀ ਨੂੰ ਸਿੱਧਾ ਠੀਕ ਕਰਦਾ ਹੈ"],
            "answer": 0, "topic": "Role of Vitamin D",
            "topic_pa": "ਵਿਟਾਮਿਨ D ਦਾ ਕੰਮ"
        },
        {
            "en": "Which is a recognised source of Vitamin D?",
            "pa": "ਵਿਟਾਮਿਨ D ਦਾ ਮੰਨਿਆ ਹੋਇਆ ਸਰੋਤ ਕਿਹੜਾ ਹੈ?",
            "opts": ["Fortified foods", "Plain sugar", "Soft drinks"],
            "opts_pa": ["ਵਿਟਾਮਿਨ D ਮਿਲਾਇਆ ਭੋਜਨ", "ਸਾਦੀ ਖੰਡ", "ਮਿੱਠੇ ਪੇਅ"],
            "answer": 0, "topic": "Food sources",
            "topic_pa": "ਭੋਜਨ ਸਰੋਤ"
        },
        {
            "en": "Can symptoms alone confirm Vitamin D deficiency?",
            "pa": "ਕੀ ਸਿਰਫ਼ ਲੱਛਣਾਂ ਨਾਲ ਵਿਟਾਮਿਨ D ਦੀ ਕਮੀ ਪੱਕੀ ਹੋ ਸਕਦੀ ਹੈ?",
            "opts": ["Yes, always", "No, symptoms alone cannot confirm it", "Only by guessing"],
            "opts_pa": ["ਹਾਂ, ਹਮੇਸ਼ਾ", "ਨਹੀਂ, ਸਿਰਫ਼ ਲੱਛਣਾਂ ਨਾਲ ਪੁਸ਼ਟੀ ਨਹੀਂ ਹੁੰਦੀ", "ਸਿਰਫ਼ ਅੰਦਾਜ਼ੇ ਨਾਲ"],
            "answer": 1, "topic": "Symptoms and diagnosis",
            "topic_pa": "ਲੱਛਣ ਅਤੇ ਜਾਂਚ"
        },
        {
            "en": "Which test is commonly used to assess Vitamin D status?",
            "pa": "ਵਿਟਾਮਿਨ D ਦੀ ਸਥਿਤੀ ਜਾਂਚਣ ਲਈ ਆਮ ਤੌਰ 'ਤੇ ਕਿਹੜਾ ਟੈਸਟ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ?",
            "opts": ["25-hydroxyvitamin D blood test", "Eye colour test", "Hearing test"],
            "opts_pa": ["25-ਹਾਈਡ੍ਰੋਕਸੀ ਵਿਟਾਮਿਨ D ਖੂਨ ਟੈਸਟ", "ਅੱਖਾਂ ਦੇ ਰੰਗ ਦਾ ਟੈਸਟ", "ਸੁਣਨ ਦਾ ਟੈਸਟ"],
            "answer": 0, "topic": "Laboratory testing",
            "topic_pa": "ਲੈਬ ਟੈਸਟ"
        },
        {
            "en": "What should you do before taking high-dose supplements?",
            "pa": "ਵੱਧ ਖੁਰਾਕ ਵਾਲੇ ਸਪਲੀਮੈਂਟ ਲੈਣ ਤੋਂ ਪਹਿਲਾਂ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ?",
            "opts": ["Guess the dose", "Take them because a friend does", "Ask a qualified healthcare professional"],
            "opts_pa": ["ਖੁਰਾਕ ਦਾ ਅੰਦਾਜ਼ਾ ਲਗਾਉਣਾ", "ਦੋਸਤ ਲੈਂਦਾ ਹੈ ਇਸ ਲਈ ਲੈਣਾ", "ਯੋਗ ਸਿਹਤ ਮਾਹਿਰ ਦੀ ਸਲਾਹ ਲੈਣਾ"],
            "answer": 2, "topic": "Supplement safety",
            "topic_pa": "ਸਪਲੀਮੈਂਟ ਸੁਰੱਖਿਆ"
        }
    ]

    def _impact_run_quiz(form_key, phase_label):
        with st.form(form_key):
            _impact_selected = []
            for _iq, _item in enumerate(_impact_questions):
                _q_text = _item["pa"] if pa else _item["en"]
                _opts = _item["opts_pa"] if pa else _item["opts"]
                _impact_selected.append(
                    st.radio(
                        f"{_iq + 1}. {_q_text}",
                        _opts,
                        index=None,
                        key=f"{form_key}_q{_iq}"
                    )
                )
            _submitted = st.form_submit_button(
                phase_label, type="primary", use_container_width=True
            )
        if _submitted:
            if any(_answer is None for _answer in _impact_selected):
                st.warning(
                    "Please answer all five questions." if not pa else
                    "ਕਿਰਪਾ ਕਰਕੇ ਪੰਜੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦਿਓ।"
                )
            else:
                _score = 0
                for _iq, _answer in enumerate(_impact_selected):
                    _opts = _impact_questions[_iq]["opts_pa"] if pa else _impact_questions[_iq]["opts"]
                    if _answer == _opts[_impact_questions[_iq]["answer"]]:
                        _score += 1
                st.session_state[form_key.replace("_form", "") + "_score"] = _score
                st.session_state[f"{form_key}_answers"] = _impact_selected
                st.rerun()

    if "impact_pre_score" not in st.session_state:
        st.subheader("Step 1 — Baseline awareness" if not pa else "ਪੜਾਅ 1 — ਸ਼ੁਰੂਆਤੀ ਜਾਗਰੂਕਤਾ")
        st.write(
            "Answer before reading the lesson. Your score will be compared with the post-test."
            if not pa else
            "ਪਾਠ ਪੜ੍ਹਨ ਤੋਂ ਪਹਿਲਾਂ ਜਵਾਬ ਦਿਓ। ਤੁਹਾਡੇ ਅੰਕਾਂ ਦੀ ਬਾਅਦ ਵਾਲੇ ਟੈਸਟ ਨਾਲ ਤੁਲਨਾ ਹੋਵੇਗੀ।"
        )
        _impact_run_quiz("impact_pre_form", "Submit pre-test" if not pa else "ਸ਼ੁਰੂਆਤੀ ਟੈਸਟ ਜਮ੍ਹਾਂ ਕਰੋ")
    else:
        st.success(
            f"Pre-test recorded: {st.session_state.impact_pre_score}/5"
            if not pa else
            f"ਸ਼ੁਰੂਆਤੀ ਟੈਸਟ ਦਰਜ: {st.session_state.impact_pre_score}/5"
        )
        st.subheader("Step 2 — Learn" if not pa else "ਪੜਾਅ 2 — ਸਿੱਖੋ")
        with st.expander("1. Why Vitamin D matters" if not pa else "1. ਵਿਟਾਮਿਨ D ਕਿਉਂ ਜ਼ਰੂਰੀ ਹੈ", expanded=True):
            st.write(
                "Vitamin D helps the body absorb calcium and supports bone and muscle health."
                if not pa else
                "ਵਿਟਾਮਿਨ D ਸਰੀਰ ਨੂੰ ਕੈਲਸ਼ੀਅਮ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ ਅਤੇ ਹੱਡੀਆਂ ਤੇ ਮਾਸਪੇਸ਼ੀਆਂ ਦੀ ਸਿਹਤ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ।"
            )
        with st.expander("2. Sources and sunlight" if not pa else "2. ਸਰੋਤ ਅਤੇ ਧੁੱਪ"):
            st.write(
                "Sources include some oily fish, egg yolks and fortified foods. Sunlight needs vary with skin, location, season and other factors; avoid sunburn."
                if not pa else
                "ਕੁਝ ਚਰਬੀ ਵਾਲੀਆਂ ਮੱਛੀਆਂ, ਅੰਡੇ ਦੀ ਜ਼ਰਦੀ ਅਤੇ ਵਿਟਾਮਿਨ D ਮਿਲਾਇਆ ਭੋਜਨ ਸਰੋਤ ਹਨ। ਧੁੱਪ ਦੀ ਲੋੜ ਚਮੜੀ, ਸਥਾਨ, ਮੌਸਮ ਅਤੇ ਹੋਰ ਕਾਰਕਾਂ ਨਾਲ ਬਦਲਦੀ ਹੈ; ਚਮੜੀ ਸੜਨ ਤੋਂ ਬਚੋ।"
            )
        with st.expander("3. Reports, symptoms and safe decisions" if not pa else "3. ਰਿਪੋਰਟਾਂ, ਲੱਛਣ ਅਤੇ ਸੁਰੱਖਿਅਤ ਫੈਸਲੇ"):
            st.write(
                "Symptoms alone cannot confirm deficiency. A 25-hydroxyvitamin D blood test may be used when clinically appropriate. Do not start high-dose supplements without professional advice."
                if not pa else
                "ਸਿਰਫ਼ ਲੱਛਣਾਂ ਨਾਲ ਕਮੀ ਦੀ ਪੁਸ਼ਟੀ ਨਹੀਂ ਹੁੰਦੀ। ਲੋੜ ਹੋਣ 'ਤੇ 25-ਹਾਈਡ੍ਰੋਕਸੀ ਵਿਟਾਮਿਨ D ਖੂਨ ਟੈਸਟ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਸਿਹਤ ਮਾਹਿਰ ਦੀ ਸਲਾਹ ਤੋਂ ਬਿਨਾਂ ਵੱਧ ਖੁਰਾਕ ਵਾਲੇ ਸਪਲੀਮੈਂਟ ਸ਼ੁਰੂ ਨਾ ਕਰੋ।"
            )

        if "impact_post_score" not in st.session_state:
            st.subheader("Step 3 — Post-test" if not pa else "ਪੜਾਅ 3 — ਬਾਅਦ ਵਾਲਾ ਟੈਸਟ")
            st.write(
                "Answer the same five questions again to measure your learning."
                if not pa else
                "ਆਪਣੀ ਸਿੱਖਿਆ ਮਾਪਣ ਲਈ ਉਹੀ ਪੰਜ ਸਵਾਲ ਦੁਬਾਰਾ ਹੱਲ ਕਰੋ।"
            )
            _impact_run_quiz("impact_post_form", "Submit post-test" if not pa else "ਬਾਅਦ ਵਾਲਾ ਟੈਸਟ ਜਮ੍ਹਾਂ ਕਰੋ")
        else:
            _pre = st.session_state.impact_pre_score
            _post = st.session_state.impact_post_score
            _change = _post - _pre
            st.subheader("Step 4 — Your learning impact" if not pa else "ਪੜਾਅ 4 — ਤੁਹਾਡੀ ਸਿੱਖਿਆ ਦਾ ਪ੍ਰਭਾਵ")
            _c1, _c2, _c3 = st.columns(3)
            _c1.metric("Pre-test" if not pa else "ਪਹਿਲਾਂ", f"{_pre}/5")
            _c2.metric("Post-test" if not pa else "ਬਾਅਦ", f"{_post}/5")
            _c3.metric("Change" if not pa else "ਤਬਦੀਲੀ", f"{_change:+d}")
            st.progress(_post / 5)
            if _change > 0:
                st.success(
                    f"Your score improved by {_change} point(s). Keep learning!"
                    if not pa else
                    f"ਤੁਹਾਡੇ ਅੰਕ {_change} ਵਧੇ। ਸਿੱਖਦੇ ਰਹੋ!"
                )
            elif _change == 0:
                st.info(
                    "Your score stayed the same. Review the lesson and try again."
                    if not pa else
                    "ਤੁਹਾਡੇ ਅੰਕ ਇੱਕੋ ਜਿਹੇ ਰਹੇ। ਪਾਠ ਦੁਹਰਾਓ ਅਤੇ ਫਿਰ ਕੋਸ਼ਿਸ਼ ਕਰੋ।"
                )
            else:
                st.info(
                    "Your post-test score was lower. Review the lesson and try again."
                    if not pa else
                    "ਬਾਅਦ ਵਾਲੇ ਟੈਸਟ ਦੇ ਅੰਕ ਘੱਟ ਰਹੇ। ਪਾਠ ਦੁਹਰਾਓ ਅਤੇ ਫਿਰ ਕੋਸ਼ਿਸ਼ ਕਰੋ।"
                )

            _missed = []
            _post_answers = st.session_state.get("impact_post_form_answers", [])
            for _iq, _item in enumerate(_impact_questions):
                _opts = _item["opts_pa"] if pa else _item["opts"]
                _correct = _opts[_item["answer"]]
                if _iq >= len(_post_answers) or _post_answers[_iq] != _correct:
                    _missed.append(_item["topic_pa"] if pa else _item["topic"])
            if _missed:
                st.write(
                    ("Topics to revise: " if not pa else "ਦੁਹਰਾਉਣ ਵਾਲੇ ਵਿਸ਼ੇ: ")
                    + ", ".join(_missed)
                )
            else:
                st.success(
                    "Excellent — all post-test answers are correct."
                    if not pa else
                    "ਸ਼ਾਨਦਾਰ — ਬਾਅਦ ਵਾਲੇ ਟੈਸਟ ਦੇ ਸਾਰੇ ਜਵਾਬ ਸਹੀ ਹਨ।"
                )

            _report_lines = [
                "D-SMART Impact Lab — Learning Report",
                "Language: " + ("Punjabi" if pa else "English"),
                "Pre-test score: " + str(_pre) + "/5",
                "Post-test score: " + str(_post) + "/5",
                "Score change: " + str(_change),
                "Topics to revise: " + (", ".join(_missed) if _missed else "None identified by this quiz"),
                "",
                "This is a brief educational awareness activity, not a validated research instrument or a medical assessment.",
                "Results reflect one session and do not prove long-term learning or population-level impact."
            ]
            st.download_button(
                "⬇️ Download learning report (.txt)" if not pa else "⬇️ ਰਿਪੋਰਟ ਡਾਊਨਲੋਡ ਕਰੋ (.txt)",
                data="\n".join(_report_lines),
                file_name="D-SMART_Impact_Report.txt",
                mime="text/plain",
                use_container_width=True
            )
            if st.button("Start a new attempt" if not pa else "ਨਵੀਂ ਕੋਸ਼ਿਸ਼ ਸ਼ੁਰੂ ਕਰੋ", key="impact_reset"):
                for _key in [
                    "impact_pre_score", "impact_pre_form_answers",
                    "impact_post_score", "impact_post_form_answers"
                ] + [
                    f"{_form}_q{_i}"
                    for _form in ["impact_pre_form", "impact_post_form"]
                    for _i in range(5)
                ]:
                    st.session_state.pop(_key, None)
                st.rerun()

    st.caption(
        "Interpretation: this small quiz shows only the score change for this session. For an exhibition study, collect consented, anonymous pre/post results from a larger group and report the method and limitations honestly."
        if not pa else
        "ਵਿਆਖਿਆ: ਇਹ ਛੋਟਾ ਕਵਿਜ਼ ਸਿਰਫ਼ ਇਸ ਸੈਸ਼ਨ ਦੇ ਅੰਕਾਂ ਦੀ ਤਬਦੀਲੀ ਦਿਖਾਉਂਦਾ ਹੈ। ਪ੍ਰਦਰਸ਼ਨੀ ਅਧਿਐਨ ਲਈ ਸਹਿਮਤੀ ਨਾਲ, ਗੁਪਤ ਪਛਾਣ-ਰਹਿਤ ਨਤੀਜੇ ਵੱਡੇ ਸਮੂਹ ਤੋਂ ਇਕੱਠੇ ਕਰੋ ਅਤੇ ਵਿਧੀ ਤੇ ਸੀਮਾਵਾਂ ਸਪਸ਼ਟ ਦੱਸੋ।"
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
