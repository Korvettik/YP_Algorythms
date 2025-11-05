def bubble_sort(n, array):
    #print(n, array)

    status = True
    while status:
        before_array = array.copy()

        for i in range(n - 1):
            if array[i] > array[i+1]:
                second = array[i+1]
                array[i+1] = array[i]
                array[i] = second

        print(*array, sep=' ')

        if before_array == array:
            status = False




n = int(input().strip())  # длинна массива
array = list(map(int, input().strip().split(' ')))  # сам массив

bubble_sort(n, array)