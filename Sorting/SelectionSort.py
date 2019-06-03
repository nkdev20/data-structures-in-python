def sort(list):
    for index in range(len(list)):
        min  = index
        for index1 in range(index+1, len(list)):
            if list[index1] < list[min]:
                min  = index1
        temp = list[index]
        list[index] = list[min]
        list[min] = temp

    return list

a = [4,2,5,1,6,3]
b = sort(a)
print(b)

        