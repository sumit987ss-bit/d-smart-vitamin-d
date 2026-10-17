
import streamlit as st

# ================= PAGE CONFIGURATION =================

st.set_page_config(
    page_title="D-SMART | Vitamin D Awareness",
    page_icon="☀️",
    layout="centered",
)

# ================= LANGUAGE =================

st.sidebar.title("☀️ D-SMART")

language = st.sidebar.selectbox(
    "Choose Language | ਭਾਸ਼ਾ ਚੁਣੋ",
    ["English", "ਪੰਜਾਬੀ"],
)

pa = language == "ਪੰਜਾਬੀ"

if pa:
    title = "ਵਿਟਾਮਿਨ D ਜਾਗਰੂਕਤਾ ਸਹਾਇਕ"
    intro = (
        "ਵਿਟਾਮਿਨ D, ਹੱਡੀਆਂ ਦੀ ਸਿਹਤ ਅਤੇ ਲੈਬ ਰਿਪੋਰਟ ਦੀਆਂ "
        "ਇਕਾਈਆਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ।"
    )
    tab_names = [
        "ਜਾਣਕਾਰੀ",
        "ਇਕਾਈ ਬਦਲੋ",
        "ਰਿਪੋਰਟ ਦੀ ਤਸਵੀਰ",
        "ਕਵਿਜ਼",
    ]
else:
    title = "Vitamin D Awareness Assistant"
    intro = (
        "Learn about Vitamin D, bone health, and laboratory "
        "report units."
    )
    tab_names = [
        "Learn",
        "Unit Converter",
        "Report Image",
        "Quiz",
    ]

# ================= HEADER =================

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #e0f7f1, #e8f0ff);
        padding: 24px;
        border-radius: 18px;
        text-align: center;
        border: 1px solid #b8ded5;
    ">
        <h1 style="color:#087e75;">☀️ D-SMART</h1>
        <p style="color:#244c58;">
            Science • Technology • Health Awareness
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.title(title)
st.write(intro)

st.info(
    "ਇਹ ਵਿਦਿਅਕ ਜਾਣਕਾਰੀ ਹੈ, ਡਾਕਟਰੀ ਸਲਾਹ ਨਹੀਂ।"
    if pa
    else
    "This is an educational tool, not a medical advice or "
    "diagnosis service."
)

# ================= MAIN TABS =================

learn_tab, convert_tab, image_tab, quiz_tab = st.tabs(tab_names)

# ================= LEARN =================

