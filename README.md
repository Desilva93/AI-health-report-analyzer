# 🩸 Blood Work Analyzer using Gemini + LangChain + Streamlit

## Project Overview
Blood Work Analyzer is an AI-powered healthcare application that analyzes blood test reports and generates:

- Blood parameter extraction
- HIGH / LOW / NORMAL classification
- Health summary in simple language
- Personalized Indian diet recommendations

The project uses:
- Google Gemini (gemini-2.5-flash)
- LangChain
- Streamlit
- Python
- Prompt Engineering

---

## Repository Structure

```bash
Blood-Work-Analyzer/
│
├── app/
│   └── app.py
├── data/
│   └── sample_bloodwork.txt
├── notebooks/
│   └── HealthAnalysis.ipynb
├── requirements.txt
├── .env.example
└── README.md
```

---

## Features

### Stage 1: Blood Report Extraction
The LLM:
- Reads blood report
- Extracts all parameters
- Compares with reference range
- Labels as:
  - HIGH
  - LOW
  - NORMAL

### Stage 2: Health Summary + Diet Plan
The LLM then:
- Generates simple health interpretation
- Creates Indian diet recommendations
- Suggests foods to avoid and foods to eat

---

## Installation

### Step 1
Clone repository

```bash
git clone <your_repo_link>
cd Blood-Work-Analyzer
```

### Step 2
Create environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Step 3
Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4
Create .env

```bash
GOOGLE_API_KEY=your_api_key
```

### Step 5
Run Streamlit

```bash
streamlit run app/app.py
```

---

## Sample Result

Input:
- CBC
- Lipid panel
- Metabolic panel
- Liver function values

Output:
- Health summary
- Cholesterol risk interpretation
- Indian diet recommendations

---

## Future Improvements
- PDF report upload
- OCR support
- Medical charts and trends
- Downloadable health reports
- Multi-language support

---

## Author
Developed as an AI + Healthcare NLP project using Gemini and LangChain.
