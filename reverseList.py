#Given the size and the elements of array A, print all the elements in reverse order.
'''
# Read input from stdin and provide input before running code

name = raw_input()
print 'Hi, %s.' % name
'''
length = int(raw_input())
new_list = []
for i in range(length):
    new_list.append(int(raw_input()))

for j in range(length):
    print(new_list[-(j+1)])
