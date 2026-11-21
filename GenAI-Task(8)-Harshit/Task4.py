# 4. Mini Dashboard

import streamlit as st

st.title("Simple Sales Dashboard")
st.write("View monthly sales performance.")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}


selected_month = st.selectbox(
    "Select Month",
    months
)

st.subheader("Monthly Sales")

st.metric(
    label=selected_month + " Sales",
    value=f"₹{sales[selected_month]}"
)

# Display sales chart
st.subheader("Sales Comparison")

st.bar_chart(list(sales.values()))
