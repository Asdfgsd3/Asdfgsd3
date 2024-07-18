lst = [60, 30, '20']

score = [85, 90, 80, 75, 95]

max(score)
min(score)
sum(score)

list(range(10))
list(range(0, 10))
list(range(0, 10, 1))

score = [85, 90, 80, 75, 95]
score[0]
score[1]
score[2]
score[3]
score[4]

score[-1]
score[-5]

score[1:3]
score[ :2]
score[2: ]

score.append(100)
print(score)

del score[5]
print(score)

score[2:0] = []
print(score)

score.append([100, 100])

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list1[5: ] + list1[ :5]
print(list2)