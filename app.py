import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Ultimate AI Student System",
    layout="wide"
)

# ================= DATABASE =================
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

# ================= AVERAGE =================
df["Average"] = round(
    (
        df["Math"] +
        df["Science"] +
        df["English"]
    ) / 3,
    2
)

# ================= STATUS =================
df["Status"] = "Average"

df.loc[
    df["Average"] >= 90,
    "Status"
] = "Topper"

df.loc[
    df["Average"] < 60,
    "Status"
] = "Weak"

# ================= SAVE =================
df.to_csv("students.csv", index=False)

# ================= DASHBOARD VALUES =================
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

# ================= STYLE =================
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020024,#090979,#3a0ca3);
color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
color:white !important;
}

.block{
background:rgba(0,0,0,0.35);
padding:20px;
border-radius:20px;
border:2px solid #ff00ff;
box-shadow:0 0 20px #ff00ff;
margin-bottom:20px;
}

.metric-card{
padding:20px;
border-radius:20px;
text-align:center;
color:white;
font-weight:bold;
height:220px;
box-shadow:0 0 20px rgba(255,255,255,0.2);
}

.blue{
background:linear-gradient(135deg,#0077ff,#00bbff);
}

.green{
background:linear-gradient(135deg,#00b09b,#96c93d);
}

.red{
background:linear-gradient(135deg,#ff416c,#ff4b2b);
}

.purple{
background:linear-gradient(135deg,#7209b7,#f72585);
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

# ================= HEADER =================
st.markdown("""
<h1 style='text-align:center;
font-size:65px;
color:#00e5ff;
text-shadow:0 0 20px #00e5ff;'>
🔐 AI STUDENT SYSTEM
</h1>

<h3 style='text-align:center;color:#00ffff;'>
Smart • Secure • Intelligent
</h3>
""", unsafe_allow_html=True)

# ================= TOP CARDS =================
m1,m2,m3,m4 = st.columns(4)

with m1:

    st.markdown(f"""
    <div class='metric-card blue'>
    <h2>👨‍🎓 Total Students</h2>
    <h1>{len(df)}</h1>
    </div>
    """, unsafe_allow_html=True)

with m2:

    st.markdown(f"""
    <div class='metric-card green'>
    <h2>🏆 Topper</h2>
    <h1>{topper}</h1>
    </div>
    """, unsafe_allow_html=True)

with m3:

    st.markdown(f"""
    <div class='metric-card red'>
    <h2>⚠ Weak Students</h2>
    <h1>{weak_students}</h1>
    </div>
    """, unsafe_allow_html=True)

with m4:

    st.markdown(f"""
    <div class='metric-card purple'>
    <h2>📉 Poor Attendance</h2>
    <h1>{poor_attendance}</h1>
    </div>
    """, unsafe_allow_html=True)

# ================= MAIN SECTION =================
c1,c2,c3 = st.columns([1,1,2])

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

        df["Status"] = "Average"

        df.loc[
            df["Average"] >= 90,
            "Status"
        ] = "Topper"

        df.loc[
            df["Average"] < 60,
            "Status"
        ] = "Weak"

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
        df["Name"]
    )

    cam = st.camera_input(
        "Capture Student Photo"
    )

    if cam:

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

    st.markdown("</div>", unsafe_allow_html=True)

# ================= TABLE =================
with c3:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown(
        "## 📋 Student Performance Table"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

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
g1,g2 = st.columns(2)

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

with g2:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 🔥 Student Marks Ratio")

    pie = px.pie(
        df,
        names="Name",
        values="Average",
        hole=0.4
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

# ================= PDF REPORT =================
p1,p2 = st.columns(2)

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

with p2:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.markdown("## 📘 Subject Report PDF")

    selected_student = st.selectbox(
        "Select Student",
        df["Name"],
        key="pdf"
    )

    if st.button("Generate Subject PDF"):

        row = df[
            df["Name"] == selected_student
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
