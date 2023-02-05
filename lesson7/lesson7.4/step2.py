def check_password(s, chars="$%!?@#"):
    flag = False
    for ch in chars:
        if ch in s:
            flag = True
            break
    if flag and len(s) >= 8:
        return True
    else:
        return False
    
