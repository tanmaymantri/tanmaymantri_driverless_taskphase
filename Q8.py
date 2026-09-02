import csv
import math

cones = []
with open("cones.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["x"] = float(row["x"])
        row["y"] = float(row["y"])
        cones.append(row)

def distance_from_origin(cone):
    x = cone["x"]
    y = cone["y"]
    return math.sqrt(x * x + y * y)

cones.sort(key=distance_from_origin)
blue_cones = []
yellow_cones = []
for cone in cones:
    if cone["colour"].lower() == "blue":
        blue_cones.append(cone)
    elif cone["colour"].lower() == "yellow":
        yellow_cones.append(cone)

with open("blue_cones.csv", "w", newline="") as file:
    fieldnames = ["cone id", "x", "y", "colour"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(blue_cones)

with open("yellow_cones.csv", "w", newline="") as file:
    fieldnames = ["cone id", "x", "y", "colour"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(yellow_cones)

centreline = []

for blue in blue_cones:
    nearest_yellow = None
    smallest_distance = float("inf")
    for yellow in yellow_cones:
        dx = blue["x"] - yellow["x"]
        dy = blue["y"] - yellow["y"]
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < smallest_distance:
            smallest_distance = distance
            nearest_yellow = yellow

    midpoint_x = (blue["x"] + nearest_yellow["x"]) / 2
    midpoint_y = (blue["y"] + nearest_yellow["y"]) / 2
    centreline.append({
        "blue_cone_id": blue["cone id"],
        "yellow_cone_id": nearest_yellow["cone id"],
        "midpoint_x": midpoint_x,
        "midpoint_y": midpoint_y
    })

with open("centreline.csv", "w", newline="") as file:
    fieldnames = [
        "blue_cone_id",
        "yellow_cone_id",
        "midpoint_x",
        "midpoint_y"
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(centreline)

print("Files created successfully!")
print("blue_cones.csv")
print("yellow_cones.csv")
print("centreline.csv")