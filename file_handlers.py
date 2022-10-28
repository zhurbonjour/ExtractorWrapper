import re


def add_expression_to_collection(filename: str, expression: str):
    """
    Добавление выражения в соответствующий файл коллекции:
    regular.txt или wrappers.txt
    :param filename: имя коллекции (regular.txt/wrappers.txt)
    :param expression: сохраняемое выражение
    """
    with open(filename, 'a') as collection_file:
        collection_file.write(expression + '\n')
        collection_file.close()


def get_expression_from_collection(filename: str) -> list:
    """
    Получение выражений из файла коллекций:
    :param filename: имя коллекции (regular.txt/wrappers.txt)
    :return: список выражений из коллекции
    """
    with open(filename, 'r') as collection_file:
        collection = collection_file.read().splitlines()
        collection_file.close()
    return collection


def check_values_in_file(filepath: str, reg_exp: str) -> list:
    """
    Вызов проверки всего файла функцией проверки значений
    :param reg_exp: переменная регулярного выражения от пользователя
    :param filepath: принимаемый от пользователя путь к проверяемому файлу
    :return: список найденных значений
    """
    values_list = []
    scheme = re.compile(r'%s' % reg_exp)
    with open(file=filepath, mode='r', encoding='utf-8') as file:
        for line in file:
            values = re.findall(scheme, line)
            values_list += values
        file.close()
    return values_list


def wrap_to_expression(values_list: list, expression: str) -> None:
    """
    Упаковка значений в конструкцию
    :param expression: выражение, принимаемое от пользователя
    :param values_list: принимаемый список значений
    """
    with open("functions.txt", "w") as file:
        for value in values_list:
            file.write(expression.replace('VARIABLE', value))
    file.close()


def get_wrapped_output_text() -> str:
    with open('functions.txt', 'r') as file:
        output_text = ''.join(file.readlines())
        file.close()
    return output_text