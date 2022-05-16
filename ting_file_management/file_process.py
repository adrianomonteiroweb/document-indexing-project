import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue):
    object_file = {}

    object_file["nome_do_arquivo"] = path_file
    object_file["qtd_linhas"] = len(txt_importer(path_file))
    object_file["linhas_do_arquivo"] = txt_importer(path_file)

    print(object_file, file=sys.stdout)

    for file in range(len(instance)):
        if (instance.search(file) == object_file):
            return object_file

    instance.enqueue(object_file)

    return object_file


def remove(instance: Queue):
    if (len(instance) == 0):
        print("Não há elementos", file=sys.stdout)
        return

    file = instance.search(0)["nome_do_arquivo"]

    print(f"Arquivo {file} removido com sucesso", file=sys.stdout)



def file_metadata(instance, position):
    """Aqui irá sua implementação"""
