def search(list_num, pos, first, last):

    if first < last:
        mid = last + (first - last) // 2
        if list_num[mid] == pos:
            return mid
        elif list_num[mid] > pos:
            if pos < list_num[mid]:
                return search(list_num, pos, first, mid - 1)
            else:
                return search(list_num, pos, mid + 1, last)
    else:
        return -1


list_num = [3, 5, 8, 22, 54, 65, 70]
result = search(list_num, 8, 0, len(list_num) - 1)

if result != -1:
    print(f'Element is found')
else:
    print('Not found')


def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list1 = [2, 45, 33, 0, 666, 34, 7]
print("The unsorted list is: ", list1)

print("The sorted list is: ", bubble_sort(list1))

