distances = []
days = int(input())
people = [input().split() for i in range(3)]

for day in range(days):
    choices = sorted([people[i][day] for i in range(3)])
    distances.append(choices[1])


print(' '.join(map(str, distances)))
