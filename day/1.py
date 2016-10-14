import time
date1=time.strftime('%Y%m%d')
bridate1=time.strftime('%m%d')
year=time.strftime('%Y')
print('今天:',date1)
date2=input('生日许愿人：你的生辰?\n')
bridate2=time.strftime('%m%d',time.strptime(date2,'%Y%m%d'))
briyear=time.strftime('%Y',time.strptime(date2,'%Y%m%d'))
nl=int(year)-int(briyear)
print()
if bridate1==bridate2:
    print('生日许愿人：祝你%d周岁生日快乐!' % nl)
else:
    print('今天不是你生日')