import time
import sys
while True:


    print("Hallå mupp!  ")
    time.sleep(1)
    name = input('vad heter du?')
    time.sleep(1)
    print('hej hej! '+name)
    time.sleep(1)
    answer = input('vet du vad jag hört...?')
    if answer == ('nej'):#indenteringen styr kodblocket!!!
        time.sleep(2)
        print('ALLT ÄR FAN SKIT!')
        time.sleep(1)
        print('Nästan iaf!!!')
        sys exit
    elif not answer == ('nej'):
        print('Vi som vet vi vet...')
        time.sleep(2)
        print('Du vet.')
        time.sleep(5)
