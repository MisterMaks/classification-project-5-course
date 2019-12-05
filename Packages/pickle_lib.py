import pickle
import os


def upload_pickle(data, filename):
    """Сохранение объекта в файл .pickle из директории App"""

    if filename[-7:] != ".pickle":
        filename += ".pickle"
    cur_dir = os.path.split(os.getcwd())[-1]
    if cur_dir == "Packages":
        path = "../App/" + filename
    if cur_dir == "classification-project-5-course":
        path = "App/" + filename
    with open(path, 'wb') as f:
        pickle.dump(data, f)


def download_pickle(filename):
    """Загрузка объекта из файла .pickle из директории App"""

    if filename[-7:] != ".pickle":
        filename += ".pickle"
    cur_dir = os.path.split(os.getcwd())[-1]
    if cur_dir == "Packages":
        path = "../App/" + filename
    if cur_dir == "classification-project-5-course":
        path = "App/" + filename
    with open(path, 'rb') as f:
        data = pickle.load(f)
        return data
