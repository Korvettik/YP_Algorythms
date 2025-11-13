def shopping_house(n, m, prices):
    #print(n, m, prices)
    my_houses = 0
    prices.sort()
    for price in prices:
        if m >= price:
            my_houses += 1
            m -= price
        else:
            break

    return my_houses


n, m = list(map(int, input().strip().split(' ')))  # количество объявлений о продаже домов  + общий бюджет
prices = list(map(int, input().strip().split(' ')))  # стоимости домов

my_houses = shopping_house(n, m, prices)
print(my_houses)
