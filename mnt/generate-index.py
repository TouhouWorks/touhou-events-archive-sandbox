import os
import sys
import json

exclude_folder = [".git", ".github", "mnt", ".gitignore", "README.md"]
rootPath = (
    os.environ["WORKSPACE"]
    if "WORKSPACE" in os.environ
    else os.path.dirname(os.path.abspath(__file__))
)


def scan_files():
    files = []
    for dirs in os.listdir(rootPath):
        if dirs in exclude_folder:
            continue
        for root, _, file in os.walk(os.path.join(rootPath, dirs)):
            for f in file:
                relative_path = os.path.relpath(os.path.join(root, f), rootPath)
                files.append(relative_path)
    return files


def read_every_file_to_lists(files):
    file_data = []
    for f in files:
        if f.endswith(".json"):
            with open(f, "r") as fileData:
                eventData = json.load(fileData)
                file_data.append(eventData)
    return file_data


def generate_index():
    files = scan_files()
    file_data = read_every_file_to_lists(files)
    with open(os.path.join(rootPath, "mnt", "indexes.json"), "w") as f:
        json.dump(file_data, f, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    generate_index()
