second = int(input())

daySecond = (60 * 60 * 24)
day = second / daySecond
second = second % daySecond
hourSecond = (60 * 60)
hour = second / hourSecond
second = second % hourSecond
minuteSecond = 60
minute = second / minuteSecond
second = second % minuteSecond


print("%d %d %d %d" % (day, hour, minute, second))