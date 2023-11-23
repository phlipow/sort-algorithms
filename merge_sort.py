def frag(arr):
    matrix = []
    for e in arr:
        matrix.append([e])

    return matrix


def inner_sort(arr1, arr2):
    i, j = 0, 0
    return_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            return_arr.append(arr1[i])
            i += 1
        else:
            return_arr.append(arr2[j])
            j += 1
    return_arr.extend(arr1[i:])
    return_arr.extend(arr2[j:])

    return return_arr

def merge_sort(arr):
    matrix = frag(arr)
    while len(matrix) > 1:
        temp_matrix = []
        i, j = 0, 1
        while j < len(matrix):
            temp_matrix.append(inner_sort(matrix[i], matrix[j]))
            i += 2
            j += 2
        if i == len(matrix) - 1:
            temp_matrix.append(matrix[i])
        matrix = temp_matrix
    
    return matrix[0]
