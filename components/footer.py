import streamlit as st

def render_footer():
    st.markdown("""
    <style>
    .custom-footer-bg {
        width: 100%;
        margin-top: 2.5rem;
        background: linear-gradient(90deg, #f1f5f9 20%, #e0e7ff 100%);
        border-radius: 24px;
        box-shadow: 0 1px 15px rgba(80,60,120,0.07);
        padding: 1.3rem 0.7rem 0.4rem 0.7rem;
        color: #5b6075;
        text-align: center;
        font-size: 1.06rem;
    }
    .custom-footer-bg .footer-links {
        margin: 0.2rem 0 0.2rem 0;
        display: flex;
        justify-content: center;
        gap: 2.1rem;
        font-size: 1rem;
    }
    .custom-footer-bg .footer-links a {
        color: #6366f1;
        text-decoration: none;
        transition: color 0.18s;
        font-weight: 500;
    }
    .custom-footer-bg .footer-links a:hover {
        color: #4f46e5;
        text-decoration: underline;
    }
    .custom-footer-bg .by {
        font-size: 1rem;
        margin-top: 0.8rem;
        color: #7c83a1;
        opacity: 0.78;
    }
    </style>
    <div class="custom-footer-bg">
        <div>
            <span style="font-size:1.2rem;vertical-align:middle;">📊</span>
            <strong> Employee Salary Predictor</strong>
            &nbsp;|&nbsp; Powered by <span style="color:#6366f1;"><b>ML</b></span> &amp; <span style="color:#10b981;"><b>Streamlit</b></span>
        </div>
        <div class="footer-links">
            <a href="https://github.com/yourusername/employee-salary-predictor" target="_blank"><i class="fab fa-github"></i> GitHub</a>
            <a href="mailto:youremail@email.com" target="_blank"><i class="fas fa-envelope"></i> Contact</a>
            <a href="https://www.linkedin.com/in/yourprofile/" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
        </div>
        <div class="by">
            &copy; 2025 <span style="font-weight:500;">Your Name</span> · All rights reserved
        </div>
    </div>
    """, unsafe_allow_html=True)
