#!/usr/bin/env python3
"""
Local development runner for Academic Research Platform
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "github_requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)


def download_nltk_data():
    """Download required NLTK data"""
    print("Downloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        print("✅ NLTK data downloaded successfully")
    except Exception as e:
        print(f"⚠️ Warning: Failed to download NLTK data: {e}")


def setup_environment():
    """Set up environment variables"""
    env_file = Path(".env")
    if not env_file.exists():
        print("Creating .env file...")
        with open(env_file, "w") as f:
            f.write("# Academic Research Platform Environment Variables\n")
            f.write("# Add your API keys here (optional)\n\n")
            f.write("# WOLFRAM_APP_ID=your_wolfram_alpha_app_id\n")
            f.write("# CROSSREF_EMAIL=your_email@domain.com\n")
            f.write("# PERPLEXITY_API_KEY=your_perplexity_api_key\n")
        print("✅ .env file created")


def run_streamlit():
    """Run the Streamlit application"""
    print("Starting Academic Research Platform...")
    print("🌐 Opening http://localhost:8501")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=localhost",
            "--server.headless=false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
    except Exception as e:
        print(f"❌ Failed to start application: {e}")
        sys.exit(1)


def run_jupyter():
    """Run Jupyter Lab"""
    print("Starting Jupyter Lab...")
    print("🔬 Opening http://localhost:8888")
    
    try:
        subprocess.run([
            sys.executable, "-m", "jupyter", "lab",
            "--ip=0.0.0.0",
            "--port=8888",
            "--no-browser",
            "--allow-root"
        ])
    except KeyboardInterrupt:
        print("\n👋 Shutting down Jupyter...")
    except Exception as e:
        print(f"❌ Failed to start Jupyter: {e}")
        sys.exit(1)


def run_tests():
    """Run test suite"""
    print("Running tests...")
    try:
        subprocess.check_call([sys.executable, "-m", "pytest", "tests/", "-v"])
        print("✅ All tests passed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
        sys.exit(1)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Academic Research Platform Runner")
    parser.add_argument("--install", action="store_true", help="Install dependencies")
    parser.add_argument("--setup", action="store_true", help="Set up environment")
    parser.add_argument("--jupyter", action="store_true", help="Run Jupyter Lab instead of Streamlit")
    parser.add_argument("--test", action="store_true", help="Run tests")
    parser.add_argument("--all", action="store_true", help="Install, setup, and run")
    
    args = parser.parse_args()
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("🧬 Academic Research Platform")
    print("=" * 50)
    
    if args.install or args.all:
        install_dependencies()
        download_nltk_data()
    
    if args.setup or args.all:
        setup_environment()
    
    if args.test:
        run_tests()
        return
    
    if args.jupyter:
        run_jupyter()
    elif args.all or len(sys.argv) == 1:
        run_streamlit()


if __name__ == "__main__":
    main()