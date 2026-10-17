        ):
            for i, question in enumerate(questions):
                correct = (
                    question["options_pa"][question["answer"]]
                    if pa else
                    question["options"][question["answer"]]
                )
                explanation = question["why_pa"] if pa else question["why"]

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
