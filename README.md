# Document Analysis AI Agent

A modern AI-powered agent to analyze research papers, identify research gaps, and answer questions.

🔗 **Live Demo:** [https://researchgaptablecrafter.streamlit.app/](https://researchgaptablecrafter.streamlit.app/)

## Features
- **Upload Multiple Files**: Supports PDF and DOCX formats.
- **Research Gap Table**: Automatically generates a structured table of findings, methodologies, and gaps.
- **Q&A Interface**: Chat with your documents.
- **Export**: Download the analysis as PDF or DOCX.
- **Modern UI**: Built with Streamlit.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

3.  **API Key**:
    - You will need a Google Gemini API Key.
    - Get it here: [Google AI Studio](https://aistudio.google.com/app/apikey)
    - Enter it in the sidebar when the app runs.

## Usage
1. Upload your research papers in the sidebar.
2. Enter your API Key.
3. Click "Analyze Papers".
4. View the generated "Research Gap Analysis Table".
5. Download the table if needed.
6. Ask questions in the chat section below.
