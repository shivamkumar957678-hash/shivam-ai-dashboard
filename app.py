import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Ultimate AI Student System",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================

if "saved_password" not in st.session_state:
    st.session_state.saved_password = "admin123"

if "saved_email" not in st.session_state:
    st.session_state.saved_email = "admin@gmail.com"

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020024,#090979,#3a0ca3);
color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
color:white !important;
}

.metric-card{
height:220px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
border-radius:20px;
padding:20px;
text-align:center;
color:white;
font-weight:bold;
box-shadow:0 0 20px rgba(255,255,255,0.2);
}

.card1{
background:linear-gradient(135deg,#00c6ff,#0072ff);
}

.card2{
background:linear-gradient(135deg,#00b09b,#96c93d);
}

.card3{
background:linear-gradient(135deg,#ff416c,#ff4b2b);
}

.card4{
background:linear-gradient(135deg,#8e2de2,#ff00ff);
}

.admin-card{
background:linear-gradient(135deg,#141e30,#243b55);
padding:20px;
border-radius:20px;
text-align:center;
box-shadow:0 0 15px #00e5ff;
height:180px;
}

.neon-box{
background:#05003b;
padding:20px;
border-radius:20px;
border:2px solid #ff00ff;
box-shadow:0 0 20px #ff00ff;
margin-bottom:20px;
}

.stButton>button{
background:linear-gradient(90deg,#0072ff,#ff00ff);
color:white;
border:none;
border-radius:15px;
padding:12px 25px;
font-size:18px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SAMPLE DATA
# =========================

data = {
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45]
}

df = pd.DataFrame(data)

df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
)/3

topper = df.loc[df["Average"].idxmax()]["Name"]

weak_students = len(df[df["Average"] < 60])

poor_attendance = len(df[df["Attendance"] < 75])

# =========================
# TITLE
# =========================

st.markdown("""
<h1 style='text-align:center;
font-size:65px;
color:#00e5ff;
text-shadow:0 0 20px #00e5ff;'>
🔐 AI STUDENT SYSTEM
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;color:#00ffff;'>
Smart • Secure • Intelligent
</h3>
""", unsafe_allow_html=True)

st.write("")

# =========================
# TOP SECTION
# =========================

col1,col2,col3,col4,col5,col6 = st.columns(6)

# =========================
# FACE AUTH
# =========================

with col1:

    st.markdown("""
    <div class="neon-box">
    <h2>📷 Face Authentication</h2>
    <p>Login with your registered face</p>
    </div>
    """, unsafe_allow_html=True)

    st.camera_input("Capture Face")

    st.button("📸 Capture & Login")

# =========================
# LOGIN
# =========================

with col2:

    st.markdown("""
    <div class="neon-box">
    <h2>🔑 Manual Login</h2>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if (
            username == "admin"
            and
            password == st.session_state.saved_password
        ):

            st.success("✅ Login Successful")

        else:

            st.error("❌ Wrong Username or Password")

# =========================
# CARDS
# =========================

with col3:

    st.markdown(f"""
    <div class="metric-card card1">
    <h2>👨‍🎓</h2>
    <h3>Total Students</h3>
    <h1>{len(df)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="metric-card card2">
    <h2>🏆</h2>
    <h3>Topper</h3>
    <h1>{topper}</h1>
    </div>
    """, unsafe_allow_html=True)

with col5:

    st.markdown(f"""
    <div class="metric-card card3">
    <h2>⚠</h2>
    <h3>Weak Students</h3>
    <h1>{weak_students}</h1>
    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown(f"""
    <div class="metric-card card4">
    <h2>📉</h2>
    <h3>Poor Attendance</h3>
    <h1>{poor_attendance}</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FORGOT PASSWORD
# =========================

st.write("")
st.write("")

st.markdown("""
<div class="neon-box">
<h1>🔐 Forgot Password System</h1>
</div>
""", unsafe_allow_html=True)

with st.expander("Open Forgot Password"):

    forgot_user = st.text_input(
        "Enter Username"
    )

    forgot_email = st.text_input(
        "Enter Email"
    )

    otp = st.text_input(
        "Enter OTP"
    )

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    if st.button("Send OTP"):

        if (
            forgot_user == "admin"
            and
            forgot_email == st.session_state.saved_email
        ):

            st.success("✅ OTP Sent Successfully")

            st.info("Demo OTP: 1234")

        else:

            st.error("❌ Invalid Username or Email")

    if st.button("Reset Password"):

        if otp == "1234":

            st.session_state.saved_password = new_password

            st.success(
                "✅ Password Reset Successful"
            )

            st.info(
                f"New Password Set: {new_password}"
            )

        else:

            st.error("❌ Wrong OTP")

# =========================
# SEARCH STUDENT
# =========================

st.markdown("""
<div class="neon-box">
<h1>🔍 Search Student</h1>
</div>
""", unsafe_allow_html=True)

search = st.text_input("Enter Student Name")

if search:

    result = df[df["Name"].str.contains(search, case=False)]

    st.dataframe(result)

# =========================
# STUDENT TABLE
# =========================

st.markdown("""
<div class="neon-box">
<h1>📋 Student Performance Table</h1>
</div>
""", unsafe_allow_html=True)

st.dataframe(df, use_container_width=True)

# =========================
# AI ANALYSIS
# =========================

st.markdown("""
<div class="neon-box">
<h1>🤖 AI Performance Analysis</h1>
</div>
""", unsafe_allow_html=True)

for i,row in df.iterrows():

    if row["Average"] >= 90:

        st.success(
            f"{row['Name']} → Excellent Performance"
        )

    elif row["Average"] >= 60:

        st.warning(
            f"{row['Name']} → Needs Practice"
        )

    else:

        st.error(
            f"{row['Name']} → Weak in Studies"
        )

# =========================
# CHARTS
# =========================

st.markdown("""
<div class="neon-box">
<h1>📊 Analytics Dashboard</h1>
</div>
""", unsafe_allow_html=True)

fig = px.bar(
    df,
    x="Name",
    y="Average",
    color="Average"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.line(
    df,
    x="Name",
    y="Attendance",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# ADMIN DASHBOARD
# =========================

st.markdown("""
<div class="neon-box">
<h1>🛠 Admin Dashboard</h1>
</div>
""", unsafe_allow_html=True)

a1,a2,a3,a4 = st.columns(4)

with a1:

    st.markdown("""
    <div class="admin-card">
    <h3>🏫 Total Classes</h3>
    <h1>12</h1>
    </div>
    """, unsafe_allow_html=True)

with a2:

    st.markdown("""
    <div class="admin-card">
    <h3>💰 Fees Pending</h3>
    <h1>3</h1>
    </div>
    """, unsafe_allow_html=True)

with a3:

    st.markdown(f"""
    <div class="admin-card">
    <h3>📊 Avg Attendance</h3>
    <h1>{round(df['Attendance'].mean(),1)}%</h1>
    </div>
    """, unsafe_allow_html=True)

with a4:

    st.markdown("""
    <div class="admin-card">
    <h3>📅 Monthly Analytics</h3>
    <h1>Good</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PDF REPORTS
# =========================

p1,p2 = st.columns(2)

with p1:

    st.markdown("""
    <div class="neon-box">
    <h2>📄 Attendance PDF Report</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Generate Attendance PDF"):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=14)

        pdf.cell(200,10,txt="Attendance Report",ln=True)

        for i,row in df.iterrows():

            pdf.cell(
                200,
                10,
                txt=f"{row['Name']} - {row['Attendance']}%",
                ln=True
            )

        pdf.output("attendance_report.pdf")

        with open("attendance_report.pdf","rb") as file:

            st.download_button(
                "Download Attendance PDF",
                file,
                file_name="attendance_report.pdf"
            )

with p2:

    st.markdown("""
    <div class="neon-box">
    <h2>📘 Subject Wise Marks PDF</h2>
    </div>
    """, unsafe_allow_html=True)

    student_name = st.selectbox(
        "Select Student",
        df["Name"]
    )

    if st.button("Generate Subject PDF"):

        student = df[df["Name"] == student_name].iloc[0]

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=14)

        pdf.cell(200,10,txt="Subject Wise Report",ln=True)

        pdf.cell(200,10,txt=f"Name: {student['Name']}",ln=True)

        pdf.cell(200,10,txt=f"Math: {student['Math']}",ln=True)

        pdf.cell(200,10,txt=f"Science: {student['Science']}",ln=True)

        pdf.cell(200,10,txt=f"English: {student['English']}",ln=True)

        pdf.output("subject_report.pdf")

        with open("subject_report.pdf","rb") as file:

            st.download_button(
                "Download Subject PDF",
                file,
                file_name="subject_report.pdf"
            )

# =========================
# VOICE ASSISTANT
# =========================

st.markdown("""
<div class="neon-box">
<h1>🎤 Voice Assistant</h1>
<p>Type: Show Rahul Marks</p>
</div>
""", unsafe_allow_html=True)

voice = st.text_input("Voice Command")

if "rahul" in voice.lower():

    st.success(df[df["Name"]=="Rahul"])

# =========================
# FOOTER
# =========================

st.markdown("""
<h3 style='text-align:center;color:#00ffff;'>
🚀 Ultimate AI Student System Developed By Shivam
</h3>
""", unsafe_allow_html=True)
