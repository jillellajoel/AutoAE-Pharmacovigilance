import streamlit as st
from ae_engine import extract_ae_data

st.set_page_config(page_title="AutoAE - Pharmacovigilance NLP Tool", layout="wide")
st.title("🧠 AutoAE: AI Adverse Event Detection from Medical Text")

st.markdown("Paste any medical article or abstract below:")

user_input = st.text_area("📋 Input Text:", height=300)

if st.button("🔍 Extract Adverse Events"):
    if user_input:
        df = extract_ae_data(user_input)
        if not df.empty:
            st.success("✅ AE Extraction Complete!")
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download AE Report", csv, "autoae_report.csv", "text/csv")
        else:
            st.warning("No drugs or AEs detected in the input.")
    else:
        st.info("Please paste an abstract or article.")
