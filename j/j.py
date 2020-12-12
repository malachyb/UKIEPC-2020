corners, edges, centres = map(int, input().split())

perimeter = corners * 2 + edges
area = corners + edges + centres
possible = False

for i, j in [(i, area / i) for i in range(1, int(area**0.5)+1) if area % i == 0]:
    if perimeter == 2 * i + 2 * j:
        if i >= j >= 2:
            print(int(i), int(j))
        else:
            print(int(j), int(i))
        possible = True
        break

if not possible:
    print("impossible")
