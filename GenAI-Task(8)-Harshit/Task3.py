# 3. Product Form
import streamlit as st

st.title("Product Form")
st.write("Enter product details using the sidebar.")


st.sidebar.header("Add New Product")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Select Category",
    ["Electronics", "Clothing", "Food", "Books", "Furniture"]
)

price = st.sidebar.number_input(
    "Enter Price (₹)",
    min_value=0.0,
    value=100.0,
    step=10.0
)

# Add Product button
if st.sidebar.button("Add Product"):

    if product_name.strip() == "":
        st.warning("Please enter a product name.")

    else:
        st.success("Product added successfully!")

        st.subheader("Product Details")

        st.write("**Product Name:**", product_name)
        st.write("**Category:**", category)
        st.write("**Price:** ₹", price)

        # Display details in table
        product = [
            ["Product Name", product_name],
            ["Category", category],
            ["Price", f"₹{price:.2f}"]
        ]

        st.table(product)
