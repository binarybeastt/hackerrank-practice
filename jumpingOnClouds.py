def jumpingOnClouds(c):
    counter = 0
    i = 0
    n = len(c)

    while i < n - 1:
        # Check if we can make a jump of 2
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        counter += 1

    return counter

c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))