def fibonacci_generator():
    """
    :return:the generator produces number
    """
    i = 0
    j = 1
    yield 1
    while True:
        yield j+i
        n = i
        i = j
        j = n + i


def main(n):
    for k in fibonacci_generator():
        if k < n:
            print(f"the number is {k}")


#test
if __name__ == '__main__':
    main(200)










