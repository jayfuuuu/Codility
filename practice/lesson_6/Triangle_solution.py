# https://app.codility.com/demo/results/trainingKT3KJQ-876/
def solution(array):
    len_array = len(array)
    if len_array < 3: return 0
    array.sort()
    for idx in range(len_array-2):
        if array[idx]+array[idx+1] > array[idx+2] : return 1
    return 0
if __name__ == '__main__':
    print(solution([10,2,5,1,8,20]))