"""
File: main
Author: antoi
Date: 16/05/2024
Description: Handle the console arguments and call the appropriate command.
"""

import argparse
from src.TreeDiagram import TreeDiagram
from src.ArchitectureDiagram import ArchitectureDiagram
from src.Obsidian import Obsidian
from src.Explorer import Explorer


class Diagram:

    def __init__(self):
        self.args = self.parse_args

    @property
    def parse_args(self):
        parser = argparse.ArgumentParser(add_help=True)

        # Primary arguments
        parser.add_argument('-t', '--type', type=str, choices=['tree', 'architecture'],
                            help='Select the type of diagram (tree or architecture)')
        parser.add_argument('-o', '--open', action='store_true',
                            help='Open obsidian ')
        parser.add_argument('-c', '--clear', action='store_true',
                            help='Clear the diagram directory ')
        parser.add_argument('-g', '--generate',action='store_true',
                            help='Create the diagram directory ')
        parser.add_argument('-e', '--explore', action='store_true',
                            help='Display the file tree in the console ')

        # Secondary arguments
        parser.add_argument('-obs', '--obsidian', type=str, default='C:/path_to_obsidian/obsidian/obsidian.exe',
                            help='Select the obsidian path ')
        parser.add_argument('-p', '--path', type=str, default='project/src',
                            help='Select the path to explore ')
        parser.add_argument('-d', '--diagram', type=str, default='diagram_vault',
                            help='Select the diagram path ')
        parser.add_argument('-i', '--ignore', type=str, default='.klmsnfnmlkjfg',
                            help='Select the ignore extension ')

        return parser.parse_args()

    def main(self):
        if self.args.type == 'tree':
            TreeDiagram(self.args.path,
                        self.args.obsidian,
                        self.args.diagram,
                        self.args.ignore).main()
        elif self.args.type == 'architecture':
            ArchitectureDiagram(self.args.path,
                                self.args.obsidian,
                                self.args.diagram,
                                self.args.ignore).main()

        elif self.args.clear:
            Obsidian(self.args.path,
                     self.args.obsidian,
                     self.args.diagram,
                     self.args.ignore).clear_diagram()
        elif self.args.generate:
            Obsidian(self.args.path,
                     self.args.obsidian,
                     self.args.diagram,
                     self.args.ignore).create_diagram_path()
        elif self.args.open:
            Obsidian(self.args.path,
                     self.args.obsidian,
                     self.args.diagram,
                     self.args.ignore).open_diagram_path()
        elif self.args.explore:
            Explorer().print_file_tree(self.args.path)
        else:
            print('Invalid type')


if __name__ == '__main__':
    Diagram().main()
