
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
        bar =bar[0:-9]
        #generating dashes
        dash ='-'*(90-(len(bar)))
        if cur ==0:
            print("processing...")

        p =str(per+bar+dash)
        p.encode("utf-8")
        print(p,end=end)
        
        print(per,bar,dash,end=end)





for i in range(100):
    time.sleep(0.1)
    progressbar(i,100)