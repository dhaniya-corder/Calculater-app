import streamlit as st
import math

st.title("🧮 Advanced Calculator")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number (if needed):")

operation = st.selectbox("Choose operation", ["+", "-", "*", "/", "Power (x^y)", "Modulus (%)", "Square root (√)"])

if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "❌ Cannot divide by zero"
    elif operation == "Power (x^y)":
        result = num1 ** num2
    elif operation == "Modulus (%)":
        result = num1 % num2
    elif operation == "Square root (√)":
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            result = "❌ Cannot find square root of negative number"
    
    st.success(f"✅ Result: {result}")
