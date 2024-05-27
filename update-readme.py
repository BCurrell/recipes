#!/usr/bin/env python3

import re

from pathlib import Path

FILE = "README.md"
HEADER = """# Recipes

There is a rough template to follow for any recipe in `/_template/`:

- `README.md` is the recipe so that Github shows the rendered Markdown as soon as you go to the folder.
- `assets` is for pictures / gifs / videos / etc to help with instructions or to show what the dish looks like. These are supposed to be embedded in the `README.md`, it's just an easy home for them.

"""

def get_recipe_name(path):
	recipe_readme = f"{path}/README.md"
	with open(recipe_readme, "r") as file:
		return re.sub(r'^\#*\s*', "", file.readline()).strip()

def write_section(file, name, path):
	file.write(f"### {name}\n\n")

	path = Path(path)
	if not path.exists():
		return

	recipe_dirs = [x for x in path.iterdir() if x.is_dir()]
	recipe_dirs.sort()

	for recipe in recipe_dirs:
		file.write(f"- [{get_recipe_name(recipe)}](/{recipe}/)\n")

	file.write("\n")

with open(FILE, "w") as file:
	file.write(HEADER)

	write_section(file, "Breakfast", "./breakfast")
	write_section(file, "Lunch", "./lunch")
	write_section(file, "Snack", "./snack")
	write_section(file, "Main Dish", "./main")
	write_section(file, "Side Dish", "./side")
	write_section(file, "Dessert", "./dessert")
	write_section(file, "Misc", "./misc")
