# https://app.codility.com/demo/results/trainingYBFBZ5-UMC/
def solution(array):
    # print(f"array:{array}")
    position = 0
    error = 0
    stack = []
    mapping = {'{':'}','[':']','(':')'}
    for ch in array:
        if ch in mapping :
            stack.append(ch)
            position += 1
        elif (position != 0) and (mapping[stack[position-1]] == ch):
            stack.pop()
            position -= 1
        else:
            error += 1

    # print(f"position:{position}")
    if position == 0 and error == 0 : return 1
    else : return 0

if __name__ == '__main__': 
    print(solution('())'))

'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
'''