numbers = [1,1,2,3,3,3,4,4,5,6]
for number in numbers:
    print(number)
    
unique_numbers = {}
for number in numbers:
    unique_numbers[number]=""

for number in unique_numbers.keys():
    print(number)
    
    
    '''
    1
1
2
3
3
3
4
4
5
6
1
2
3
4
5
6
'''
    
