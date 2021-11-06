#https://app.codility.com/demo/results/training96XKBP-K6W/
def solution(array:list, p:int):
    if(p<1) : return array
    result = array.copy()
    array_len = len(array)
    for idx ,data in enumerate(array):
        print(f"data:{data},idx:{idx},array_len:{array_len},result:{array}")
        result[(idx+p)%array_len] = data
        print(result)
    return result
if __name__ == "__main__":
    array = [3, 8, 9]
    position = 3
    solution(array,position)