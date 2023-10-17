import json

Types = []
Position = []
Corners1 = []
Corners2 = []
Scale = []

# this is chat gpt magic
def calculate_cube_scale(Position, corner1, corner2):
    # Calculate scale values along x, y, and z axes
    scale_x = abs(corner2[0] - corner1[0])
    scale_y = abs(corner2[1] - corner1[1])
    scale_z = abs(corner2[2] - corner1[2])

    return scale_x, scale_y, scale_z
def calculate_multiple_cubes_scales(Position, Corners1, Corners2):

    # Calculate scale values for each cube
    scales = []
    for i in range(len(Position)):
        scale = calculate_cube_scale(Position[i], Corners1[i], Corners2[i])
        scales.append(scale)

    return scales

# Open file
with open("model.bbmodel", "r") as model:
  model = json.load(model)

# Find and store data
elements = model["elements"]
for data in elements:
  Types.append(data["name"])
  Position.append(data["origin"])
  Corners1.append(data["from"])
  Corners2.append(data["to"])


# Calculate scale values for multiple cubes
Scale = calculate_multiple_cubes_scales(Position, Corners1, Corners2)

print(Types)
print(Scale)
print(Position)

Enviroment = []

# create the json file
for x in range(len(Scale)):
  Enviroment.append(
      {
          "geometry": {
          "type": Types[x],
          "material": "standard"
          },
        "scale": Scale[x],
        "position": Position[x]
        }
      )

# dump 
newData = json.dumps(Enviroment, indent=4)
with open("new.json", "w") as file:
  file.write(newData)
