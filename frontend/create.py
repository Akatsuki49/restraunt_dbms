import streamlit as st
import pandas as pd
from database import *


def display(table_name):
    result = show_table(table_name)
    if table_name == "waiter":
        df = pd.DataFrame(result, columns=["waiter id", "waiter name", "age"])
    elif table_name == "chef":
        df = pd.DataFrame(result, columns=["emp_id", "emp_name", "age", "head_id"])
        df['head_id'] = df['head_id'].astype('Int64')
    elif table_name == "food_items":
        df = pd.DataFrame(result, columns=["f_id", "f_name", "price", "category", "cuisine", "prep_time"])
        st.dataframe(df)
        return  # Skip the remaining code for "food_items" here
    elif table_name == "tables":
        df = pd.DataFrame(result, columns=["table_no", "capacity", "reserved", "w_id"])

    # Common code for all other tables
    st.dataframe(df)
    if table_name == "food_items":
        st.subheader('View ingredients')
        f_id = st.text_input('Enter food name')
        if st.button('Show ingredients'):
            res = showingredients(f_id)
            df1 = pd.DataFrame(res)
            st.dataframe(df1)