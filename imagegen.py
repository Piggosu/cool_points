from random import *
from math import *
from PIL import Image, ImageDraw

radius = sqrt(float(input('Insert radius of circle for testing. \nLarger radii will exponentially increase processing time. \n')) ** 2)
print('Radius entered as %f. \n'%(radius))

while True:
    try:
        increment = int(input('Insert the number of increments you would like the circle to shift by. \nLarger increments will exponentially increase processing time but will increase data precision. \n'))
        break
    except:
        print('An integer is required for the purpose of this test. \nPlease reenter your answer. ')
print('Increment entered as %d. \n'%(increment))

while True:
    try:
        scale = int(sqrt(int(input('Insert image scaling. Must be integer. ')) ** 2))
        break
    except:
        print('An integer is required. \nPlease reenter your answer. ')
print('Scale entered as %d. \n'%(scale))

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

img = Image.new('RGB', (increment * scale, increment * scale), color = (256, 256, 256))

def determine_cool_points(radius_considered, radius, xpos, ypos):

    cp = 0

    if check_boundary == True:
        for i in range(-radius_considered, radius_considered + 1):
            for j in range(-radius_considered, radius_considered + 1):
                if (i + xpos) ** 2 + (j + ypos) ** 2 <= radius ** 2:
                    cp += 1
        return(cp)

    if check_boundary == False:
        for i in range(-radius_considered, radius_considered + 1):
            for j in range(-radius_considered, radius_considered + 1):
                if (i + xpos) ** 2 + (j + ypos) ** 2 < radius ** 2:
                    cp += 1
        return(cp)

print(increment * '|')

datalist = []

for i in range(increment):
    for j in range(increment):
        datalist.append(determine_cool_points(radius_considered, radius, i / increment, j / increment))

    print('|', end = '')
print('\n')

newlist = [None] * len(datalist)

for i in range(len(datalist)):
    newlist[i] = int((max(datalist) - datalist[i]) / (max(datalist) - min(datalist)) * 256)

draw = ImageDraw.Draw(img)

for i in range(increment):
    for j in range(increment):
        draw.rectangle([(scale * j, scale * i), (scale * j + scale, scale * i + scale)], fill=((newlist[i * increment + j]), (newlist[i * increment + j]), (newlist[i * increment + j])))
    print('|', end = '')

if check_boundary == True:
    placeholder = 'True'
else:
    placeholder = 'False'

print("\n")
for i in range(increment):
    print(datalist[i*increment:(i+1)*increment])

img.show()
img.save('data_r=' + str(radius) + '_i=' + str(increment) + '_' + placeholder + '.png')
