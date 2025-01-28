def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst


numbers = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(numbers)
print(result)  
