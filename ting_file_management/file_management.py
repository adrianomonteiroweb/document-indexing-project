import sys


def txt_importer(path_file: str):
    if (path_file.endswith(".txt") is False):
        sys.stderr.write('Formato inválido\n')
        return

    try:
        with open(path_file) as file:
            return [f.rstrip() for f in file.readlines()]

    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
