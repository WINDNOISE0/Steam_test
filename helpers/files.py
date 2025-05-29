import os
import random

class FileUtils:
    @staticmethod
    def get_random_file(path: str) -> str:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        if not files:
            raise FileNotFoundError("No files found in the directory.")
        return os.path.join(path, random.choice(files))

    @staticmethod
    def get_folder_path(folder_name: str) -> str:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(base_dir)
        return os.path.join(project_root, folder_name)
