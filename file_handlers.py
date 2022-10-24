import re


def check_values_in_line(line: str, reg_exp: str) -> str | None:
    """
    Проверка, есть ли в строке значение
    если таковое находится, то оно возвращается,
    если такового нет - возвращается None
    """
    domain_scheme = re.compile(r'%s' % reg_exp)
    return re.search(pattern=domain_scheme, string=line)


def check_values_in_file(filepath: str, reg_exp: str) -> list:
    """
    Вызов проверки всего файла функцией проверки значений
    :param reg_exp: переменная регулярного выражения от пользователя
    :param filepath: принимаемый от пользователя путь к проверяемому файлу
    :return: список найденных значений
    """
    values_list = []
    with open(file=filepath, mode='r') as file:
        for line in file:
            value = check_values_in_line(line=line, reg_exp=reg_exp)
            if value is None:
                continue
            values_list.append(value)
        file.close()
    return values_list


def wrap_to_expression(values_list: list, first_expression: str, second_expression: str) -> None:
    """
    Упаковка значений в конструкцию
    :param expression: выражение, принимаемое от пользователя
    :param values_list: принимаемый список значений
    """
    with open("functions.txt", "w") as file:
        for value in values_list:
            file.write(first_expression + value + second_expression)
    file.close()