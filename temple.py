# import streamlit as st
# import pandas as pd
# import numpy as np
# # import streamlit_authenticator as stauth
# # import yaml
# # from yaml.loader import SafeLoader
# from streamlit_phone_number import st_phone_number
# import pgeocode
# import phonenumbers

# st.set_page_config(layout="wide", initial_sidebar_state="expanded")
# st.markdown("<style>section[data-testid='stSidebar'] {width: 372px !important;}</style>", unsafe_allow_html=True) #setting width of sidebar

# st.sidebar.text_input('Input')

# st.markdown(f'<p style="background-color:#C6093B;color:#FFFFFF;font-size:40px;border-radius:2%;text-align: center; margin-top:-50px;margin-left:-75px;margin-right:-75px;"><i><b>Welcome to Aadinath Jain Mandir<b><i></p>', unsafe_allow_html=True)

# jinalay, about_jinalay, donation, payment, contact = st.tabs(["Jinalay", "About Jinalay", "Donation", "Payment", "Contact"])


# def pinCodeFinder():
#     area_col1, area_col2, area_col3, area_col4 = st.columns([0.20, 0.25, 0.25, 0.18])
#     pin_code = area_col1.text_input("PIN Code", placeholder="Enter Pin", max_chars=6)
#     pin_location_dict = pgeocode.Nominatim('in').query_postal_code(str(pin_code))
#     area_name = pin_location_dict['place_name'] if pin_location_dict['place_name'] == pin_location_dict['place_name'] else None
#     city_name = pin_location_dict['county_name'] if pin_location_dict['place_name'] == pin_location_dict['place_name'] else None
#     state_name = pin_location_dict['state_name'] if pin_location_dict['place_name'] == pin_location_dict['place_name'] else None
#     if pin_code:
#         if not state_name:
#             area_col1.error("Please enter valid Pin Code")
#         else:
#             city_name = area_col2.text_input("City", value=city_name, disabled=True)
#             state_name = area_col3.text_input("State", value=state_name, disabled=True)
#             area_col4.text_input("Country", value='India', disabled=True)
#             sub_col1, sub_col2 = st.columns([0.35, 0.65])
#             area_name = sub_col1.text_input("Locality", placeholder="Enter Locality", value = "Kharadi" if str(pin_code) == '411014' else area_name.split(',')[-1].strip())
#             landmark = sub_col2.text_input("Landmark", placeholder="Nearby Area")
#     else:
#         landmark = None
#     return pin_code, area_name, city_name, state_name, landmark
# with donation:
#     st.subheader("Please fill below details - ")
#     col1, col2 = st.columns([0.50, 0.50], gap='medium', border=True)
#     with col1:
#         st.markdown("***Donor Detail***")
#         sub_col1, sub_col2 = st.columns([0.50, 0.50])
#         sub_col1.text_input("First Name", placeholder='First Name', help='', key='first_name')
#         sub_col1.text_input("Address Detail", placeholder='Enter House No', help='', key='flat_no')
#         pin_code, area_name, city_name, state_name, landmark = pinCodeFinder()
#         sub_col2.text_input("Last Name", placeholder='Last Name', key='last_name')
#         sub_col2.text_input("Society Name", placeholder='Enter Society Name', help='', key='society_name')
#         mobile_number = st_phone_number("Contact Detail", placeholder="Enter Mobile Number", default_country="IN")
#         if mobile_number:
#             mobile_number = mobile_number['number']
#             if not phonenumbers.is_valid_number(phonenumbers.parse(str(mobile_number))):
#                 st.error("Please enter valid mobile no.")
#     with col2:
#         st.markdown("***Payment Detail***")
#         sub_col1, sub_col2 = st.columns([0.50, 0.50])
#         sub_col1.text_input("PAN No.", placeholder="Enter PAN No.", max_chars=10)
#         sub_col2.number_input("Amount", min_value=0, placeholder="Fill Amount", step=100)


    
# with jinalay:
#     st.image("Images/Jinalay1.jpg", use_container_width=False, width=1000)
# with contact:
#     st.header("Please contact our custome support for any issue")
#     st.markdown("***Email*** - singhaiparag320@gmail.com")
#     st.markdown("***Contact No.*** +91-9584455771")

# # with open('config.yaml') as file:
# #     config = yaml.load(file, Loader=SafeLoader)
# # authenticator = stauth.Authenticate(config['credentials'], config['cookie']['name'], config['cookie']['key'], config['cookie']['expiry_days'])
# # #### Login
# # authenticator.login(location='sidebar', captcha=False, key='login')
# # if st.session_state["authentication_status"] == False:
# #     st.sidebar.error('Username/password is incorrect')
# # elif st.session_state["authentication_status"] == None:
# #     st.sidebar.warning('Please enter your username and password')
# # elif st.session_state["authentication_status"]:
# #     authenticator.logout('Logout', 'sidebar')
# #     if st.session_state["username"] == 'admin':
# #         st.write(f'Welcome *{st.session_state["name"]}*')






from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(layout="wide")

st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard', 'Money', 'Economy'], 
                         iconName=['dashboard', 'money', 'economy'], default_choice=0)

if tabs =='Dashboard':
    st.title("Navigation Bar")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Money':
    st.title("Paper")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Economy':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))
    






