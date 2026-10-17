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
    padding-top: 2rem;
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

st.title("☀️ D-SMART")
st.subheader(title)
st.write(intro)
st.info(notice)

st.divider()
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

    if sunlight == sun_options[2]:
        st.write(sun_advice)

    if food in food_options[2:]:
        st.write(food_advice)

    if concern == concern_options[1]:
        st.warning(health_advice)

    if tested == test_options[1]:
        st.write(test_advice)

    if tested == test_options[0]:
        st.write(report_advice)

    st.success(safe_end)

st.divider()
st.header(learn_title)

with st.expander(why_title):
    st.write(why_text)

with st.expander(sources_title):
    st.write(sources_text)

with st.expander(symptoms_title):
    st.write(symptoms_text)

st.caption("D-SMART | Science Exhibition Project")

st.divider()

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
                "Keep exploring the learning section and try again."
                if not pa else
                "ਜਾਣਕਾਰੀ ਵਾਲਾ ਭਾਗ ਪੜ੍ਹੋ ਅਤੇ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।"
            )
            
            with st.expander(
                "Review answers" if not pa else "ਜਵਾਬ ਵੇਖੋ"
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

                    st.write(f"**{i + 1}. {correct}**")
                    st.caption(explanation)
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
