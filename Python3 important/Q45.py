import json
data={"numbers":[1,2,3,4,5]}
with open("numbers.json", "w") as f:
    json.dump(data, f)
with open("numbers.json", "r") as f:
    loaded_data=json.load(f)
    print(loaded_data["numbers"][-1])