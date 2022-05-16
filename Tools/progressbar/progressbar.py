
import time



def progressbar(cur,total):
    bar ="▮"
    end="\r"
    one_per = total//100

    if cur==total-1:
        end="\n"
    if cur%one_per==0:
        #generating bar
        bar *=cur//one_per 
        per =str(len(bar)+1)+"%"
        #striping bar
        bar =bar[0:-10]
        #generating dashes
        dash ='-'*(90-(len(bar)))
        print(per,bar,dash,end=end)





for i in range(100):
    time.sleep(0.1)
    progressbar(i,100)