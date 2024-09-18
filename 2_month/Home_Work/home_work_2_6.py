def bubble_sort(lists):
    for i in range(len(lists)):
        for j in range(len(lists) - 1):
            if lists[j+1] < lists[j]:
                lists[j], lists[j+1] = lists[j+1], lists[j]

    return lists
print(bubble_sort([5, 2, 8, 3, 9, 1, 7, 5, 15]), "\n")


def binario_search(num, lists):
    global num1
    ResultOK = False
    last = len(lists) - 1
    for first in range(last):
        middle = (first + last) // 2
        if lists[middle] == num:
            first = middle
            last = first
            ResultOK = True
            num1 = middle
        else:
            if num > lists[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if ResultOK:
        print("Элемент найден это:", num1)
    else:
        print("Элемент не найден")

print(binario_search(42, [1, 3, 6, 7, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69]))




