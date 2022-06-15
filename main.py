import random, time

class Tree():

    def __init__(self):
        self.start()

    def start(self):
        try:
            print("Tree drawing program")
            age = int(input("enter age of tree: "))

            kind = random.randrange(2)

            if kind == 1:

                leaf=round((age/3)*2)
                for s in range(0,leaf):
                    print(" "*(leaf-s),"*"*((s*2)+1)," "*(leaf-s))

                body= round(age/3)

                for i in range(body):
                    print(" "*(body*2-1),"||"," "*(body*2-1))

            else:
                leaves1=[]
                leaves2=[]
                leaves3=[]
                leaf=(age//3)*2
                for s in range(leaf,0,-1):
                    leaves2.append(" "*s+"*"*(leaf-s)+ "*"*(leaf-s)+" "*s)

                for s in range(1,leaf):
                    leaves1.append(" "*s+"*"*(leaf-s)+"*"*(leaf-s)+" "*s)

                leaves3 = leaves2+leaves1
                print(*leaves3,sep="\n")

                body=age//3


                for i in range(body):
                    print(" "*(body*2-2),"||"," "*(body*2-1))

        except:
            print("There is an error")

if __name__ == "__main__":
    tree=Tree()

    print("")
    count=20
    while count:
        print("\r Program is closing. Last {} seconds...".format(count),end="")
        count -= 1
        time.sleep(1)