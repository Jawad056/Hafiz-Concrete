# app.py

import streamlit as st
from stack import Stack

# Descriptive slab sizes
slab_sizes = [
    "3'-0\" x 1'-6\"",
    "3'-0\" x 1'-0\"",
    "3'-6\" x 1'-6\"",
    "3'-6\" x 1'-0\"",
    "4'-0\" x 1'-6\"",
    "4'-0\" x 1'-0\"",
    "4'-6\" x 1'-6\"",
    "4'-6\" x 1'-0\"",
    "5'-0\" x 1'-6\"",
    "5'-6\" x 1'-6\"",
    "6'-0\" x 1'-6\"",
]

# Initialize the stack with persistent saving
if "stack" not in st.session_state:
    st.session_state.stack = Stack(sizes=slab_sizes)

stack = st.session_state.stack

st.title("🏗️ Slab Stock Management")

# --- Tabs
tab1, tab2, tab3 = st.tabs(["📦 Add Slabs", "🗑️ Remove Slabs", "📊 View Stock"])

# --- Add Slabs ---
with tab1:
    st.header("Add Slabs")
    size = st.selectbox("Select slab size", slab_sizes)
    qty = st.number_input("How many slabs to add?", min_value=1, step=1)
    if st.button("Add"):
        msg = stack.add_slab(size, qty)
        st.success(msg)

# --- Remove Slabs ---
with tab2:
    st.header("Remove Slabs")
    size = st.selectbox("Select slab size", slab_sizes, key="remove_size")
    qty = st.number_input("How many slabs to remove?", min_value=1, step=1, key="remove_qty")
    if st.button("Remove"):
        msg = stack.remove_slab(size, qty)
        if "Removed" in msg:
            st.success(msg)
        else:
            st.error(msg)

# -- View Stock --

with tab3:
    st.header("Current Stock")

    if st.button("🔄 Reset Stock"):
        msg = stack.reset_stock()
        st.success(msg)

    stock = stack.get_stock()

    # Convert stock to DataFrame and fix index to start from 1
    import pandas as pd
    df = pd.DataFrame({
        "Slab Size": list(stock.keys()),
        "Number of Slabs": list(stock.values())
    })

    df.index = df.index + 1  # Make index start from 1
    st.table(df)
