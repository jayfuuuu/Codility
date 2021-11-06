# https://app.codility.com/demo/results/trainingPQE6KN-A22/
def solution(array:list):
    res_array = {}
    for res in array:
        res_array[res] = 0
    for res in array:
        res_array[res]=res_array[res]+1
    for res in res_array:
        if res_array[res]%2 : return res

if __name__ == "__main__":
    array = [1,2,201,3,201,24,2,1,3,201,201]
    solution(array)