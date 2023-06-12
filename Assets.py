
import csv
import os
import re
#import pymel.core as pm

import os
import csv

class AssetManager:
    def __init__(self):
        """Initialize the AssetManager object."""
        self.all_data = self.get_all_data()

    def get_all_data(self):
        """Get all asset data from a CSV file and return it as a dictionary.

        Returns:
            dict: A dictionary containing asset data, where the asset name is the key.
        """
        home_directory = os.path.expanduser("~")
        file_path = os.path.join(home_directory, "Documents/Wayland's 2022 Job Search", "techart_test.csv")
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            assets = {}
            for row in reader:
                assets[row['asset_name']] = {
                    "asset_name": row['asset_name'],
                    "asset_type": row['asset_type'],
                    "txt_res": row['texture_resolution'],
                    "vrt_count": row['vertex_count'],
                    "model_file": row['modeling'],
                    "texture_file": row['texture'],
                    "rigging_file": row['rigging']
                }
        return assets


class Asset:
    def __init__(self, asset_name):
        """Initialize the Asset object.

        Args:
            asset_name (str): The name of the asset.
        """
        self.get_asset(asset_name)
        self.asset_name = asset_name
        self.asset_type = self.get_asset_type()
        self.vertex_count = self.get_vertex_count()
        self.texture_resolution = self.get_texture_resolution()
        self.modeling_file = self.get_modeling_file()
        self.texture_file = self.get_texture_file()
        self.rigging_file = self.get_rigging_file()

    @classmethod
    def get_asset(cls, asset_name):
        """Retrieve asset data for the specified asset name.

        Args:
            asset_name (str): The name of the asset.
        """
        home_directory = os.path.expanduser("~")
        file_path = os.path.join(home_directory, "Documents/Wayland's 2022 Job Search", "techart_test.csv")
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['asset_name'] == asset_name:
                    cls.asset_type = row['asset_type']
                    cls.texture_resolution = row['texture_resolution']
                    cls.vertex_count = row['vertex_count']
                    cls.modeling_file = row['modeling']
                    cls.texture_file = row['texture']
                    cls.rigging_file = row['rigging']
                    break

    def get_asset_type(self):
        """Get the asset type.

        Returns:
            str: The asset type.
        """
        return self.asset_type

    def get_texture_resolution(self):
        """Get the texture resolution.

        Returns:
            str: The texture resolution.
        """
        return self.texture_resolution

    def get_vertex_count(self):
        """Get the vertex count.

        Returns:
            str: The vertex count.
        """
        return self.vertex_count

    def get_modeling_file(self):
        """Get the modeling file.

        Returns:
            str: The modeling file path.
        """
        return self.modeling_file

    def get_texture_file(self):
        """Get the texture file.

        Returns:
            str: The texture file path.
        """
        return self.texture_file

    def get_rigging_file(self):
        """Get the rigging file.

        Returns:
            str: The rigging file path.
        """
        return self.rigging_file

    @classmethod
    def load_maya_file(cls, file_path):

        # Check if the file exists
        if not os.path.exists(file_path):
            print("File does not exist:", file_path)
            return

        # Check if the file is a Maya file
        if not file_path.endswith('.ma') and not file_path.endswith('.mb'):
            print("Invalid file format. Only Maya files (.ma, .mb) are supported.")
            return

        try:
            pm.openFile(file_path, force=True)
            print("Maya file loaded:", file_path)
        except Exception as e:
            print("Error loading Maya file:", str(e))


if __name__ == "__main__":

    # all_data = AssetManager()
    # print(all_data.get_all_data())
    
    hero = Asset("Character_01")
    hero_texture_file = hero.get_texture_file()
    print(hero_texture_file)



