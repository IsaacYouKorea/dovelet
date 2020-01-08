#
computer, printer, router = map(int , input().split())

needAmpere = int(((computer * 2.5 + printer * 2.0 + router * 0.5) * 2 + 9) / 10) * 10


print("%d amperes" % needAmpere)
