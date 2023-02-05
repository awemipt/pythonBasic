d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    for data in d:
        if type(data) == list:
            get_line_list(data,a)
        else:
            a.append(data)
    return a
