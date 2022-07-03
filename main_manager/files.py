import os.path
import os
import pickle

def path_exists(path: str) -> bool:
    return os.path.exists(path)

def create_path(path: str):
    os.makedirs(path)


def save(data: dict, with_name: str, on_path: str):

    with open(on_path + with_name + ".txt", "w+", encoding='utf-8') as f:
        pickle.dump(data, f)