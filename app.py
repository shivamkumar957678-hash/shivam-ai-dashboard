import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Student System", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020024,#090979,#3a0ca3);
color:white;
}

h1,h2,h3,h4,h5,h6,label,p{
color:white !important;
}

.block-container{
padding-top:20px;
}

.card{
padding:20px;
border-radius:20px;
text-align:center;
color:white;
font-weight:bold;
box-shadow:0 0 15px rgba(255,255,255,0.2);
height:220px;
display:flex;
flex-direction:column;
justify-content:center;
}

.blue{
background:linear-gradient(135deg,#0077ff,#00bbff);
}

.green{
background:linear-gradient(135deg,#008000,#38b000);
}

.red{
background:linear-gradient(135deg,#d00000,#ff4d6d);
}

.purple{
background:linear-gradient(135deg,#7209b7,#f72585);
}

.login-box{
padding:20px;
border:2px solid #ff00ff;
border-radius:20px;
background:rgba(0,0,0,0.3);
box-shadow:0 0 20px #ff00ff;
}

</style>
""", unsafe_allow_html=True)

# ================= DATA =================
data = {
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45]
}

df = pd.DataFrame(data)
df["Average"] = round((df["Math"]+df["Science"]+df["English"])/3,2)

topper = df.sort_values("Average", ascending=False).iloc[0]["Name"]
weak = len(df[df["Average"] < 60])
poor_att = len(df[df["Attendance"] < 75])

# ================= TITLE =================
st.markdown("""
<h1 style='text-align:center;font-size:60px;color:#00e5ff;'>
🔐 AI STUDENT SYSTEM
</h1>
""", unsafe_allow_html=True)

# ================= TOP SECTION =================
left,right = st.columns([1,2])

# ===== LEFT =====
with left:

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.subheader("📷 Face Authentication")

    img = st.camera_input("Capture Face")

    st.subheader("🔑 Manual Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.success("Login Successful")
        else:
            st.error("Wrong Username or Password")

    # ===== FORGOT PASSWORD =====
    st.markdown("### Forgot Password")

    forgot_user = st.text_input("Enter Username")
    forgot_email = st.text_input("Enter Email")

    if st.button("Send OTP"):
        st.success("OTP Sent Successfully")
        st.info("Demo OTP: 1234")

    otp = st.text_input("Enter OTP")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Reset Password"):
        if otp == "1234":
            st.success("Password Reset Successful")
        else:
            st.error("Wrong OTP")

    st.markdown("</div>", unsafe_allow_html=True)

# ===== RIGHT =====
with right:

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class='card blue'>
        <h2>🎓 Total Students</h2>
        <h1>{len(df)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class='card green'>
        <h2>🏆 Topper</h2>
        <h1>{topper}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class='card red'>
        <h2>⚠ Weak Students</h2>
        <h1>{weak}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class='card purple'>
        <h2>📉 Poor Attendance</h2>
        <h1>{poor_att}</h1>
        </div>
        """, unsafe_allow_html=True)

    # ===== TABLE =====
    st.subheader("📋 Student Performance Table")
    st.dataframe(df, use_container_width=True)

    # ===== CHARTS =====
    ch1,ch2 = st.columns(2)

    with ch1:
        fig = px.bar(
            df,
            x="Name",
            y="Attendance",
            title="Attendance Graph"
        )
        st.plotly_chart(fig, use_container_width=True)

    with ch2:
        fig2 = px.pie(
            df,
            names="Name",
            values="Average",
            title="Student Marks Ratio"
        )
        st.plotly_chart(fig2, use_container_width=True)

# ================= AI ANALYSIS =================
st.subheader("🤖 AI Performance Analysis")

for i,row in df.iterrows():

    if row["Average"] >= 90:
        st.success(f"{row['Name']} : Excellent Performance")
    elif row["Average"] >= 60:
        st.info(f"{row['Name']} : Good Performance")
    else:
        st.warning(f"{row['Name']} : Needs Practice")

# ================= SEARCH =================
st.subheader("🔍 Search Student")

search = st.text_input("Enter Student Name")

if search:
    result = df[df["Name"].str.lower() == search.lower()]

    if not result.empty:
        st.dataframe(result, use_container_width=True)
    else:
        st.error("Student Not Found")

# ================= ADMIN DASHBOARD =================
st.subheader("🛠 Admin Dashboard")

a1,a2,a3,a4 = st.columns(4)

with a1:
    st.metric("Total Classes", "12")

with a2:
    st.metric("Fees Pending", "3")

with a3:
    st.metric("Avg Attendance", "77%")

with a4:
    st.metric("Monthly Analytics", "Good")

# ================= PDF SECTION =================
st.subheader("📄 PDF Reports")

p1,p2 = st.columns(2)

with p1:
    st.download_button(
        "Download Attendance Report",
        data=df.to_csv(index=False),
        file_name="attendance_report.csv",
        mime="text/csv"
    )

with p2:
    st.download_button(
        "Download Subject Report",
        data=df.to_csv(index=False),
        file_name="subject_report.csv",
        mime="text/csv"
    )

# ================= CHATBOT =================
st.subheader("🤖 AI Chatbot")

question = st.text_input("Ask Something")

if st.button("Ask AI"):
    st.success(f"AI Response: {question} analysis completed")

# ================= FOOTER =================
st.markdown("""
<hr>
<h4 style='text-align:center;color:white;'>
Made with ❤️ by Shivam Kumar
</h4>
""", unsafe_allow_html=True)
