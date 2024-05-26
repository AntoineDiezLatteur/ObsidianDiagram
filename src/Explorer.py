"""
File: explorer
Author: Antoine Diez-Latteur
Date: 08/05/2024
Description: explores a directory and prints the file tree in the console.
"""

import os

class Explorer:

    def __init__(self):
        pass

    def print_file_tree(self, path, indent=0, ignore='.sqdfgqfdgqd'):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print('  ' * indent + '- ' + item)
                self.print_file_tree(item_path, indent + 1)
            else:
                if not item.endswith(ignore):
                    print('  ' * indent + '- ' + item)


if __name__ == '__main__':
    path = 'project/src'

    explorer = Explorer()
    explorer.print_file_tree(path)
