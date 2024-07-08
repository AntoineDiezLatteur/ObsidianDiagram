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

    def print_file_tree(self, file_path, indent='', ignore=None, depth_max=np.inf, only_dir=False, start=True):
        try : #handle permission error
            if start : #if it's the first call of the function, print the root directory
                if file_path[-1] == '/' or file_path[-1] == '\\':
                    root = file_path
                else:
                    root = os.path.   basename(file_path)
                print(' └── ' + root)
                start = False
            items = sorted(os.listdir(file_path))
            for i, item in enumerate(items):
                if len(indent)/5 >= depth_max: # handle the max depth of the tree
                    pass
                else:
                    if item.endswith(tuple(ignore)) and ignore != ['']: # handle the ignored extensions
                        pass
                    else:
                        if i == len(items) - 1: # handle the graphical display of the last item of a directory
                            add_to_indent = ' └── '
                            next_indent = indent + '     '
                        else:
                            add_to_indent = ' ├── '
                            next_indent = indent + ' │   '
                        item_path = os.path.join(file_path, item)
                        if os.path.isdir(os.path.join(file_path, item)): # handle the display of directories and only directories representation
                            print('    ' + indent + add_to_indent, item)
                            self.print_file_tree(item_path, next_indent, ignore, depth_max, only_dir, start)
                        elif not only_dir:
                            print('    ' + indent + add_to_indent, item)
                        elif only_dir:
                            pass
        except PermissionError as e:
            print(f"Error: {e}")



if __name__ == '__main__':
    path = 'project/src'

    explorer = Explorer()
    explorer.print_file_tree(path)
