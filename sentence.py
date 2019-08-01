from re import split
from scipy.spatial import distance


def tokenization(sentence):
    return list(filter(None, split('[^a-z]', sentence.lower())))


file = open('text.txt', 'r')
lines = file.readlines()
file.close()

lines = list(map(lambda line: tokenization(line), lines))

dictionary = dict()
d = 0
for line in lines:
    for word in line:
        if word not in dictionary:
            dictionary[word] = d
            d += 1

matrix = []
for line in lines:
    array = []
    for word in dictionary:
        array.append(line.count(word))
    matrix.append(array)

min_dist = 1.0
number = -1

for i in range(1, len(lines)):
    dist = distance.cosine(matrix[0], matrix[i])
    if min_dist > dist:
        min_dist = dist
        number = i + 1

print(min_dist, ' with_line ', number)

