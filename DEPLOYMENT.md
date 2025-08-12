# Deployment Guide

This guide covers various deployment options for the Academic Research Platform.

## 🚀 Quick Deployment Options

### 1. Streamlit Cloud (Recommended - Free)

[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

**Steps:**
1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your forked repository
5. Set main file path: `app.py`
6. Set Python version: `3.11`
7. Add secrets in the Streamlit Cloud dashboard (optional):
   ```toml
   # .streamlit/secrets.toml
   WOLFRAM_APP_ID = "your_key_here"
   CROSSREF_EMAIL = "your_email@domain.com"
   PERPLEXITY_API_KEY = "your_key_here"
   ```
8. Click "Deploy"

**Pros:** Free, automatic updates, easy setup
**Cons:** Resource limitations, public repositories only

### 2. Heroku (Free Tier Available)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

**Steps:**
1. Create a Heroku account
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Clone and deploy:
   ```bash
   git clone https://github.com/your-username/academic-research-platform.git
   cd academic-research-platform
   heroku create your-app-name
   heroku stack:set container
   git push heroku main
   ```

**Configuration:**
```bash
# Set environment variables (optional)
heroku config:set WOLFRAM_APP_ID=your_key
heroku config:set CROSSREF_EMAIL=your_email@domain.com
```

### 3. Docker (Local/VPS)

**Prerequisites:** Docker and Docker Compose

**Steps:**
```bash
# Clone repository
git clone https://github.com/your-username/academic-research-platform.git
cd academic-research-platform

# Build and run with Docker Compose
docker-compose up -d

# Access application
# Streamlit: http://localhost:8501
# Jupyter (optional): http://localhost:8888
```

**Configuration:**
Create `.env` file:
```env
WOLFRAM_APP_ID=your_key
CROSSREF_EMAIL=your_email@domain.com
PERPLEXITY_API_KEY=your_key
```

### 4. Local Development

**Requirements:** Python 3.11+

**Steps:**
```bash
# Clone repository
git clone https://github.com/your-username/academic-research-platform.git
cd academic-research-platform

# Quick setup and run
python run_local.py --all

# Or manual setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r github_requirements.txt
streamlit run app.py
```

## 🌐 Cloud Platform Deployments

### Google Cloud Run

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT_ID/academic-research-platform
gcloud run deploy --image gcr.io/PROJECT_ID/academic-research-platform --platform managed
```

### AWS App Runner

1. Create `apprunner.yaml`:
```yaml
version: 1.0
runtime: python3
build:
  commands:
    build:
      - pip install -r github_requirements.txt
run:
  runtime-version: 3.11
  command: streamlit run app.py --server.port=8000 --server.address=0.0.0.0
  network:
    port: 8000
    env: PORT
```

2. Deploy via AWS Console or CLI

### DigitalOcean App Platform

1. Create `deploy/digitalocean.yaml`:
```yaml
name: academic-research-platform
services:
- name: web
  source_dir: /
  github:
    repo: your-username/academic-research-platform
    branch: main
  run_command: streamlit run app.py --server.port=8080 --server.address=0.0.0.0
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  http_port: 8080
```

## 🔧 Configuration Options

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `WOLFRAM_APP_ID` | Wolfram Alpha API key for enhanced math | No |
| `CROSSREF_EMAIL` | Email for CrossRef API (literature search) | No |
| `PERPLEXITY_API_KEY` | Perplexity API for advanced literature analysis | No |
| `PORT` | Port number (auto-set by most platforms) | No |

### Streamlit Configuration

Create `.streamlit/config.toml`:
```toml
[server]
headless = true
port = 8501
address = "0.0.0.0"

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

## 📊 Performance Optimization

### Memory Management
- **Small deployments (512MB)**: Use sampling in visualizations
- **Medium deployments (1GB)**: Full functionality available
- **Large deployments (2GB+)**: Optimal performance for all features

### Scaling Options
- **Horizontal scaling**: Multiple instances behind load balancer
- **Vertical scaling**: Increase memory/CPU for single instance
- **Caching**: Enable Streamlit caching for better performance

## 🔒 Security Considerations

### API Keys
- Never commit API keys to version control
- Use environment variables or secrets management
- Rotate keys regularly

### Data Privacy
- No user data is stored by default
- Uploaded files are processed in memory only
- Consider adding data retention policies for production

### Network Security
- Use HTTPS in production
- Implement rate limiting for API endpoints
- Consider VPN access for sensitive research

## 🚨 Troubleshooting

### Common Issues

1. **Memory Issues**
   ```bash
   # Reduce memory usage
   export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=50
   ```

2. **Port Conflicts**
   ```bash
   # Use different port
   streamlit run app.py --server.port=8502
   ```

3. **Package Installation Issues**
   ```bash
   # For RDKit issues
   conda install -c conda-forge rdkit
   
   # For molecular visualization
   pip install py3dmol --no-cache-dir
   ```

4. **R Integration Issues**
   ```bash
   # Install R and packages
   sudo apt-get install r-base
   Rscript -e "install.packages(c('meta', 'metafor'))"
   ```

### Platform-Specific Issues

**Streamlit Cloud:**
- Ensure requirements.txt is in root directory
- Check resource limits (1GB RAM, 1 CPU)
- Verify all imports are available

**Heroku:**
- Use Procfile for custom commands
- Monitor dyno usage and scaling
- Check buildpack compatibility

**Docker:**
- Ensure port mapping is correct
- Check container logs: `docker logs container_name`
- Verify volume mounts for data persistence

## 📈 Monitoring and Maintenance

### Health Checks
- Application: `curl http://localhost:8501/_stcore/health`
- Database connections: Built-in status indicators
- API endpoints: Response time monitoring

### Logging
- Streamlit logs: Available in application interface
- System logs: Check platform-specific logging
- Error tracking: Consider Sentry or similar services

### Updates
- **Automatic**: Configure auto-deployment from main branch
- **Manual**: Pull latest changes and redeploy
- **Rollback**: Keep previous version for quick rollback

## 💰 Cost Optimization

### Free Tier Options
- **Streamlit Cloud**: Free for public repositories
- **Heroku**: 550 dyno hours/month free
- **Railway**: $5 credit monthly
- **Render**: Free tier with limitations

### Paid Recommendations
- **Small projects**: $5-10/month (Heroku Hobby, DigitalOcean Basic)
- **Medium projects**: $15-25/month (DigitalOcean Professional)
- **Large projects**: $50+/month (AWS, GCP with auto-scaling)

## 🆘 Support and Documentation

- **Documentation**: [GitHub Wiki](https://github.com/your-username/academic-research-platform/wiki)
- **Issues**: [GitHub Issues](https://github.com/your-username/academic-research-platform/issues)
- **Community**: [GitHub Discussions](https://github.com/your-username/academic-research-platform/discussions)
- **Email**: For enterprise support inquiries

---

**Choose the deployment option that best fits your needs and budget. All options provide the full functionality of the Academic Research Platform.**