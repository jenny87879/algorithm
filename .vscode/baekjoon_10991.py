star = int(input())
for i in range(1, star+1, 1):
    for j in range(star-i):
        print('@', end='')
    # for k in range(1, star, 1):
        print('*', end='')
        for l in range(1, i-1, 1):
            print('@*', end='')
    print('')