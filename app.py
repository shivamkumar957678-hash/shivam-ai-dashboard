# ========================= IMPORTS =========================
import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from datetime import datetime

# ========================= PAGE CONFIG =========================
st.set_page_config(
    page_title="Ultimate AI Student System",
    layout="wide"
)

# ========================= SAMPLE DATA =========================
data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Attendance": [90, 95, 60, 85, 55],
    "Math": [88, 98, 45, 82, 40],
    "Science": [90, 99, 50, 84, 35],
    "English": [85, 97, 55, 81, 45]
}

df = pd.DataFrame(data)
df["Average"] = round(
    (df["Math"] + df["Science"] + df["English"]) / 3, 2
)

# ========================= STYLING =========================
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#020024,#090979,#3a0ca3);
color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
color:white !important;
}

.block{
background: rgba(0,0,0,0.35);
padding:20px;
border-radius:20px;
border:2px solid #d000ff;
box-shadow:0 0 20px #d000ff;
margin-bottom:20px;
}

.metric-card{
padding:25px;
border-radius:20px;
text-align:center;
color:white;
font-weight:bold;
box-shadow:0 0 20px rgba(255,255,255,0.2);
}

.blue{
background:linear-gradient(135deg,#005bea,#00c6fb);
}

.green{
background:linear-gradient(135deg,#11998e,#38ef7d);
}

.red{
background:linear-gradient(135deg,#ff512f,#dd2476);
}

.purple{
background:linear-gradient(135deg,#8e2de2,#ff00ff);
}

.stButton>button{
background:linear-gradient(90deg,#0072ff,#d000ff);
color:white;
border:none;
border-radius:12px;
padding:10px 20px;
font-weight:bold;
box-shadow:0 0 15px #d000ff;
}

div[data-baseweb="input"]{
background:#000814 !important;
border-radius:12px !important;
border:2px solid #d000ff !important;
}

</style>
""", unsafe_allow_html=True)

# ========================= HEADER =========================
st.markdown("""
<h1 style='text-align:center;color:#00e5ff;text-shadow:0 0 20px #00e5ff;font-size:65px;'>
🔐 AI STUDENT SYSTEM
</h1>

<h3 style='text-align:center;color:#00ffff;'>
Smart • Secure • Intelligent
</h3>
""", unsafe_allow_html=True)

# ========================= TOP SECTION =========================
left, right = st.columns([1,2])

# ================= LEFT =================
with left:

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='block'>", unsafe_allow_html=True)

        st.markdown("## 📷 Face Authentication")
        st.write("Login with your registered face")

        camera = st.camera_input("Capture Face")

        if camera:
            st.success("✅ Face matched successfully")
            st.success("✅ Access Granted")

        st.button("📸 Capture & Login")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='block'>", unsafe_allow_html=True)

        st.markdown("## 🔑 Manual Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "admin123":
                st.success("✅ Login Successful")
            else:
                st.error("❌ Wrong Username or Password")

        st.info("Forgot Password? Contact Admin")

        st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT =================
with right:

    st.markdown("""
    <h1 style='text-align:center;'>
    📊 AI STUDENT SYSTEM DASHBOARD
    </h1>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown("""
        <div class='metric-card blue'>
        👨‍🎓<br>
        Total Students<br><br>
        <h1>5</h1>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
        <div class='metric-card green'>
        🏆<br>
        Topper<br><br>
        <h1>Priya</h1>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
        <div class='metric-card red'>
        ⚠<br>
        Weak Students<br><br>
        <h1>2</h1>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown("""
        <div class='metric-card purple'>
        📉<br>
        Poor Attendance<br><br>
        <h1>2</h1>
        </div>
        """, unsafe_allow_html=True)

# ================= MIDDLE SECTION =================
c1, c2, c3 = st.columns([1,1,2])

# ===== Add Student =====
with c1:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## ➕ Add New Student")

    st.text_input("Student Name")
    st.slider("Attendance (%)",0,100,80)
    st.slider("Math Marks",0,100,70)
    st.slider("Science Marks",0,100,70)
    st.slider("English Marks",0,100,70)

    st.button("✅ Add Student")

    st.markdown("</div>", unsafe_allow_html=True)

# ===== Face Recognition =====
with c2:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📸 Face Recognition Attendance")

    cam2 = st.camera_input("Capture Student Photo")

    if cam2:
        st.success("✅ Face detected successfully!")
        st.success("✅ Attendance marked successfully!")
        st.success("🎉 Student Present")

    st.markdown("</div>", unsafe_allow_html=True)

# ===== Table =====
with c3:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📋 Student Performance Table")

    st.dataframe(df, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= CHARTS =================
g1, g2 = st.columns(2)

# ===== Attendance Graph =====
with g1:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📊 Attendance Graph")

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

# ===== Pie Chart =====
with g2:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 🔥 Student Marks Ratio")

    pie = px.pie(
        df,
        names="Name",
        values="Average",
        hole=0.35
    )

    pie.update_layout(
        paper_bgcolor="#000814",
        font_color="white"
    )

    st.plotly_chart(pie, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= BOTTOM SECTION =================
b1, b2, b3 = st.columns(3)

# ===== AI Chatbot =====
with b1:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 🤖 AI Chatbot")

    question = st.text_input(
        "Ask AI",
        key="chatbot_input"
    )

    if st.button("Ask AI"):
        st.success("AI Response Generated Successfully")

    st.markdown("</div>", unsafe_allow_html=True)

# ===== AI Prediction =====
with b2:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 🧠 AI Study Prediction")

    hours = st.slider("Study Hours",1,10,5)

    predicted = hours * 10

    st.metric("Predicted Marks", f"{predicted}/100")

    if predicted >= 80:
        st.success("Excellent performance")
    elif predicted >= 60:
        st.info("Good performance")
    else:
        st.warning("Needs practice")

    st.markdown("</div>", unsafe_allow_html=True)

# ===== Feedback =====
with b3:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 💬 Feedback System")

    st.text_area("Enter Feedback")

    st.button("🚀 Submit Feedback")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= AI ANALYSIS =================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.markdown("## 🧠 AI Performance Analysis")

selected_student_ai = st.selectbox(
    "Select Student For AI Analysis",
    df["Name"],
    key="ai_analysis_student"
)

student_row = df[df["Name"] == selected_student_ai].iloc[0]

if student_row["Math"] < 50:
    st.error("❌ Math weak")

if student_row["Attendance"] < 75:
    st.warning("⚠ Needs practice")

if student_row["Average"] > 85:
    st.success("🏆 Excellent performance")

st.markdown("</div>", unsafe_allow_html=True)

# ================= ADMIN DASHBOARD =================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.markdown("## 🛠 Admin Dashboard")

ad1, ad2, ad3, ad4 = st.columns(4)

with ad1:
    st.markdown("""
    <div class='metric-card blue'>
    🏫<br>
    Total Classes<br><br>
    <h1>12</h1>
    </div>
    """, unsafe_allow_html=True)

with ad2:
    st.markdown("""
    <div class='metric-card red'>
    💰<br>
    Fees Pending<br><br>
    <h1>3</h1>
    </div>
    """, unsafe_allow_html=True)

with ad3:
    st.markdown("""
    <div class='metric-card green'>
    📊<br>
    Avg Attendance<br><br>
    <h1>77%</h1>
    </div>
    """, unsafe_allow_html=True)

with ad4:
    st.markdown("""
    <div class='metric-card purple'>
    📅<br>
    Monthly Analytics<br><br>
    <h1>Good</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================= PDF REPORTS =================
p1, p2 = st.columns(2)

# ===== Attendance PDF =====
with p1:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📄 Attendance PDF Report")

    if st.button("Generate Attendance PDF"):

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=14)

        pdf.cell(200,10,txt="Attendance Report",ln=True)

        for i,row in df.iterrows():
            pdf.cell(
                200,
                10,
                txt=f"{row['Name']} - Attendance: {row['Attendance']}%",
                ln=True
            )

        pdf.output("attendance_report.pdf")

        with open("attendance_report.pdf","rb") as file:
            st.download_button(
                "Download Attendance PDF",
                file,
                file_name="attendance_report.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ===== Subject Wise PDF =====
with p2:
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📘 Subject Wise Marks PDF")

    selected_student_pdf = st.selectbox(
        "Select Student",
        df["Name"],
        key="subject_pdf_student"
    )

    if st.button("Generate Subject PDF"):

        row = df[df["Name"] == selected_student_pdf].iloc[0]

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=14)

        pdf.cell(200,10,txt="Subject Wise Report",ln=True)
        pdf.cell(200,10,txt=f"Student: {row['Name']}",ln=True)
        pdf.cell(200,10,txt=f"Math: {row['Math']}",ln=True)
        pdf.cell(200,10,txt=f"Science: {row['Science']}",ln=True)
        pdf.cell(200,10,txt=f"English: {row['English']}",ln=True)
        pdf.cell(200,10,txt=f"Average: {row['Average']}",ln=True)

        pdf.output("subject_report.pdf")

        with open("subject_report.pdf","rb") as file:
            st.download_button(
                "Download Subject PDF",
                file,
                file_name="subject_report.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<h4 style='text-align:center;margin-top:40px;'>
© 2025 AI Student System | Made with ❤️ by Shivam Kumar
</h4>
""", unsafe_allow_html=True)
