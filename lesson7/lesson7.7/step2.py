def get_rec_N(N):
    if N > 1:
        get_rec_N(N - 1)
    print(N)


N = int(input())
get_rec_N(N)