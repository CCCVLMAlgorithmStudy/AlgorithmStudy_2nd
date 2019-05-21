def flatlandSpaceStations(n, c):
    sortedC = sorted(c)
    result = sortedC[0] if sortedC[0] > (n-1 -sortedC[-1]) else (n-1 - sortedC[-1])
    for i in range(0,len(sortedC)-1):
        dist = sortedC[i+1] - sortedC[i]
        if dist%2 == 0:
            temp = dist//2
            result = result if result>temp else temp
        else:
            temp = (dist-1)//2
            result = result if result>temp else temp
    return result