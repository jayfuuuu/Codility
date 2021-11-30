# https://app.codility.com/demo/results/trainingPURU8U-DP4/
def solution(array):
    set_array = set()
    for val in array:
        if val not in set_array :
            set_array.add(val)
    return len(set_array)
if __name__ == '__main__':
    print(solution([0]))