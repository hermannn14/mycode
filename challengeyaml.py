import json
import yaml

# open file with json, convert to python object
with open("classdata.json","r") as jsonfile:
    x= json.load(jsonfile)

# create new python dictionary to be added
new= { 
      "name":"Herman",
      "awesome": True,
      "number": 0,
      "favorites":{
          "movie":"Coming To America",
          "ice cream":"espresso",
          "color":"purple"}
     }

# add to data read in from json file
x.append(new)

# open a yaml file and dump the changed data inside it
with open("classdataedit.yml","w") as yamlfile:
    yaml.dump(x, yamlfile)
