import json

with open("helmod/recipe.json", "r") as f:
    recipe = json.load(f)

ingredients = recipe["ingredients"]

bp_json = {"blueprint": dict()}
bp = bp_json["blueprint"]

icons = []
for index, p in enumerate(recipe["products"]):
    icon = dict()
    icon["signal"] = dict()
    icon["signal"]["type"] = p["type"]
    icon["signal"]["name"] = p["name"]
    icon["index"] = index
    icons.append(icon)

bp["icons"] = icons

bp["entities"] = []
