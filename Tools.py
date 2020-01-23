import numpy

def permutation(source, by):
    dest = by[:]

    for i, bit in enumerate(by):
        dest[i] = source[bit]

    return dest

def leftShift(arrayA):
    arrayB = arrayA[:]
    F = arrayA[0]

    for i in range(len(arrayA) - 1):
        arrayB[i] = arrayB[i + 1]
    arrayB[len(arrayB) - 1] = F

    return arrayB

def wrap(binaries):
    size = len(binaries)
    packs = int(size / 64)
    binaries += [0 for i in range(((packs + 1) * 64 - size) % 64)]

    return numpy.array_split(binaries, packs + 1)

"""
def expansion(source, by):
    E = list()

    for i in range(3):
        E += permutation(source, by)

    print(numpy.tile(source, 3))
"""

def xor(arrayA, arrayB):
    arrayC = arrayA[:]

    for i, value in enumerate(arrayC):
        arrayC[i] ^= arrayB[i]

    return arrayC

def sumBinary(B):
    n = 0

    for i, bit in enumerate(B):
        n <<= 1
        n |= bit

    return n

def toBinary(n, pad):
    return [int(x) for x in bin(n)[2:].zfill(pad)]

def toString(source):
    return "".join([str(char) for char in source])