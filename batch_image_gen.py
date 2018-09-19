from random import *
from math import *
from PIL import Image, ImageDraw


def determine_cool_points(lol):
    radius = lol/10

    increment = 100

    scale = 40

    check_boundary = 1

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

    print('\n' + increment * '|')

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

    img.save('data_r=' + str(radius) + '_i=' + str(increment) + '_' + placeholder + '.png')

for i in range(400):
    determine_cool_points(i + 51)
