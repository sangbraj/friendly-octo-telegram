import datetime
new=datetime.datetime.now()
hour=new.hour
if 5<= hour <12:
  greeting = "It's Morning"
elif hour <=15:
   greeting = "It's afternoon"
if 15< hour <=18:
   greeting = "It's eve"
else:
   greeting = "It's night"
print("{}!".format(greeting))
