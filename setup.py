# Quick Setup Script for MRI Anomaly Detection System

print("🚀 MRI Anomaly Detection System - Quick Setup")
print("=" * 50)

# Install required packages
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("📦 Installing required packages...")

packages = [
    "langchain==0.1.0",
    "openai==1.10.0", 
    "requests==2.31.0",
    "pillow==10.2.0",
    "numpy==1.24.3",
    "matplotlib==3.7.1",
    "python-dotenv==1.0.0",
    "ipywidgets==8.1.1"
]

for package in packages:
    try:
        install_package(package)
        print(f"✅ Installed: {package}")
    except Exception as e:
        print(f"❌ Failed to install {package}: {e}")

print("\n🔐 Don't forget to:")
print("1. Set your OpenAI API key")
print("2. Set your Tavily API key") 
print("3. Open the Jupyter notebook: mri_anomaly_detection_system.ipynb")

print("\n✨ Setup complete! Ready to analyze MRI images!")