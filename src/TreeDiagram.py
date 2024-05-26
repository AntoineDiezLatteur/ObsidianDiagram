"""
File: TreeDiagram
Author: Antoine Diez-Latteur
Date: 08/05/2024
Description: Daughter class of Obsidian to generate the tree diagram of a project.
"""

from src.Obsidian import Obsidian
import os
import json
import seaborn as sns


class TreeDiagram(Obsidian):

    def __init__(self, path, obsidian_path, diagram_path, ignore='.klmsnfnmlkjfg'):
        super().__init__(path, obsidian_path, diagram_path, ignore)
        self.lst_path = []

    def generate_node(self, name, local_path):
        name = name.replace("/", "_")
        name = name.replace("\\", "_")
        local_path = local_path.replace("\\", "/")
        local_path = local_path.replace("/", "_")
        with open('{}/{}.md'.format(self.diagram_path, name), 'w') as f:
            f.write('#{}\n'.format(str(local_path).replace("\\", "_")))
            f.write('[[{}]]\n'.format(local_path.replace("/", "_")))
            self.lst_path.append(str(local_path))
        return None

    def generate_diagram(self, path=None):
        if path is None:
            path = self.path
        self.generate_node(path, path)
        for root, dirs, files in os.walk(path):
            # Générer des fichiers de feuilles pour chaque fichier dans le répertoire courant
            for file in files:
                file_name = file  # Nom du fichier sans extension
                file_path = root  # Chemin complet du fichier
                self.generate_node(file_name, file_path)

            # Récursion pour parcourir les sous-répertoires
            for directory in dirs:
                file_name = os.path.join(root, directory)
                subdir_path = root
                self.generate_node(file_name, subdir_path)

    def json_update(self):
        num_colors = len(set(self.lst_path))
        palette = sns.color_palette("hls", n_colors=num_colors)
        hex_concatenated = []
        for i, color in enumerate(palette):
            hex_concatenated.append(int(''.join('{:X}'.format(int(number*255)) for number in palette[i]),16))
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
        # Enregistrer les modifications dans le fichier JSON
        with open('{}/.obsidian/graph.json'.format(self.diagram_path), 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    path = 'sim_sp/SIM_SP_MFR/src'
    tree_path = 'sim_sp_tree'
    obsidian_path = 'C:/Users/antoi/AppData/Local/programs/obsidian/obsidian.exe'

    tree = TreeDiagram(path, obsidian_path, tree_path, ignore='.ads')
    tree.main()