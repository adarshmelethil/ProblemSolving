'''
	Problem D Game Rank


	25 regular ranks plus 'Legend' rank
	25 lowest, 1 second highest, 'Legend' highest

	winning a game gives you a star
	a certain number of stars are required to advance to next rank
	win streaks gets you 2 star 
	stars are carried over to new rank when advancing to new rank with 2 stars
	a star is not consumed when ranking, e.g. rank 25 and 3 stars, wins, rank 24 and 1 star 

	rank 20 and lower can't lose stars
	losing a star when at a rank with 0 star will result in losing a rank and a star in the lower rank 

	 "If a player reaches the Legend rank, she will stay legend no matter how many losses she incurs afterwards."
'''

'''
25-21: 2 stars (1-5) -> 5*2=10		10
20-16: 3 stars (6-10) -> 5*3=15 	25
15-11: 4 stars (11-15) -> 5*4=20 	45
10-1: 5 stars 	(16-25) -> 10*5=50 	95
'''

total_stars = 0
win_streak = 0

def starsToRank(stars):
	rank = 25
	for i in range(5):
		if stars-3 < 0:	
			if stars == 2 and win_streak==0 and rank == 21: rank -= 1
			break
		stars -= 2
		rank -= 1
	# for i in range(5):
	# 	if stars-4 < 0: 
	# 		if stars == 3 and win_streak==0: rank -= 1
	# 		break
	# 	stars -= 3
	# 	rank -= 1
	# for i in range(5):
	# 	if stars-5 < 0: 
	# 		if stars == 4 and win_streak==0: rank -= 1
	# 		break
	# 	stars -= 4
	# 	rank -= 1
	for i in range(2):
		for j in range(5):
			if stars-(i+4) < 0:
				if stars == (i+3) and win_streak==0: rank -= 1
				break
			stars -= 2
			rank -= 1

	for i in range(10):
		if stars-6 < 0: 
			if stars == 5 and win_streak==0: rank -= 1
			break
		stars -= 5
		rank -= 1
	if rank <= 0:
		rank = "Legend"
	return rank 

def updateStar(game):
	global total_stars
	global win_streak
	if game.lower() == 'w':
		win_streak += 1
		stars_gained = 2 if win_streak>2 and total_stars < 71 else 1
		total_stars += stars_gained
	elif game.lower() == 'l':
		if total_stars > 10 and total_stars < 96
			total_stars -= 1
		win_streak = 0

# n = int(input())
# for i in range(n):
game_history = input()
total_stars = 0
win_streak = 0
# print(game_history)
for game in game_history:
	# print (game)
	updateStar(game)

	# print(game,starsToRank(total_stars), total_stars, win_streak)
print(starsToRank(total_stars))
