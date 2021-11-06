import random

def solution(array):
    print(f"array:{array}")
    if not array : return True
    for idx,res in enumerate(sorted(array)):
        if res-1-idx : 
            print(idx+1)
            if idx != len(array)-1 : 
                return idx+1
        if idx == len(array)-1 : 
            print(len(array)+1)
            return len(array)
        else : continue

    
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    # for idx in range(65536):
    #     array.append(idx)
    # array.remove(random.randint(1,65536))
    solution(array)