import time
# def whilefun():
#     i=0
#     while(i<5000):
#         i+=1
#         print(i)
# def forfun():
#    for i in range(5000):
#        print(i)
# start_time=time.time()


# whilefun()
# end_time1=time.time()-start_time

# start_time2=time.time()
# forfun()
# end_time2=time.time()-start_time2
# print(end_time1)
# print(end_time2)
# print(10)
# time.sleep(6)
# print("this will print after 6 second")
t=time.localtime()
s=time.strftime("%Y-%M-%D-%H-%M-%S",t)
print(s)
