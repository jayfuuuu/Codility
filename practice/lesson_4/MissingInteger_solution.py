# https://app.codility.com/demo/results/trainingP3983E-45J/
def solution_1(array):
    max_num = array[0]
    for idx,val in enumerate(array):
        # print(f"idx:{idx},idx+1:{idx+1},val:{val}")
        max_num = val if val > max_num else max_num
        if idx+1 not in array : return max_num if max_num > 0 else 1
        if idx+1 == len(array) : return idx+2

def final_solution_2(array):
    copy_array = set(array)
    max_num = max(copy_array)
    if max_num < 0 : return 1
    else :
        for idx in range(1,max_num+2):
            if idx not in copy_array : return idx

def solution_3(array):
    min_num = 1
    copy_array = set(array)
    for idx,val in enumerate(array):
        if idx in array : min_num += 1
    if min_num == len(array) : return min_num+1
    return min_num

if __name__ == '__main__':
    print(final_solution_2([1,2,3,3,4]))