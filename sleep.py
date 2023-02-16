def alarm(hr,minu):

    if minu < 40:
        hr -= 1
        if hr < 0:
            hr = 23
    minu -= 40
    if minu <0:
        minu += 60
    print("OUTPUT ", hr, " ", minu)

while True:
    h = int(input("Hour> "))
    m = int(input("Minutes> "))
    alarm(h,m)
    print()
