# ----------^^**SearchingAndSorting Algorithm Using Python**^^-------------!

# 1.Python Program for Binary Search (Recursive and Iterative)

pos = -1

def Binary_Search(L_list, num):

    l = 0
    u = len(L_list) - 1

    while l <= u:
        mid = (l + u) // 2
        if L_list[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if L_list[mid] < num:
                l = mid + 1
            else:
                u = mid - 1
    return False
l_list = [2, 3, 8, 7, 1, 4, 5]
l_list = sorted(l_list)
print("Sorted List: ", l_list)
num = int(input("Enter the number: "))

if Binary_Search(l_list, num):
    print("Number Found At Position : ", pos + 1)
else:
    print("Number Not Found")

#****************************************************

# 2.Python Program for Linear Search

pos = -1

def Linear_Search(l_list, num):
    count = 0

    while count < len(l_list):
        if l_list[count] == num:
            globals()['pos'] = count
            return True
        count += 1
    return False

l_list = [2, 5, 8, 0, 7, 3]

num = int(input("Enter the searching number: "))

if Linear_Search(l_list, num):
    print("Number found at Position:", pos + 1)
else:
    print("Number Not Found")

#***********************************************************

# 3.Python Program for Insertion Sort

def Insertion_Sort(list):
    for i in range(1, len(list)):
        num = list[i]
        j = i - 1
        while j >= 0 and num < list[j]:
            list[j + 1] = list[j]
            j -= 1
            list[j + 1] = num

ele_list = [23, 33, 83, 53, 13, 3, 93, 43]
print("Elements Before Appling Insertion Sort:", ele_list)
Insertion_Sort(ele_list)

print("Elements After Insertion Sort :", ele_list)

#***********************************************************

# *4.Python Program for Recursive Insertion Sort

def Insertion_Sort_Recursive(list, list_len):
    if list_len <= 1:      # when there only 1 element to sort
        return
    Insertion_Sort_Recursive(list, list_len - 1 )    # Recursive call to the function for sorting inner elements
    last = list[list_len - 1]
    j = list_len - 2

    while j >= 0 and list[j] > last:        # Insertion over each elements in the sorted sublist to insert current element
        list[j + 1] = list[j]
        j =j - 1                # shifting the elements to insert current element at right position
    list[j + 1] = last         # Inserting current elements at the appropriate position


ele_list = [23, 33, 83, 53, 13, 3, 93, 43]
ele_len = len(ele_list)
print("Elements Before Appling Insertion Sort:", ele_list)
Insertion_Sort_Recursive(ele_list, ele_len)

print("Elements After Insertion Sort :", ele_list)

#***************************************************************

# 5.Python Program for Selection Sort

def selection_sort(l_list, size):
    for i in range(size):
        minimum = i

        for j in range(i + 1, size):
            if l_list[minimum] > l_list[j]:
                minimum = j
        l_list[i], l_list[minimum] = l_list[minimum], l_list[i]

l_list = [1, 22, 13, 50, 40,20]
size = len(l_list)
selection_sort(l_list, size)
print('List after sorted:', l_list)

#**********************************************************

# 6.Python Program for Bubble Sort

def Bubble_Sort(l_list, size):
    for i in range(size - 1):
        for j in range(size - i - 1):
            if l_list[j] > l_list[j + 1]:
                temp = l_list[j]
                l_list[j] = l_list[j + 1]
                l_list[j + 1] = temp

l_list = [10, 50, 20, 80, 30, 40]
size = len(l_list)
Bubble_Sort(l_list, size)
print("Sorted List:", l_list)