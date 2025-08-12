# Academic Research Platform

> **Comprehensive Streamlit-based platform for systematic review validation, meta-analysis research, molecular biophysical chemistry simulation, and automatic research paper validation.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/your-username/academic-research-platform)](https://github.com/your-username/academic-research-platform/issues)

## 🌟 Overview

The Academic Research Platform is an all-in-one solution for researchers conducting systematic reviews, meta-analyses, and molecular studies. It integrates multiple tools for statistical analysis, research paper processing, citation validation, academic writing enhancement, molecular docking simulation, and automated testing workflows.

### 🔬 Key Features

- **Statistical Analysis**: R-based computing with comprehensive effect size calculations
- **Meta-Analysis Verification**: Systematic review validation with PRISMA-compliant methodology
- **Paper Rewriter**: Academic writing enhancement with NLP processing
- **Data Import**: Research data processing with automatic validation
- **Molecular Docking**: PyMOL & WebINA-like molecular visualization and biophysical simulation
- **Validation Results**: Comprehensive automatic testing dashboard
- **Pharmacological Topological Maps**: 3D visualization of drug responses using UniProt multiomic data
- **Teratrend Analysis**: Large-scale drug class pattern recognition beyond megatrends
- **Literature Review Generator**: Automated 50+ article systematic reviews and meta-analyses

## 🚀 Quick Start

### 1-Click Deploy (Recommended)

[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

1. **Fork this repository** to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)  
3. Select your forked repository
4. Deploy with `app.py` as main file
5. **Your research platform is live!**

**See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for detailed deployment instructions.**

### Local Development

**One-command setup:**
```bash
git clone https://github.com/your-username/academic-research-platform.git
cd academic-research-platform
python run_local.py --all
```

**Manual setup:**
```bash
# Clone and setup
git clone https://github.com/your-username/academic-research-platform.git
cd academic-research-platform
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install and run
pip install -r github_requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## 🔧 Configuration

### Environment Variables (Optional)

Create a `.env` file in the root directory for optional API integrations:

```env
# Optional: For enhanced mathematical analysis
WOLFRAM_APP_ID=your_wolfram_alpha_app_id

# Optional: For literature search enhancements
CROSSREF_EMAIL=your_email@domain.com

# Optional: For advanced AI features
PERPLEXITY_API_KEY=your_perplexity_api_key
```

### R Integration Setup (Optional)

For advanced statistical analysis, install R and required packages:

1. **Install R** from [r-project.org](https://www.r-project.org/)

2. **Install R packages**
   ```r
   install.packages(c("meta", "metafor", "dmetar", "robvis", "forestplot", "tidyverse", "ggplot2", "compute.es", "effsize"))
   ```

## 📖 Usage Guide

### 1. Statistical Analysis
- Upload research data in CSV, Excel, or PDF format
- Perform effect size calculations and meta-analysis
- Generate forest plots and statistical visualizations
- Export results in multiple formats

### 2. Pharmacological Mapping
- Input drug names or UniProt protein IDs
- Generate 3D topological maps showing drug response vs concentration vs time
- Analyze therapeutic windows and drug-likeness scores
- Explore protein-drug interaction networks

### 3. Teratrend Analysis
- Enter drug names for comprehensive class analysis
- Explore structural motifs and innovation patterns
- Analyze mechanism evolution and market dynamics
- Visualize combination therapy potential

### 4. Literature Review
- Generate systematic reviews with 50+ articles
- Perform meta-analyses with pooled effect estimates
- Create scoping reviews with knowledge gap identification
- Include gray literature and clinical trials data

### 5. Molecular Docking
- Visualize protein structures in 3D
- Perform molecular docking simulations
- Calculate binding affinities and drug-likeness properties
- Analyze molecular dynamics trajectories

## 📂 Project Structure

```
academic-research-platform/
├── app.py                          # Main Streamlit application
├── pages/                          # Individual page modules
│   ├── 1_Statistical_Analysis.py
│   ├── 2_Meta_Analysis_Verification.py
│   ├── 3_Paper_Rewriter.py
│   ├── 4_Data_Import.py
│   ├── 5_Molecular_Docking.py
│   ├── 6_Validation_Results.py
│   ├── 7_Pharmacological_Topological_Maps.py
│   ├── 8_Data_Citations.py
│   └── 9_Plot_Implications.py
├── utils/                          # Utility modules
│   ├── statistical_tools.py
│   ├── nlp_processor.py
│   ├── pdf_processor.py
│   ├── citation_validator.py
│   ├── mathematical_engine.py
│   ├── drug_database.py
│   ├── teratrend_analyzer.py
│   ├── literature_analyzer.py
│   └── auto_validator.py
├── notebooks/                      # Jupyter notebooks for advanced analysis
├── attached_assets/               # Sample data and documentation
├── github_requirements.txt       # Python dependencies
├── README.md                     # This file
└── LICENSE                       # MIT License
```

## 🧪 Example Workflows

### Basic Statistical Analysis
```python
# Upload your research data (CSV/Excel/PDF)
# Select analysis type (effect sizes, meta-analysis, etc.)
# Configure parameters and run analysis
# Export results and visualizations
```

### Drug Analysis Pipeline
```python
# Enter drug names: "Atorvastatin, Simvastatin, Rosuvastatin"
# Select analysis: Pharmacological mapping + Teratrend analysis
# Generate 3D visualizations and trend analysis
# Export comprehensive reports
```

### Literature Review Generation
```python
# Enter research topic: "COVID-19 treatments"
# Set target articles: 50
# Select review types: Systematic + Meta-analysis
# Generate comprehensive review with evidence grading
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

### Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Add docstrings for all functions and classes
- Write tests for new features

## 📊 Performance & Scalability

- **Memory Management**: Optimized for datasets up to 100,000 data points
- **Processing**: Supports batch processing for large-scale analyses
- **Visualization**: Adaptive sampling for interactive plots with large datasets
- **Free Tier Friendly**: Optimized resource usage for deployment on free platforms

## 🐛 Troubleshooting

### Common Issues

1. **ImportError for molecular chemistry libraries**
   ```bash
   # Install conda first, then:
   conda install -c conda-forge rdkit
   ```

2. **NLTK data not found**
   ```python
   import nltk
   nltk.download('all')
   ```

3. **Memory issues with large datasets**
   - Use the sampling options in visualizations
   - Process data in smaller chunks
   - Consider upgrading your deployment environment

4. **R integration issues**
   - Ensure R is installed and in your PATH
   - Install required R packages manually
   - Check R version compatibility (R >= 4.0 recommended)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Data Sources**: UniProt, PubChem, ChEMBL, DrugBank
- **Computational Methods**: SymPy, SciPy, RDKit, py3Dmol, NetworkX
- **Statistical Computing**: R ecosystem (meta, metafor, tidyverse)
- **Pharmacological Models**: Hill equation, Michaelis-Menten kinetics, PBPK modeling

## 📞 Support

- **Documentation**: [Wiki](https://github.com/your-username/academic-research-platform/wiki)
- **Issues**: [GitHub Issues](https://github.com/your-username/academic-research-platform/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/academic-research-platform/discussions)

## 🔮 Roadmap

- [ ] Machine learning-enhanced drug discovery
- [ ] Real-time collaboration features
- [ ] Advanced natural language processing for literature mining
- [ ] Integration with more chemical databases
- [ ] Enhanced mobile responsiveness
- [ ] Docker containerization
- [ ] Cloud deployment templates

---

**Built with ❤️ for the scientific research community**

*Created by David Joshua Ferguson, BS, MS, PharmD Candidate, RSci MRSB MRSC*