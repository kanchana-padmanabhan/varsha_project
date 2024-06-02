import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = st.session_state["config"]["mongo"]["uri"]
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


st.write("# In-take form for students 👋")

if "authentication_status" not in st.session_state:
    st.write("Please go to the main page and get authenticated")
else:
    if st.session_state["authentication_status"]:
        st.write("You are authenticated")

        with st.form("my_form"):
            st.write("Inside the form")
            name = st.text_input("Name")
            email = st.text_input("Email")
            number = st.text_input("Phone")
            method = st.radio("Preferred contact method", ["phone", "email"])

            submitted = st.form_submit_button("Submit")
            if submitted:
                #st.write("name", name, "email", email, "phone", number, "method", method)
                mydb = client["mudita_info"]
                mycol = mydb["enquiry"]
                mydict = { "name": name, "email": email, "phone": number, "method": method}
                x = mycol.insert_one(mydict)
                print(x)
    else:
        st.write("Please go to the main page and get authenticated")

    #authenticator.logout()


