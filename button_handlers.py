def get_regulars() -> list:
    with open('regular.txt', 'r') as regulars:
        reg_exp_list = regulars.read().splitlines()
        regulars.close()
    return reg_exp_list


def get_wrappers() -> list:
    with open('wrappers.txt', 'r') as wrappers:
        wrappers_list = wrappers.read().splitlines()
        wrappers.close()
    return wrappers_list
