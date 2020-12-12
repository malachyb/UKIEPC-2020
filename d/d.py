input()
total_money = sum(map(int, input().split()))
print("no" if total_money % 3 else "yes")
