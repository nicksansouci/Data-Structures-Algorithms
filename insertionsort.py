def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

my_list = [45,3425,6547,13,4325,6874,4675,5679,8670,24254235,675980670]

print(insertion_sort(my_list))
