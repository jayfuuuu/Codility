#https://app.codility.com/demo/results/trainingVZRFME-V6H/
def solution(end, process):
    check = set()
    target = sum(range(end+1))
    tail = len(process)-1
    for idx, res in enumerate(process):
        if (res not in check):
            if (res <= end): 
                check.add(res)
                target -= res
        if target == 0 : return idx
        elif idx == tail : return  int(-1)
if __name__ == "__main__":
    solution(2, [1, 3, 1, 4, 2, 3, 5, 4])
