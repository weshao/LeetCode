def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)
        print(i)

countdown(5)