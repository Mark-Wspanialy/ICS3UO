#This program finds the area of a triangle
import math
#Import math for square root
print("This program will find the area of a triangle.")
#inform user of the purpose
height_known = input("Do you know the height of the triangle?")
#Checks if the easiest solution is possible
if height_known == "Yes" or height_known == "yes":
    try:
        height = float(input("What is the height of the triangle?"))
        base = float(input("What is the length of the base?"))
        triangle_area = height*base*0.5
        #Solves it easily
    except:
        #Will loop if a letter is added
        print("Both values must be numbers.")
else:
    #The more difficult way (there are more, I only added 2)
    equilateral_triangle = input("Is the triangle equilateral? (all sides the same, all angles 60 degrees)")
    if equilateral_triangle == "yes" or equilateral_triangle == "Yes":
        #if its equilateral one size will give all info
        try:
            side_size = float(input("What is the size of any side?"))
            side_size_2 = side_size/2
            side_size_3 = sqrt((side_size*side_size) + (side_size_2*side_size_2))
            triangle_area = side_size*side_size_3/2
        except:
            print("All values must be numbers")
    else:
        print("This program cannot solve this.")
        triangle_area = 0
if triangle_area > 0:
    #Output data
    print("The final area found is", triangle_area)
