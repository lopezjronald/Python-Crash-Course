def alternatingSort(a):
    if len(a) == 1:
        return True

    odd_num = 0
    if (len(a) % 2 == 1):
        odd_num = int(len(a) / 2)
        odd_num += 1

    arr = a[:]
    b = []

    if (len(a) % 2 == 0):
        for i in range(int(len(arr) / 2)):
            b.append(arr[i])
            b.append(arr.pop())
    else:
        for i in range(odd_num):
            if i == odd_num - 1:
                b.append(arr[i])
            else:
                b.append(arr[i])
                b.append(arr.pop())
    return (sorted(a) == b and len(sorted(a)) == len(b))


a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]

print(alternatingSort(a))


def almostIncreasingSequence(sequence):
    if len(sequence) <= 2:
        return True

    for value in range(len(sequence)):
        copy = sequence[:]
        del copy[value]
        if len(set(copy)) != len(copy):
            continue
        elif copy == sorted(copy):
            return True

    return False


sequence = [1, 2, 5, 3, 5]
set_seq = set(sequence)
sequ_copy = []
for val in set_seq:
    sequ_copy.append(val)
print(sequ_copy)
print(sorted(sequence))
print(almostIncreasingSequence(sequence))

print(sequence.pop(0))
