# 🛡️ Echo Pro Digital Manager

## Overview
**Echo Pro v2.1** is an enterprise-grade AI-powered digital management assistant built with Streamlit and OpenAI GPT-4. It provides intelligent task management, document generation, and operational analytics for business, therapeutic, educational, and creative domains.

## Features
✅ **Enterprise Security** - Secure API key management with hashing  
✅ **Multi-Domain Support** - Business Operations, Therapeutic Support, Educational Management, Creative Strategy  
✅ **Intelligent Tier System** - Standard (GPT-4o Mini) & Ultra (GPT-4o) models  
✅ **PDF Report Generation** - Executive reports with operational analytics  
✅ **Session Tracking** - ROI metrics and spending analysis  
✅ **Secure Vault Storage** - Protected local data storage  

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Setup
```bash
# Clone the repository
git clone https://github.com/lovedoctor69179/ECHO-BOT-PRO.git
cd ECHO-BOT-PRO

# Install dependencies
pip install -r requirements.txt

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

## Usage
```bash
# Run the Streamlit application
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Configuration
- **Intelligence Tier**: Choose between Standard (cost-efficient) or Ultra (advanced reasoning)
- **Operational Domain**: Select your use case (Business, Therapeutic, Educational, Creative)
- **Secure Vault**: All user sessions stored in `secure_vault/` directory

## Security Notes
⚠️ **Never commit `.env` file** - It contains sensitive API keys  
⚠️ Keep dependencies updated: `pip install -r requirements.txt --upgrade`  
⚠️ Use environment variables for production deployments  

## Project Structure
```
ECHO-BOT-PRO/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (git-ignored)
├── .gitignore          # Git ignore rules
├── secure_vault/       # Protected user data storage
└── README.md           # This file
```

## Technologies
- **Streamlit** - Web application framework
- **OpenAI GPT-4 / GPT-4o** - AI intelligence engine
- **FPDF2** - PDF report generation
- **Python-dotenv** - Environment management

## License
Proprietary - Echo Pro Digital Manager v2.1

## Support
For issues and feature requests, please open a GitHub issue.