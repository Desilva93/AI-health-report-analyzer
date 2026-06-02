from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API keys
load_dotenv()

# Streamlit page setup
st.set_page_config(page_title="Blood Work Analyzer", layout="wide")

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# CSS Styling
st.markdown("""
<style>
.scroll-box {
    height: 230px;
    overflow-y: auto;
    padding: 15px;
    border: 1px solid #444;
    border-radius: 10px;
    background-color: #1e1e1e;
    color: #f5f5f5 !important;
    font-size: 16px;
    line-height: 1.7;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.3);
}

.scroll-box * {
    color: #f5f5f5 !important;
}

.stButton > button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 8px;
    border: none;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #e63b3b;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Blood Work Analyzer")

# Layout
left_col, right_col = st.columns([1, 1])

# LEFT SIDE
with left_col:
    st.subheader("Blood Work Report")

    blood_report = st.text_area(
        label="Paste your report below",
        height=500,
        placeholder="Paste your blood work report here...",
        label_visibility="collapsed"
    )

    analyze_clicked = st.button(
        "Analyze",
        type="primary",
        use_container_width=True
    )

# RIGHT SIDE
with right_col:
    st.subheader("Health Summary")
    health_box = st.empty()
    health_box.markdown(
        '<div class="scroll-box">Health summary will appear here...</div>',
        unsafe_allow_html=True
    )

    st.subheader("Suggested Diet Plan")
    diet_box = st.empty()
    diet_box.markdown(
        '<div class="scroll-box">Diet recommendation will appear here...</div>',
        unsafe_allow_html=True
    )

# ANALYSIS
if analyze_clicked:

    if not blood_report.strip():
        st.warning("Please paste a blood work report before analyzing.")

    else:
        with st.spinner("Analyzing your blood work..."):

            # STEP 1: Extract blood values
            extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or NORMAL
based on the reference ranges.

Format:

Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
"""

            extraction_response = llm.invoke(extraction_prompt)

            # FIX: use .content instead of .text
            extracted_values = extraction_response.content

            # STEP 2: Summary + Diet
            diet_prompt = f"""
You are a clinical nutritionist specializing in Indian dietary habits.

Based on the blood work analysis below, provide two clearly separated sections.

SECTION 1 - HEALTH SUMMARY:
Explain the condition in 4–5 simple lines.

SECTION 2 - INDIAN DIET PLAN:
Mention foods to eat more and foods to avoid using Indian foods.
Use bullet points and keep it practical.

Blood Work Analysis:
{extracted_values}
"""

            diet_response = llm.invoke(diet_prompt)

            # FIX: use .content
            full_response = diet_response.content

        # Split sections
        if "SECTION 2" in full_response:
            parts = full_response.split("SECTION 2")

            health_summary = (
                parts[0]
                .replace("SECTION 1 - HEALTH SUMMARY:", "")
                .replace("SECTION 1", "")
                .strip()
            )

            diet_plan = (
                "SECTION 2" + parts[1]
            ).replace(
                "SECTION 2 - INDIAN DIET PLAN:", ""
            ).replace(
                "SECTION 2", ""
            ).strip()

        else:
            health_summary = full_response
            diet_plan = ""

        # Convert line breaks to HTML
        health_summary = health_summary.replace("\n", "<br>")
        diet_plan = diet_plan.replace("\n", "<br>")

        # Render
        health_box.markdown(
            f'<div class="scroll-box">{health_summary}</div>',
            unsafe_allow_html=True
        )

        diet_box.markdown(
            f'<div class="scroll-box">{diet_plan if diet_plan else full_response}</div>',
            unsafe_allow_html=True
        )
