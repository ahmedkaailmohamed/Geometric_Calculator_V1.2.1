import perimeter as p
import area as a
import tsa as t
import volume as v
again=True
print("The GEOMETRIC CALCULATOR V1.2.1")
while again:
    while True:
        try:
            choice = int(
                input("What do you want to find? Press 1 for perimeter, 2 for area, 3 for TSA/CSA and 4 for volume: "))
            while choice < 1 or choice > 4:
                print("Please input 1, 2, 3 or 4")
                choice = int(input(
                    "What do you want to find? Press 1 for perimeter, 2 for area, 3 for TSA/CSA and 4 for volume: "))
            break
        except ValueError:
            print("Please input 1, 2, 3 or 4")
    if choice == 1:
        while True:
            try:
                shape = int(input(
                    "What do you want to find the perimeter of? Press 1 for square, 2 for rectangle and 3 for circle: "))
                while shape < 1 or shape > 3:
                    print("Please input 1, 2 or 3")
                    shape = int(input(
                        "What do you want to find the perimeter of? Press 1 for square, 2 for rectangle and 3 for circle: "))
                break
            except ValueError:
                print("Please input 1, 2 or 3")
        if shape == 1:
            length = float(input("Please input the length of the square: "))
            perm = p.perm_square(length)
            print(f"The perimeter of the square is {perm}")
        elif shape == 2:
            length = float(input("Please input the length of the rectangle: "))
            width = float(input("Please input the width of the rectangle: "))
            perm = p.perm_rectangle(length, width)
            print(f"The perimeter of the rectangle is {perm}")
        elif shape == 3:
            radius = float(input("Please input the radius of the circle: "))
            perm = p.perm_circle(radius)
            print(f"The circumference of the circle is {perm}")
        while True:
            answer=input("Do you want to try again? (yes/no): ").lower()
            if answer=="yes":
                again=True
                break
            elif answer=="no":
                again=False
                break
            else:
                print("That is not valid, please input yes or no")
    elif choice == 2:
        while True:
            try:
                shape = int(input("What shape do you want to find the area of?"
                                  "Press 1 for square, 2 for rectangle, 3 for circle,"
                                  "4 for Triangle(With base length and height), 5 "
                                  "for Triangle(With 2 sides and angle in between),"
                                  "6 for parallelogram and 7 for trapezium: "))
                break
            except ValueError:
                print("Please input 1, 2, 3, 4, 5, 6 or 7")
        if shape == 1:
            length = float(input("Please input the length of the square: "))
            print(f"The area of the square is {a.area_square(length)}")
        elif shape == 2:
            length = float(input("Please input the length of the rectangle: "))
            width = float(input("Please input the width of the rectangle: "))
            print(f"The area of the rectangle is {a.area_rectangle(length, width)}")
        elif shape == 3:
            radius = float(input("Please input the radius of the circle: "))
            print(f"The area of the circle is {a.area_circle(radius)}")
        elif shape == 4:
            base = float(input("Please input the base length of the triangle: "))
            height = float(input("Please input the height of the triangle: "))
            print(f"The area of the triangle is {a.area_triangle1(base, height)}")
        elif shape == 5:
            len_a = float(input("Please input length a of the triangle: "))
            len_b = float(input("Please input length b of the triangle: "))
            ang_C = float(input("Please input angle between a and b of the triangle: "))
            print(f"The area of the triangle is {a.area_triangle2(len_a, len_b, ang_C)}")
        elif shape == 6:
            length = float(input("Please input the length of the parallelogram: "))
            height = float(input("Please input the height of the parallelogram: "))
            print(f"The area of the parallelogram is {a.area_parallelogram(length, height)}")
        elif shape == 7:
            len_a = float(input("Please input length a of the trapezium: "))
            len_b = float(input("Please input length b of the trapezium: "))
            height = float(input("Please input the height of the trapezium: "))
            print(f"The area of the trapezium is {a.area_trapezium(len_a, len_b, height)}")
        while True:
            answer=input("Do you want to try again? (yes/no): ").lower()
            if answer=="yes":
                again=True
                break
            elif answer=="no":
                again=False
                break
            else:
                print("That is not valid, please input yes or no")
    elif choice == 3:
        while True:
            try:
                choice2 = int(input("What do you want to find? Press 1 for TSA and 2 for CSA: "))
                while choice2 < 1 or choice2 > 2:
                    print("Please input 1 or 2")
                    choice2 = int(input("What do you want to find? Press 1 for TSA and 2 for CSA: "))
                break
            except ValueError:
                print("Please input 1 or 2: ")
        if choice2 == 1:
            while True:
                try:
                    shape = int(input("What do you want to find the TSA of? Press 1 for cube, "
                                      "2 for cuboid, "
                                      "3 for sphere, "
                                      "4 for hemisphere, "
                                      "5 for cylinder, "
                                      "and 6 for cone: "))
                    while shape < 1 or shape > 6:
                        print("Please input 1, 2, 3, 4, 5 or 6")
                        shape = int(input("What do you want to find the TSA of? Press 1 for cube, "
                                          "2 for cuboid, "
                                          "3 for sphere, "
                                          "4 for hemisphere, "
                                          "5 for cylinder, "
                                          "and 6 for cone: "))
                    break
                except ValueError:
                    print("Please input 1, 2, 3, 4, 5 or 6")
            if shape == 1:
                length = float(input("Please input the length of the cube: "))
                print(f"The TSA of the cube is {t.tsa_cube(length)}")
            elif shape == 2:
                length = float(input("Please input the length of the cuboid: "))
                width = float(input("Please input the width of the cuboid: "))
                height = float(input("Please input the height of the cuboid: "))
                print(f"The TSA of the cuboid is {t.tsa_cuboid(length, width, height)}")
            elif shape == 3:
                radius = float(input("Please input the radius of the sphere: "))
                print(f"The TSA of the sphere is {t.tsa_sphere(radius)}")
            elif shape == 4:
                radius = float(input("Please input the radius of the hemisphere: "))
                print(f"The TSA of the hemisphere is {t.tsa_halfsphere(radius)}")
            elif shape == 5:
                radius = float(input("Please input the radius of the cylinder: "))
                height = float(input("Please input the height of the cylinder: "))
                print(f"The TSA of the cylinder is {t.tsa_cylinder(radius, height)}")
            elif shape == 6:
                radius = float(input("Please input the radius of the cone: "))
                s_height = float(input("Please input the slant height of the cone: "))
                print(f"The TSA of the cone is {t.tsa_cone(radius, s_height)}")
            while True:
                answer = input("Do you want to try again? (yes/no): ").lower()
                if answer == "yes":
                    again = True
                    break
                elif answer == "no":
                    again = False
                    break
                else:
                    print("That is not valid, please input yes or no")
        elif choice2 == 2:
            while True:
                try:
                    shape = int(input("What do you want to find the CSA of? Press"
                                      "1 for Hemisphere, "
                                      "2 for cylinder, "
                                      "and 3 for cone: "))
                    while shape < 1 or shape > 3:
                        print("Please input 1, 2, or 3")
                        shape = int(input("What do you want to find the CSA of? Press"
                                          "1 for Hemisphere, "
                                          "2 for cylinder "
                                          "and 3 for cone: "))
                    break
                except ValueError:
                    print("Please input 1,2 or 3")
            if shape == 1:
                radius = float(input("Please input the radius of the hemisphere: "))
                print(f"The CSA of the hemisphere is {t.csa_halfsphere(radius)}")
            elif shape == 2:
                radius = float(input("Please input the radius of the cylinder: "))
                height = float(input("Please input the height of the cylinder: "))
                print(f"The CSA of the cylinder is {t.csa_cylinder(radius, height)}")
            elif shape == 3:
                radius = float(input("Please input the radius of the cone: "))
                s_height = float(input("Please input the slant height of the cone: "))
                print(f"The CSA of the cone is {t.csa_cone(radius, s_height)}")
            while True:
                answer = input("Do you want to try again? (yes/no): ").lower()
                if answer == "yes":
                    again = True
                    break
                elif answer == "no":
                    again = False
                    break
                else:
                    print("That is not valid, please input yes or no")
    if choice == 4:
        while True:
            try:
                shape = int(input("What do you want to find the volume of? Press"
                                  "1 for Cube, "
                                  "2 for Cuboid, "
                                  "3 for sphere, "
                                  "4 for hemisphere, "
                                  "5 for pyramid, "
                                  "6 for cylinder, "
                                  "and 7 for cone:  "))
                while shape < 1 or shape > 7:
                    print("Please input 1, 2, 3, 4, 5, 6 or 7")
                    shape = int(input("What do you want to find the volume of? Press"
                                      "1 for Cube, "
                                      "2 for Cuboid, "
                                      "3 for sphere, "
                                      "4 for hemisphere, "
                                      "5 for pyramid, "
                                      "6 for cylinder, "
                                      "and 7 for cone:  "))
                break
            except ValueError:
                print("Please input 1, 2, 3, 4, 5, 6 or 7")
        if shape == 1:
            length = float(input("Please input the length of the cube: "))
            print(f"The volume of the cube is {v.vol_cube(length)}")
        elif shape == 2:
            length = float(input("Please input the length of the cuboid: "))
            width = float(input("Please input the width of the cuboid: "))
            height = float(input("Please input the height of the cuboid: "))
            print(f"The volume of the cuboid is {v.vol_cuboid(length, width, height)}")
        elif shape == 3:
            radius = float(input("Please input the radius of the sphere: "))
            print(f"The volume of the sphere is {v.vol_sphere(radius)}")
        elif shape == 4:
            radius = float(input("Please input the radius of the hemisphere: "))
            print(f"The volume of the hemisphere is {v.vol_halfsphere(radius)}")
        elif shape == 5:
            length = float(input("Please input the length of the square base pyramid: "))
            height = float(input("Please input the height of the square base pyramid: "))
            print(f"The volume of the square base pyramid is {v.vol_pyramid(length, height)}")
        elif shape == 6:
            radius = float(input("Please input the radius of the cylinder: "))
            height = float(input("Please input the height of the cylinder: "))
            print(f"The volume of the cylinder is {v.vol_cylinder(radius, height)}")
        elif shape == 7:
            radius = float(input("Please input the radius of the cone: "))
            height = float(input("Please input the height of the cone: "))
            print(f"The volume of the cone is {v.vol_cone(radius, height)}")
        while True:
            answer=input("Do you want to try again? (yes/no): ").lower()
            if answer=="yes":
                again=True
                break
            elif answer=="no":
                again=False
                break
            else:
                print("That is not valid, please input yes or no")
print("Thank you for using the Geometric Calculator V1.2.1. Hope you enjoyed your experience!")


