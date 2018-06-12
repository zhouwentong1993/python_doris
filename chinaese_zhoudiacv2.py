#记录生肖，根据年份来判断生肖
chinese_zodiac='猴鸡狗猪鼠牛虎兔龙蛇马羊'
#print(chinese_zodiac[0:4])
#print(chinese_zodiac[-1])

year=int (input ('请用户输入出生年份'))


print(chinese_zodiac[year%12])


