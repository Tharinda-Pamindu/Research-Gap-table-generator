import google.generativeai as genai
import PyPDF2
import docx
import pandas as pd
import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def extract_text_from_files(uploaded_files):
    """
    Extracts text from a list of uploaded files (PDF or DOCX).
    Returns a combined string of text and a list of filenames.
    """
    combined_text = ""
    filenames = []
    
    for uploaded_file in uploaded_files:
        filenames.append(uploaded_file.name)
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        try:
            if file_extension == 'pdf':
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                for page in pdf_reader.pages:
                    combined_text += page.extract_text() + "\n"
            elif file_extension in ['docx', 'doc']:
                doc = docx.Document(uploaded_file)
                for para in doc.paragraphs:
                    combined_text += para.text + "\n"
        except Exception as e:
            print(f"Error reading {uploaded_file.name}: {e}")
            
    return combined_text, filenames

def get_gemini_response(prompt, text_input, api_key):
    """
    Sends a prompt and text input to Google Gemini and returns the response.
    """
    if not api_key:
        return "Please provide a valid Google Gemini API Key."
        
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content([prompt, text_input])
        return response.text
    except Exception as e:
        return f"Error accessing Gemini API: {str(e)}"

def generate_research_gap_table(text, api_key):
    """
    Generates a research gap table from the provided text using Gemini.
    Returns a Pandas DataFrame.
    """
    prompt = """
    You are an expert academic researcher. Analyze the provided research paper text and identify the research gaps.
    Create a comprehensive table summarizing the findings.
    
    The output MUST be a valid Markdown table with the following columns:
    | Reference | Year | Study Aim / Topic | Method / Approach | Data / Tools | Key Findings | Relevance to Project | Gaps / Notes | Research Gap / Limitations |
    
    IMPORTANT:
    - Do NOT include any introductory or concluding text.
    - Output ONLY the markdown table.
    - Ensure the table is well-formatted.
    """
    
    response_text = get_gemini_response(prompt, text, api_key)
    
    # Parse markdown table to DataFrame
    try:
        lines = response_text.strip().split('\n')
        table_lines = [line.strip() for line in lines if '|' in line]
        
        if len(table_lines) < 2:
            return pd.DataFrame({"Error": ["Could not find a valid table in the response."], "Raw Response": [response_text]})

        # Extract headers from the first valid table line
        headers = [h.strip() for h in table_lines[0].split('|') if h.strip()]
        
        data = []
        # Iterate through the rest of the lines
        for line in table_lines[1:]:
            # Skip separator lines (e.g., |---|---|)
            if '---' in line:
                continue
                
            row = [cell.strip() for cell in line.split('|') if cell.strip()]
            
            # Handle row length mismatches
            if len(row) > 0:
                if len(row) == len(headers):
                    data.append(row)
                elif len(row) > len(headers):
                     data.append(row[:len(headers)])
                else:
                    # Pad with empty strings if short
                    row += [''] * (len(headers) - len(row))
                    data.append(row)
        
        if not data:
             return pd.DataFrame({"Error": ["Table found but no data parsed."], "Raw Response": [response_text]})
             
        df = pd.DataFrame(data, columns=headers)
        return df
    except Exception as e:
        return pd.DataFrame({"Error": [f"Failed to parse table: {str(e)}"], "Raw Response": [response_text]})

def answer_question(context, question, api_key):
    """
    Answers a user question based on the provided context.
    """
    prompt = f"""
    You are a helpful research assistant. Use the following context from research papers to answer the user's question.
    
    Context:
    {context[:30000]} # Limit context to avoid token limits if necessary, though Gemini handles large context well.
    
    Question: {question}
    
    Answer:
    """
    return get_gemini_response(prompt, "", api_key)

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_download(df):
    """
    Creates a PDF file from the DataFrame with text wrapping and landscape orientation.
    """
    # Calculate column widths
    # Landscape letter is approx 792 points wide.
    # Margins are usually 72 each side (default) -> ~648 usable width.
    # We'll set specific margins to get more space.
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    
    usable_width = doc.width
    num_cols = len(df.columns)
    
    if num_cols > 0:
        col_width = usable_width / num_cols
    else:
        col_width = usable_width
    
    # Create Table
    # splitByRow=1 allows the table to split across pages
    t = Table(data, colWidths=[col_width] * num_cols, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'), # Left align text
        ('VALIGN', (0, 0), (-1, -1), 'TOP'), # Top align text
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    elements.append(t)
    doc.build(elements)
    buffer.seek(0)
    return buffer

def create_docx_download(df):
    """
    Creates a DOCX file from the DataFrame.
    """
    doc = docx.Document()
    doc.add_heading('Research Gap Analysis', 0)
    
    # Add table
    table = doc.add_table(rows=1, cols=len(df.columns))
    table.style = 'Table Grid'
    
    # Add headers
    hdr_cells = table.rows[0].cells
    for i, column in enumerate(df.columns):
        hdr_cells[i].text = str(column)
    
    # Add data
    for index, row in df.iterrows():
        row_cells = table.add_row().cells
        for i, value in enumerate(row):
            row_cells[i].text = str(value)
            
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer
