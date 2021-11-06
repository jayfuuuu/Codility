# https://app.codility.com/demo/results/trainingDUCGBT-EXB/
def solution(array):
    # result = []
    # N = len(array)
    # p = 0
    # a = 0
    # for idx in range(N) :
    #     for idx_loop in range(idx):
    #         p = p + array[idx_loop]
    #     for idx_loop in range(N-idx,idx,-1):
    #         a = a + array[idx_loop-1]
    #     result.append(abs(p-a))
    #     a = 0
    #     p = 0
    # # for idx in result:
    # #     print(idx)
    result = []
    sum = []
    for idx,val in enumerate(array):
        if idx == 0 : sum.append(val)
        else : sum.append(sum[-1]+val)
    print(f"all:{sum}")
    for idx,val in enumerate(sum) :
        if idx == len(sum)-1 : continue
        else : result.append(abs(sum[-1]-(2*val)))
    print(f"result:{result}")
    return sorted(result)[0]
if __name__ == '__main__':
    array = [1,1,1,1,1,1]
    solution(array)