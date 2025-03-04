#02 project strength Meter..
#build a password strength meter in python 

import re
import streamlit as st

# 🛠 Page design
st.set_page_config(page_title="Password Strength Meter By Sheeraz Ali", 
                   page_icon="🔑", layout="centered")

# 🎨 Custom CSS for styling and alignment
st.markdown("""
<style>
    .main {text-align: center;} /* Center align text */
    .stTextInput {width:60% !important; margin: auto;} /* Center password input */
    .stButton {text-align: center;} /* Center button */
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px; border-radius: 5px;}
    .stButton button:hover {background-color: purple; color: white;}
</style>
""", unsafe_allow_html=True)

# 📌 Page title and description
st.title("🔐 Password Strength Generator")  
st.write("Enter your password below to check its security level. 🔎")  

# 🔍 Function to check password strength
def check_password_strength(password):
    score = 0  # Initial password strength score
    feedback = []  # List to store feedback messages

    # ✅ Check password length
    if len(password) >= 8:
        score += 1  # Increase score if password is at least 8 characters
    else:
        feedback.append("❌ Password should be *at least 8 characters long*.")  

    # ✅ Check uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):  # 🔴 Fixed Syntax Error (removed :)
        score += 1  
    else:
        feedback.append("❌ Password should include *both uppercase and lowercase letters*.")  

    # ✅ Check if password contains a number
    if re.search(r"\d", password):
        score += 1  
    else:
        feedback.append("❌ Password should include *at least one number (0-9)*.")  

    # ✅ Check if password contains a special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1  
    else:
        feedback.append("❌ Include *at least one special character (!@#$%^&).")  

    # 🔽 Display password strength message
    if score == 4:
        st.success("✅ *Strong Password* - Your password is secure.")  
    elif score == 3:
        st.info("⚠ *Moderate Password* - Consider improving security by adding more features.")  
    else:
        st.error("❌ *Weak Password* - Follow the suggestions below to strengthen it.")  

    # 📝 Display feedback suggestions
    if feedback:
        with st.expander("🔍 *Improve Your Password*"):
            for item in feedback:
                st.write(item)  

# 🔑 Password Input Field
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔒")  

# ▶ Button to check password strength
if st.button("Check Strength"):
    if password:  
        check_password_strength(password)  # Call function to check strength
    else:
        st.warning("⚠ Please enter a password first!")  # Show warning if input is empty
  

 

