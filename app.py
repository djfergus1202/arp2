import streamlit as st
import pandas as pd
import numpy as np
from utils.r_integration import RAnalytics
from utils.pdf_processor import PDFProcessor
import os

# Page configuration
st.set_page_config(
    page_title="Academic Research Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'uploaded_data' not in st.session_state:
    st.session_state.uploaded_data = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'r_analytics' not in st.session_state:
    st.session_state.r_analytics = RAnalytics()

def main():
    st.title("📊 Academic Research Platform")
    st.markdown("### Comprehensive Research Platform: Statistical Analysis, Meta-Analysis, Academic Writing & Molecular Simulation")
    
    # Sidebar navigation
    with st.sidebar:
        st.header("Navigation")
        st.markdown("Use the pages on the left to navigate through different modules:")
        st.markdown("- **Statistical Analysis**: R-based statistical computing")
        st.markdown("- **Meta-Analysis Verification**: Validate and recalculate meta-analyses")
        st.markdown("- **Paper Rewriter**: Academic writing enhancement")
        st.markdown("- **Data Import**: Upload and process research data with automatic validation")
        st.markdown("- **Molecular Docking**: PyMOL & WebINA-like molecular simulation")
        st.markdown("- **Validation Results**: View automatic validation test results")
        st.markdown("- **Pharmacological Maps**: 3D topological maps of drug responses from UniProt data")
        st.markdown("- **Data Citations**: Complete attribution and citations for all data sources")
        st.markdown("- **Plot Implications**: Clinical insights and research implications of generated plots")
    
    # Main dashboard
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Statistical Analysis")
        st.write("Integrated R computing environment for comprehensive statistical validation")
        if st.button("Open Statistical Analysis", use_container_width=True):
            st.switch_page("pages/1_Statistical_Analysis.py")
        
        st.subheader("✍️ Paper Rewriter")
        st.write("Academic tone enhancement and structure optimization")
        if st.button("Open Paper Rewriter", use_container_width=True):
            st.switch_page("pages/3_Paper_Rewriter.py")
        
        st.subheader("🧬 Molecular Docking")
        st.write("PyMOL & WebINA-like molecular visualization and biophysical simulation")
        if st.button("Open Molecular Docking", use_container_width=True):
            st.switch_page("pages/5_Molecular_Docking.py")
    
    with col2:
        st.subheader("🔬 Meta-Analysis Tools")
        st.write("Verify effect sizes, confidence intervals, and heterogeneity measures")
        if st.button("Open Meta-Analysis", use_container_width=True):
            st.switch_page("pages/2_Meta_Analysis_Verification.py")
        
        st.subheader("📊 Data Import")
        st.write("Upload and process research data with automatic validation")
        if st.button("Open Data Import", use_container_width=True):
            st.switch_page("pages/4_Data_Import.py")
        
        st.subheader("📋 Validation Results")
        st.write("View automatic validation results and detailed analysis reports")
        if st.button("Open Validation Results", use_container_width=True):
            st.switch_page("pages/6_Validation_Results.py")
        
        st.subheader("🧬 Pharmacological Maps")
        st.write("Generate 3D topological maps of drug responses using UniProt data")
        if st.button("Open Pharmacological Maps", use_container_width=True):
            st.switch_page("pages/7_Pharmacological_Topological_Maps.py")
            
        st.subheader("📚 Data Citations")
        st.write("Complete bibliography and attribution for all data sources")
        if st.button("Open Data Citations", use_container_width=True):
            st.switch_page("pages/8_Data_Citations.py")
            
        st.subheader("📈 Plot Implications")
        st.write("Clinical insights and research implications of pharmacological plots")
        if st.button("Open Plot Implications", use_container_width=True):
            st.switch_page("pages/9_Plot_Implications.py")
    
    # Quick file upload section
    st.header("Quick Data Upload")
    uploaded_file = st.file_uploader(
        "Upload research data or papers",
        type=['csv', 'xlsx', 'pdf', 'txt'],
        help="Upload CSV/Excel data files or PDF papers for analysis"
    )
    
    if uploaded_file is not None:
        st.session_state.uploaded_data = uploaded_file
        file_type = uploaded_file.name.split('.')[-1].lower()
        
        if file_type == 'pdf':
            st.success(f"PDF uploaded: {uploaded_file.name}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔍 Run Automatic Validation", type="primary"):
                    st.info("Running automatic validation tests... This may take a few moments.")
                    st.switch_page("pages/4_Data_Import.py")
            
            with col2:
                if st.button("📖 Preview PDF Text"):
                    with st.expander("PDF Preview", expanded=True):
                        try:
                            pdf_processor = PDFProcessor()
                            text_content = pdf_processor.extract_text(uploaded_file)
                            st.text_area("Extracted Text (first 1000 characters)", 
                                       text_content[:1000], height=200)
                        except Exception as e:
                            st.error(f"Error processing PDF: {str(e)}")
            
            st.info("💡 Tip: Upload your PDF in the Data Import module for comprehensive automatic validation including statistical analysis, citation checking, and methodology assessment.")
        
        elif file_type in ['csv', 'xlsx']:
            st.success(f"Data file uploaded: {uploaded_file.name}")
            try:
                if file_type == 'csv':
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                with st.expander("Data Preview"):
                    st.dataframe(df.head(), use_container_width=True)
                    st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
            except Exception as e:
                st.error(f"Error reading data file: {str(e)}")
    
    # Recent analysis section
    if st.session_state.analysis_results:
        st.header("Recent Analysis Results")
        st.json(st.session_state.analysis_results)
    
    # Platform citation
    st.markdown("### 📝 Platform Citation")
    st.info("**Ferguson, D.J., BS, MS, PharmD Candidate, RSci MRSB MRSC**. Academic Research Platform for Systematic Review Validation and Pharmacological Analysis. Developed using Streamlit, integrating data from UniProt, PubChem, DrugBank, and ChEMBL databases. 2025.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "**Academic Research Platform** - Built with Streamlit and R integration for "
        "reproducible research and statistical transparency."
    )
    st.markdown("*Developed for academic and research purposes. Ensure proper citation of original sources when publishing results.*")

if __name__ == "__main__":
    main()
