import streamlit as st

name = st.text_input("Enter your name :")
F_name = st.text_input("Enter first name :")
Txt_mess = st.text_input("Enter the Message :")
class_Data = st.selectbox("Enter your class :",(1,2,3,4,5,6,7,8,9,10))
button = st.button("SUBMIT")
if button:
    st.markdown(f"""
                Name : {name} \
                Father_name : {F_name} 
                Text_Mess : {Txt_mess}
                classdata : {class_Data}""")