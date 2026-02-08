import streamlit as st
import numpy as np

st.title("Matrix Operations Tool")

operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Transpose", "Determinant"]
)

st.subheader("Enter Matrix A")
rows_a = st.number_input("Rows (Matrix A)", min_value=1, step=1, key="rows_a")
cols_a = st.number_input("Columns (Matrix A)", min_value=1, step=1, key="cols_a")

matrix_a_input = st.text_area(
    "Enter Matrix A values (each row on new line, values separated by space)",
    key="matrix_a"
)

if operation in ["Addition", "Subtraction", "Multiplication"]:
    st.subheader("Enter Matrix B")
    rows_b = st.number_input("Rows (Matrix B)", min_value=1, step=1, key="rows_b")
    cols_b = st.number_input("Columns (Matrix B)", min_value=1, step=1, key="cols_b")

    matrix_b_input = st.text_area(
        "Enter Matrix B values (each row on new line, values separated by space)",
        key="matrix_b"
    )

if st.button("Calculate"):
    try:
        # Convert Matrix A
        matrix_a = []
        for line in matrix_a_input.strip().split("\n"):
            matrix_a.append([float(num) for num in line.split()])
        A = np.array(matrix_a)

        if operation in ["Addition", "Subtraction", "Multiplication"]:
            matrix_b = []
            for line in matrix_b_input.strip().split("\n"):
                matrix_b.append([float(num) for num in line.split()])
            B = np.array(matrix_b)

        # Perform operation
        if operation == "Addition":
            if A.shape != B.shape:
                st.error("Matrices must have same dimensions.")
            else:
                result = A + B
                st.success("Result:")
                st.write(result)

        elif operation == "Subtraction":
            if A.shape != B.shape:
                st.error("Matrices must have same dimensions.")
            else:
                result = A - B
                st.success("Result:")
                st.write(result)

        elif operation == "Multiplication":
            if A.shape[1] != B.shape[0]:
                st.error("Columns of A must equal rows of B.")
            else:
                result = np.dot(A, B)
                st.success("Result:")
                st.write(result)

        elif operation == "Transpose":
            result = A.T
            st.success("Result:")
            st.write(result)

        elif operation == "Determinant":
            if A.shape[0] != A.shape[1]:
                st.error("Matrix must be square.")
            else:
                result = np.linalg.det(A)
                st.success("Result:")
                st.write(result)

    except:
        st.error("Invalid input format. Please check matrix values.")