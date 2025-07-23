import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_welcome():
    st.markdown("""
    <style>
    .welcome-hero {
        background: linear-gradient(120deg, #a78bfa 0%, #6366f1 100%);
        color: #fff;
        padding: 2.7rem 1rem 2rem 1rem;
        border-radius: 24px;
        box-shadow: 0 6px 30px rgba(99,102,241,0.09);
        margin-bottom: 2rem;
        text-align: center;
        animation: fadeInDown 1.1s;
    }
    .welcome-icon {
        font-size: 3.4rem;
        margin-bottom: 1rem;
        opacity: 0.95;
        animation: pop-in 1.1s;
    }
    .welcome-hero h2 {
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }
    .welcome-hero p {
        font-size: 1.18rem;
        margin-bottom: 2rem;
        opacity: 0.97;
        max-width: 700px;
        margin-left:auto;
        margin-right:auto;
    }
    .features-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 1.4rem;
        justify-items: center;
        margin-top: 1.6rem;
        max-width: 350px;
        margin-left: auto;
        margin-right: auto;
    }
    .feature-card {
        background: linear-gradient(115deg, rgba(99,102,241,0.08) 0%, rgba(255,255,255,0.13) 100%);
        color: #fff;
        border-radius: 20px;
        width: 100%;
        padding: 1.2rem 1.3rem 1.3rem 1.3rem;
        box-shadow: 0 4px 28px 0px rgba(120, 72, 255, 0.15), 0 0.5px 3.5px 1px rgba(76,81,255,0.08);
        border: 1.5px solid rgba(255,255,255,0.18);
        text-align:left;
        position:relative;
        transition:transform 0.24s, box-shadow 0.22s, border 0.22s;
        margin-bottom: 0.2rem;
        overflow: hidden;
        animation: cardFadeIn 0.7s;
    }
    .feature-card:hover {
        transform: translateY(-7px) scale(1.035) rotate(-0.5deg);
        box-shadow: 0 10px 34px 2px #8b5cf6aa, 0 3px 25px 2px #6366f144;
        border: 1.5px solid #a78bfa;
        background: linear-gradient(120deg, #c7d2fe 0%, #a5b4fc 100%);
        color: #403484;
    }
    .feature-icon-bg {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 3.2rem;
        height: 3.2rem;
        border-radius: 16px;
        background: linear-gradient(120deg, #facc15 0%, #4f46e5 100%);
        margin-right: 1.05rem;
        box-shadow: 0 2px 16px #8b5cf699;
        font-size: 1.65rem;
        color: #fff;
        border: 2.5px solid #fff4;
        transition: background 0.2s, color 0.2s;
        animation: pop-in 1.2s;
    }
    .feature-card:hover .feature-icon-bg {
        background: linear-gradient(120deg, #fff176 0%, #818cf8 100%);
        color: #6366f1;
    }
    .feature-title {
        font-size: 1.18rem;
        font-weight: 700;
        margin-bottom: 0.12rem;
        letter-spacing: 0.03em;
    }
    .feature-desc {
        font-weight: 400;
        font-size: 1.02rem;
        margin-top: 0.08rem;
        color: #ede9fe;
        opacity: 0.93;
    }
    .feature-card:hover .feature-desc {
        color: #403484;
        opacity: 0.96;
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-40px);}
        to { opacity: 1; transform: translateY(0);}
    }
    @keyframes pop-in {
        0% { opacity: 0; transform: scale(0.7);}
        80% { opacity: 1; transform: scale(1.13);}
        100% { transform: scale(1);}
    }
    @keyframes cardFadeIn {
        from { opacity:0; transform:translateY(30px);}
        to { opacity:1; transform:translateY(0);}
    }
    </style>
    <div class="welcome-hero">
        <div class="welcome-icon"><i class="fas fa-robot"></i></div>
        <h2>Welcome to <span style="color:#fff176;">SalaryIQ</span></h2>
        <p>
            Discover your real earning potential.<br>
            <span style="opacity:0.89;">Fill in the employee details to get an instant, accurate salary prediction, along with personalized insights—powered by <b>AI & ML</b>.</span>
        </p>
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon-bg"><i class="fas fa-bolt"></i></span>
                <span>
                  <div class="feature-title">Lightning Fast</div>
                  <div class="feature-desc">Instant, interactive salary estimates</div>
                </span>
            </div>
            <div class="feature-card">
                <span class="feature-icon-bg"><i class="fas fa-chart-pie"></i></span>
                <span>
                  <div class="feature-title">Breakdown &amp; Analysis</div>
                  <div class="feature-desc">Monthly, daily &amp; hourly insights</div>
                </span>
            </div>
            <div class="feature-card">
                <span class="feature-icon-bg"><i class="fas fa-brain"></i></span>
                <span>
                  <div class="feature-title">Powered by AI</div>
                  <div class="feature-desc">Smart predictions for your unique profile</div>
                </span>
            </div>
            <div class="feature-card">
                <span class="feature-icon-bg"><i class="fas fa-shield-alt"></i></span>
                <span>
                  <div class="feature-title">Secure &amp; Private</div>
                  <div class="feature-desc">No information stored. Ever.</div>
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



def render_results(base_salary, total_experience):
    st.markdown("""
    <style>
    .prediction-result {
        animation: fadeInDown 0.9s;
        background: rgba(255,255,255,0.96);
        border-radius: 30px;
        box-shadow: 0 8px 44px 0 #818cf833, 0 2.5px 8px 2px #6366f1aa;
        padding: 2.3rem 2.1rem 1.7rem 2.1rem;
        margin-bottom: 2.5rem;
        margin-top: 0.7rem;
        border: 1.5px solid #c7d2fe44;
        max-width: 520px;
        margin-left:auto; margin-right:auto;
        position:relative;
    }
    .salary-display {
        background: linear-gradient(135deg, #10b981 0%, #6366f1 100%);
        color: white;
        padding: 2.3rem 1.2rem 2rem 1.2rem;
        border-radius: 22px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(16,185,129,0.10);
        position: relative;
        margin-bottom: 1.4rem;
        animation: pop-in 1.1s;
    }
    .salary-label {
        font-size: 1.16rem;
        opacity: 0.93;
        font-weight: 500;
        margin-bottom:0.22rem;
        letter-spacing: 0.04em;
    }
    .salary-amount {
        font-size: 3.2rem;
        font-weight: 800;
        margin: 0.7rem 0 0.25rem 0;
        line-height: 1.12;
        z-index: 1;
        letter-spacing: 1px;
        text-shadow: 0 2px 22px #a7f3d0cc;
        animation: pop-in 1.3s;
    }
    .profile-badge {
        display: inline-block;
        background: #fff8;
        color: #047857;
        font-size: 0.92rem;
        border-radius: 10px;
        padding: 0.13rem 0.85rem;
        margin-top: 0.4rem;
        font-weight: 600;
        letter-spacing: 0.01em;
        box-shadow: 0 2px 6px #10b98133;
    }
    .breakdown-grid {
        display: flex;
        justify-content: space-between;
        gap: 1.1rem;
        margin-bottom: 1.2rem;
        margin-top:1.3rem;
    }
    .breakdown-card {
        background: linear-gradient(110deg,#eef2ff 60%, #dbeafe 100%);
        padding: 1.2rem 1.3rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 2px 14px rgba(99,102,241,0.06);
        min-width: 120px;
        flex:1 1 0;
        border:1.5px solid #818cf82a;
        animation: cardFadeIn 1.2s;
    }
    .breakdown-label {
        color: #6d28d9;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
        letter-spacing: 0.01em;
    }
    .breakdown-amount {
        color: #0f172a;
        font-size: 1.45rem;
        font-weight: 800;
        margin-bottom: 0.04rem;
    }
    .chart-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #6366f1;
        margin: 1.4rem 0 0.3rem 0;
        letter-spacing: 0.01em;
    }
    .insights-section {
        margin-top: 2.1rem;
        padding-top: 0.6rem;
        border-top: 1.5px solid #c7d2fe66;
    }
    .insights-grid {
        display: flex;
        flex-direction: column;
        gap: 1.05rem;
        margin-top: 1.2rem;
    }
    .insight-card {
        display: flex;
        gap: 1.08rem;
        align-items: flex-start;
        padding: 1.1rem 1.15rem;
        background: linear-gradient(100deg,#f1f5f9 60%, #c7d2fe 100%);
        border-radius: 14px;
        border-left: 5px solid #6366f1;
        box-shadow: 0 2px 8px #a5b4fc22;
        animation: cardFadeIn 1.3s;
    }
    .insight-card i {
        color: #6366f1;
        font-size: 1.35rem;
        margin-top:0.2rem;
    }
    .insight-card strong {
        color: #0f172a;
        font-size: 1.03rem;
    }
    .insight-card p {
        color: #5b6075;
        font-size: 0.97rem;
        margin:0;
    }
    .action-buttons {
        display: flex;
        gap: 1rem;
        margin-top: 2.1rem;
        justify-content:center;
        flex-wrap: wrap;
    }
    .secondary-btn {
        flex: 1;
        min-width: 140px;
        background: linear-gradient(120deg,#6366f1 70%,#10b981 100%);
        color: white;
        border: none;
        padding: 0.85rem 1.12rem;
        border-radius: 14px;
        font-size: 1.09rem;
        font-weight: 700;
        box-shadow: 0 3px 16px #8b5cf688;
        cursor: pointer;
        transition: background 0.2s, box-shadow 0.22s, transform 0.18s;
        text-align:center;
        margin-bottom:0.3rem;
        outline:none;
    }
    .secondary-btn:hover {
        background: linear-gradient(120deg,#818cf8 60%,#34d399 100%);
        box-shadow: 0 4px 18px #6366f1bb;
        color:#fff;
        transform: translateY(-2px) scale(1.04);
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-34px);}
        to { opacity: 1; transform: translateY(0);}
    }
    @keyframes pop-in {
        0% { opacity: 0; transform: scale(0.87);}
        80% { opacity: 1; transform: scale(1.12);}
        100% { transform: scale(1);}
    }
    @keyframes cardFadeIn {
        from { opacity:0; transform:translateY(30px);}
        to { opacity:1; transform:translateY(0);}
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="prediction-result">
        <div class="salary-display">
            <div class="salary-label">Predicted Annual Salary</div>
            <div class="salary-amount">₹{base_salary:,.0f}</div>
            <div class="profile-badge"><i class="fas fa-user-check"></i> Based on your profile analysis</div>
        </div>
        <div class="breakdown-grid">
            <div class="breakdown-card">
                <div class="breakdown-label">Monthly</div>
                <div class="breakdown-amount">₹{base_salary // 12:,.0f}</div>
            </div>
            <div class="breakdown-card">
                <div class="breakdown-label">Daily</div>
                <div class="breakdown-amount">₹{base_salary // 365:,.0f}</div>
            </div>
            <div class="breakdown-card">
                <div class="breakdown-label">Hourly</div>
                <div class="breakdown-amount">₹{base_salary // (365*8):,.0f}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

    # --- Market Comparison Chart (Plotly) ---
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="chart-title"><i class="fas fa-chart-line"></i> Market Comparison</div>
    """, unsafe_allow_html=True)
    chart_df = pd.DataFrame({
        "Category": ["Industry Average", "Your Prediction", "Top 10% Range"],
        "Salary": [base_salary * 0.85, base_salary, base_salary * 1.2]
    })
    fig = go.Figure(go.Bar(
        x=chart_df["Salary"],
        y=chart_df["Category"],
        orientation="h",
        marker_color=["#f59e0b", "#10b981", "#6366f1"],
        text=[f"₹{x:,.0f}" for x in chart_df["Salary"]],
        textposition="outside"
    ))
    fig.update_layout(height=230, showlegend=False, margin=dict(l=10, r=10, t=20, b=10), xaxis_title="Annual Salary (₹)")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insights-section">
        <h4><i class="fas fa-lightbulb"></i> Key Insights</h4>
        <div class="insights-grid">
            <div class="insight-card">
                <i class="fas fa-trending-up"></i>
                <div>
                    <strong>Growth Potential</strong>
                    <p>Based on your experience, you're positioned for {"senior" if total_experience >= 10 else "rapid"} growth opportunities</p>
                </div>
            </div>
            <div class="insight-card">
                <i class="fas fa-star"></i>
                <div>
                    <strong>Market Position</strong>
                    <p>Your predicted salary is {"above" if base_salary > 800000 else "competitive with"} market standards</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="action-buttons">
        <button class="secondary-btn"><i class="fas fa-download"></i> Download Report</button>
        <button class="secondary-btn"><i class="fas fa-share"></i> Share Result</button>
        <button class="secondary-btn" onclick="window.location.reload()"><i class="fas fa-sync-alt"></i> New Prediction</button>
    </div>
    """, unsafe_allow_html=True)
