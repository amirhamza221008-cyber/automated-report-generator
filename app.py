import streamlit as st
import pandas as pd
from chart_maker import create_bar_chart
from ai_summary import generate_summary
from report_generator import generate_report
import os

# Page title
st.title("📊 Automated Business Report Generator")
st.write("CSV file upload karo — automatic chart, summary aur PDF ban jayegi!")

# CSV upload
uploaded_file = st.file_uploader("CSV file choose karo", type=["csv"])

if uploaded_file is not None:
    # Data load karo
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ File load ho gayi! {len(df)} records mile.")

    # Data preview
    st.subheader("📋 Data Preview")
    st.dataframe(df.head(10))

    # Generate button
    if st.button("🚀 Report Generate Karo"):
        with st.spinner("Report ban rahi hai..."):

            # CSV save karo temporarily
            temp_csv = "temp_upload.csv"
            df.to_csv(temp_csv, index=False)

            # Report generate karo
            generate_report(temp_csv, output_path="report.pdf")

            # Chart dikhao
            st.subheader("📈 Power Consumption Chart")
            st.image("chart.png")

            # Summary dikhao
            st.subheader("📝 Executive Summary")
            summary = generate_summary(df)
            st.write(summary)

            # PDF download button
            with open("report.pdf", "rb") as f:
                st.download_button(
                    label="📥 PDF Download Karo",
                    data=f,
                    file_name="business_report.pdf",
                    mime="application/pdf"
                )

            # Temp file hatao
            os.remove(temp_csv)