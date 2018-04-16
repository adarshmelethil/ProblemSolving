
poss = "POSSIBLE"
imposs = "IMPOSSIBLE"

def isValidHCut(waffle, cut_h, cut_v):
  top_left_c = 0
  top_right_c = 0

  bottom_left_c = 0
  bottom_right_c = 0
  for i in range(len(waffle)):
    if i < cut_h:
      top_left_c += waffle[i][:cut_v].count("@")
      top_right_c += waffle[i][cut_v:].count("@")
    else:
      bottom_left_c += waffle[i][:cut_v].count("@")
      bottom_right_c += waffle[i][cut_v:].count("@")

  # if (top_left_c == top_right_c) and (bottom_left_c == bottom_right_c) and (top_left_c == bottom_left_c):
  #   print(top_left_c,top_right_c, bottom_left_c, bottom_right_c)
  return (top_left_c == top_right_c) and (bottom_left_c == bottom_right_c) and (top_left_c == bottom_left_c)

def makeHCut(waffle, H, cut_v):
  height = len(waffle)

  for x in range(1, height):
    if isValidHCut(waffle, x, cut_v):
      return x 

def isValidVCut(waffle, cut_v, V):
  height = len(waffle)
  width = len(waffle[0])
  left_count = 0
  right_count = 0
  for i in range(width):
    if i < cut_v:
      for j in range(height):
        # print(waffle[j][i])
        if waffle[j][i] == '@':
          left_count += 1
    else:
      for j in range(height):
        if waffle[j][i] == '@':
          right_count += 1

    # print(cut_v,left_count, right_count)
  
  return left_count == right_count

def makeVCut(waffle, V):
  width = len(waffle[0])

  for x in range(1, width):
    if isValidVCut(waffle, x):
      yield x 
      
def solve(R, C, H, V, waffle):
  cut_v_gen = makeVCut(waffle, V)

  for cut_v in cut_v_gen:
    cut_h = makeHCut(waffle, H, cut_v)
    if cut_h is None:
      continue
    else:
      return poss

  return imposs


t = int(input())
for case in range(t):
  R, C, H, V = map(int, input().split())
  waffle = []
  for i in range(R):
    waffle.append(input())

  ans = solve(R, C, H, V, waffle)
  # exit()
  print('Case #{case}: {ans}'.format(case=case+1, ans=ans))