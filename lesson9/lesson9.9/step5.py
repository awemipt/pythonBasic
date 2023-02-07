def is_free(lst):
    return  any([any([x =='o' for x in row])for row in lst])