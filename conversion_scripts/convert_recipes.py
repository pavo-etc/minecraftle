import json, os
from pprint import pprint

def process_recipes(path):
    recipe_filenames = [recipe for recipe in os.listdir(path) if recipe.endswith('.json')]
    new_recipes = {}

    for recipe_filename in recipe_filenames:
        print(f"{recipe_filename=}")
        jsonfile = json.load(open(os.path.join(path, recipe_filename)))
        if jsonfile["type"] != "minecraft:crafting_shaped": continue
        
        
        new_recipe = {
            "type": "",
            "group": "",
            "output": "",
            "input": []
        }

        new_recipe["type"] = jsonfile["type"]
        new_recipe["group"] = jsonfile.get("group", "")
        
        new_recipe["output"] = jsonfile["result"]["item"]
        for row in jsonfile["pattern"]:
            new_row = []
            for char in row:
                print(f"{char=}")
                if char == " ":
                    new_row.append(None)
                else:
                    key_item = jsonfile["key"][char]
                    if isinstance(key_item, list):
                        key_item = key_item[0]
                    itemname = key_item.get("item", None)
                    if itemname is None:
                        itemname = key_item.get("tag", None)
                        if "planks" in itemname:
                            itemname = "minecraft:planks"
                        elif "wooden_slabs" in itemname:
                            itemname = "minecraft:oak_slab"
                        elif "logs" in itemname:
                            itemname = "minecraft:oak_log"
                        elif "stone" in itemname:
                            itemname = "minecraft:cobblestone"
                        elif "wool" in itemname:
                            itemname = "minecraft:white_wool"
                        elif "coals" in itemname:
                            itemname = "minecraft:coal"


                    if itemname == "minecraft:oak_planks":
                        itemname = "minecraft:planks"
                    new_row.append(itemname)

            new_recipe["input"].append(new_row)
        
        extless_filename = recipe_filename[:recipe_filename.find(".")]
        new_recipes[extless_filename] = new_recipe
        pprint(new_recipe)
    return new_recipes


def main():
    processed_recipes = process_recipes("./recipes/")
    outputfilename = "./recipes.json"
    with open(outputfilename, "w") as write_file:
        json.dump(processed_recipes, write_file, indent = 4)
    print("Written to", outputfilename)

if __name__ == "__main__":
    main()