def squares_generator(N):
    for i in range(N):
        yield i ** 2


N = 5
for square in squares_generator(N):
    print(square)