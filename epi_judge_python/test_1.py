row_dict = {}

def min_weight(triangle):
    min_weight_sum = 0
    for index, row in enumerate(triangle):
        row_dict_local = {}
        elements = []
        if index == 0:
            min_weight_sum += row[0]
            row_dict[index] = 0
        else:
            curr_j = row_dict[index - 1]
            if 0 <= curr_j-1:
                row_dict_local[row[curr_j-1]] = curr_j - 1
                elements.append(row[curr_j-1])
            if curr_j + 1 < len(row):
                row_dict_local[row[curr_j+1]] = curr_j + 1
                elements.append(row[curr_j+1])
            if curr_j == 0 or curr_j:
                row_dict_local[row[curr_j]] = curr_j
                elements.append(row[curr_j])
            small_elem = min(elements)
            min_weight_sum += small_elem
            row_dict[index] = row_dict_local[small_elem]
    return min_weight_sum

print(min_weight([[2], [3, 9], [1, 6, 7]]))
