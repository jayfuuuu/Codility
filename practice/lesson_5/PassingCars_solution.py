#https://app.codility.com/demo/results/training9BJSGY-AD5/
def solution(array):
    pair_base = 0
    pair = 0
    for val in array:
        if(val==1) : 
            pair += pair_base
        else :
            pair_base += 1
    return pair if pair <= 1000000000 else -1

if __name__=='__main__':
    solution([0,1,0,1,1])
