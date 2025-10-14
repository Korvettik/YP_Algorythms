from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
    res_count = 0

    len_temperatures = len(temperatures)

    if len_temperatures == 1:
        return 1
    else:
        for i in range(len_temperatures):
            #print(f'сейчас {temperatures[i]}')

            if i == 0:
                if temperatures[i] > temperatures[i+1]:
                    #print(f'берем1 {temperatures[i]}')
                    res_count += 1
            elif i < len_temperatures-1:
                if temperatures[i-1] < temperatures[i] > temperatures[i+1]:
                    #print(f'берем2 {temperatures[i]}')
                    res_count += 1
            elif i == len_temperatures-1:
                if temperatures[i] > temperatures[i-1]:
                    #print(f'берем3 {temperatures[i]}')
                    res_count += 1

    return res_count










def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
