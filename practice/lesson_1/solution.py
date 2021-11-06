# https://app.codility.com/demo/results/trainingSYMT93-WEX/
import sys

bin_num = []
len_arr = []

def short_mod(num , bin_num):
    if(num<2) : return bin_num.append(str(num))
    bin_num.append(str(num%2))
    return short_mod(num//2,bin_num)

def space(obj):
    start_flag = False
    len_v = 0
    loop = 0

    for idx, val in enumerate(obj):
        # print(f"idx:{idx},start_flag:{start_flag},len:{len}")
        if (int(val)) : 
            start_flag = not start_flag
            if(not start_flag) : 
                start_flag = not start_flag
                len_arr.append(len_v)
                len_v = 0
                loop = loop + 1
        else : 
            len_v = len_v + 1

        if (idx == len(obj)-1) :
            if (val == '0') : 
                len_v = 0
                len_arr.append(len_v)
            return True

def solution(N):
    if(int(N)<2) : return 0 
    short_mod(int(N),bin_num)
    print(f"final : {bin_num[::-1]}")
    space(bin_num[::-1])
    print(f"max_len:{sorted(len_arr)[-1]}")
    return sorted(len_arr)[-1]