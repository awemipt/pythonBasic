# put your python code here

d = input().split()
d = [x.split("=") for x in d]
d = [[z,int(x)] for z,x in d]
d = dict(d)

if 'house' in d and 'True' in d and '5' in d:
    print("ДА")
else:
    print("НЕТ")

