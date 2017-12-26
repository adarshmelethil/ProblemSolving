#!/use/bin/env/ python

'''

TheSalesman.py

Author:  		Adarsh Melethil
Created:		25, December 2017
Last-Modified:	25, December 2017

'''

def minimumTime(house_info, number_of_houses):
    if number_of_houses < 2: return 0
    cur_house = max(house_info)
    house_info.remove(cur_house)
    time = 0
    while(house_info):
        next_house = max(house_info)
        time += cur_house - next_house
        cur_house = next_house
        house_info.remove(cur_house)

    return time

T = int(input())

for _ in range(T):
    N = int(input())
    X = list(map(int, input().split() ))
    print(minimumTime(X, N))

