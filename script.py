import json

Types = []
Origin = []
From = []
To = []

with open("model.bbmodel", "r") as model:
  model = json.load(model)

elements = model["elements"]
for data in elements:
  Types.append(data["name"])
  Origin.append(data["origin"])
  From.append(data["from"])
  To.append(data["to"])

print (Types)
print (Origin)
print (From)
print (To)




newData = json.dumps(elements, indent=4)
with open("new.json", "w") as file:
  file.write(newData)
