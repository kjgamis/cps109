# def riffle(items, out = True):
# Given a list of ​items that is guaranteed to contain an even number of elements (note that the integer zero is an even number), create and return a list produced by performing a perfect ​riffle to the ​items​ by interleaving the items of the two halves of the list in an alternating fashion.
# When performing a perfect riffle, also known as the ​Faro shuffle​, the list of ​items is split in two equal sized halves, either conceptually or in actuality. The first two elements of the result are then the first elements of those halves. The next two elements of the result are the second elements of those halves, followed by the third elements of those halves, and so on up to the last elements of those halves. The parameter ​out determines whether this function perfor


def riffle(items, out=True):
    half = int(len(items) / 2)
    first = items[0:half]
    second = items[half:len(items)]
    new_items = []

    for i in range(0, half):
        if out is True:
            new_items.append(first[i])
            new_items.append(second[i])
        else:
            new_items.append(second[i])
            new_items.append(first[i])

    return new_items




print(riffle([1, 2, 3, 4, 5, 6, 7, 8], True))
print(riffle([1, 2, 3, 4, 5, 6, 7, 8], False))
print(riffle([], True))
print(riffle(['bob', 'jack'], True))
print(riffle(['bob', 'jack'], False))