#!/bin/python3 
from random import choice
from math import sqrt

#This is a coding interview question:
'''
Given a function that generate random number.
Calculate Pi ?!?!?!?!?!
'''

#create a list of numbers to randomly choose from 
size = 100000
#the "size" is also the radius of a circle,
#and half the length of a side of the square
random_source = list(range(0,size))

#initiate list of all the coordinate in a 2D field
point_list = []

#randomly add points to the point list (2D field)
for i in range(0,size):
    point_list.append([choice(random_source),choice(random_source)])    

incircle = [] #list of all the point that in a circle
for i in point_list:
    #calculate the distance between point i to the origin (0,0) (center of the circle)w
    if sqrt((i[0]**2)+(i[1]**2)) <size:
        incircle.append(i)


#the number of points in the circle IS 
#the area of a quater of the circle
circle_area = len(incircle)*4
print(circle_area/(size**2))

#ratio_circle_to_square = (len(incircle)/len(point_list))
#circle_area = ((size*2)**2)*ratio_circle_to_square