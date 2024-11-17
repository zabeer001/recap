def get_series_sum(n):
    if n % 2 == 0:
        result = n/2 * pow(-1, n)
    else:
        result = (n+1)/2 * pow(-1, n)
    return int(result)
n = int(input())
print(get_series_sum(n))
