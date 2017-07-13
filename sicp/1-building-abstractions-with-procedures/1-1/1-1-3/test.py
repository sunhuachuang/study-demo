def add_two_bigger(*args):
    params_list = sorted(list(args))
    return params_list[-1] + params_list[-2]


print(add_two_bigger(1, 2, 3, 4))
