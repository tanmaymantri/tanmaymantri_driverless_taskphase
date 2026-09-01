n = int(input("Enter number of points: "))

def sort_by_distance(points, reference):
    rx = reference[0]
    ry = reference[1]
    def distance(points):
        x= points[0]
        y= points[1]
        return (x-rx)**2 + (y-ry)**2
    n = len(points)
    for i in range(n):
        smallest = i
        for j in range(i+1, n):
            if distance(points[j])<distance(points[smallest]):
                smallest = j
        temp = points[i]
        points[i] = points[smallest]
        points[smallest] = temp
    return points
points = []
for i in range(n):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    print("\n")
    points.append((x,y))

print("Enter reference point's coordinates: ")
rx = int(input("Enter x coordinate: "))
ry = int(input("Enter y coordinate: "))
reference = (rx, ry)

result = sort_by_distance(points, reference)
print(result)
