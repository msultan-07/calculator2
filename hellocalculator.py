import streamlit as st

st.title("Calculator")

# Define a function for basic arithmetic operations
def perform_calculation(a, b, operation):
    if operation == 'Add':
        return a + b
    elif operation == 'Subtract':
        return a - b
    elif operation == 'Multiply':
        return a * b
    elif operation == 'Divide':
        if b != 0:
            return a / b
        else:
            return 'Error: Division by zero'
    else:
        return 'Invalid Operation'

# Streamlit app layout
st.title('Simple Mathematics Calculator')

# Input fields
num1 = st.number_input('Enter first number', value=0)
num2 = st.number_input('Enter second number', value=0)

# Selectbox for operations
operation = st.selectbox('Select an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Button to perform the calculation
if st.button('Calculate'):
    result = perform_calculation(num1, num2, operation)
    st.write(f'The result of {operation} {num1} and {num2} is: {result}')







