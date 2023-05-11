import time
import numpy as np
import multiprocessing
import streamlit as st

def parallel_multiply(mat1, mat2):
    # Multiply two matrices in parallel using numpy's parallelization
    return np.matmul(mat1, mat2)

def main():
    # Define matrix sizes
    n = 5000 
    m = 3000 
    p = 4000

    # Generate random matrices
    A = np.random.rand(n, m)
    B = np.random.rand(m, p)

    # Multiply matrices in serial
    start = time.time()
    C_serial = np.matmul(A, B)
    end = time.time()
    st.write("Serial multiplication took {:.4f} seconds".format(end - start))

    # Multiply matrices in parallel
    start = time.time()
    C_parallel = parallel_multiply(A, B)
    end = time.time()
    st.write("Parallel multiplication took {:.4f} seconds".format(end - start))

    # Check if the results match
    if np.allclose(C_serial, C_parallel):
        st.success("The results of serial and parallel multiplication are the same")
    else:
        st.failure("The results of serial and parallel multiplication are different")

if __name__ == '__main__':
    st.set_page_config(page_title="Matrix Multiplication", page_icon=":memo:")
    st.title("Matrix Multiplication with NumPy")
    st.write("This app multiplies two matrices in serial and parallel using NumPy.")
    main()