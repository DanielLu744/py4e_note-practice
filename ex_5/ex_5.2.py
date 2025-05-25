largest = None
smallest = None

while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        n = int(num)
    except:
        print('Invalid input')
        continue
    # print(n)
    if largest is None or n > largest:
        largest = n
    if smallest is None or n < smallest:
        smallest = n

print('Maximun is', largest)
print('Minimun is', smallest)