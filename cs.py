import streamlit as st
import re
import string
import secrets

def password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*()_+-=]", password):
        score += 1
    if re.search("\s", password):
        score -= 1
        
    return score

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def main():
    st.set_page_config(page_title="Password Strength Checker and Generator", page_icon=":lock:", layout="wide")
    st.title("Password Strength Checker and Generator")
    st.write("Use this app to check the strength of your password and generate a strong one if needed.")
    
    # Password strength checker
    st.header("Password Strength Checker")
    password = st.text_input("Enter your password:", type="password", key="password_input")
    if password:
        strength = password_strength(password)
        st.write(f"Password Strength Score: {strength}")
        with open("passwords.txt", "a") as file:
            file.write(f"Password: {password}, Score: {strength}\n")
            
        if strength < 4:
            st.warning("Your password is weak, consider changing it.")
        else:
            st.success("Your password is strong!")
        

    
    # Password generator
    st.header("Password Generator")
    password_length = st.slider("Select password length", 8, 64, 12, key="password_length")
    generated_password = generate_password(password_length)
    st.write(f"Generated Password: {generated_password}")
    st.write("Use this password at your own risk!")
    
if __name__ == "__main__":
    main()
