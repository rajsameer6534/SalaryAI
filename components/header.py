import streamlit as st

def render_header():
    st.markdown("""
    <style>
    .custom-header-bg {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 8px 40px rgba(99,102,241,0.13);
        border-radius: 28px;
        margin: 2.2rem 0 1.7rem 0;
        padding: 2.2rem 1.7rem 1.3rem 1.7rem;
        position: relative;
        overflow: hidden;
        z-index: 1;
        backdrop-filter: blur(9px);
    }
    .custom-header-bg:before {
        content: '';
        position: absolute;
        top: -60px; left: -70px;
        width: 240px; height: 220px;
        background: radial-gradient(circle, #a5b4fc 0%, transparent 70%);
        opacity: 0.23;
        z-index: 0;
    }
    .salaryiq-logo {
        font-size:2.3rem;
        font-weight: 900;
        letter-spacing: -1px;
        color: #fff;
        text-shadow: 1px 2px 9px rgba(76,86,219,0.13);
        display: flex;
        align-items: center;
        gap: 0.7rem;
        justify-content: center;
    }
    .salaryiq-logo i {
        font-size:2.5rem;
        color:#ffd700;
        filter: drop-shadow(0 2px 7px #6366f188);
        animation: pulseIcon 1.4s infinite alternate;
    }
    @keyframes pulseIcon {
        to { transform: scale(1.15);}
        from {transform: scale(1);}
    }
    .subtitle {
        color: #e0e7ff;
        font-size: 1.17rem;
        font-weight: 400;
        margin-top: 0.3rem;
        margin-bottom: 0.3rem;
        letter-spacing: 0.5px;
        text-align: center;
        opacity: 0.93;
    }
    .chip-row {
        margin-top:1.1rem; display:flex; justify-content:center; gap:1.1rem;
    }
    .chip {
        background: rgba(255,255,255,0.16);
        color: #fff;
        font-size: 0.99rem;
        font-weight: 600;
        padding: 0.37rem 1.3rem;
        border-radius: 16px;
        box-shadow: 0 2px 13px rgba(99,102,241,0.13);
        border: 1.2px solid #c7d2fe33;
        backdrop-filter: blur(3px);
        letter-spacing: 0.05em;
        display: flex; align-items:center; gap:0.5em;
    }
    .chip i { color:#ffd700;font-size:1.1rem; }
    </style>

    <div class="custom-header-bg">
        <div class="salaryiq-logo">
            <i class="fas fa-chart-line"></i> SalaryIQ
        </div>
        <div class="subtitle">
            <span style="font-weight:500;">AI-Powered Employee Salary Predictor & Market Analytics</span>
        </div>
        <div class="chip-row">
            <div class="chip"><i class="fas fa-bolt"></i> 95% Accuracy Rate</div>
            <div class="chip"><i class="fas fa-users"></i> 50K+ Predictions</div>
            <div class="chip"><i class="fas fa-building"></i> 500+ Companies</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
