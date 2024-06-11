def sockMerchant(n, ar):
    color_count = {}
    for color in ar:
        if color in color_count:
            color_count[color]+=1
        else:
            color_count[color]=1

    pairs=0
    for count in color_count.values():
        pairs+=count//2
    
    return pairs

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(ar)

print(sockMerchant(n, ar))