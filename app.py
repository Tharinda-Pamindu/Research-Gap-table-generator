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
            
    # Main Content
    if uploaded_files and api_key:
        if 'processed_data' not in st.session_state:
            st.session_state.processed_data = None
            
        # Process Button
        if st.button("Analyze Papers"):
            with st.spinner("Extracting text and analyzing..."):
                text, filenames = utils.extract_text_from_files(uploaded_files)
                st.session_state.extracted_text = text
                
                # Generate Table
                df = utils.generate_research_gap_table(text, api_key)
                st.session_state.processed_data = df
                st.success("Analysis Complete!")

        # Display Results
        if st.session_state.processed_data is not None:
            st.subheader("🔍 Research Gap Analysis Table")
            
            # View Toggle using Tabs (prevents rerun)
            tab1, tab2 = st.tabs(["Interactive Table", "Full Text Table"])
            
            with tab1:
                st.dataframe(
                    st.session_state.processed_data, 
                    use_container_width=True, 
                    hide_index=True
                )
                
            with tab2:
                st.markdown(st.session_state.processed_data.to_markdown(index=False))
            
            # Download Options
            col1, col2 = st.columns(2)
            with col1:
                pdf_data = utils.create_pdf_download(st.session_state.processed_data)
                st.download_button(
                    label="Download as PDF",
                    data=pdf_data,
                    file_name="research_gap_analysis.pdf",
                    mime="application/pdf"
                )
            with col2:
                docx_data = utils.create_docx_download(st.session_state.processed_data)
                st.download_button(
                    label="Download as DOCX",
                    data=docx_data,
                    file_name="research_gap_analysis.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            
            st.divider()
            
            # Q&A Section
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
