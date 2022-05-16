import re
from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    line = []

    for content, row in enumerate(instance.search(0)["linhas_do_arquivo"]):
        if word.lower() in row.lower():
            line.append({"linha": content + 1})

    if len(line) == 0:
        return []

    return [{
        "palavra": word,
        "arquivo": instance.search(0)["nome_do_arquivo"],
        "ocorrencias": line
    }]


def search_by_word(word, instance):
    ocurrence, counter = [], 1

    for content in instance.search(0)['linhas_do_arquivo']:
        if re.search(word, content, re.IGNORECASE):
            ocurrence.append({'linha': counter, 'conteudo': content})

        counter += 1

    file = instance.search(0)['nome_do_arquivo']

    message = [{'palavra': word, 'arquivo': file, 'ocorrencias': ocurrence}]

    return [] if len(ocurrence) == 0 else message

# https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
