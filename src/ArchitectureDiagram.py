"""
File: ArchitectureDiagram
Author: Antoine Diez-Latteur
Date: 08/05/2024
Description: Daughter class of Obsidian to generate the architecture diagram of a project.
"""

from src.Obsidian import Obsidian
import re
import os
import json
import seaborn as sns


class ArchitectureDiagram(Obsidian):

    def __init__(self, path, obsidian_path, diagram_path, ignore='.klmsnfnmlkjfg'):
        super().__init__(path, obsidian_path, diagram_path, ignore)
        self.lst_path = []


    def generate_node(self, name, path):
        item_path = os.path.join(path, name)
        links = self.read_links(item_path)
        with open('{}/{}.md'.format(self.diagram_path,name), 'w') as f:
            f.write('#{}\n'.format(str(path).replace("\\", "_")))
            for link in links:
                f.write('[[{}]]\n'.format(link))

    @staticmethod
    def read_links(filename):
        with open(filename, 'r') as f:
            content = f.readlines()
        imports = set()
        for line in content:
            # Utiliser une expression régulière pour rechercher les lignes commençant par "with"
            if line.startswith('with'):
                match = re.match(r'^with\s+(\w+(\.\w+)*)', line)
                if match:
                    package_name = match.group(1)
                    imports.add(package_name)
        return imports

    def generate_diagram(self, path=None) :
        if path is None:
            path = self.path
        self.lst_path.append(str(path).replace("\\", "_"))
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                if item.endswith('.adb'):
                    self.generate_node(item, path)
                self.generate_diagram(item_path)
            else :
                if not item.endswith(self.ignore):
                    if item.endswith('.adb'):
                        self.generate_node(item, path)

    def json_update(self):
        num_colors = len(set(self.lst_path))
        palette = sns.color_palette("hls", n_colors=num_colors)
        hex_concatenated = []
        for i, color in enumerate(palette):
            hex_concatenated.append(int(''.join('{:X}'.format(int(number * 255)) for number in palette[i]), 16))

        with open('{}/.obsidian/graph.json'.format(self.diagram_path), 'r') as file:
            data = json.load(file)
        data['colorGroups'] = []
        for i in range(len(set(self.lst_path))):
            # Ajouter le nouveau color group à la liste existante
            new_color_group = {
                "query": "tag:#{}".format(list(set(self.lst_path))[i]),
                "color": {
                    "a": 1,
                    "rgb": hex_concatenated[i]
                }
            }
            data['colorGroups'].append(new_color_group)
        with open('{}/.obsidian/graph.json'.format(self.diagram_path), 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    path = 'project/src'
    architecture_path = 'architecutre_vault'
    obsidian_path = 'C:/path_to_obsidian/obsidian/obsidian.exe'

    arch = ArchitectureDiagram(path, obsidian_path, architecture_path, ignore='.ads')
    arch.main()
