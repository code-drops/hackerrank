def is_leap(year):
    if year%400==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    return False

year = int(input())
print(is_leap(year))
