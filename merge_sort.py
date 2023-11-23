def ms_split(arr):
    matrix = []
    for e in arr:
        matrix.append([e])

    return matrix


def ms_sort(arr1, arr2):
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

def ms_merge_sort(arr):
    matrix = ms_split(arr)
    i, j = 0, 1
    return_arr = []
    while j < len(matrix):
        return_arr.append(ms_sort(matrix[i], matrix[j]))
    
    return return_arr

print(ms_merge_sort([8, 7, 6, 5, 4, 3, 2, 1]))