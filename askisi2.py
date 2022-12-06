import heapq

class PriorityQueue :
    
    def __init__(self):
        self.count = 0 
        self.heap = []

    def push(pq , item , priority):
        found = False
        for x in range(pq.count):
            if ( (item,priority) in pq.heap ): 
                found = True        # apofeygw duplicate stoixeiwn
                print("The item ur trying to enter is already in with the same priorirty.")
                
        if (found == False):    # an den yparxei hdh to stoixeio prosthese to 
            heapq.heappush(pq.heap , (item,priority))
            heapq.heapify(pq.heap)
            pq.count += 1
    
    def pop(pq):
        if pq.isEmpty(): # αν η στοιβα ειναι αδεια 
            print("Heap is Empty i Can't Pop.") 
        else: # αν υπαρχει εστω ενα στοιχειο κανε pop
            temp = heapq.heappop(pq.heap)
            pq.count = pq.count -1 
            return temp
    
    
    def isEmpty(pq):
        if (len(pq.heap) == 0 ) :
            return True
        else :
            return False
    
    
        
    def update(pq,item,priority):
        count = 0 # count poses fores allakse ena stoixeio
        for k in range(pq.count):
            it , prio = pq.heap[k]
            if (item == it):
                if (priority < prio) : # an h nea protereotita einai mikroterh sto stoixeio item tote allakse tin se (item,priority)
                    pq.heap[k] = (item,priority)
                    print("I'm Changing tuple (",item,",",prio,") to -> (",item,",",priority,")." )
                    count = count + 1
                    
        # Efoson yparxoyn diplotypa tuples sthn lista afereseta gia na meinei mono mia fora to kathena
        pq.heap = list(set([i for i in pq.heap]))
        
        pq.count = pq.count - count + 1 # ftiakse to pq.count analoga me poses afereseis eginan
            
            
    
def PQSort(list) :
    sorted = []
    q = PriorityQueue()
    
    for x in range(len(list)):
        k1,k2 = list[x]
        q.push(k1,k2)
    
    for x in range(len(list)):
        sorted.append(q.pop())

    return sorted
            



def main():
    
    # DIKH MOY MAIN GIA TON ELEGXO TWN SYNARTHSEWN 
    # H MAIN THS EKFWNISHS EINAI KATW STA SXOLIA
    
    pq = PriorityQueue()
    input = [('k',6), ('k', 10) , ('k' , 6) , ('k' , 2) , ('b' , 13) , ('z' , 4321) , ('z' , 113), ('k' , 311), ('k' , 17), ('z' , 1312)]
    for item , priority in input :
        pq.push(item,priority)
    print (pq.heap )
    print("PQ.Count = " , pq.count)
    print()
    
    
    pq.update('k',1)
    print()
    
    print("Priority Queue After Update = ")
    print (pq.heap)
    print("PQ.Count = " , pq.count)
    
    print()
    print()
    for z in range(0,pq.count):
       pq.pop()
       print (pq.heap)
       print("PQ.Count = " , pq.count)
    

    # q = PriorityQueue()
    # q.push("task1",1)
    # q.push("task1",2)
    # q.push("task0",0)
    # t = q.pop()
    # print(t)
    # t = q.pop()
    # print(t)
    # q.push("task3",3)
    # q.push("task3",4)
    # q.push("task2",0)
    # t = q.pop()
    # print(t)
    
    print()
    unsorted = ((1,1) , (5,5) , (9,9) , (3,3) , (6,6) , (0,0))
    print("Unsorted Array = " , unsorted)
    sorted = PQSort(unsorted)
    print("Sorted Array = " , sorted)
    

    
    
if __name__ == "__main__":
    main()