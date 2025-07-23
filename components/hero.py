import streamlit as st

def render_hero():
    st.markdown("""
<style>
.hero-banner {
    background: linear-gradient(135deg, #7c3aed, #6366f1);
    color: white;
    padding: 3.5rem 2rem 3rem 2rem;
    border-radius: 24px;
    margin-bottom: 3rem;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    animation: heroFade 1.2s ease-in-out;
}
.hero-banner h1 {
    font-size: 2.9rem;
    font-weight: 800;
    margin-bottom: 1rem;
}
.hero-banner p {
    font-size: 1.15rem;
    max-width: 740px;
    margin: 0 auto 2.8rem;
    line-height: 1.6;
    opacity: 0.95;
}
.hero-cards {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 2rem;
    margin-top: 1.5rem;
}
.card-hero {
    background: rgba(255, 255, 255, 0.12);
    padding: 1.5rem 1.2rem;
    border-radius: 16px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.1);
    min-width: 240px;
    max-width: 320px;
    backdrop-filter: blur(8px);
    transition: transform 0.3s ease, box-shadow 0.3s;
    text-align: center;
    border: 1.5px solid rgba(255,255,255,0.23);
}
.card-hero:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 8px 30px rgba(99,102,241,0.22);
    border-color: #fff;
}
.card-icon {
    font-size: 2.1rem;
    margin-bottom: 0.7rem;
    animation: pop-in 1.1s;
}
.card-title {
    font-size: 1.13rem;
    font-weight: 700;
    margin-bottom: 0.35rem;
    color: #fff;
    letter-spacing: 0.5px;
}
.card-text {
    font-size: 0.98rem;
    opacity: 0.92;
    color: #f8fafc;
    margin-bottom: 0;
}
@keyframes heroFade {
    from { opacity: 0; transform: translateY(40px);}
    to { opacity: 1; transform: translateY(0);}
}
@keyframes pop-in {
    0% { opacity: 0; transform: scale(0.7);}
    80% { opacity: 1; transform: scale(1.08);}
    100% { transform: scale(1);}
}
</style>

<div class="hero-banner">
    <h1>Empower Your Career Growth with AI</h1>
    <p>
        Ready to discover your real market worth? <b>SalaryIQ</b> brings you transparent, data-driven salary projections tailored to your skills, experience, and industry benchmarks.
    </p>
    <div class="hero-cards">
        <div class="card-hero">
            <div class="card-icon">📊</div>
            <div class="card-title">Smart Salary Reports</div>
            <div class="card-text">Instant salary insights personalized to your unique profile.</div>
        </div>
        <div class="card-hero">
            <div class="card-icon">🌐</div>
            <div class="card-title">Industry Benchmarking</div>
            <div class="card-text">Compare your compensation with 500+ top companies in India.</div>
        </div>
        <div class="card-hero">
            <div class="card-icon">✨</div>
            <div class="card-title">Transparent AI</div>
            <div class="card-text">ML-driven predictions with clear confidence scores.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# How to use:
# render_hero()
