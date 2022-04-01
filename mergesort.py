def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list) / 2)
    left = my_list[:mid]
    right = my_list[mid:]
    #Merge function only works on sorted lists so we need to break left and right in half again with merge sort function
    #Recursivley call merge sort to break in half, and return lists.
    return merge(merge_sort(left), merge_sort(right))


def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

list1 = [1, 3, 7, 8]
list2 = [4, 6, 9, 12, 1, 100, 500, 3425]

print(merge_sort(list1))
print(merge_sort(list2))
