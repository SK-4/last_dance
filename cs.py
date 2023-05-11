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
    st.title("Password Strength Checker and Generator")
    password = st.text_input("Enter your password:", type="password")
    if password:
        strength = password_strength(password)
        st.write(f"Password Strength Score: {strength}")
        if strength < 4:
            st.warning("Your password is weak, consider changing it.")
        else:
            st.success("Your password is strong!")
        
        with open("passwords.txt", "a") as file:
            file.write(f"Password: {password}, Score: {strength}\n")
    
    st.subheader("Generate Password")
    password_length = st.slider("Select password length", 8, 64, 12)
    generated_password = generate_password(password_length)
    st.write(f"Generated Password: {generated_password}")
    
if __name__ == "__main__":
    main()
