import mysql.connector
import pandas as pd
import psycopg2
import streamlit as st
from sqlalchemy import create_engine

import PIL
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
import plotly.express as px



# connect to the database
import mysql.connector
#establishing the connection
conn = mysql.connector.connect(user='root', password='Sairam123', host='localhost', database="phonepe")

# create a cursor object
cursor = conn.cursor()



SELECT = st.selectbox(
    "Select an option",
    ["About", "Basic insights"],
    format_func=lambda x: "About" if x == 0 else "Basic insights",
    index=0)
# ---------------------Basic Insights -----------------#


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount",
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 Districts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]

    # 1

    select = st.selectbox("Select the option", options)
    if select == "Top 10 states based on year and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT States, Transaction_Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_tran GROUP BY States, Transaction_Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");

        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Transaction_Year', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            #st.bar_chart(data=df, x="Transaction_Amount", y="States")
            x = px.bar(df, x='States', y='Transaction_Amount')
            st.plotly_chart(x)
            # 2

    elif select == "List 10 states based on type and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT States, SUM(Transaction_Count) as Total FROM top_tran GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Total_Transaction'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            #st.bar_chart(data=df, x="Total_Transaction", y="States")
            y = px.bar(df, x='States', y='Total_Transaction')
            st.plotly_chart(y)
            # 3

    elif select == "Top 5 Transaction_Type based on Transaction_Amount":
        cursor.execute(
            "SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM agg_user GROUP BY Transaction_Type ORDER BY Amount DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_Type', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_Type based on Transaction_Amount")
            #st.bar_chart(data=df, x="Transaction_Type", y='Transaction_Amount')
            a=px.bar(df, x="Transaction_Type",y='Transaction_Amount')
            st.plotly_chart(a)
            #plt.figure(figsize=(15, 6))
            #plt.bar(df['Transaction_Type'], df['Transaction_Amount '])
            #plt.title("Top 5 Transaction_Type based on Transaction_Amount")
            #plt.show()

            # 4

    elif select == "Top 10 Registered-users based on States and District":
        cursor.execute("SELECT DISTINCT State, District, SUM(RegisteredUsers) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10;")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'District', 'RegisteredUsers'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District")
            #st.bar_chart(data=df, x="State", y="RegisteredUsers")
            b = px.bar(df, x='State', y='RegisteredUsers')
            st.plotly_chart(b)
            # 5

    elif select == "Top 10 Districts based on states and Count of transaction":
        cursor.execute(
            "SELECT DISTINCT States,District,SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'Transaction_Count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            #st.bar_chart(data=df, x="States", y="Transaction_Count")
            c = px.bar(df, x='State', y='Transaction_Count')
            st.plotly_chart(c)

            # 6

    elif select == "List 10 Districts based on states and amount of transaction":
        cursor.execute(
           "SELECT DISTINCT States,Transaction_year,SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY States, Transaction_year ORDER BY Amount ASC LIMIT 10");

        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Transaction_year', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            #st.bar_chart(data=df, x="States", y="Transaction_Amount")
            d = px.bar(df, x='States', y='Transaction_Amount')
            st.plotly_chart(d)

            # 7

    elif select == "List 10 Transaction_Count based on Districts and states":
        cursor.execute(
            "SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'Transaction_Count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 Transaction_Count based on Districts and states")
            #st.bar_chart(data=df, x="States", y="Transaction_Count")
            e = px.bar(df, x='States', y='Transaction_Count')
            st.plotly_chart(e)

            # 8

    elif select == "Top 10 RegisteredUsers based on states and District":
        cursor.execute(
            "SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'RegisteredUsers'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 RegisteredUsers based on states and District")
            #st.bar_chart(data=df, x="States", y="RegisteredUsers")
            f= px.bar(df, x='States', y='RegisteredUsers')
            st.plotly_chart(f)


cursor = conn.cursor()
# execute a SELECT statement
cursor.execute("SELECT * FROM agg_trans")

# fetch all rows
rows = cursor.fetchall()


# ----------------About-----------------------#
if SELECT == "About":
    col1, col2 = st.columns(2)
    with col1:

        # Display simple text
        st.text("NATHIYA PALANISAMY")

        # Display links
        st.markdown("GITHUB:(https://github.com/nathiyaapj)")
        st.markdown(
            "LINKEDIN:(www.linkedin.com/in/nathiya-palanisamy-610805285)")

    with col2:
        st.title("PHONE PE")
        st.write("---")
        st.subheader("The Indian digital payments story has truly captured the world's imagination."
                     " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                     " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                     "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
        st.write("---")
        st.title("THE BEAT OF PHONEPE")
        st.write("---")
        st.subheader("Phonepe became a leading digital payments company")
        with open("E:\\Backup\\New folder\\Documents\\PhonePe_Pulse_report.pdf", "rb") as f:
            data = f.read()
        st.download_button("DOWNLOAD REPORT", data, file_name="PhonePe_Pulse_report.pdf")



