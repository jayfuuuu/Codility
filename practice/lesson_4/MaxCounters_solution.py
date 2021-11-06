#https://app.codility.com/demo/results/trainingPDWFXQ-5BQ/
def solution_1(N,array):
    Counter = [0] * N
    for val in array:
        if (val >= N+1 ) : 
            Counter = [max(Counter)] * N
        else :
            Counter[val-1] += 1
    return Counter

def solution(N,array):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for idx,item in enumerate(array):
        if 1 <= item <= N :
            counters[item-1] = max(counters[item-1],last_update)
            counters[item-1] += 1
            max_counter = max(counters[item-1],max_counter)
        elif item == N+1 :
            last_update = max_counter
    for idx in range(N):
        counters[idx] = max(counters[idx],last_update)
    return counters

if __name__ == '__main__':
    print(f"Result:{solution(5, [3, 4, 4, 6, 1, 4, 4])}") # [3, 2, 2, 4, 2]
