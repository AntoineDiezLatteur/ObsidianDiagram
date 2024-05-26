"""
File: Obsidian
Author: Antoine Diez-Latteur
Date: 08/05/2024
Description: Mother class to generate diagrams in Obsidian.
"""

from abc import abstractmethod
import os
import subprocess


class Obsidian:

    def __init__(self, path, obsidian_path, diagram_path, ignore):
        self.path = path
        self.ignore = ignore
        self.diagram_path = diagram_path
        self.lst_path = []
        self.obsidian_path = obsidian_path

    def create_diagram_path(self):
        try:
            os.mkdir(self.diagram_path)
            print(f"Directory '{self.diagram_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{self.diagram_path}' already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def open_diagram_path(self):
        try:
            subprocess.run([self.obsidian_path], check=True)
            print("Obsidian opened successfully.")

        except subprocess.CalledProcessError as e:
            print(f"Failed to open Obsidian vault: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def clear_diagram(self):
        for filename in os.listdir(self.diagram_path) :
            filepath = os.path.join(self.diagram_path, filename)
            try:
                os.remove(filepath)
                print(f"File {filepath} successfully removed.")
            except OSError as e:
                print(f"Error during file {filepath} removal : {e}")


    @abstractmethod
    def generate_node(self, name, path):
        pass

    @abstractmethod
    def generate_diagram(self, path=None):
        pass

    @abstractmethod
    def json_update(self):
        pass

    def main(self):
        self.clear_diagram()
        # self.create_diagram_path()
        self.generate_diagram()
        self.json_update()
        return None

