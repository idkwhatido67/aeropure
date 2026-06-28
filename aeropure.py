import streamlit as st

# 1. PAGE CONFIG
st.set_page_config(page_title="AeroPure Official", layout="wide")

# 2. BRIGHT, PREMIUM CORPORATE CSS
def apply_bright_theme():
    st.markdown("""
    <style>
    /* Force Bright White Background */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Top Bar Wrapper */
    .header-wrapper {
        background-color: #FFFFFF;
        border-bottom: 2px solid #0056b3;
        margin-bottom: 20px;
    }
    
    /* Ticker Styling */
    .ticker {
        background-color: #0056b3;
        color: white;
        padding: 5px 0;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
    }
    .ticker p {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 20s linear infinite;
        margin: 0;
    }
    @keyframes marquee {
        0% { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }
    
    /* Nav Styling */
    .nav-bar {
        padding: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    /* Text and Elements */
    h1, h2, h3, p, div { color: #1A1A1A !important; font-family: 'Helvetica', sans-serif !important; }
    .brand-title { color: #0056b3 !important; font-weight: 800; font-size: 2em; }
    
    /* Buttons */
    div.stButton > button {
        background-color: #0056b3 !important;
        color: white !important;
        border-radius: 0px !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

apply_bright_theme()

# 3. TOP NAVIGATION BAR WITH TICKER
st.markdown("""
<div class="header-wrapper">
    <div class="ticker"><p>AEROPURE: PURE WATER SOLUTIONS • INNOVATIVE ATMOSPHERIC TECHNOLOGY • SUSTAINABILITY FIRST • AEROPURE: PURE WATER SOLUTIONS • INNOVATIVE ATMOSPHERIC TECHNOLOGY</p></div>
    <div class="nav-bar">
        <div class="brand-title">AEROPURE</div>
        <div>
            <strong>ABOUT US</strong> | <strong>TECHNOLOGY</strong> | <strong>SUSTAINABILITY</strong>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. CONTENT
st.title("PREMIUM ATMOSPHERIC WATER")
st.write("Welcome to the next generation of atmospheric water generation.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("SYSTEM PERFORMANCE")
    st.info("System Status: OPERATIONAL")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Tank Level", "85%")
    m2.metric("Efficiency", "92%")
    m3.metric("Temp", "22°C")

with col2:
    st.subheader("DASHBOARD")
    voucher = st.text_input("VOUCHER KEY", type="password")
    if st.button("VALIDATE KEY"):
        if voucher == "3688f3h":
            st.success("ACCESS GRANTED")
        else:
            st.error("ACCESS DENIED")
    st.write("Balance: 0 Aqua Points")