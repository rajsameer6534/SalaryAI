import streamlit as st

def inject_custom_css():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
    /* Paste your CSS here, or use a triple-quoted string with your whole style block from app.py */
    body { font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;}
    ... /* rest of your CSS */
    </style>
    """, unsafe_allow_html=True)
