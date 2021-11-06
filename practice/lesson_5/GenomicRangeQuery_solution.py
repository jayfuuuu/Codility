# https://app.codility.com/demo/results/trainingQ33NRC-9RN/
def solution_1(S, P, Q):
    diff_position = [0] * len(P)
    result = [0] * len(P)
    for idx in range(len(P)):
        diff_position[idx] = S[P[idx]:Q[idx]+1] if P[idx] != Q[idx] else S[P[idx]]
    for idx in range(len(result)):
        if 'A' in diff_position[idx] : 
            result[idx] = 1
            continue
        elif 'C' in diff_position[idx] :
            result[idx] = 2
            continue
        elif 'G' in diff_position[idx] :
            result[idx] = 3
        elif 'T' in diff_position[idx] :
            result[idx] = 4
    return result
def solution(S, P, Q):
    res = []
    for idx in range(len(P)):
        print(f"S[P[idx]:Q[idx]+1]:{S[P[idx]:Q[idx]+1]}")
        if 'A' in S[P[idx]:Q[idx]+1] :
            res.append(1)
        elif 'C' in S[P[idx]:Q[idx]+1] :
            res.append(2)
        elif 'G' in S[P[idx]:Q[idx]+1] :
            res.append(3)
        elif 'T' in S[P[idx]:Q[idx]+1] :
            res.append(4)
    return res
if __name__ == '__main__':
    print(solution('CAGCCTA',[2,5,0],[4,5,6]))