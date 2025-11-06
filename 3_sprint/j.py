def bubble_sort(n, array):
    #print(n, array)


    before_array = array.copy()
    status = True
    steps = 0

    while status:
        for i in range(n - 1):
            if array[i] > array[i+1]:
                second = array[i+1]
                array[i+1] = array[i]
                array[i] = second

        steps += 1

        if before_array == array and steps == 1:
            print(*array, sep=' ')
            status = False
        elif before_array == array:
            status = False
        else:
            before_array = array.copy()
            print(*array, sep=' ')









n = int(input().strip())  # длинна массива
array = list(map(int, input().strip().split(' ')))  # сам массив

bubble_sort(n, array)