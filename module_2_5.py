number_of_strings = int(input("Enter amount of matrix strings: "))
number_of_columns = int(input("Enter amount of matrix columns: "))
element_of_matrix = input("Enter your matrix element: ")
def get_matrix(n,m,value):
    matrix = []
    n = number_of_strings
    m = number_of_columns
    value = element_of_matrix
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result = get_matrix(number_of_strings,number_of_columns,element_of_matrix)
print(result)