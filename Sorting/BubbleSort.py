def sort(list):
    for index1 in range(len(list)):
        for index in range(len(list)-1):
            if list[index] > list[index+1]:
                swap(list, index)
    return list
        
def swap(list, index):
    temp = list[index]
    list[index] = list[index+1]
    list[index+1] = temp 
    return

a = [4,2,5,1,6,9,8,3]
b = sort(a)
print(b)