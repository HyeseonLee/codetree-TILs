import sys

n = int(sys.stdin.readline().strip())

# 날짜, 요일, 날씨정보
# 가장 근 시일내에 비 오늘 날을 찾아요.

class Info:
    def __init__(self, date,day,wea):
        self.date = date
        self.day = day
        self.wea = wea

infos = []
for _ in range(n):
    date, day, wea = sys.stdin.readline().strip().split()
    infos.append(Info(date, day, wea))

sorted_infos = sorted(infos, key=lambda x:x.date)
for item in sorted_infos:
    if item.wea == "Rain":
        print(f"{item.date} {item.day} {item.wea}")
        break