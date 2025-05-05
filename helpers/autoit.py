import os
import subprocess
from helpers.files import FileUtils


class AutoItUtils:
    SCRIPT_FILE_TEMP = "script_file_load.au3"

    @staticmethod
    def compile_au3_to_exe(au3_path, aut2exe_path):
        new_folder_path = os.path.dirname(au3_path)
        name, _ = os.path.splitext(os.path.basename(au3_path))
        new_file_path = os.path.join(new_folder_path, f"{name}.exe")

        subprocess.run([aut2exe_path, '/in', au3_path, '/out', new_file_path], check=True)
        return new_file_path

    @staticmethod
    def add_file_to_browser(script_path):
        subprocess.call(script_path)

    @classmethod
    def perform_load_autoit_script(cls, load_file_path: str, aut2exe_path, file_name=SCRIPT_FILE_TEMP):
        script_folder_path = FileUtils.get_folder_path("scripts")
        autoit_script_path = os.path.join(script_folder_path, file_name)

        with open(autoit_script_path, "w", encoding="utf-8") as file_script:
            file_script.write('WinWaitActive("Открытие")\n')
            file_script.write(f'Send("{load_file_path}")\n')
            file_script.write('Send("{ENTER}")\n')

        script_exe_path = cls.compile_au3_to_exe(autoit_script_path, aut2exe_path)
        cls.add_file_to_browser(script_exe_path)
