def getMinMax(a, n):
    minimum = a[0]
    maximum = a[0]
    for val in a:
        minimum = min(minimum, val)
        maximum = max(maximum, val)

    return [minimum, maximum]
