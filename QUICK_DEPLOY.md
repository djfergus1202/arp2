# Quick Deployment Guide 🚀

**Get your Academic Research Platform running in 5 minutes on any free platform!**

## Option 1: Streamlit Cloud (Easiest - Free Forever)

### Steps:
1. **Fork this repository** to your GitHub account
2. Go to **[share.streamlit.io](https://share.streamlit.io)**
3. Click **"New app"** 
4. Select your forked repository
5. Set these settings:
   - **Main file path**: `app.py`
   - **Python version**: `3.11`
6. Click **"Deploy!"**

**Your app will be live at**: `https://your-username-academic-research-platform-app-xyz123.streamlit.app`

### Optional API Keys (for enhanced features):
In Streamlit Cloud dashboard, add these secrets:
```toml
WOLFRAM_APP_ID = "your_wolfram_key"
CROSSREF_EMAIL = "your_email@domain.com"
PERPLEXITY_API_KEY = "your_perplexity_key"
```

---

## Option 2: Heroku (Free Tier Available)

### Prerequisites:
- Heroku account (free)
- Git installed

### One-Command Deploy:
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/academic-research-platform.git
cd academic-research-platform

# Deploy to Heroku
heroku create your-app-name
heroku stack:set container
git push heroku main
```

**Your app will be live at**: `https://your-app-name.herokuapp.com`

---

## Option 3: Local Development

### Quick Start:
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/academic-research-platform.git
cd academic-research-platform

# One-command setup and run
python run_local.py --all
```

**Your app will be available at**: `http://localhost:8501`

### Manual Setup:
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r github_requirements.txt

# Download required data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Run application
streamlit run app.py
```

---

## Option 4: Docker (Any Platform)

### Prerequisites:
- Docker installed

### Run with Docker:
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/academic-research-platform.git
cd academic-research-platform

# Build and run
docker-compose up -d

# Access your app
# Main app: http://localhost:8501
# Jupyter (optional): http://localhost:8888
```

---

## Platform-Specific Instructions

### GitHub Codespaces
1. Click **"Code"** → **"Open with Codespaces"** → **"New codespace"**
2. Wait for environment setup
3. Run: `python run_local.py --all`
4. Click the forwarded port link when it appears

### Gitpod
1. Go to: `https://gitpod.io/#https://github.com/YOUR_USERNAME/academic-research-platform`
2. Wait for workspace setup
3. Run: `python run_local.py --all`
4. Click the preview URL when ready

### Railway
1. Go to [railway.app](https://railway.app)
2. Click **"Start a New Project"** → **"Deploy from GitHub repo"**
3. Select your forked repository
4. Railway will automatically detect and deploy

### Render
1. Go to [render.com](https://render.com)
2. Click **"New"** → **"Web Service"**
3. Connect your GitHub repository
4. Use these settings:
   - **Build Command**: `pip install -r github_requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

---

## Essential Environment Variables (Optional)

Add these for enhanced functionality:

| Variable | Purpose | Required |
|----------|---------|----------|
| `WOLFRAM_APP_ID` | Advanced mathematical analysis | No |
| `CROSSREF_EMAIL` | Literature search enhancement | No |
| `PERPLEXITY_API_KEY` | AI-powered research analysis | No |

---

## Verification Steps

After deployment, test these features:

1. **Basic functionality**: Visit your app URL
2. **Statistical Analysis**: Upload a CSV file
3. **Pharmacological Maps**: Enter "Atorvastatin" and generate 3D visualization
4. **Teratrend Analysis**: Run analysis on any drug name
5. **Literature Review**: Generate 25-article review

---

## Troubleshooting

### Common Issues:

**"Requirements not found"**
- Ensure `github_requirements.txt` is in root directory
- Check file is properly uploaded to GitHub

**"Memory limit exceeded"**
- Use smaller datasets initially
- Enable sampling in visualization options

**"Module not found errors"**
- Wait for full dependency installation
- Check deployment logs for specific missing packages

**"Port already in use"**
- For local development: `streamlit run app.py --server.port=8502`
- Platform deployments handle ports automatically

### Platform-Specific Help:

**Streamlit Cloud**: [docs.streamlit.io](https://docs.streamlit.io/streamlit-community-cloud)
**Heroku**: [devcenter.heroku.com](https://devcenter.heroku.com)
**Docker**: Check container logs with `docker logs container_name`

---

## Need Help?

- **Documentation**: [Full deployment guide](DEPLOYMENT.md)
- **Issues**: [GitHub Issues](https://github.com/your-username/academic-research-platform/issues)
- **Community**: [GitHub Discussions](https://github.com/your-username/academic-research-platform/discussions)

**Your Academic Research Platform will be running in minutes! 🎉**