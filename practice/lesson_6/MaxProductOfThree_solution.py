# https://app.codility.com/demo/results/trainingQSNZJF-MWA/
def solution_1(array):
    max_num = -2000
    for idx,val_x in enumerate(array):
        for idy,val_y in enumerate(array):
            for idz,val_z in enumerate(array):
                if (idx==idy) or (idx==idz) or (idy==idz) : continue
                else :
                    result = val_x * val_y * val_z
                    max_num = result if result > max_num else max_num
    return max_num

# https://app.codility.com/demo/results/training7SEXW7-UEA/
def solution(array):
    array = sorted(array)
    num_1 = array[-3] * array[-2] * array[-1]
    num_2 = array[-1] * array[0] * array[1]
    return num_1 if num_1 > num_2 else num_2
if __name__ == '__main__':
    print(solution([-9,-10,-2,-2,-5,-6,-9]))