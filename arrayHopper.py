#Author: Kai Wang
#contact: kai.wang.magic@gmail.com

import sys

class ArrayHopper:
    a=[]            #store array
    
    #search by breadth-first retrieval
    def hop(self):
        l=[]
        l.append((0, 1, -1))            #push in (arrayIndex, level, treeParentIndex)
        result=[]
        
        pos=0
        while pos < len(l) :
            head= l[pos]
            
            for i in range(1, self.a[head[0]]+1):
                t= (head[0]+i, head[1]+1, pos)
                l.append(t)
                
                if(t[0]>= len(self.a)):
                    #print l
                    item= l[-1]
                    while True:
                        result.insert(0, item[0])
                        if item[2]== -1:
                            break
                        item= l[item[2]]
                    #print 'hop path:'
                    print ', '.join(str(x) for x in result[:-1])+', out'
                    return
            pos= pos +1
        print "failure"
        
    # read array from input file
    def __init__(self, input_path):
        with open(input_path) as f:
            for item in f:
                try:
                    self.a.append(int(item))
                except:
                    print "error when converting string to number!"
        #print 'array is:\n'+' '.join( str(x) for x in self.a)

def main():
    if len(sys.argv)!=2:
        print 'Usage:  arrayHopper [inputfile]'
        sys.exit(1)
    input_path= sys.argv[1]
    hopper= ArrayHopper(input_path)
    hopper.hop()

if __name__ == '__main__':
    main()
