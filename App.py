import streamlit as st
import math

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Dark Calculator", page_icon="🧮", layout="centered")

# ---- DARK MODE STYLE ----
dark_style = """
<style>
body {
    background-color: #0f1117;
    color: #e1e1e1;
}
[data-testid="stAppViewContainer"] {
    background-color: #1e1e1e;
    color: white;
}
button[kind="secondary"] {
    background-color: #333 !important;
    color: white !important;
}
</style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

# ---- TITLE ----
st.markdown("<h1 style='color:#00ffcc;'>🧮 Dark Mode Calculator</h1>", unsafe_allow_html=True)

# ---- HISTORY ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- INPUT ----
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number (if needed):")

st.markdown("### Select Operation:")

# ---- BUTTON DESIGN ----
col1, col2, col3, col4 = st.columns(4)
col5, col6, col7 = st.columns(3)

operation = None

if col1.button("+"):
    operation = "+"
elif col2.button("-"):
    operation = "-"
elif col3.button("*"):
    operation = "*"
elif col4.button("/"):
    operation = "/"
elif col5.button("Power xʸ"):
    operation = "power"
elif col6.button("Modulus %"):
    operation = "mod"
elif col7.button("√ Square Root"):
    operation = "sqrt"

# ---- CALCULATE ----
if operation:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "❌ Cannot divide by 0"
    elif operation == "power":
        result = num1 ** num2
    elif operation == "mod":
        result = num1 % num2
    elif operation == "sqrt":
        result = math.sqrt(num1) if num1 >= 0 else "❌ Cannot sqrt negative"

    # Save to history
    calc_str = f"{num1} {operation} {num2 if operation != 'sqrt' else ''} = {result}"
    st.session_state.history.append(calc_str)
    st.success(f"✅ Result: {result}")

# ---- HISTORY DISPLAY ----
if st.session_state.history:
    st.markdown("### 📝 History")
    for item in st.session_state.history[::-1]:  # reverse order
        st.write(item)
