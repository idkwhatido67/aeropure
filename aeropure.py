import streamlit as st

# 1. PAGE CONFIG
st.set_page_config(page_title="AeroPure Official", layout="wide")

# 2. SESSION STATE FOR POINTS
if 'balance' not in st.session_state:
    st.session_state.balance = 0

# 3. CSS (Forcing dark text on white background)
st.markdown("""
<style>
    /* Force everything to black text for visibility */
    .stApp, h1, h2, h3, h4, p, div, span, label {
        color: #000000 !important;
    }
    .stApp { background-color: #FFFFFF !important; }
    
    /* Header/Ticker Styling */
    .header-wrapper { background-color: #FFFFFF; border-bottom: 2px solid #0056b3; margin-bottom: 20px; }
    .ticker { background-color: #0056b3; color: white !important; padding: 5px 0; overflow: hidden; white-space: nowrap; }
    .ticker p { display: inline-block; padding-left: 100%; animation: marquee 20s linear infinite; margin: 0; }
    @keyframes marquee { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }
    .nav-bar { padding: 20px; display: flex; justify-content: space-between; align-items: center; }
    .brand-title { color: #0056b3 !important; font-weight: 800; font-size: 2em; }
</style>
""", unsafe_allow_html=True)

# 4. HEADER
st.markdown("""
<div class="header-wrapper">
    <div class="ticker"><p>AEROPURE: PURE WATER SOLUTIONS • SUSTAINABILITY FIRST • INNOVATIVE ATMOSPHERIC TECHNOLOGY</p></div>
    <div class="nav-bar"><div class="brand-title">AEROPURE</div></div>
</div>
""", unsafe_allow_html=True)

# 5. DASHBOARD CONTENT
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
            st.session_state.balance += 50
            st.success("CODE REDEEMED: +50 Points")
        elif voucher == "PROMO100":
            st.session_state.balance += 100
            st.success("CODE REDEEMED: +100 Points")
        else:
            st.error("INVALID CODE")
            
    st.write(f"### Balance: {st.session_state.balance} Aqua Points")