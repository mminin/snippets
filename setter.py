#This snippet shows how to make a setter function in an object of a void class (useful for working in QT)

class Q():pass
q=Q()
q.myQ=0
def setMyQ(myWindow, val):
    myWindow.myQ=val
q.setMyQ=lambda val: setMyQ(q, val)
print (q.myQ)
q.setMyQ(5)
print (q.myQ)
