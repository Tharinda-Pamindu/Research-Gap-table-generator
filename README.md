# 📚 Research Gap Table Crafter

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://researchgaptablecrafter.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Research Gap Table Crafter** is a powerful, AI-driven agent designed to streamline the literature review process for researchers, students, and academics. By leveraging Google's Gemini Pro models, it automatically analyzes research papers (PDF/DOCX) and generates comprehensive "Research Gap Tables," identifying key findings, methodologies, and critical gaps in existing literature.

🔗 **Live Demo:** [https://researchgaptablecrafter.streamlit.app/](https://researchgaptablecrafter.streamlit.app/)

---

## 🚀 Key Features

*   **📄 Multi-Format Support**: Upload and analyze multiple **PDF** and **DOCX** research papers simultaneously.
*   **🤖 AI-Powered Analysis**: Automatically extracts and synthesizes information to create a structured **Research Gap Table** containing:
    *   Study Aim / Topic
    *   Methodology
    *   Key Findings
    *   Research Gaps / Limitations
    *   Relevance to Project
*   **💬 Interactive Q&A**: Chat with your documents! Ask specific questions about the uploaded papers and get context-aware answers.
*   **📥 Versatile Exports**:
    *   **PDF & DOCX**: Download the generated gap table for your reports.
    *   **Markdown**: Export conversation history for sharing.
    *   **JSON**: Save and load your chat sessions to resume work later.
*   **🎨 Modern UI**: A sleek, dark-themed interface built for focus and readability.

---

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **AI Model**: [Google Gemini 1.5 Flash](https://ai.google.dev/)
*   **Data Processing**: Pandas, PyPDF2, python-docx
*   **Report Generation**: ReportLab (PDF), Tabulate

---

## ⚙️ Installation & Setup

Follow these steps to run the application locally.

### Prerequisites
*   Python 3.9 or higher
*   A Google Gemini API Key ([Get it here](https://aistudio.google.com/app/apikey))

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/research-gap-crafter.git
cd research-gap-crafter
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

---

## 📖 Usage Guide

1.  **Configure API Key**:
    *   Launch the app.
    *   Click **"⚙️ Configure API Key"** in the sidebar.
    *   Enter your Google Gemini API Key and click **"Save & Login"**.
2.  **Upload Papers**:
    *   Use the sidebar to upload one or more research papers (PDF or DOCX).
3.  **Analyze**:
    *   Click the **"Analyze Papers"** button.
    *   The AI will generate a detailed Research Gap Table.
4.  **Interact**:
    *   Switch between **Interactive** and **Full Text** table views.
    *   Use the **Chat** interface to ask specific questions about the papers.
5.  **Export**:
    *   Download the table as PDF or DOCX.
    *   Save your conversation history as JSON or Markdown.

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit application entry point
├── utils.py              # Core logic (Text extraction, AI interaction, PDF generation)
├── requirements.txt      # Project dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration (Theme settings)
└── README.md             # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the project
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed with ❤️ by [Your Name/Team]**
