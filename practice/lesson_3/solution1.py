# https://app.codility.com/demo/results/trainingB7MK35-XJD/
def solution(x1,x2,step):
    result=(x2-x1)//step
    ex_step=(x2-x1)%step
    if ex_step != 0 : result = result + 1
    return result

if __name__ == '__main__':
    solution(3,1,3)