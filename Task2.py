"""
2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

# import os
#
# def split_file_path(file_path):
#     """
#     Разделяет абсолютный путь до файла на путь, имя файла и расширение.
#     :param file_path: str, абсолютный путь до файла
#     :return: tuple, содержащий путь, имя файла и расширение
#     """
#     path, full_file_name = os.path.split(file_path)
#     file_name, file_extension = os.path.splitext(full_file_name)
#     return path, file_name, file_extension


def split_file_path(file_path):
    """
    Разделяет абсолютный путь до файла на путь, имя файла и расширение.
    :param file_path: str, абсолютный путь до файла
    :return: tuple, содержащий путь, имя файла и расширение
    """
    parts = file_path.split('/')
    file_name_with_extension = parts[-1]
    path = '/'.join(parts[:-1])
    file_name, file_extension = file_name_with_extension.split('.')
    return path, file_name, '.' + file_extension


file_path = "/home/user/documents/example.txt"
path, name, ext = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", ext)
