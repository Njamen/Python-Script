def decompose(n, result):
    if n == 1:
        print(1, " ")
        result.append(1)
    else:
        for d in range(2,n+1):
            if n % d == 0:
                print(d, end=" * ")
                result.append(d)
                break
        decompose( n // d, result)
                
result = []            
decompose(100, result)
print(result)