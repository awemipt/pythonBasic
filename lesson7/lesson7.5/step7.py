def str_min(s1, s2):
    return s1 if s1 < s2 else s2

def str_min3(s1, s2 ,s3):
    return str_min(str_min(s1, s2), s3)

def str_min4(s1, s2, s3, s4):
    return str_min(str_min3(s1, s2, s3), s4)