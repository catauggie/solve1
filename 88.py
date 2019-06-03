print(list(map(lambda x: x**2, list(filter(lambda x: not x%3, (int(input() for _ in range(int(input())))))))))
