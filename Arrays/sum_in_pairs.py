def sum_in_pairs(list, size, sum):
    hash = [0]*10
    for index in range(size):
        temp = sum-list[index]
        if hash[temp] == 1:
            print('Pair is ({}, {})'.format(temp,list[index]))

        hash[list[index]] = 1
    print(hash)
arr = [4,7,6,5,8]
sum_in_pairs(arr, 5, 9)
