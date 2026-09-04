def turn_row(args):
    n, X, Y, A, B = (int(i) for i in args.split(' '))
    n_list = [i for i in range(1, n + 1)]

    xy_list = n_list[X-1:Y]
    xy_list.reverse()

    s_index_xy = X - 1
    for new_value in xy_list:
        n_list[s_index_xy] = new_value
        s_index_xy += 1

    ab_list = n_list[A-1:B]
    ab_list.reverse()

    s_index_ab = A - 1
    for new_value in ab_list:
        n_list[s_index_ab] = new_value
        s_index_ab += 1


    return n_list


print(*turn_row(input()))
