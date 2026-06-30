import streamlit as st
import pandas as pd
from data_analyzer import analyze
from ai_summary import get_summary
from chart_maker import make_chart
from report_generator import create_pdf

st.title("Automated Business Report Generator")
st.caption("CSV upload karo → AI PDF report ready!")

uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())
    
    if st.button("Generate Report"):
        with st.spinner("AI report bana raha hai..."):
            stats = analyze(df)
            summary = get_summary(stats)
            chart = make_chart(df)
            pdf_path = create_pdf(summary, chart)
        
        st.success("Report ready!")
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", f, "report.pdf")