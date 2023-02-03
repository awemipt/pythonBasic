month, day = map(int, input().split())
months =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
prevDay = day - 1 if day > 1 else months[month-2]
prevMonth = month if day > 1 else month -1
nextDay = day + 1 if day < months[month-1] else 1
nextMonth = month if day < months[month-1] else month+1
print(str(prevMonth).rjust(2,'0')+"."+str(prevDay).rjust(2,'0') +' '+
      str(nextMonth).rjust(2,'0')+'.'+str(nextDay).rjust(2,'0'))