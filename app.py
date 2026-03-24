import streamlit as st
from openai import OpenAI
import datetime
import json
import os
import hashlib
from fpdf import FPDF  # pip install fpdf2
from dotenv import load_dotenv  # pip install python-dotenv

# --- 1. ENTERPRISE CONFIG & SECURITY ---
load_dotenv()
st.set_page_config(page_title="Echo AI | Digital Manager Pro", page_icon="🛡️", layout="wide")

VAULT_DIR = "secure_vault"
if not os.path.exists(VAULT_DIR):
    os.makedirs(VAULT_DIR)

def get_user_hash(api_key):
    return hashlib.sha256(api_key.encode()).hexdigest()[:12]

# --- 2. THE PDF SUMMARY ENGINE ---
def generate_executive_report(domain, history, stats):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"ECHO PRO: {domain.upper()} REPORT", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"System Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Operational Analytics", ln=True)
    pdf.set_font("Arial", size=10)
    # Corrected dictionary access for stability
    spend = stats.get('spend', 0.0)
    pdf.multi_cell(0, 5, txt=f"Session Investment: ${spend:.4f}\nMessages: {len(history)}\nTier: Ultra (4o)")
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Executive Summary & Next Actions", ln=True)
    pdf.set_font("Arial", size=10)
    summary = history[-1]['content'] if history else "No session data available."
    pdf.multi_cell(0, 5, txt=summary)

    pdf.ln(20)
    pdf.cell(100, 10, txt="__________________________", ln=False)
    pdf.cell(100, 10, txt="__________________________", ln=True)
    pdf.cell(100, 10, txt="Supervisor Signature", ln=False)
    pdf.cell(100, 10, txt="Date", ln=True)
    return pdf.output(dest='S')

# --- 3. SIDEBAR: THE COMMAND CENTER ---
with st.sidebar:
    st.title("🛡️ Echo Pro v2.1")
    st.caption("Enterprise Digital Manager | Lab Build")
    
    # Secure API Key entry
    api_key = st.text_input("Enterprise Access Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    
    if not api_key:
        st.warning("🔑 Awaiting Vault Key...")
        st.stop()

    user_id = get_user_hash(api_key)
    st.success(f"Vault Secured: {user_id}")
    
    st.divider()
    tier = st.radio("Intelligence Tier", ["Standard (Efficiency)", "Ultra (Complex Strategy)"])
    model = "gpt-4o-mini" if "Standard" in tier else "gpt-4o"
    
    domain = st.selectbox("Operational Domain", ["Business Operations", "Therapeutic Support", "Educational Management", "Creative Strategy"])
    
    # Use session_state to track ROI metrics
    if 'stats' not in st.session_state:
        st.session_state.stats = {"spend": 0.0, "msgs": 0}
    
    st.divider()
    st.subheader("📊 Session ROI")
