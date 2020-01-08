#
currentHour, currentMin, currentSec= map(int , input().split())
duration = int(input())

currentTime = currentSec + ( currentMin * 60 ) + ( currentHour * 60 * 60 )

sec = currentTime + duration

hourSecond = (60 * 60)
hour = (sec / hourSecond) % 24
sec = sec % hourSecond
minuteSecond = 60
minute = sec / minuteSecond
sec = sec % minuteSecond

print("%d %d %d" % (hour, minute, sec))

# durationSec = duration % 60
# duration = int(duration / 60)
# durationMin = duration % 60
# duration = int(duration / 60)
# durationHour = duration % 24

