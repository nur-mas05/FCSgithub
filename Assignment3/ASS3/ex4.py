def insert_into_sorted_list(sorted_list, value):
    # Find the correct position to insert the value
    for i in range(len(sorted_list)):
        if sorted_list[i] > value:
            sorted_list.insert(i, value)
            return
    # If the value is greater than all elements, append it to the end
    sorted_list.append(value)


list1 = [1, 34, 56, 78, 89]
val = 77

insert_into_sorted_list(list1, val)
print(list1)  # Output: [1, 34, 56, 77, 78, 89]
