# ========================= IMPORTS =========================
import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# ========================= PAGE CONFIG =========================
st.set_page_config(
    page_title="Ultimate AI Student System",
    layout="wide"
)

# ========================= DATA =========================
data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Attendance": [90, 95, 60, 85, 55],
    "Math": [88, 98, 45, 82, 40],
    "Science": [90, 99, 50, 84, 35],
    "English": [85, 97, 55, 81, 45]
}

df = pd.DataFrame(data)

df["Average"] = round(
    (df["Math"] + df["Science"] + df["English"]) / 3,
    2
)

# ========================= CSS =========================
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

.stButton>button{
background:linear-gradient(90deg,#0072ff,#d000ff);
color:white;
border:none;
border-radius:12px;
padding:10px 20px;
font-weight:bold;
width:100%;
}

</style>
""", unsafe_allow_html=True)

# ========================= HEADER =========================
st.markdown("""
<h1 style='text-align:center;
color:#00e5ff;
font-size:65px;
text-shadow:0 0 20px #00e5ff;'>
🔐 AI STUDENT SYSTEM
</h1>

<h3 style='text-align:center;color:#00ffff;'>
Smart • Secure • Intelligent
</h3>
""", unsafe_allow_html=True)

# ========================= MAIN LAYOUT =========================
left, right = st.columns([1,2])

# ========================= LEFT SIDE =========================
with left:

    l1, l2 = st.columns(2)

    # FACE AUTH
    with l1:

        st.markdown("<div class='block'>", unsafe_allow_html=True)

        st.markdown("## 📷 Face Authentication")

        camera = st.camera_input("Capture Face")

        if camera:
            st.success("✅ Face matched successfully!")

        st.button("📸 Capture & Login")

        st.markdown("</div>", unsafe_allow_html=True)

    # LOGIN
    with l2:

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

# ========================= RIGHT SIDE =========================
with right:

    st.markdown("""
    <h1 style='text-align:center;'>
    📊 AI STUDENT SYSTEM DASHBOARD
    </h1>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)

    card_style = """
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
    """

    with m1:
        st.markdown(f"""
        <div style="
        {card_style}
        background:linear-gradient(135deg,#005bea,#00c6fb);
        ">
        <h2>👨‍🎓</h2>
        <h3>Total Students</h3>
        <h1>5</h1>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div style="
        {card_style}
        background:linear-gradient(135deg,#11998e,#38ef7d);
        ">
        <h2>🏆</h2>
        <h3>Topper</h3>
        <h1>Priya</h1>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div style="
        {card_style}
        background:linear-gradient(135deg,#ff512f,#dd2476);
        ">
        <h2>⚠</h2>
        <h3>Weak Students</h3>
        <h1>2</h1>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
        <div style="
        {card_style}
        background:linear-gradient(135deg,#8e2de2,#ff00ff);
        ">
        <h2>📉</h2>
        <h3>Poor Attendance</h3>
        <h1>2</h1>
        </div>
        """, unsafe_allow_html=True)

# ========================= TABLE =========================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.markdown("## 📋 Student Performance Table")

st.dataframe(df, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ========================= CHARTS =========================
c1, c2 = st.columns(2)

with c1:

    fig = px.bar(
        df,
        x="Name",
        y="Attendance",
        color="Name",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#000814",
        plot_bgcolor="#000814"
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:

    pie = px.pie(
        df,
        names="Name",
        values="Average",
        hole=0.35,
        template="plotly_dark"
    )

    pie.update_layout(
        paper_bgcolor="#000814",
        plot_bgcolor="#000814"
    )

    st.plotly_chart(pie, use_container_width=True)

# ========================= AI FEATURES =========================
a1, a2, a3 = st.columns(3)

# AI CHATBOT
with a1:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 🤖 AI Chatbot")

    q = st.text_input("Ask AI")

    if st.button("Ask AI"):
        st.success("AI Response Generated Successfully")

    st.markdown("</div>", unsafe_allow_html=True)

# AI ANALYSIS
with a2:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 🧠 AI Performance Analysis")

    student = st.selectbox(
        "Select Student",
        df["Name"],
        key="analysis"
    )

    row = df[df["Name"] == student].iloc[0]

    if row["Math"] < 50:
        st.error("❌ Math Weak")

    elif row["Average"] > 85:
        st.success("🏆 Excellent Performance")

    else:
        st.warning("⚠ Needs Practice")

    st.markdown("</div>", unsafe_allow_html=True)

# VOICE ASSISTANT
with a3:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 🎤 Voice Assistant")

    voice = st.text_input(
        "Example: Show Rahul marks"
    )

    if st.button("Run Voice Command"):

        cmd = voice.lower()

        for i, row in df.iterrows():

            if row["Name"].lower() in cmd:

                st.success(f"{row['Name']} Marks")

                st.write(f"Math: {row['Math']}")
                st.write(f"Science: {row['Science']}")
                st.write(f"English: {row['English']}")

    st.markdown("</div>", unsafe_allow_html=True)

# ========================= ADMIN DASHBOARD =========================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.markdown("## 🛠 Admin Dashboard")

ad1, ad2, ad3, ad4 = st.columns(4)

with ad1:
    st.metric("🏫 Total Classes", "12")

with ad2:
    st.metric("💰 Fees Pending", "3")

with ad3:
    st.metric(
        "📊 Avg Attendance",
        f"{round(df['Attendance'].mean(),2)}%"
    )

with ad4:
    st.metric("📅 Monthly Analytics", "Good")

st.markdown("</div>", unsafe_allow_html=True)

# ========================= PDF REPORTS =========================
p1, p2 = st.columns(2)

# ATTENDANCE PDF
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
                "⬇ Download Attendance PDF",
                file,
                file_name="attendance_report.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# SUBJECT PDF
with p2:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📘 Subject Wise PDF Report")

    student_pdf = st.selectbox(
        "Select Student",
        df["Name"],
        key="pdf_student"
    )

    if st.button("Generate Subject PDF"):

        row = df[df["Name"] == student_pdf].iloc[0]

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=14)

        pdf.cell(200,10,txt="Subject Wise Report",ln=True)

        pdf.cell(200,10,txt=f"Student: {row['Name']}",ln=True)

        pdf.cell(200,10,txt=f"Math: {row['Math']}",ln=True)

        pdf.cell(200,10,txt=f"Science: {row['Science']}",ln=True)

        pdf.cell(200,10,txt=f"English: {row['English']}",ln=True)

        pdf.output("subject_report.pdf")

        with open("subject_report.pdf","rb") as file:

            st.download_button(
                "⬇ Download Subject PDF",
                file,
                file_name="subject_report.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ========================= FOOTER =========================
st.markdown("""
<h4 style='text-align:center;color:white;'>
© 2025 AI Student System | Made with ❤️ by Shivam Kumar
</h4>
""", unsafe_allow_html=True)
