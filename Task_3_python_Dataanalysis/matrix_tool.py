import numpy as np


def display_menu():
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")


def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    for i in range(rows):
        while True:
            row = input(f"Enter values for row {i+1} separated by space: ").split()

            if len(row) != cols:
                print("Incorrect number of values. Try again.")
                continue

            matrix.append([float(num) for num in row])
            break

    return np.array(matrix)


def add_matrices():
    print("\nMatrix A")
    A = get_matrix()
    print("\nMatrix B")
    B = get_matrix()

    if A.shape != B.shape:
        print("Error: Matrices must have the same dimensions for addition.")
        return

    result = A + B
    print("\nResult:")
    print(result)


def subtract_matrices():
    print("\nMatrix A")
    A = get_matrix()
    print("\nMatrix B")
    B = get_matrix()

    if A.shape != B.shape:
        print("Error: Matrices must have the same dimensions for subtraction.")
        return

    result = A - B
    print("\nResult:")
    print(result)


def multiply_matrices():
    print("\nMatrix A")
    A = get_matrix()
    print("\nMatrix B")
    B = get_matrix()

    if A.shape[1] != B.shape[0]:
        print("Error: Columns of Matrix A must equal rows of Matrix B.")
        return

    result = np.dot(A, B)
    print("\nResult:")
    print(result)


def transpose_matrix():
    print("\nMatrix")
    A = get_matrix()

    result = A.T
    print("\nTranspose:")
    print(result)


def determinant_matrix():
    print("\nMatrix")
    A = get_matrix()

    if A.shape[0] != A.shape[1]:
        print("Error: Determinant can only be calculated for square matrices.")
        return

    result = np.linalg.det(A)
    print("\nDeterminant:")
    print(result)


def main():
    print("===== MATRIX OPERATIONS TOOL =====")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            subtract_matrices()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            determinant_matrix()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
    