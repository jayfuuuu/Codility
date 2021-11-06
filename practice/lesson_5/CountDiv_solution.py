# https://app.codility.com/demo/results/trainingWRZJ9H-R44/
import math
def solution(start,end,mod):
    print(f"math.floor(end/mod):{math.floor(end/mod)},math.floor((start-1)/mod):{math.floor((start-1)/mod)},\nend/mod:{end/mod},(start-1)/mod:{(start-1)/mod}")
    return int( math.floor(end/mod) - math.floor((start-1)/mod) )
if __name__ == '__main__':
    print(solution(0,32333,11))