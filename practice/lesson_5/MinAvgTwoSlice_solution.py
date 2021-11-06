# https://app.codility.com/demo/results/trainingEXSU9X-52K/
def solution(array):
    len_array = len(array)
    min_num = float('inf')
    min_idx = 0
    for idx in range(len_array):
        if idx <= len_array-2 :
            Pice2 = (array[idx] + array[idx+1]) / 2
            if (Pice2 < min_num):
                min_idx = idx
                min_num = Pice2
        if idx <= len_array-3 :
            Pice3 = (array[idx] + array[idx+1] + array[idx+2]) / 3
            if (Pice3 < min_num):
                min_idx = idx
                min_num = Pice3
    return min_idx
if __name__ == '__main__':
    print(solution([10, 10, -1, 2, 4, -1, 2, -1]))