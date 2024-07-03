# E_true = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 0]]
# E_false = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 0, 0, 0], [0, 0, 0, 0]]
# E_false2 = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
# G = [
#   [0,1,1,1],
#   [0,0,1,1],
#   [0,0,0,0],
#   [0,0,1,0]
#     ]

# def uni_exit(T: list) -> bool:
#     n=len(T)
#     i,j=0,0
#     flag=True
#     while i<n and j<n:
#         if i==j and i<n-1:
#            i+=1
#         elif T[i][j]==0 and j<n:
#             j+=1
#         elif T[i][j]==1 and i<n-1:
#             i+=1
    
#     for k in range(n):
#         if T[i][k] == 1:
#             return False
#     for k in range(n):
#         if k == i:
#             continue
#         if T[k][i] == 0:
#             return False

#     return flag


# print(uni_exit(E_true))
# print(uni_exit(E_false))
# print(uni_exit(E_false2))
# print(uni_exit(G))

def uniwersalne_ujscie(G):
  i=0
  j=0
  n=len(G)
  while i<n and j<n:
    if G[i][j] == 0:
      j += 1
    else:
      i += 1
  for k in range(n):
    if G[i][k] == 1:
      return False
  for k in range(n):
    if k == i:
      continue
    if G[k][i] == 0:
      return False
  return True

G = [
  [0,1,1,0],
  [1,0,1,1],
  [0,0,0,0],
  [1,0,1,0]
    ]

print(uniwersalne_ujscie(G))