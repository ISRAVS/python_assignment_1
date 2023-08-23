import math

def main():
    radius = float(input("Input the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is: {area}")

if __name__ == "__main__":
    main()
