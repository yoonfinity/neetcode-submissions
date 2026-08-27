from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_elem = 0 
    max_arr = [] 

    for sublist in nested_arr:
        for elem in sublist: 
            if elem > max_elem: 
                max_elem = elem
        max_arr.append(max_elem)
        max_elem = 0
    
    return max_arr



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
