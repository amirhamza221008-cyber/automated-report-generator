from fpdf import FPDF
import pandas as pd
from chart_maker import create_bar_chart
from ai_summary import generate_summary
import os

def generate_report(csv_path, output_path="report.pdf"):
    # Step 1: Data load karo
    df = pd.read_csv(csv_path)
    print("Data loaded!")

    # Step 2: Chart banao
    chart_path = "chart.png"
    df_small = df.head(10)
    create_bar_chart(df_small, "Time", "Global_active_power", save_path=chart_path)
    print("Chart created!")

    # Step 3: Summary banao
    summary = generate_summary(df)
    print("Summary created!")

    # Step 4: PDF banao
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 15, "Automated Business Report", new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.ln(5)

    # Summary section
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Executive Summary", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 8, summary)
    pdf.ln(5)

    # Chart section
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Power Consumption Chart", new_x="LMARGIN", new_y="NEXT")
    pdf.image(chart_path, x=10, w=180)

    # Save PDF
    pdf.output(output_path)
    print(f"Report saved as {output_path}")


if __name__ == "__main__":
    generate_report("sample_data/household_power_consumption.csv")