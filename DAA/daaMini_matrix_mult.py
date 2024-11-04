import time
import threading
import random

# Standard matrix multiplication
def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Function to multiply one row of A by matrix B
def multiply_row(A, B, result, row):
    for j in range(len(B[0])):
        result[row][j] = sum(A[row][k] * B[k][j] for k in range(len(B)))

# Multithreaded matrix multiplication using one thread per row
def matrix_multiply_threaded_row(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    threads = []
    
    for i in range(len(A)):
        thread = threading.Thread(target=multiply_row, args=(A, B, result, i))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return result

# Function to multiply one cell in the result matrix
def multiply_cell(A, B, result, i, j):
    result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

# Multithreaded matrix multiplication using one thread per cell
def matrix_multiply_threaded_cell(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    threads = []
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            thread = threading.Thread(target=multiply_cell, args=(A, B, result, i, j))
            threads.append(thread)
            thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return result

# Helper function to generate random matrices
def generate_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# Helper function to print matrices
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Performance Comparison
if __name__ == "__main__":
    # Matrix size (change for performance testing)
    N = 4  # Adjust N for larger matrices
    A = generate_matrix(N, N)
    B = generate_matrix(N, N)

    print("Matrix A:")
    print_matrix(A)
    print("\nMatrix B:")
    print_matrix(B)

    # Regular matrix multiplication
    start_time = time.time()
    result_standard = matrix_multiply(A, B)
    standard_time = time.time() - start_time
    print("\nResult of Standard Matrix Multiplication:")
    print_matrix(result_standard)
    print(f"Standard matrix multiplication took {standard_time:.4f} seconds\n")

    # Multithreaded matrix multiplication (one thread per row)
    start_time = time.time()
    result_threaded_row = matrix_multiply_threaded_row(A, B)
    row_thread_time = time.time() - start_time
    print("\nResult of Multithreaded (Per Row) Matrix Multiplication:")
    print_matrix(result_threaded_row)
    print(f"Multithreaded (per row) matrix multiplication took {row_thread_time:.4f} seconds\n")

    # Multithreaded matrix multiplication (one thread per cell)
    start_time = time.time()
    result_threaded_cell = matrix_multiply_threaded_cell(A, B)
    cell_thread_time = time.time() - start_time
    print("\nResult of Multithreaded (Per Cell) Matrix Multiplication:")
    print_matrix(result_threaded_cell)
    print(f"Multithreaded (per cell) matrix multiplication took {cell_thread_time:.4f} seconds")
