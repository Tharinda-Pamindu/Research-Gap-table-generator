# 📚 Research Gap Table Crafter

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://researchgaptablecrafter.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini%202.5%20Flash-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Research Gap Table Crafter** is a powerful, AI-driven agent designed to streamline the literature review process for researchers, students, and academics. By leveraging Google's **Gemini 2.5 Flash** models, it automatically analyzes research papers (PDF/DOCX) and generates comprehensive "Research Gap Tables," identifying key findings, methodologies, and critical gaps in existing literature.

🔗 **Live Demo:** [Live Demo](https://researchgaptablecrafter.streamlit.app)

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
*   **🔐 Secure Configuration**: "Login-style" API key configuration ensures your key is stored securely in the session.
*   **💾 Chat Persistence**:
    *   **Save & Resume**: Download your conversation as JSON and restore it anytime.
    *   **Share**: Export chat history as Markdown or copy directly to clipboard.
*   **🎨 Modern Dark UI**: A sleek, dark-themed interface designed for focus and readability (Dark Mode by default).
*   **📥 Versatile Exports**: Download the generated gap table as **PDF** (A3 Landscape) or **DOCX** for your reports.

---

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **AI Model**: [Google Gemini 2.5 Flash](https://ai.google.dev/)
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
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

---

## 📅 Release History

**Current Version:** [v2.0](https://github.com/Tharinda-Pamindu/Research-Gap-table-generator/releases/tag/V2.0) - Literature Review & Dual Mode

For detailed release notes, changelog, and upgrade guides, see **[RELEASES](RELEASES.md)**.

### Quick Overview
*   **v1.2.0** - Literature Review Generator, IEEE Citations, Dual Mode Persistence
*   **v1.1.0** - Dark Mode, PDF Export Fix, Chat Persistence
*   **v1.0.0** - Initial Release with Gap Table Generation

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

**Developed with ❤️ by [Tharinda-Pamindu](https://github.com/Tharinda-Pamindu)**
