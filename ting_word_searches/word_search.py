from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    line = []

    for index, row in enumerate(instance.search(0)["linhas_do_arquivo"]):
        if word.lower() in row.lower():
            line.append({"linha": index + 1})

    if len(line) == 0:
        return []

    return [{
        "palavra": word,
        "arquivo": instance.search(0)["nome_do_arquivo"],
        "ocorrencias": line
    }]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
