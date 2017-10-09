'''
	N swathers
	M stages
	Pij unit of time for each swather i and each stage j

	- only one worker at each stage
	- a stage can't start until a previous stage for that swather is done

'''

num_swather, num_stages = map(int, (input()).split())


swather_time = []
for _ in range(num_swather):
	swather_time.append(list(map(int, (input()).split())))

stage_time = []
for i in range(num_stages):
	stage_time.append([])
	for j in range(num_swather):
		stage_time[i].append(swather_time[j][i])

# print(stage_time)
# print("***")
done = False
time_done = [0] * num_swather
active_worker = [-1]

while True:
	# min_time_to_work = []
	for i in range(len(active_worker)):
		if(active_worker[i] < 0):
			if i == 0:
				done_swather = stage_time[i]
			else:
				done_swather = [a for a,b in zip(stage_time[i], stage_time[i-1]) if b == 0]
			done_swather = [a for a in done_swather if a > 0]
			if len(done_swather) == 0:
				continue

			index = stage_time[i].index(done_swather[0])
			active_worker[i] = index

	t = [stage_time[i][active_worker[i]] for i in range(len(active_worker)) if active_worker[i] >= 0]
	min_time = min(t)

	for i in range(num_swather):
		if stage_time[num_stages-1][i] > 0:
			time_done[i] += min_time

	for i in range(len(active_worker)):
		if(active_worker[i] < 0): continue
		stage_time[i][active_worker[i]] -= min_time
		
		if stage_time[i][active_worker[i]] == 0:
			active_worker[i] = -1
			if i == (len(active_worker)-1) and len(active_worker) < num_stages:
				active_worker.append(-1)

	if max(stage_time[num_stages-1]) == 0:
		break

print(' '.join('{}'.format(t) for t in time_done))
