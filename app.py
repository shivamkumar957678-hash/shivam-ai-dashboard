import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from datetime import datetime
import os

# ========================= PAGE CONFIG =========================
st.set_page_config(
    page_title="Ultimate AI Student System",
    layout="wide"
)

# ========================= DATABASE =========================
if os.path.exists("students.csv"):

    df = pd.read_csv("students.csv")

else:

    data = {
        "Name": ["Rahul", "Priya", "Aman"],
        "Attendance": [90,95,60],
        "Math": [88,98,45],
        "Science": [90,99,50],
        "English": [85,97,55]
    }

    df = pd.DataFrame(data)

    df.to_csv("students.csv", index=False)

df["Average"] = round(
    (df["Math"] + df["Science"] + df["English"]) / 3,
    2
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

</style>
""", unsafe_allow_html=True)

# ========================= HEADER =========================
st.markdown("""
<h1 style='text-align:center;color:#00e5ff;
text-shadow:0 0 20px #00e5ff;font-size:65px;'>
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

    # ===== FACE LOGIN =====
    with col1:

        st.markdown("<div class='block'>", unsafe_allow_html=True)

        st.markdown("## 📷 Face Authentication")

        camera = st.camera_input("Capture Face")

        if camera:
            st.success("✅ Face matched successfully")
            st.success("✅ Access Granted")

        st.button("📸 Capture & Login")

        st.markdown("</div>", unsafe_allow_html=True)

    # ===== LOGIN =====
    with col2:

        st.markdown("<div class='block'>", unsafe_allow_html=True)

        st.markdown("## 🔑 Manual Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if (
                username == "admin"
                and
                password == "admin123"
            ):

                st.success("✅ Login Successful")

            else:

                st.error(
                    "❌ Wrong Username or Password"
                )

        st.info("Forgot Password? Contact Admin")

        st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT =================
with right:

    st.markdown("""
    <h1 style='text-align:center;'>
    📊 AI STUDENT SYSTEM DASHBOARD
    </h1>
    """, unsafe_allow_html=True)

    topper = df.sort_values(
        "Average",
        ascending=False
    ).iloc[0]["Name"]

    weak_students = len(
        df[df["Average"] < 60]
    )

    poor_attendance = len(
        df[df["Attendance"] < 75]
    )

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(f"""
        <div class='metric-card blue'>
        👨‍🎓<br>
        Total Students<br><br>
        <h1>{len(df)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class='metric-card green'>
        🏆<br>
        Topper<br><br>
        <h1>{topper}</h1>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class='metric-card red'>
        ⚠<br>
        Weak Students<br><br>
        <h1>{weak_students}</h1>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
        <div class='metric-card purple'>
        📉<br>
        Poor Attendance<br><br>
        <h1>{poor_attendance}</h1>
        </div>
        """, unsafe_allow_html=True)

# ========================= MIDDLE SECTION =========================
c1, c2, c3 = st.columns([1,1,2])

# ================= ADD STUDENT =================
with c1:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## ➕ Add New Student")

    new_name = st.text_input("Student Name")

    new_att = st.slider(
        "Attendance (%)",
        0,
        100,
        80
    )

    new_math = st.slider(
        "Math Marks",
        0,
        100,
        70
    )

    new_science = st.slider(
        "Science Marks",
        0,
        100,
        70
    )

    new_english = st.slider(
        "English Marks",
        0,
        100,
        70
    )

    if st.button("✅ Add Student"):

        new_row = pd.DataFrame([{
            "Name": new_name,
            "Attendance": new_att,
            "Math": new_math,
            "Science": new_science,
            "English": new_english
        }])

        df = pd.concat(
            [df,new_row],
            ignore_index=True
        )

        df["Average"] = round(
            (
                df["Math"] +
                df["Science"] +
                df["English"]
            ) / 3,
            2
        )

        df.to_csv(
            "students.csv",
            index=False
        )

        st.success(
            "✅ Student Added Permanently"
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= FACE ATTENDANCE =================
with c2:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown(
        "## 📸 Face Recognition Attendance"
    )

    student_name = st.selectbox(
        "Select Student",
        df["Name"],
        key="attendance_student"
    )

    cam2 = st.camera_input(
        "Capture Student Photo"
    )

    if cam2:

        idx = df[
            df["Name"] == student_name
        ].index[0]

        df.loc[idx,"Attendance"] += 1

        df.to_csv(
            "students.csv",
            index=False
        )

        st.success(
            "✅ Face detected successfully!"
        )

        st.success(
            "📈 Attendance Increased"
        )

        st.success(
            "🎉 Student Present"
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= TABLE =================
with c3:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📋 Student Performance Table")

    st.dataframe(df, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= DELETE STUDENT =================
st.markdown("## ❌ Delete Student")

delete_student = st.selectbox(
    "Select Student To Delete",
    df["Name"]
)

if st.button("Delete Student"):

    df = df[
        df["Name"] != delete_student
    ]

    df.to_csv(
        "students.csv",
        index=False
    )

    st.success(
        "✅ Student Deleted Permanently"
    )

# ================= CHARTS =================
g1, g2 = st.columns(2)

# ===== ATTENDANCE GRAPH =====
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

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ===== PIE CHART =====
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

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= AI ANALYSIS =================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.markdown("## 🧠 AI Performance Analysis")

selected_student_ai = st.selectbox(
    "Select Student For AI Analysis",
    df["Name"]
)

student_row = df[
    df["Name"] == selected_student_ai
].iloc[0]

if student_row["Math"] < 50:
    st.error("❌ Math weak")

if student_row["Attendance"] < 75:
    st.warning("⚠ Needs practice")

if student_row["Average"] > 85:
    st.success("🏆 Excellent performance")

st.markdown("</div>", unsafe_allow_html=True)

# ================= PDF REPORTS =================
p1, p2 = st.columns(2)

# ===== ATTENDANCE PDF =====
with p1:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📄 Attendance PDF Report")

    if st.button("Generate Attendance PDF"):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=14
        )

        pdf.cell(
            200,
            10,
            txt="Attendance Report",
            ln=True
        )

        for i,row in df.iterrows():

            pdf.cell(
                200,
                10,
                txt=f"{row['Name']} - Attendance: {row['Attendance']}%",
                ln=True
            )

        pdf.output(
            "attendance_report.pdf"
        )

        with open(
            "attendance_report.pdf",
            "rb"
        ) as file:

            st.download_button(
                "Download Attendance PDF",
                file,
                file_name="attendance_report.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ===== SUBJECT PDF =====
with p2:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📘 Subject Wise Marks PDF")

    selected_student_pdf = st.selectbox(
        "Select Student",
        df["Name"]
    )

    if st.button("Generate Subject PDF"):

        row = df[
            df["Name"] == selected_student_pdf
        ].iloc[0]

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=14
        )

        pdf.cell(
            200,
            10,
            txt="Subject Wise Report",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Student: {row['Name']}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Math: {row['Math']}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Science: {row['Science']}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"English: {row['English']}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Average: {row['Average']}",
            ln=True
        )

        pdf.output(
            "subject_report.pdf"
        )

        with open(
            "subject_report.pdf",
            "rb"
        ) as file:

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
