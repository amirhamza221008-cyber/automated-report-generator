from fpdf import FPDF
import datetime

def create_pdf(summary, chart_path, output_path="output/report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "Business Analytics Report", ln=True, align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Generated: {datetime.date.today()}", ln=True, align="C")
    pdf.ln(6)
    
    # AI Summary Section
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 10, "Executive Summary (AI Generated)", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 7, summary)
    pdf.ln(4)
    
    # Chart
    pdf.image(chart_path, w=170)
    
    pdf.output(output_path)
    return output_path