with learn_tab:
    if pa:
        st.subheader("☀️ ਵਿਟਾਮਿਨ D ਕੀ ਹੈ?")
        st.write(
            "ਵਿਟਾਮਿਨ D ਸਰੀਰ ਨੂੰ ਕੈਲਸ਼ੀਅਮ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ "
            "ਅਤੇ ਹੱਡੀਆਂ ਤੇ ਮਾਸਪੇਸ਼ੀਆਂ ਦੀ ਸਿਹਤ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ।"
        )

        st.subheader("🌞 ਵਿਟਾਮਿਨ D ਦੇ ਸਰੋਤ")
        st.write(
            "- ਸੂਰਜ ਦੀ ਰੌਸ਼ਨੀ ਤੋਂ ਸਰੀਰ ਵਿੱਚ ਵਿਟਾਮਿਨ D ਬਣ ਸਕਦਾ ਹੈ।\n"
            "- ਕੁਝ ਭੋਜਨ, ਜਿਵੇਂ ਚਰਬੀ ਵਾਲੀ ਮੱਛੀ ਅਤੇ ਵਿਟਾਮਿਨ D "
            "ਮਿਲਾਇਆ ਹੋਇਆ ਦੁੱਧ, ਇਸ ਦੇ ਸਰੋਤ ਹਨ।\n"
            "- ਲੋੜ ਪੈਣ 'ਤੇ ਡਾਕਟਰ ਸਪਲੀਮੈਂਟ ਦੀ ਸਲਾਹ ਦੇ ਸਕਦਾ ਹੈ।"
        )

        st.subheader("🦴 ਇਹ ਕਿਉਂ ਜ਼ਰੂਰੀ ਹੈ?")
        st.write(
            "ਇਹ ਹੱਡੀਆਂ ਦੀ ਮਜ਼ਬੂਤੀ, ਕੈਲਸ਼ੀਅਮ ਦੇ ਜਜ਼ਬ ਹੋਣ ਅਤੇ "
            "ਮਾਸਪੇਸ਼ੀਆਂ ਦੇ ਆਮ ਕੰਮ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।"
        )

        st.subheader("🧪 ਲੈਬ ਰਿਪੋਰਟ ਸਮਝੋ")
        st.write(
            "25-hydroxyvitamin D (25-OH Vitamin D) ਦੀ ਜਾਂਚ ਆਮ ਤੌਰ "
            "ਤੇ ਸਰੀਰ ਵਿੱਚ ਵਿਟਾਮਿਨ D ਦੇ ਪੱਧਰ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। "
            "ਰਿਪੋਰਟ ਦੀ ਵਿਆਖਿਆ ਲਈ ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਲਓ।"
        )
    else:
        st.subheader("☀️ What is Vitamin D?")
        st.write(
            "Vitamin D helps the body absorb calcium and supports "
            "healthy bones and muscles."
        )

        st.subheader("🌞 Sources of Vitamin D")
        st.write(
            "- The body can produce Vitamin D through exposure "
            "to sunlight.\n"
            "- Food sources include fatty fish and some "
            "Vitamin D-fortified foods.\n"
            "- A healthcare professional may recommend supplements "
            "when appropriate."
        )

        st.subheader("🦴 Why is it important?")
        st.write(
            "Vitamin D supports calcium absorption, bone health, "
            "and normal muscle function."
        )

        st.subheader("🧪 Understanding a laboratory report")
        st.write(
            "The 25-hydroxyvitamin D (25-OH Vitamin D) test is commonly "
            "used to assess Vitamin D status. A healthcare professional "
            "should interpret the result in its clinical context."
        )

# ================= UNIT CONVERTER =================

with convert_tab:
    st.subheader(
        "ਵਿਟਾਮਿਨ D ਦੀ ਇਕਾਈ ਬਦਲੋ"
        if pa else
        "Vitamin D Unit Converter"
    )

    value = st.number_input(
        "ਰਿਪੋਰਟ ਦਾ ਮੁੱਲ" if pa else "Laboratory result",
        min_value=0.0,
        value=20.0,
        step=0.1,
    )

    source_unit = st.selectbox(
        "ਰਿਪੋਰਟ ਵਿੱਚ ਦਿੱਤੀ ਇਕਾਈ ਚੁਣੋ"
        if pa else
        "Select the unit shown in your report",
        ["ng/mL", "nmol/L"],
    )

    if source_unit == "ng/mL":
        converted = value * 2.5
        result_unit = "nmol/L"
    else:
        converted = value / 2.5
        result_unit = "ng/mL"

    st.metric(
        "ਬਦਲਿਆ ਹੋਇਆ ਮੁੱਲ" if pa else "Converted result",
        f"{converted:.2f} {result_unit}",
    )

    st.caption(
        "1 ng/mL = 2.5 nmol/L. ਇਹ ਗਣਿਤਕ ਬਦਲਾਅ ਹੈ, "
        "ਰਿਪੋਰਟ ਦੀ ਡਾਕਟਰੀ ਵਿਆਖਿਆ ਨਹੀਂ।"
        if pa else
        "1 ng/mL = 2.5 nmol/L. This is a mathematical conversion, "
        "not a medical interpretation of the result."
    )

    st.warning(
        "ਵਿਟਾਮਿਨ D ਦੀ ਉਚਿਤ ਮਾਤਰਾ ਵਿਅਕਤੀ ਦੀ ਸਥਿਤੀ ਅਤੇ ਲੈਬ ਦੇ "
        "ਮਾਪਦੰਡਾਂ ਅਨੁਸਾਰ ਵੱਖਰੀ ਹੋ ਸਕਦੀ ਹੈ।"
        if pa else
        "Interpretation depends on individual circumstances and "
        "the laboratory's reference guidance."
    )

