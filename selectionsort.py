def selection_sort(my_list):
    length = len(my_list) - 1
    for i in range(length):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

my_list = [3,54,32,5436,12,1234,3265]
print(selection_sort(my_list))   