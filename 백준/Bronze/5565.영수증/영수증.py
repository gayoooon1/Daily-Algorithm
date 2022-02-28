total = int(input())
book = 0
for i in range(9):
    price = int(input())
    book += price
print(total - book)