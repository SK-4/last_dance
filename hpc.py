import time
import numpy as np
import multiprocessing
import streamlit as st

def serial_multiply(mat1, mat2):
    # Multiply two matrices in serial
    return np.dot(mat1, mat2)

def multiply_partial(args):
    start, end, mat1, mat2 = args
    result = np.zeros((len(mat1), len(mat2[0])))
    for j in range(start, end):
        result[j] = np.dot(mat1[j], mat2)
    return result

def parallel_multiply(mat1, mat2):
    # Multiply two matrices in parallel
    num_processes = multiprocessing.cpu_count()
    rows_per_process = len(mat1) // num_processes

    pool = multiprocessing.Pool(processes=num_processes)
    args_list = [(i * rows_per_process, (i+1) * rows_per_process, mat1, mat2) for i in range(num_processes)]
    results = pool.map(multiply_partial, args_list)
    pool.close()
    pool.join()

    return np.sum(results, axis=0)

def main():
    st.set_page_config(page_title="Matrix Multiplication", page_icon=":lock:", layout="wide")
    st.title("Matrix Multiplication")
    st.write("Use this app to Multiply the matrix and check their speed.")

    # Define matrix sizes
    n = st.number_input("Enter the number of rows for matrix A", value=2000)
    m = st.number_input("Enter the number of columns for matrix A", value=3000)
    p = st.number_input("Enter the number of columns for matrix B", value=4000)

    # Generate random matrices
    A = np.random.rand(n, m)
    B = np.random.rand(m, p)

    # Multiply matrices in serial
    start = time.time()
    C_serial = serial_multiply(A, B)
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
    main()
