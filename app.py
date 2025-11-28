import streamlit as st
import pandas as pd
import utils

# Set page config
st.set_page_config(
    page_title="Research Gap AI Agent",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
def apply_custom_css(is_dark_mode):
    if is_dark_mode:
        bg_color = "#0e1117"
        text_color = "#fafafa"
        sidebar_bg = "#262730"
        input_bg = "#1e1e1e"
        card_bg = "#1e1e1e"
        border_color = "#333333"
    else:
        bg_color = "#ffffff"
        text_color = "#000000"
        sidebar_bg = "#f0f2f6"
        input_bg = "#ffffff"
        card_bg = "#f0f2f6"
        border_color = "#cccccc"
        
    st.markdown(f"""
    <style>
        /* Main App Background and Text */
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}
        
        /* Sidebar */
        [data-testid="stSidebar"] {{
            background-color: {sidebar_bg};
        }}
        
        /* Buttons */
        .stButton>button {{
            background-color: #ff4b4b;
            color: white;
            border-radius: 20px;
            border: none;
            padding: 10px 24px;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        .stButton>button:hover {{
            background-color: #ff3333;
            transform: scale(1.05);
        }}
        
        /* Inputs (Text, Select, etc.) */
        .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {{
            background-color: {input_bg};
            color: {text_color};
            border-radius: 10px;
            border: 1px solid {border_color};
        }}
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Inter', sans-serif;
            color: {text_color} !important;
        }}
        p, li, label, .stMarkdown, .stText, .stCaption {{
            color: {text_color} !important;
        }}
        
        /* Custom Card Style */
        .uploadedFile {{
            background-color: {card_bg};
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 5px;
            color: {text_color};
        }}
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{
            border-bottom: 1px solid {border_color};
        }}
        .stTabs [data-baseweb="tab"] {{
            color: {text_color};
        }}
        
        /* Expander */
        .streamlit-expanderHeader {{
            background-color: {card_bg};
            color: {text_color};
        }}
        
        /* Chat Messages */
        [data-testid="stChatMessage"] {{
            background-color: {card_bg};
        }}
        [data-testid="stChatMessageContent"] {{
            color: {text_color};
        }}
        
        /* Code Blocks - Ensure visibility */
        code {{
            color: #d63384; /* Default pinkish for code */
        }}
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("📚 Research Gap AI Agent")
    st.markdown("### Analyze research papers and identify gaps instantly.")

    # Sidebar
    with st.sidebar:
        # Enforce Dark Mode
        apply_custom_css(True)
        
        st.header("Configuration")
        
        # Initialize Session State for API Key
        if "api_key" not in st.session_state:
            st.session_state.api_key = ""
            
        # Login-style API Key Entry
        if not st.session_state.api_key:
            if st.button("⚙️ Configure API Key", type="primary"):
                st.session_state.show_api_input = True
            
            if st.session_state.get("show_api_input", False):
                with st.form("api_key_form"):
                    key_input = st.text_input("Enter Google Gemini API Key", type="password", help="Get your key from Google AI Studio")
                    submitted = st.form_submit_button("Save & Login")
                    if submitted and key_input:
                        st.session_state.api_key = key_input
                        st.session_state.show_api_input = False
                        st.rerun()
        else:
            st.success("✅ API Key Configured")
            if st.button("Logout / Change Key"):
                st.session_state.api_key = ""
                st.rerun()
        
        api_key = st.session_state.api_key
        
        st.divider()
        st.header("Upload Documents")
        uploaded_files = st.file_uploader("Upload PDF or DOCX files", type=['pdf', 'docx', 'doc'], accept_multiple_files=True)
        
        if uploaded_files:
            st.success(f"{len(uploaded_files)} files uploaded.")
            
        st.divider()
        st.header("Analysis Options")
        run_gap_analysis = st.checkbox("Generate Gap Table", value=True)
        run_lit_review = st.checkbox("Generate Literature Review")
            
    # Main Content
    if uploaded_files and api_key:
        # Initialize session state variables if not present
        if 'processed_data' not in st.session_state:
            st.session_state.processed_data = None
        if 'concise_data' not in st.session_state:
            st.session_state.concise_data = None
        if 'literature_review' not in st.session_state:
            st.session_state.literature_review = None
            
        # Process Button
        if st.button("Analyze Papers"):
            if not (run_gap_analysis or run_lit_review):
                st.warning("Please select at least one analysis option.")
            else:
                with st.spinner("Analyzing documents..."):
                    # Extract text once
                    text, filenames = utils.extract_text_from_files(uploaded_files)
                    
                    # Validate Document
                    is_valid = utils.validate_research_paper(text, api_key)
                    
                    if not is_valid:
                        st.error("Please upload relevant document. The uploaded file does not appear to be a research paper.")
                    else:
                        st.session_state.extracted_text = text
                        
                        # Run Gap Analysis
                        if run_gap_analysis:
                            status_msg = st.empty()
                            status_msg.info("Generating Research Gap Table...")
                            df = utils.generate_research_gap_table(text, api_key)
                            st.session_state.processed_data = df
                            status_msg.empty()
                            
                        # Run Literature Review
                        if run_lit_review:
                            status_msg = st.empty()
                            status_msg.info("Generating Literature Review...")
                            review = utils.generate_literature_review(text, api_key)
                            st.session_state.literature_review = review
                            status_msg.empty()
                            
                        st.success("Analysis Complete!")

        # Display Results using Tabs
        # Determine which tabs to show
        tabs = []
        tab_names = []
        
        if st.session_state.processed_data is not None:
            tab_names.append("🔍 Gap Table")
        
        # Concise table is dependent on Gap Table, but we show the tab if Gap Table exists 
        # to allow generation, or if concise data already exists.
        if st.session_state.processed_data is not None:
             tab_names.append("📋 Concise Table")
             
        if st.session_state.literature_review is not None:
            tab_names.append("📝 Literature Review")
            
        if tab_names:
            st.divider()
            
            # Modern Navigation Menu Styling
            st.markdown("""
            <style>
                /* Style the tab container */
                .stTabs [data-baseweb="tab-list"] {
                    gap: 10px;
                    background-color: transparent;
                    border-bottom: none;
                }
                
                /* Style individual tabs */
                .stTabs [data-baseweb="tab"] {
                    height: 50px;
                    white-space: pre-wrap;
                    background-color: #262730;
                    border-radius: 10px;
                    color: #fafafa;
                    font-weight: 600;
                    padding: 0 20px;
                    border: 1px solid #444;
                    transition: all 0.3s ease;
                }
                
                /* Hover effect */
                .stTabs [data-baseweb="tab"]:hover {
                    background-color: #333;
                    border-color: #666;
                    color: #ff4b4b;
                }
                
                /* Active tab style */
                .stTabs [aria-selected="true"] {
                    background-color: #ff4b4b !important;
                    color: white !important;
                    border-color: #ff4b4b !important;
                }
                
                /* Remove default focus outline */
                .stTabs [data-baseweb="tab"]:focus {
                    outline: none;
                }
            </style>
            """, unsafe_allow_html=True)
            
            tabs = st.tabs(tab_names)
            
            # Iterate through tabs and render content based on name
            for i, tab_name in enumerate(tab_names):
                with tabs[i]:
                    
                    # --- GAP TABLE TAB ---
                    if tab_name == "🔍 Gap Table":
                        st.subheader("Research Gap Analysis Table")
                        sub_tab1, sub_tab2 = st.tabs(["Interactive", "Full Text"])
                        with sub_tab1:
                            st.dataframe(st.session_state.processed_data, use_container_width=True, hide_index=True)
                        with sub_tab2:
                            st.markdown(st.session_state.processed_data.to_markdown(index=False))
                            
                        col1, col2 = st.columns(2)
                        with col1:
                            pdf_data = utils.create_pdf_download(st.session_state.processed_data)
                            st.download_button("Download PDF", pdf_data, "research_gap.pdf", "application/pdf")
                        with col2:
                            docx_data = utils.create_docx_download(st.session_state.processed_data)
                            st.download_button("Download DOCX", docx_data, "research_gap.docx", "application/vnd.openxmlformats-officedocument.wordprocessingprocessingml.document")

                    # --- CONCISE TABLE TAB ---
                    elif tab_name == "📋 Concise Table":
                        st.subheader("Concise Research Gap Table")
                        
                        # Generation Button (if not already generated or to regenerate)
                        if st.button("✨ Generate Concise Table", key="gen_concise"):
                            with st.spinner("Condensing table..."):
                                concise_df = utils.generate_concise_table(st.session_state.processed_data, api_key)
                                st.session_state.concise_data = concise_df
                                st.rerun()
                        
                        if st.session_state.concise_data is not None:
                            sub_tab3, sub_tab4 = st.tabs(["Interactive", "Full Text"])
                            with sub_tab3:
                                st.dataframe(st.session_state.concise_data, use_container_width=True, hide_index=True)
                            with sub_tab4:
                                st.markdown(st.session_state.concise_data.to_markdown(index=False))
                                
                            col3, col4 = st.columns(2)
                            with col3:
                                c_pdf = utils.create_pdf_download(st.session_state.concise_data)
                                st.download_button("Download Concise PDF", c_pdf, "concise_gap.pdf", "application/pdf")
                            with col4:
                                c_docx = utils.create_docx_download(st.session_state.concise_data)
                                st.download_button("Download Concise DOCX", c_docx, "concise_gap.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                        else:
                            st.info("Click the button above to generate a concise version of the gap table.")

                    # --- LITERATURE REVIEW TAB ---
                    elif tab_name == "📝 Literature Review":
                        st.subheader("Literature Review")
                        st.markdown(st.session_state.literature_review)
                        lr_docx = utils.create_review_docx(st.session_state.literature_review)
                        st.download_button("Download Review DOCX", lr_docx, "literature_review.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

            # Q&A Section (Always visible if any analysis is done)
            st.divider()
            st.subheader("💬 Ask Questions")
            
            # Initialize chat history if not present
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []

            # Display chat history
            for role, message in st.session_state.chat_history:
                with st.chat_message(role):
                    st.markdown(message)

            # Chat input
            if prompt := st.chat_input("Ask anything about the uploaded papers:"):
                # Add user message to history
                st.session_state.chat_history.append(("user", prompt))
                with st.chat_message("user"):
                    st.markdown(prompt)

                # Generate answer
                with st.spinner("Thinking..."):
                    answer = utils.answer_question(st.session_state.extracted_text, prompt, api_key)
                    
                # Add assistant response to history
                st.session_state.chat_history.append(("assistant", answer))
                with st.chat_message("assistant"):
                    st.markdown(answer)
            
            # Chat History Management (Sidebar)
            st.sidebar.divider()
            st.sidebar.header("Chat History")
            
            # 1. Download Chat History (JSON) - For restoring later
            import json
            chat_json = json.dumps(st.session_state.chat_history)
            st.sidebar.download_button(
                label="💾 Save Conversation (JSON)",
                data=chat_json,
                file_name="chat_history.json",
                mime="application/json",
                help="Download this file to resume the conversation later."
            )
            
            # 2. Upload Chat History (JSON) - To restore
            uploaded_chat = st.sidebar.file_uploader("📂 Load Conversation", type=["json"], help="Upload a previously saved JSON chat file.")
            if uploaded_chat is not None:
                try:
                    loaded_history = json.load(uploaded_chat)
                    # Validate structure (list of lists/tuples)
                    if isinstance(loaded_history, list):
                        st.session_state.chat_history = loaded_history
                        st.success("Chat history loaded!")
                        st.rerun()
                except Exception as e:
                    st.sidebar.error(f"Error loading chat: {e}")

            # 3. Download as Markdown (For reading/sharing)
            chat_md = "# Research Gap AI Agent - Conversation History\n\n"
            for role, msg in st.session_state.chat_history:
                chat_md += f"**{role.title()}:**\n{msg}\n\n---\n\n"
            
            st.sidebar.download_button(
                label="📥 Download as Markdown",
                data=chat_md,
                file_name="conversation_history.md",
                mime="text/markdown",
                help="Download the conversation as a readable text file."
            )
                    
    elif not api_key:
        st.warning("Please enter your Google Gemini API Key in the sidebar to proceed.")
    elif not uploaded_files:
        st.info("Please upload research papers to begin analysis.")

if __name__ == "__main__":
    main()
