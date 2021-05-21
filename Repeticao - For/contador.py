from time  import sleep

for min in range (9,-1,-1):
    for seg in range (59,-1,-1):
        print (f'{min:02d}:{seg:02d}', end = "\r")
        sleep(0.1)