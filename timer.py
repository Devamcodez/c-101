import time
def countdown(seconds):
    while seconds>0:
        min=int(seconds/60)
        sec=int(seconds%60)
        if min<10:
            timer=f'0{min}:{sec}'
        else:
            timer=f'{min}:{sec}'
        if sec<10:
            timer=f'{min}:0{sec}'
        else:
            timer=f'{min}:{sec}'
        print(timer,end='\r')
        time.sleep(1)
        seconds=seconds-1
    print("Time is up!")
seconds=int(input("Enter time in seconds :  "))
countdown(seconds)