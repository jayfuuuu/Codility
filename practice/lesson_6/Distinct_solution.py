# https://app.codility.com/demo/results/training5N85FS-GJ4/
def solution(array):
    time = 0
    set_array = set()
    for val in array:
        if val not in set_array : 
            time += 1
            set_array.add(val)
    return time
if __name__ == '__main__':
    print(solution([0]))