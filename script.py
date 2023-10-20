import json

types = []
position = []
corners1 = []
corners2 = []
scale = []
uuid = []
tracks = []
children = []

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
with open("model.bbmodel", "r") as model_file:
    model_data = json.load(model_file)

# Find and store cubes
elements = model_data.get("elements", [])
for element in elements:
    types.append(element.get("name", ""))
    position.append(element.get("origin", []))
    corners1.append(element.get("from", []))
    corners2.append(element.get("to", []))
    uuid.append(element.get("uuid", ""))

# find and store tracks
outliner = [entry for entry in model_data.get("outliner", []) if isinstance(entry, dict)]
for entry in outliner:
    tracks.append(entry.get("name", ""))
    children.append(entry.get("children", []))

# Calculate scale values for multiple cubes
scale = calculate_multiple_cubes_scales(position, corners1, corners2)

# create the json file

Enviroment = []
for i in range(len(scale)):
    Enviroment.append(
        {
            "geometry": {
                "type": types[i],
                "material": "standard"
            },
            "scale": scale[i],
            "position": position[i],
        }
    )

# dump
new_data = json.dumps(Enviroment, indent=4)
with open("new.json", "w") as file:
    file.write(new_data)
