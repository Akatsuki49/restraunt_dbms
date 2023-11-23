import streamlit as st
import pandas as pd
import mysql.connector
from create import *

mydb = mysql.connector.connect(**st.secrets["mysql"])
c = mydb.cursor()


def show_table(table_name):
    c.execute('select * from ' + table_name)
    data = c.fetchall()
    return data


def HomeData():
    c.execute('show tables')
    data = c.fetchall()
    return data


# add values to the table
def addVal(o, v):
    q = 'INSERT INTO {}  VALUES {}'.format(o, v)
    c.execute(q)
    mydb.commit()
    st.success("value added successfully")


def displayorder(n):
    q = 'SELECT * FROM bill WHERE table_no = ' + str(n)
    c.execute(q)
    res = c.fetchall()
    df = pd.DataFrame(res, columns=['table_no', 'food_id', 'quality'])
    st.dataframe(df)


def editOrder(v):
    res = v.split(',')
    q = 'UPDATE bill set quantity =' + res[2] + ' where table_no = ' + res[0] + ' AND f_id =' + res[1]
    c.execute(q)
    mydb.commit()
    st.success('value successfully updated')


def runquery(a):
    c.execute(a)
    res = c.fetchall()
    df = pd.DataFrame(res)
    st.dataframe(df)
    st.success('query executed successfully')


# @st.cache(allow_output_mutation=True, suppress_st_warning=True, max_entries=1, ttl=1)
def placeorder(t, f_name, quantity):
    try:
        # Check if a record with the same f_name and table_no already exists
        c.execute(
            'SELECT COUNT(*) FROM bill WHERE f_id = (SELECT f_id FROM food_items WHERE f_name = %s) AND table_no = %s',
            (f_name, t))
        result = c.fetchone()

        if result[0] == 0:
            # The record does not exist, proceed with the INSERT
            c.execute(
                'INSERT INTO bill (table_no, f_id, quantity) VALUES (%s, (SELECT f_id FROM food_items WHERE f_name = %s), %s)',
                (t, f_name, quantity))
            mydb.commit()
            st.success('Placed order successfully')

            # Retrieve f_id for the food item
            f_id_query = 'SELECT f_id FROM food_items WHERE f_name = %s'
            c.execute(f_id_query, (f_name,))
            f_id_result = c.fetchone()

            if f_id_result:
                f_id = f_id_result[0]

                # Call the stored procedure to update inventory
                c.callproc('update_inventory_procedure', args=(f_id, quantity))

                mydb.commit()
                st.success('Updated ingredient quantities successfully')
            else:
                st.error('Food item not found.')
        else:
            # The record already exists, update the quantity
            c.execute(
                'UPDATE bill SET quantity = quantity + %s WHERE f_id = (SELECT f_id FROM food_items WHERE f_name = %s) AND table_no = %s',
                (quantity, f_name, t))
            mydb.commit()
            st.success('Updated order successfully')
    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")


def generatebill(n):
    # Fetching relevant data from the database
    cq = 'SELECT food_items.f_id, food_items.f_name, food_items.price, bill.quantity FROM bill JOIN food_items WHERE bill.f_id = food_items.f_id AND bill.table_no = ' + n
    c.execute(cq)
    nres = c.fetchall()

    # Creating a DataFrame for better visualization
    df1 = pd.DataFrame(nres, columns=['food_id', 'food_name', 'price', 'quantity_ordered'])
    st.dataframe(df1)

    # Calculating the total bill by multiplying price and quantity for each item
    total_bill_query = 'SELECT bill.table_no, SUM(food_items.price * bill.quantity) AS "total_bill" FROM bill JOIN food_items WHERE bill.table_no = ' + n + ' AND bill.f_id = food_items.f_id'
    c.execute(total_bill_query)
    total_bill_result = c.fetchall()

    # Creating a DataFrame for the total bill
    total_bill_df = pd.DataFrame(total_bill_result, columns=['table_no', 'total_amount'])
    st.dataframe(total_bill_df)


def showingredients(f_name):
    q = 'SELECT ingredients.ingr_id, ingredients.ingr_name FROM ingredients \
         JOIN recepie ON ingredients.ingr_id = recepie.ingr_id \
         JOIN food_items ON recepie.f_id = food_items.f_id \
         WHERE food_items.f_name = %s'
    c.execute(q, (f_name,))
    res = c.fetchall()
    return res


def showview():
    # q = 'CREATE VIEW IF NOT EXISTS all_employees (emp_id, emp_name) AS SELECT chef.emp_id, chef.emp_name from chef UNION SELECT waiter.w_id, waiter.w_name from waiter'
    q = 'CREATE OR REPLACE VIEW all_employees AS SELECT chef.emp_id, chef.emp_name FROM chef UNION SELECT waiter.w_id, waiter.w_name FROM waiter;'
    c.execute(q)
    c.execute('SELECT * from all_employees')
    res = c.fetchall()
    df = pd.DataFrame(res)
    st.dataframe(df)


def removechef(i):
    q = 'DELETE FROM chef where emp_id = ' + i
    c.execute(q)
    mydb.commit()
    st.success('Employee removed')


def removewaiter(i):
    q = 'DELETE FROM waiter where w_id =' + i
    c.execute(q)
    mydb.commit()
    st.success('Employee removed')