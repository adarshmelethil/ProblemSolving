#!/use/bin/env/ python

'''

RedKnightsShortestPath.py

Author:  		Adarsh Melethil
Created:		25, December 2017
Last-Modified:	25, December 2017

'''

import sys

def printShortestPath(n, i_start, j_start, i_end, j_end):
    #  Print the distance along with the sequence of moves.
    upward_distance = (i_start - i_end)
    if  (upward_distance % 2) != 0 or \
        ((j_start + ((upward_distance)//2))%2) != (j_end % 2): 
        print("Impossible")
        return
    
    total_moves = 0
    moves_l = ['UL', 'UR', 'R', 'LR', 'LL', 'L']
    moves_c = [0, 0, 0, 0, 0, 0]
    while i_start != i_end or j_start != j_end:
        total_moves += 1
        if i_start > i_end:
            i_start -= 2
            if j_start >= j_end:
                moves_c[0] += 1
                j_start -= 1 
            else:
                moves_c[1] += 1
                j_start += 1 
        elif i_start < i_end:
            i_start += 2
            if j_start >= j_end:
                moves_c[4] += 1
                j_start -= 1 
            else:
                moves_c[3] += 1
                j_start += 1 
        elif j_start < j_end:
            j_start += 2
            moves_c[2] += 1
        elif j_start > j_end:
            j_start -= 2
            moves_c[5] += 1
    print(total_moves)
    
    print(' '.join([' '.join([moves_l[i]]*val) for i,val in enumerate(moves_c) if val > 0] ) )




if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    printShortestPath(n, i_start, j_start, i_end, j_end)
