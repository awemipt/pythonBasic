def get_data_fig(*args, **kwargs):
    que = ('type', 'color', 'closed', 'width')
    ans = []
    for x in que:
        if x in kwargs:
           ans.append(kwargs[x])
    return (sum(args), *ans)

print(get_data_fig(1,2,color=1,closed=True,width=1,type=False,))