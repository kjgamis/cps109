# def count_dominators(items):
# An element of ​items is said to be a ​dominator if every element to its right is strictly smaller than it. This function should count how many elements in the given list of ​items are dominators, and return that count. For example, in the list ​[42, 7, 12, 9, 2, 5]​, the elements 42, 12, 9 and 5 are dominators. By this definition, the last item of the list is automatically a dominator.


def count_dominators(items):
    count = 0
    if len(items) > 0:
        count = 1
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                count += 1
    return count


print(count_dominators([42, 7, 12, 9, 2, 5]))        # 4
print(count_dominators([]))                          # 0
print(count_dominators([99]))                        # 1
print(count_dominators(list(range(10**7))))          # 1
print(count_dominators(list(range(10**7, 0, -1))))   # 10000000
