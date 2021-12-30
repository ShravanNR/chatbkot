import datetime
def tim():
    no = datetime.datetime.now()#gives current time and date
    h=int(no.hour)
    m=int(no.minute)
    s=int(no.second)
    print(h,':',m,':',s)
