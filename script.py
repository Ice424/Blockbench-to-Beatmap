import json

types = []
position = []
corners1 = []
corners2 = []
scale = []
uuid = []
tracks = []
children = []
skip = 0

# this is chat gpt magic


def calculate_cube_scale(position, corner1, corner2):
    # Calculate scale values along x, y, and z axes
    scale_x = abs(corner2[0] - corner1[0])
    scale_y = abs(corner2[1] - corner1[1])
    scale_z = abs(corner2[2] - corner1[2])

    return scale_x, scale_y, scale_z


def calculate_multiple_cubes_scales(position, corners1, corners2):

    # Calculate scale values for each cube
    scales = []
    for i in range(len(position)):
        scale = calculate_cube_scale(position[i], corners1[i], corners2[i])
        scales.append(scale)

    return scales
# end of chatgpt  magic


# Open file
with open("model.bbmodel", "r") as model:
    model = json.load(model)

# Find and store cubes
elements = model["elements"]
for i in elements:
    types.append(i["name"])
    position.append(i["origin"])
    corners1.append(i["from"])
    corners2.append(i["to"])
    uuid.append(i["uuid"])

# find and store tracks
outliner = model["outliner"]
for y in outliner:
    children.append(y["children"])

print(outliner)
print(elements)

print(children)
print(uuid)
# Calculate scale values for multiple cubes
scale = calculate_multiple_cubes_scales(position, corners1, corners2)

Enviroment = []

# create the json file
for x in range(len(scale)):
    Enviroment.append(
        {
            "geometry": {
                "type": types[x],
                "material": "standard"
            },
            "scale": scale[x],
            "position": position[x]
        }
    )

# dump
newData = json.dumps(Enviroment, indent=4)
with open("new.json", "w") as file:
    file.write(newData)
