import streamlit as st
import random

from components.style import inject_custom_css
from components.header import render_header
from components.hero import render_hero
from components.form import render_form
from components.results import render_welcome, render_results
from components.footer import render_footer

st.set_page_config(page_title="💼 Employee Salary Predictor - AI SalaryIQ", page_icon="💰", layout="wide")
inject_custom_css()
render_header()
render_hero()

col1, col2 = st.columns([1,2], gap="large")

with col1:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    submitted, age, gender, marital_status, dependents, department, position, insurance, total_experience, company_experience = render_form()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="results-area">', unsafe_allow_html=True)
    if not submitted:
        render_welcome()
    else:
        # --- Salary Calculation Logic ---
        base_salary = 500000
        base_salary += (age - 25) * 15000
        base_salary += total_experience * 45000
        dept_multiplier = {
            'IT': 1.3, 'Sales': 1.1, 'Marketing': 1.0, 'Finance': 1.2, 'Human Resources': 0.9
        }
        base_salary *= dept_multiplier[department]
        if "Director" in position:
            base_salary *= 1.8
        elif "Manager" in position or "Lead" in position:
            base_salary *= 1.4
        elif "Senior" in position or "III" in position:
            base_salary *= 1.2
        base_salary += (random.random() - 0.5) * 100000
        base_salary = max(300000, round(base_salary))
        render_results(base_salary, total_experience)
    st.markdown('</div>', unsafe_allow_html=True)

render_footer()
