import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher
import yaml
from yaml.loader import SafeLoader



# # Pass the list of passwords directly to the 
# # Hasher constructor and generate the hashes
# passwords_to_hash = ['Apple2334']
# hashed_passwords = Hasher(passwords_to_hash).generate()

# print(hashed_passwords)

# st.write(**st.secrets["credentials"])

# @st.cache_data 
# def load_credentials():
#     with open('creds.yaml') as file:
#         config = yaml.load(file, Loader=SafeLoader)
#         st.session_state["config"] = config

# load_credentials()

# st.write(type(st.session_state["config"]['credentials']))

# authenticator = stauth.Authenticate(
#     st.session_state["config"]['credentials'],
#    st.session_state["config"]['cookie']['name'],
#     st.session_state["config"]['cookie']['key'],
#    st.session_state["config"]['cookie']['expiry_days']
# )

# cookie_name = st.secrets['cookie']['name']
# cookie_key = st.secrets['cookie']['key']
# exp_days =  st.secrets['cookie']['expiry_days']

credentials = st.secrets['credentials'].to_dict()
authenticator = stauth.Authenticate(
    credentials,
   st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
  st.secrets['cookie']['expiry_days']
)


authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
