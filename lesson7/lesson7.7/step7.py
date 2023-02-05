def get_path(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return get_path(N - 1) + get_path(N - 2)


print(get_path(7))
