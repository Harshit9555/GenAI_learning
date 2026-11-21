# 2. Price Calculator
import streamlit as st 

price = st.number_input("Enter original price",min_value=0.0,value=1000.0,step=100.0)

discount = st.slider("Select Discount (%)",min_value=0,max_value = 50,value = 10)

if st.button("Calculate Final Price"):
    
    discount_amount = price * discount/100
    final_price = price - discount_amount
    st.success(f"Final Price: {final_price:.2f}")
    
    st.write(f"Original Price: {price:.2f}")
    st.write(f"Discount: {discount}%")
    st.write(f"You save: {discount_amount:.2f}")