# ================= REPORT IMAGE UPLOAD =================

with image_tab:
    st.subheader(
        "ਲੈਬ ਰਿਪੋਰਟ ਦੀ ਤਸਵੀਰ ਅਪਲੋਡ ਕਰੋ"
        if pa else
        "Upload a Laboratory Report Image"
    )

    st.write(
        "ਤਸਵੀਰ ਵਿੱਚ ਦਿੱਤੀ ਜਾਣਕਾਰੀ ਖੁਦ ਜਾਂਚੋ।"
        if pa else
        "Upload an image to view your laboratory report."
    )

    uploaded_file = st.file_uploader(
        "ਤਸਵੀਰ ਚੁਣੋ" if pa else "Choose an image",
        type=["png", "jpg", "jpeg"],
    )

    if uploaded_file is not None:
        st.image(
            uploaded_file,
            caption=(
                "ਅਪਲੋਡ ਕੀਤੀ ਰਿਪੋਰਟ"
                if pa else
                "Uploaded laboratory report"
            ),
            use_container_width=True,
        )

        st.info(
            "ਇਹ ਵਰਜਨ ਤਸਵੀਰ ਦਿਖਾਉਂਦਾ ਹੈ, ਪਰ ਇਸ ਵਿੱਚੋਂ ਆਪਣੇ ਆਪ "
            "ਟੈਸਟ ਦੇ ਨਤੀਜੇ ਨਹੀਂ ਪੜ੍ਹਦਾ।"
            if pa else
            "This version previews the image but does not "
            "automatically extract or interpret its results."
        )

# ================= QUIZ =================

