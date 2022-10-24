def check(x):
    sum = 0
    for i in range(1,x//2+1):
         if x % i ==0:
             sum +=i
    if sum == x :
        return 'Yes'
    return 'NO'
test_cases = int (input())
list=list()
for i in range(test_cases):
    list.append(int(input()))
print('\n----------\n')
for i in list:
    print (check(i))


    '''# def check(x):
    sum = 0
    for i in range(1,x//2+1):
         if x % i ==0:
             sum +=i
    if sum == x :
        return 'Yes'
    return 'NO'
test_cases = int (input())
list=list()
for i in range(test_cases):
    list.append(int(input()))
# print('\n----------\n')
for i in list:
    # print (check(i))'''