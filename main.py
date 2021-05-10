import random
'''
Sample code, which gives out random predictions of all instances. 
'''
n = 1481
with open('outputs/submission.csv','w') as f:
    f.write('id,answer\n')
    for i in range(n):
        j = random.randint(1,5)
        f.write(str(i+1) + ',' + str(j) + '\n')