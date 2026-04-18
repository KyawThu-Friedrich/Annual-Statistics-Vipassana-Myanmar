import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("AnnualReport2024.csv")

st.title("Vipassana Myanmar 2024: Annual Report Dashboard")

# Summary stats
st.header("Summary Statistics")
total_courses = df['Courses'].fillna(0).astype(int).sum()
total_students = df['StudentTotal'].fillna(0).astype(int).sum()
total_centers = df['Center'].nunique()
st.metric("Total Courses", total_courses)
st.metric("Total Students", total_students)
st.metric("Centers", total_centers)

# Courses and Students by Center
st.header("Courses & Students by Center")
center_stats = df.groupby('Center').agg(
    Courses=('Courses', 'sum'),
    Students=('StudentTotal', 'sum')
).reset_index()
fig1 = px.bar(center_stats, x='Center', y=['Courses', 'Students'],
              barmode='group', title="Courses & Students per Center")
st.plotly_chart(fig1, use_container_width=True)

# Distribution by Course Type
st.header("Distribution by Course Type")
course_stats = df.groupby('CourseType').agg(
    Courses=('Courses', 'sum'),
    Students=('StudentTotal', 'sum')
).reset_index()
fig2 = px.pie(course_stats, values='Students', names='CourseType',
              title="Student Participation by Course Type")
st.plotly_chart(fig2, use_container_width=True)

# Gender Distribution
st.header("Gender Distribution")
gender_totals = {
    "New Male": df['NewMale'].fillna(0).astype(int).sum(),
    "New Female": df['NewFemale'].fillna(0).astype(int).sum(),
    "Old Male": df['OldMale'].fillna(0).astype(int).sum(),
    "Old Female": df['OldFemale'].fillna(0).astype(int).sum(),
}
fig3 = px.bar(
    x=list(gender_totals.keys()),
    y=list(gender_totals.values()),
    labels={'x':'Category', 'y':'Number'},
    title="Gender & New/Old Distribution"
)
st.plotly_chart(fig3, use_container_width=True)

# Raw Data Display
st.header("Raw Data")
st.dataframe(df)