import time


def elements():
    yield 'element 1'
    yield 'element 2'
    yield 'element 3'
    print("hello world")
    yield 'element 4'



if __name__ == '__main__':

    generator = elements()

    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())

    for e in elements():
        print(e)

    for i in range(10000000000000000000):
        print(i)
        if i > 10:
            break

    # start = time.time()
    # range_list = [i for i in range(100000000)]
    # end = time.time()
    # print(f'Time needed: {end - start}')
    #
    # for i in range_list:
    #     print(i)
    #     if i > 10:
    #         break

    def tens():
        i = 1
        while True:
            yield i * 10
            i += 1



    generator_tens = tens()

    print(generator_tens.__next__())
    print(generator_tens.__next__())
    print(next(generator_tens))

    print("And now in for loop")

    for ten in generator_tens:
        print(ten)
        if ten > 100:
            break

    #  Stworz generator ktory bedzie przyjmowal przez parametr ilosc elementow a nastepnie zwracal elementy o tresci
    #  'element o indeksie x'( gdzie x bedzie numerem podawanego elementu) czekajac 1 sekunde przed zwrotem kazdego elementu.

