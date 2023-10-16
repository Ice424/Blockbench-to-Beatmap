import json
with open("model.bbmodel", "r") as model:
  data = json.load(model)
print(data)
newData = json.dumps(data, indent=4)
with open("new.json", "w") as file:
  file.write(newData)