questions = [
    {
        "en": "Which vitamin helps the body absorb calcium?",
        "pa": "ਸਰੀਰ ਨੂੰ ਕੈਲਸ਼ੀਅਮ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਕਿਹੜਾ ਵਿਟਾਮਿਨ ਮਦਦ ਕਰਦਾ ਹੈ?",
        "options": [
            "Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"
        ],
        "options_pa": [
            "ਵਿਟਾਮਿਨ A", "ਵਿਟਾਮਿਨ C", "ਵਿਟਾਮਿਨ D", "ਵਿਟਾਮਿਨ K"
        ],
        "answer": 2,
        "why": "Vitamin D helps the body absorb calcium.",
        "why_pa": "ਵਿਟਾਮਿਨ D ਸਰੀਰ ਨੂੰ ਕੈਲਸ਼ੀਅਮ ਜਜ਼ਬ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।",
    },
    {
        "en": "Which test is commonly used to assess Vitamin D status?",
        "pa": "ਵਿਟਾਮਿਨ D ਦੇ ਪੱਧਰ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਕਿਹੜੀ ਜਾਂਚ ਆਮ ਹੈ?",
        "options": [
            "Blood glucose", "25-OH Vitamin D",
            "Haemoglobin only", "Blood group"
        ],
        "options_pa": [
            "ਬਲੱਡ ਗਲੂਕੋਜ਼", "25-OH ਵਿਟਾਮਿਨ D",
            "ਸਿਰਫ਼ ਹੀਮੋਗਲੋਬਿਨ", "ਬਲੱਡ ਗਰੁੱਪ"
        ],
        "answer": 1,
        "why": "The 25-OH Vitamin D test is commonly used.",
        "why_pa": "25-OH ਵਿਟਾਮਿਨ D ਦੀ ਜਾਂਚ ਆਮ ਤੌਰ 'ਤੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।",
    },
    {
        "en": "Which is a possible source of Vitamin D?",
        "pa": "ਵਿਟਾਮਿਨ D ਦਾ ਇੱਕ ਸੰਭਾਵੀ ਸਰੋਤ ਕਿਹੜਾ ਹੈ?",
        "options": [
            "Sunlight", "Plain sugar", "Salt", "Drinking water alone"
        ],
        "options_pa": [
            "ਸੂਰਜ ਦੀ ਰੌਸ਼ਨੀ", "ਸਾਦੀ ਖੰਡ", "ਨਮਕ", "ਸਿਰਫ਼ ਪੀਣ ਵਾਲਾ ਪਾਣੀ"
        ],
        "answer": 0,
        "why": "Sunlight exposure can help the body produce Vitamin D.",
        "why_pa": "ਸੂਰਜ ਦੀ ਰੌਸ਼ਨੀ ਸਰੀਰ ਵਿੱਚ ਵਿਟਾਮਿਨ D ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ।",
    },
    {
        "en": "Which units may appear on a Vitamin D report?",
        "pa": "ਵਿਟਾਮਿਨ D ਦੀ ਰਿਪੋਰਟ ਵਿੱਚ ਕਿਹੜੀਆਂ ਇਕਾਈਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ?",
        "options": [
            "kg and metre", "ng/mL and nmol/L",
            "litre and watt", "°C and km"
        ],
        "options_pa": [
            "ਕਿਲੋਗ੍ਰਾਮ ਅਤੇ ਮੀਟਰ", "ng/mL ਅਤੇ nmol/L",
            "ਲੀਟਰ ਅਤੇ ਵਾਟ", "°C ਅਤੇ ਕਿਲੋਮੀਟਰ"
        ],
        "answer": 1,
        "why": "Vitamin D results may be reported in ng/mL or nmol/L.",
        "why_pa": "ਵਿਟਾਮਿਨ D ਦੇ ਨਤੀਜੇ ng/mL ਜਾਂ nmol/L ਵਿੱਚ ਹੋ ਸਕਦੇ ਹਨ।",
    },
    {
        "en": "Who should help interpret a concerning laboratory result?",
        "pa": "ਚਿੰਤਾਜਨਕ ਲੈਬ ਨਤੀਜੇ ਦੀ ਵਿਆਖਿਆ ਕੌਣ ਕਰੇ?",
        "options": [
            "A healthcare professional", "A guessing game",
            "A social media comment", "No one"
        ],
        "options_pa": [
            "ਸਿਹਤ ਸੰਭਾਲ ਮਾਹਿਰ", "ਅੰਦਾਜ਼ਾ ਲਗਾਉਣ ਵਾਲੀ ਖੇਡ",
            "ਸੋਸ਼ਲ ਮੀਡੀਆ ਦੀ ਟਿੱਪਣੀ", "ਕੋਈ ਨਹੀਂ"
        ],
        "answer": 0,
        "why": "A healthcare professional can interpret the result in context.",
        "why_pa": "ਸਿਹਤ ਸੰਭਾਲ ਮਾਹਿਰ ਵਿਅਕਤੀ ਦੀ ਸਥਿਤੀ ਅਨੁਸਾਰ ਨਤੀਜੇ ਦੀ ਵਿਆਖਿਆ ਕਰ ਸਕਦਾ ਹੈ।",
    },
]

with quiz_tab:
    st.subheader(
        "ਵਿਟਾਮਿਨ D ਬਾਰੇ ਕਵਿਜ਼"
        if pa else
        "Vitamin D Awareness Quiz"
    )

    with st.form("vitamin_d_quiz"):
        answers = []

        for i, question in enumerate(questions):
            st.write(
                f"**{i + 1}. "
                f"{question['pa'] if pa else question['en']}**"
            )

            options = (
                question["options_pa"]
                if pa else
                question["options"]
            )

            selected = st.radio(
                "ਆਪਣਾ ਜਵਾਬ ਚੁਣੋ" if pa else "Choose your answer",
                options,
                key=f"quiz_question_{i}",
                index=None,
            )

            answers.append(selected)

        submitted = st.form_submit_button(
            "ਨਤੀਜਾ ਵੇਖੋ" if pa else "Check My Score",
            use_container_width=True,
        )

    if submitted:
        score = 0

        for i, question in enumerate(questions):
            correct_options = (
                question["options_pa"]
                if pa else
                question["options"]
            )

            correct_answer = correct_options[question["answer"]]

            if answers[i] == correct_answer:
                score += 1

        st.success(
            f"ਤੁਹਾਡੇ ਅੰਕ: {score}/{len(questions)}"
            if pa else
            f"Your score: {score}/{len(questions)}"
        )

        st.markdown(
            "### ਸਹੀ ਜਵਾਬ ਅਤੇ ਵਿਆਖਿਆ"
            if pa else
            "### Correct Answers and Explanations"
        )

        for i, question in enumerate(questions):
            correct_options = (
                question["options_pa"]
                if pa else
                question["options"]
            )

            correct_answer = correct_options[question["answer"]]
            explanation = question["why_pa"] if pa else question["why"]

            st.write(f"**{i + 1}. {correct_answer}**")
            st.caption(explanation)

