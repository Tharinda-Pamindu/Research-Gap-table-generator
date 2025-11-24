# 📅 Release Notes - Research Gap Table Crafter

This document contains detailed release notes for all versions of the Research Gap Table Crafter project.

---

## [v1.2.0](https://github.com/Tharinda-Pamindu/Research-Gap-table-generator/releases/tag/v1.2.0) - Literature Review & Dual Mode
**Release Date:** November 25, 2025

### 🎉 New Features
*   **Literature Review Generator**: Added a completely new mode that synthesizes multiple research papers into a coherent, academic-style literature review.
    *   Structured output with Introduction, Thematic Analysis, Critical Evaluation, and Conclusion sections.
    *   Automatic extraction of key themes and methodologies from uploaded papers.
*   **IEEE Citation Standard**: Implemented standardized IEEE citation format.
    *   Numeric citations in square brackets (e.g., [1], [2]) throughout the review text.
    *   Automatic generation of a References section at the end of the review.
*   **Dual Mode Persistence**: Enhanced session state management to preserve both Gap Table and Literature Review data.
    *   Users can now switch between modes without losing previously generated content.
    *   Seamless workflow for researchers who need both analysis types.

### 📥 Export Enhancements
*   Added DOCX export functionality for literature reviews.
*   Improved paragraph formatting in exported documents.

### 🎨 UI Improvements
*   Added "Mode Selection" radio button in sidebar for easy switching between:
    *   Gap Table Generator
    *   Literature Review Generator
*   Enhanced visual feedback for mode-specific content display.

---

## [v1.1.0](https://github.com/Tharinda-Pamindu/Research-Gap-table-generator/releases/tag/v1.1.0) - UI/UX Polish & Stability
**Release Date:** November 24, 2025

### 🎨 UI/UX Enhancements
*   **Dark Mode Default**: Enforced a sleek, professional dark theme by default.
    *   Removed theme toggle to maintain consistent user experience.
    *   Optimized color scheme for extended reading sessions.
*   **Secure API Configuration**: Implemented a "login-style" API key input flow.
    *   Session-based storage for enhanced security.
    *   Clear visual feedback for configuration status.
    *   Easy logout/change key functionality.

### 🐛 Critical Bug Fixes
*   **PDF Export Layout Error**: Resolved `LayoutError` that occurred with wide tables (9+ columns).
    *   Implemented **A3 Landscape** page size for more horizontal space.
    *   Added dynamic column width calculation based on available page width.
    *   Implemented text truncation (1000 chars) to prevent cells from exceeding page height.
    *   Enhanced text wrapping using ReportLab Paragraph objects.

### 💾 Data Persistence
*   **Chat History Management**:
    *   Save conversation history as JSON for later restoration.
    *   Load previously saved conversations to continue research sessions.
    *   Export chat history as Markdown for documentation purposes.
    *   Copy to clipboard functionality for easy sharing.

### 🔧 Technical Improvements
*   Fixed `NameError` in PDF generation by restoring buffer initialization.
*   Improved HTML tag handling in PDF exports (replaced `<br>` with `<br/>`).
*   Added fallback text sanitization for robust error handling.

---

## [v1.0.0](https://github.com/Tharinda-Pamindu/Research-Gap-table-generator/releases/tag/v1.0.0) - Initial Release
**Release Date:** November 23, 2025

### 🚀 Core Features
*   **Multi-Format Document Upload**:
    *   Support for PDF files (via PyPDF2).
    *   Support for DOCX files (via python-docx).
    *   Batch upload capability for multiple documents.

*   **AI-Powered Research Gap Analysis**:
    *   Integration with Google Gemini 2.5 Flash model.
    *   Automatic generation of structured Research Gap Tables with columns:
        *   Reference
        *   Year
        *   Study Aim / Topic
        *   Method / Approach
        *   Data / Tools
        *   Key Findings
        *   Relevance to Project
        *   Gaps / Notes
        *   Research Gap / Limitations

*   **Interactive Q&A Interface**:
    *   Chat-based interface for asking questions about uploaded papers.
    *   Context-aware responses based on document content.
    *   Auto-clearing input field for improved UX.
    *   Persistent chat history during session.

*   **Export Functionality**:
    *   Download Research Gap Tables as PDF (landscape orientation).
    *   Download Research Gap Tables as DOCX.
    *   Markdown table view for easy copying.

### 🎨 User Interface
*   Modern Streamlit-based web interface.
*   Sidebar navigation for configuration and file management.
*   Tabbed view for Interactive Table and Full Text Table modes.
*   Custom CSS styling for professional appearance.

### 🛠️ Technical Stack
*   **Frontend**: Streamlit
*   **AI Model**: Google Gemini 2.5 Flash
*   **Data Processing**: Pandas, PyPDF2, python-docx
*   **Report Generation**: ReportLab, Tabulate

---

## Upgrade Guide

### From v1.1.0 to v1.2.0
No breaking changes. Simply pull the latest code and restart the application. Your existing API key configuration will be preserved in the session.

### From v1.0.0 to v1.1.0
No breaking changes. The dark mode is now enforced by default. If you had custom theme configurations, they will be overridden.

---

## Known Issues

### v1.2.0
*   None reported.

### v1.1.0
*   Streamlit deprecation warning for `use_container_width` parameter (will be addressed in future release).

### v1.0.0
*   PDF export may fail with very wide tables (9+ columns) - **Fixed in v1.1.0**.

---

## Future Roadmap

*   **v1.3.0** (Planned):
    *   Support for additional citation formats (APA, MLA, Chicago).
    *   Enhanced literature review customization options.
    *   PDF export for literature reviews.
    *   Improved table column width optimization.

*   **v2.0.0** (Planned):
    *   Multi-language support.
    *   Cloud storage integration for saving projects.
    *   Collaborative features for team research.
    *   Advanced analytics and visualization.

---

**For questions or issues, please visit our [GitHub Issues](https://github.com/Tharinda-Pamindu/Research-Gap-table-generator/issues) page.**
