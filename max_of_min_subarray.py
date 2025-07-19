k = int(input())
n = int(input())
space = []

for i in range(n):
    space.append(int(input()))


def get_min_segment(k,n, space):

    if k == 1:
        return max(space)
    
    curr_min = 0
    max_min = float('-inf')

    for i in range(k, n):
        curr_min = min(space[i-k: i])
        max_min = max(curr_min, max_min)

    return max_min




