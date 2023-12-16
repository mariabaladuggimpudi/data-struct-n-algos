from typing import List

def even_odd_order(A) -> List[int]:


    write_index, start, end = 0, 0, len(A) - 1
    while start < end:
        if A[start] % 2 == 0:
            start += 1
        else:
            A[start], A[end] = A[end], A[start]
            end -= 1

    return A

print(even_odd_order([1,2,3,4,5,6,7]))