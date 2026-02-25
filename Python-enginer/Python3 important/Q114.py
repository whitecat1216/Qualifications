import json
data={"numbers":[1,2,3,7,8]}
with open('data.json','w') as f:
    json.dump(data,f)

with open("data.json","r") as f:
    loaded_data=json.load(f)
    print(loaded_data["numbers"][-1])