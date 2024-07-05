"""
File: explorer
Author: Antoine Diez-Latteur
Date: 08/05/2024
Description: explores a directory and prints the file tree in the console.
"""

import os
import numpy as np

class Explorer:

    def __init__(self):
        pass

    # def print_file_tree(self, path, indent=0, ignore='.git', depth_max=np.inf , only_dir=False):
    #     try :
    #         for item in os.listdir(path):
    #             if indent >= depth_max:
    #                 pass
    #             else :
    #                 if item.endswith(ignore) or item.startswith('.'):
    #                     pass
    #                 else:
    #                     item_path = os.path.join(path, item)
    #                     if os.path.isdir(item_path):
    #                         print('  ' * indent + '- ' + item)
    #                         self.print_file_tree(item_path, indent + 1, ignore, depth_max, only_dir)
    #                     elif not only_dir:
    #                         print('  ' * indent + '- ' + item)
    #                     elif only_dir:
    #                         pass
    #     except PermissionError as e:
    #         print(f"Error: {e}")

    # def print_file_tree(self, path, indent=0, ignore='.git', depth_max=float('inf'), only_dir=False):
    #     try:
    #         for item in os.listdir(path):
    #             if indent >= depth_max:
    #                 continue
    #             if item.endswith(ignore) or item.startswith('.'):
    #                 continue
    #             item_path = os.path.join(path, item)
    #             if os.path.isdir(item_path):
    #                 if indent == 0:
    #                     print(item)
    #                 else:
    #                     print('│   ' * (indent - 1) + '└── ' + item)
    #                 self.print_file_tree(item_path, indent + 1, ignore, depth_max, only_dir)
    #             elif not only_dir:
    #                 print('│   ' * indent + '├── ' + item)
    #     except PermissionError as e:
    #         print(f"Error: {e}")

    def print_file_tree(self, path, indent='', ignore='.git', depth_max=np.inf, only_dir=False):
        try:
            items = sorted(os.listdir(path))
            for i, item in enumerate(items):
                if indent:
                    if i == len(items) - 1:
                        print(indent[:-1] + '└── ', end='')
                    else:
                        print(indent[:-1] + '├── ', end='')
                else:
                    print('', end='')

                print(item)

                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    if indent:
                        self.print_file_tree(item_path, indent + '│   ', ignore, depth_max, only_dir)
                    else:
                        self.print_file_tree(item_path, '    ', ignore, depth_max, only_dir)
                elif not only_dir:
                    pass
                elif only_dir:
                    pass
        except PermissionError as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    path = 'project/src'

    explorer = Explorer()
    explorer.print_file_tree(path)
