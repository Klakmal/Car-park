class Queue(object): #Implementation of Queue
    def __init__(self):
        self.items = []
        self.count = 0
    def isEmpty(self):
        return self.items == []
    def size(self):
        return self.count
    def enqueue(self,item):
        self.items.append(item)
        self.count += 1
    def dequeue(self):
        if self.count == 0:
            print ("Cannot dequeue from an empty queue")
        else:
            val = self.items.pop(0)
            self.count -= 1
            return val
    def peek(self):
        if self.count == 0:
            print ("Cannot peek from an empty queue")
        else:    
            return self.items[0]
        
print ("Enter \"a\" or \"d\" with license plate number to")
print ("indicate a car's arrival or departure")



q=Queue() #create a Queue for garage.
l=[] #create a list for car waiting list.
reg=[] #keep register for license numbers of arrived cars.
tq=Queue()#tempery queue.
while True:
    print ("")
    n =input('Input: ')#get inputs.
    a_d=n[0] #take first index as arrive or depart.
    lsn_n= n[1:] #take other indexes as license number.
    m = 0 #count car movements.
    Car = [lsn_n,m] #create temporary car list
    
    
    
    if a_d=="a": #check whether arrive or departure . 
        if lsn_n in reg: #check if car is already in garage.
            print("Car is alredy in this place")
            
        else:
            if q.size()<=4:  #check if garage is full.
                print("A car with license no "+lsn_n+" has arrived. There is room for the car.")
                q.enqueue(Car)
                reg.append(lsn_n)
            else:
               print("A car with license no "+lsn_n+" has arrived. There is no room for the car.""It enters the waiting line")
               l.insert(0,Car)
               reg.append(lsn_n)
    elif a_d=="d": #check whether arrive or departure .
        if lsn_n not in reg: #check whether the entered license number is not in the garage.
            print("car is not in this place")
        else:
            if [lsn_n,0] in l: #check if the entered license number is in waiting list.
                print ('A car with license number ' + lsn_n + ' has departed from the WAITING LINE')
                l.remove([lsn_n,0])
                reg.remove(lsn_n)
            else:    
                Car1 = q.dequeue()
                 
                while Car1[0] != lsn_n: #find the entered departure license number.
                    
                    tq.enqueue(Car1)
                    Car1 = q.dequeue()

                Car1[1] = Car1[1] + 1  #increase times moved
                
                print ('A car with license number ' + str(Car1[0]) + ' has departed, It was moved ' + str(Car1[1]) + ' time(s).')
                reg.remove(lsn_n)
                while not q.isEmpty():
                    Car1 = q.dequeue()
                    tq.enqueue(Car1)
                    
                
                while not tq.isEmpty():
                    Car2 = tq.dequeue()
                    
                    Car2[1] = Car2[1] + 1 #increase times moved
                    q.enqueue(Car2)
                if not len(l) == 0:# insert the cars into garage from waiting list until waiting list is empty.
                    Car0 = l.pop()
                    print ("There is room for one car in the garage, car "+str(Car0[0])+" is moved in.")
                    q.enqueue(Car0)
            
    else:
        print ('Invalid Input')