# ================= PROJECT CREDITS =================

st.divider()

with st.expander(
    "🏫 ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਜਾਣਕਾਰੀ"
    if pa else
    "🏫 About the Project & Credits",
    expanded=False,
):
    if pa:
        st.markdown("### ☀️ D-SMART")
        st.subheader("ਵਿਟਾਮਿਨ D ਜਾਗਰੂਕਤਾ ਸਹਾਇਕ")
        st.write("ਵਿਗਿਆਨ • ਤਕਨਾਲੋਜੀ • ਸਿਹਤ ਜਾਗਰੂਕਤਾ")

        st.markdown("### 🎯 ਪ੍ਰੋਜੈਕਟ ਦਾ ਉਦੇਸ਼")
        st.write(
            "ਵਿਟਾਮਿਨ D ਬਾਰੇ ਜਾਗਰੂਕਤਾ ਵਧਾਉਣਾ, ਸਿਹਤਮੰਦ ਆਦਤਾਂ "
            "ਬਾਰੇ ਸਿੱਖਿਆ ਦੇਣਾ ਅਤੇ ਲੈਬ ਰਿਪੋਰਟ ਦੀਆਂ ਇਕਾਈਆਂ ਸਮਝਣ "
            "ਵਿੱਚ ਮਦਦ ਕਰਨਾ।"
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
        st.write("- ਪੰਜਾਬੀ ਅਤੇ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਜਾਣਕਾਰੀ")
        st.write("- ਇੰਟਰਐਕਟਿਵ ਵਿਟਾਮਿਨ D ਕਵਿਜ਼")
        st.write("- ਵਿਟਾਮਿਨ D ਦੀਆਂ ਇਕਾਈਆਂ ਬਦਲਣ ਦੀ ਸਹੂਲਤ")
        st.write("- ਲੈਬ ਰਿਪੋਰਟ ਦੀ ਤਸਵੀਰ ਦੇਖਣ ਦੀ ਸਹੂਲਤ")

        st.info(
            "ਇਹ ਵਿਦਿਅਕ ਜਾਗਰੂਕਤਾ ਐਪ ਹੈ। ਇਹ ਡਾਕਟਰੀ ਜਾਂਚ, "
            "ਨਿਦਾਨ ਜਾਂ ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਦਾ ਬਦਲ ਨਹੀਂ ਹੈ।"
        )

    else:
        st.markdown("### ☀️ D-SMART")
        st.subheader("Vitamin D Awareness Assistant")
        st.write("Science • Technology • Health Awareness")

        st.markdown("### 🎯 About the Project")
        st.write(
            "D-SMART aims to improve Vitamin D awareness, encourage "
            "healthy habits, and help users understand laboratory "
            "report units."
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
        st.write("- English and Punjabi information")
        st.write("- Interactive Vitamin D awareness quiz")
        st.write("- Vitamin D unit conversion")
        st.write("- Laboratory report image preview")

        st.info(
            "D-SMART is an educational awareness tool. It does not "
            "replace professional medical advice, diagnosis, or treatment."
        )

    st.caption("Science Exhibition Project | Academic Session 2026–27")
