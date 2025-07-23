import streamlit as st

def render_form():
    st.markdown("""
    <style>
    .form-section-title {
        font-size: 1.14rem;
        font-weight: 700;
        color: #6366f1;
        margin: 1.2rem 0 0.5rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .stSlider, .stSelectbox, .stButton button {
        margin-bottom: 0.5rem !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #6366f1 0%, #10b981 100%) !important;
        color: #fff !important;
        font-weight: 700;
        font-size: 1.09rem;
        border-radius: 14px !important;
        padding: 0.65rem 1.4rem !important;
        margin-top: 1.3rem !important;
        border: none;
        box-shadow: 0 2px 14px rgba(99,102,241,0.13);
        transition: box-shadow 0.14s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #4f46e5 0%, #059669 100%) !important;
        box-shadow: 0 6px 22px rgba(99,102,241,0.16);
    }
    </style>
    """, unsafe_allow_html=True)

    with st.form("salary_predict_form"):
        st.markdown('<div class="form-section-title"><i class="fas fa-user"></i> Personal Details</div>', unsafe_allow_html=True)
        age = st.slider("Age", 18, 65, 30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
        dependents = st.slider("Number of Dependents", 0, 10, 2)

        st.markdown('<div class="form-section-title"><i class="fas fa-building"></i> Professional Details</div>', unsafe_allow_html=True)
        department = st.selectbox("Department", [
            "IT", "Sales", "Marketing", "Finance", "Human Resources"
        ])
        position = st.selectbox("Position", [
            "Software Engineer I", "Software Engineer II", "Software Engineer III", "Technical Lead", "IT Manager",
            "Sales Representative", "Sales Executive", "Regional Sales Manager", "Sales Director",
            "Marketing Associate", "Marketing Executive", "Marketing Director",
            "HR Associate", "HR Executive", "HR Director"
        ])
        insurance = st.selectbox("Insurance Coverage", [
            "Both", "Medical", "Life", "None"
        ])

        st.markdown('<div class="form-section-title"><i class="fas fa-chart-line"></i> Experience</div>', unsafe_allow_html=True)
        total_experience = st.slider("Total Experience (Years)", 0, 50, 10)
        company_experience = st.slider("Years in Current Company", 0, 40, 5)

        submitted = st.form_submit_button("🔮 Predict Salary")
    return submitted, age, gender, marital_status, dependents, department, position, insurance, total_experience, company_experience
