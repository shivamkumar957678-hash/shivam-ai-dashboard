import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Student System", layout="wide")

# ===================== CSS =====================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#000814,#140152,#3a0ca3);
    color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#00e5ff;
    text-shadow:0 0 20px #00e5ff;
}

.sub-title{
    text-align:center;
    color:#00ffff;
    font-size:24px;
    margin-bottom:25px;
}

.neon-box{
    background:rgba(0,0,0,0.45);
    border:1px solid #bb00ff;
    border-radius:18px;
    padding:18px;
    box-shadow:0 0 18px #bb00ff;
    margin-bottom:20px;
}

.metric-card{
    padding:20px;
    border-radius:18px;
    text-align:center;
    color:white;
    font-weight:bold;
    box-shadow:0 0 20px rgba(255,255,255,0.2);
}

.blue-card{
    background:linear-gradient(135deg,#0052D4,#4364F7);
}

.green-card{
    background:linear-gradient(135deg,#11998e,#38ef7d);
}

.orange-card{
    background:linear-gradient(135deg,#ff512f,#dd2476);
}

.purple-card{
    background:linear-gradient(135deg,#8E2DE2,#DA22FF);
}

.stTextInput input{
    background:#020b2d !important;
    color:white !important;
    border:2px solid #bb00ff !important;
    border-radius:10px !important;
}

.stTextArea textarea{
    background:#020b2d !important;
    color:white !important;
    border:2px solid #bb00ff !important;
    border-radius:10px !important;
}

.stSlider{
    color:white !important;
}

.stButton button{
    width:100%;
    background:linear-gradient(90deg,#0072ff,#d400ff);
    color:white;
    border:none;
    border-radius:10px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
    box-shadow:0 0 15px #bb00ff;
}

table{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ===================== TITLE =====================

st.markdown("<div class='main-title'>🔐 AI STUDENT SYSTEM</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Smart • Secure • Intelligent</div>", unsafe_allow_html=True)

# ===================== DATA =====================

df = pd.DataFrame({
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45],
    "Average":[87.67,98,50,82.33,40]
})

# ===================== TOP SECTION =====================

left,right = st.columns([1.1,2])

# ===================== LEFT =====================

with left:

    col1,col2 = st.columns(2)

    with col1:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
        st.markdown("## 📷 Face Authentication")
        st.write("Login with your registered face")
        st.camera_input("Capture Face")
        st.button("📸 Capture & Login")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
        st.markdown("## 🔑 Manual Login")
        st.text_input("Username")
        st.text_input("Password", type="password")
        st.button("Login")
        st.error("❌ Wrong Username or Password")
        st.markdown("</div>", unsafe_allow_html=True)

    col3,col4 = st.columns(2)

    with col3:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
        st.markdown("## ➕ Add New Student")
        st.text_input("Student Name")
        st.slider("Attendance (%)",0,100,80)
        st.slider("Math Marks",0,100,70)
        st.slider("Science Marks",0,100,70)
        st.slider("English Marks",0,100,70)
        st.button("✅ Add Student")
        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
        st.markdown("## 🪪 Face Recognition Attendance")
        st.write("Click below to capture student photo")
        st.camera_input(" ")
        st.button("📷 Take Photo")
        st.success("✅ Face detected successfully!")
        st.success("✅ Attendance marked successfully!")
        st.write("🎉 Student Present")
        st.markdown("</div>", unsafe_allow_html=True)

# ===================== RIGHT =====================

with right:

    st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class='metric-card blue-card'>
            <h4>👨‍🎓 Total Students</h4>
            <h1>5</h1>
            <p>All Registered Students</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric-card green-card'>
            <h4>🏆 Topper</h4>
            <h1>Priya</h1>
            <p>Highest Average Marks</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-card orange-card'>
            <h4>⚠️ Weak Students</h4>
            <h1>2</h1>
            <p>Need Improvement</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class='metric-card purple-card'>
            <h4>📉 Poor Attendance</h4>
            <h1>2</h1>
            <p>Attendance &lt; 75%</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
    st.markdown("## 📋 Student Performance Table")
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    g1,g2 = st.columns(2)

    with g1:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)

        fig = px.bar(
            df,
            x="Name",
            y="Attendance",
            color="Name",
            text="Attendance"
        )

        fig.update_layout(
            paper_bgcolor="#000814",
            plot_bgcolor="#000814",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with g2:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)

        pie = px.pie(
            df,
            names="Name",
            values="Average",
            hole=0.35
        )

        pie.update_layout(
            paper_bgcolor="#000814",
            plot_bgcolor="#000814",
            font_color="white"
        )

        st.plotly_chart(pie, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    b1,b2,b3 = st.columns(3)

    with b1:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
        st.markdown("## 🤖 AI Chatbot")
        st.write("Ask any question about students")
        st.text_input("Type your question...")
        st.button("Ask")
        st.write("Quick Examples:")
        st.info("Rahul Math marks")
        st.info("Priya Attendance")
        st.info("Topper")
        st.info("Weak Students")
        st.markdown("</div>", unsafe_allow_html=True)

    with b2:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
        st.markdown("## 🧠 AI Study Prediction")

        hours = st.slider("Study Hours (per day)",1,10,6)

        marks = hours * 10

        st.metric("Predicted Marks", f"{marks}/100")

        if marks >= 60:
            st.success("🚀 Good! Keep it up and you can score well.")
        else:
            st.error("⚠️ Study more to improve marks.")

        st.markdown("</div>", unsafe_allow_html=True)

    with b3:
        st.markdown("<div class='neon-box'>", unsafe_allow_html=True)
        st.markdown("## 💬 Feedback System")
        st.write("We value your feedback")
        st.text_area("Enter your feedback...")
        st.button("📨 Submit Feedback")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<center><h4 style='color:white;'>© 2025 AI Student System | Made with ❤️ by Shivam Kumar</h4></center>",
    unsafe_allow_html=True
)
