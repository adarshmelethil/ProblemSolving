#!/use/bin/env/ python

'''

CityDestruction.py

Author:  		Adarsh Melethil
Created:		22, November 2017
Last-Modified:	20, December 2017

'''

import math
import pprint 

memo = list()
N, D = 0, 0
H, E = list(), list()
def getAnswer(i, b, j):
    end  = '\n' + ('  '*(i+1)) + '->'
    print(i, b, j, end=end)
    if i == N : 
        print(0)
        return 0

    if memo[b][i] != -1:
        print(memo[b][i])
        return memo[b][i]

    val1 = max([0, int((H[i] - j + D - 1)/D) ])
    val2 = max([0, int((H[i] - E[i+1] - j + D - 1)/D) ])


    ans = min([val1 + getAnswer(i+1, True, E[i]), val2 + getAnswer(i+1, False, 0)])
    memo[b][i] = ans
    print('ans =',ans)
    return ans 


T = int(input())
for _ in range(T):
    N, D = map(int, (input()).split(' '))
    H = list(map(int, (input()).split(' ')))
    E = list(map(int, (input()).split(' ')))
    # print(N, D, '\n', H, '\n', E)

    memo = [[-1]*N, [-1]*N]

    H.append(0)
    E.append(0)

    # print(simulate_game(H, E, N, D))
    
    print(getAnswer(0, True, 0))
    # print(memo)
