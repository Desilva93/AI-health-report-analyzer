# 🩸 AI Health Report Analyzer

An AI-powered Blood Work Analyzer built using **Streamlit, LangChain, and Google Gemini** that analyzes blood test reports and generates easy-to-understand **health summaries** along with **Indian diet recommendations**.

---

## 🚀 Features

✅ Upload or paste blood work reports  
✅ AI-based blood value extraction  
✅ Detect HIGH / LOW / NORMAL parameters  
✅ Generate simple health summaries  
✅ Personalized Indian diet suggestions  
✅ Interactive Streamlit UI  
✅ Powered by Google Gemini + LangChain  

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- Python Dotenv
- Jupyter Notebook

---

## 📂 Project Structure

```bash
AI-health-report-analyzer/
│
├── main.py                 # Streamlit application
├── HealthAnalysis.ipynb    # Development notebook
├── Requirements.txt        # Dependencies
├── .env                    # API key file
├── README.md               # Project documentation
└── LICENSE
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Desilva93/AI-health-report-analyzer.git
```

Move into the project folder:

```bash
cd AI-health-report-analyzer
```

Install dependencies:

```bash
pip install -r Requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file and add your Gemini API key:

```python
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run main.py
```

The application will open in your browser.

---

## 🧠 How It Works

### Step 1
Paste blood report into the input box.

### Step 2
Gemini extracts blood test values and identifies whether values are:

- HIGH
- LOW
- NORMAL

### Step 3
AI generates:

- Health Summary
- Indian Diet Recommendations

---

## 📸 Application Preview

Add screenshots of the application here.

Example:

- Blood report input
- Health summary output
- Diet recommendation section

---

## 🔮 Future Improvements

- PDF blood report upload
- OCR support for scanned reports
- Downloadable PDF reports
- Health risk visualization
- Multi-language support

---
