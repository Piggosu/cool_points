from random import *
from math import *

radius = sqrt(float(input('Insert radius of circle for testing. \nLarger radii will exponentially increase processing time. \n')) ** 2)
print('Radius entered as %f. \n'%(radius))

while True:
    try:
        increment = int(input('Insert the number of increments you would like the circle to shift by. \nLarger increments will exponentially increase processing time but will increase data precision. \n'))
        break
    except:
        print('An integer is required for the purpose of this test. \nPlease reenter your answer. ')
print('Increment entered as %d. \n'%(increment))

check_boundary = -1
while check_boundary == -1:
    check_boundary = input('Check circle boundary for points with integer coordinates? (Y/N)\n')
    if check_boundary in('yes', 'Yes', 'y', 'Y', 'true', 'True', 't', 'T'):
        check_boundary = 1
    elif check_boundary in('no', 'No', 'n', 'N', 'false', 'False', 'f', 'F'):
        check_boundary = 0
    else:
        check_boundary = -1
        print('Please reenter your answer. \n')

if radius == int(radius):
    radius_considered = int(radius)
else:
    radius_considered = int(radius) + 1

f = open('data.txt', 'w+')
cp = 0
if check_boundary == True:
    for i in range(-radius_considered, radius_considered + 1):
        for j in range(-radius_considered, radius_considered + 1):
            if i ** 2 + j ** 2 <= radius_considered ** 2:
                cp += 1
    f.write(str(cp) + '\t')
    print(cp)

if check_boundary == False:
    for i in range(-radius_considered, radius_considered + 1):
        for j in range(-radius_considered, radius_considered + 1):
            if i ** 2 + j ** 2 < radius_considered ** 2:
                cp += 1
    f.write(str(cp) + '\t')

f.close()
