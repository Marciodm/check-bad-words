def read_file():
    """Abre o arquivo .txt a ser verificado."""
    with open(r'files\text_file.txt') as file:
        contents = file.read()
    # print(contents)
    check_file(contents)


def check_file(text_check):
    """Abre o arquivo contendo as palavras a serem procuradas"""
    with open(r'files/bad_file.txt') as bad_words:
        contents = bad_words.read()
    contents = contents.split('\n')
    print(contents)
    for name in contents:
        if name in text_check:
            print(text_check.count(name), 'Bad words found.')
            print(name)
        else:
            print('Bad words not found.')


read_file()
