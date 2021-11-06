#https://app.codility.com/demo/results/training9QXXG5-FUA/
def solution(A):
  S = set(A)
  return 1 if max(S) == len(S) and len(S) == len(A) else 0
if __name__ == '__main__':
    solution([4, 1, 3])

#1st version
# # print(f"input_array:{array}")
# ###
# length = len(array)
# target = sum(range(length+1))
# compared = sum(array)
# Flag = target-compared
# # print(f"target:{target},compared:{compared},Flag:{Flag}")
# ###
# if(Flag == 0):
#     for idx,val in enumerate(array):
#         if idx+1 not in array: return 0
#     return 1
# else:
#     return 0

### 2st version
    # for idx,val in enumerate(array):
    #     if idx+1 not in array: return 0
    # return 1