#heuristic=[00,15,24,33,15,18,27,36,24,27,30,39,33,36,39,44]
import math
columns=15                #no of cloumns in the matrix
k=10                    #matrix values are initilised bi this number
h=0                     #iterator for heuristic list
mat=[]                  #matrix holder list
open_list=[]            #nodes to be processed
close=[]                    #node that have been processed
mapping=[]                 #final path map list
class Node:             #data structure for node type
    xPos=0              #x coordinate of a node
    yPos=0              #y coordinate of a node
    f_cost=0               #f_cost of the node
    value=0                 #name of the node in matrix
    parent=None

    def __init__(self,xPos,yPos,f_cost,value):
        self.xPos=xPos
        self.yPos=yPos
        self.f_cost=f_cost
        self.value=value

    def __repr__(self):
        return (str(self.value))

#--------------------------------------------GUI----------------------------------------------------------#
from Tkinter import *
root=Tk()       #Tkinter class object
root.title("A Star")         #title for window
root.geometry("400x500")        #default size
app=Frame(root)    #Frame is widget holder for all other widget and by this line a
                    #  frame is placed into root window
app.grid()
#--------------------------------------------GUI----------------------------------------------------------#

def findchild(n):  #Find all the neighbours
    def findcost(ch):
        xdist = dest.xPos - ch.xPos  # distance in x direction
        ydist = dest.yPos - ch.yPos  # disatnce in y direction
        #mht = abs(xdist) + abs(ydist)  # Manhatten Distance
        mht = math.sqrt(xdist ** 2 + ydist ** 2)
        #print "mhtCost", mht
        return mht

    child = []
    fchild = []
    xpdx = n.xPos + 1
    ypdy = n.yPos + 1
    xndx = n.xPos - 1
    yndy = n.yPos - 1
    if xpdx < columns:
        mat[xpdx][n.yPos].f_cost=findcost(mat[xpdx][n.yPos])+10 #finding the cost of child node and adding 10 to direct child
        child.append(mat[xpdx][n.yPos])
    if ypdy < columns:
        mat[n.xPos][ypdy].f_cost=findcost(mat[n.xPos][ypdy])+10
        child.append(mat[n.xPos][ypdy])
    if xndx >= 0:
        mat[xndx][n.yPos].f_cost=findcost(mat[xndx][n.yPos])+10
        child.append(mat[xndx][n.yPos])
    if yndy >= 0:
        mat[n.xPos][yndy].f_cost=findcost(mat[n.xPos][yndy])+10
        child.append(mat[n.xPos][yndy])
    if (n.xPos - 1 >= 0 and n.yPos - 1 >= 0):
        mat[n.xPos - 1][n.yPos - 1].f_cost=findcost(mat[n.xPos - 1][n.yPos - 1])+14
        child.append(mat[n.xPos - 1][n.yPos - 1])       #finding diagonal child and its cost ,then added 14
    if (n.xPos + 1 < columns and n.yPos + 1 < columns):
        mat[n.xPos + 1][n.yPos + 1].f_cost=findcost(mat[n.xPos + 1][n.yPos + 1])+14
        child.append(mat[n.xPos + 1][n.yPos + 1])
    if (n.xPos - 1 >= 0 and n.yPos + 1 < columns):
        mat[n.xPos - 1][n.yPos + 1].f_cost=findcost(mat[n.xPos - 1][n.yPos + 1])+14
        child.append(mat[n.xPos - 1][n.yPos + 1])
    if (n.xPos + 1 < columns and n.yPos - 1 >= 0):
        mat[n.xPos + 1][n.yPos - 1].f_cost=findcost(mat[n.xPos + 1][n.yPos - 1])+14
        child.append(mat[n.xPos + 1][n.yPos - 1])

    for c in child:
        if (c not in open_list and c not in close):#to prevent duplicate entries only new/non
            # processed node are select as child or neighboures
            fchild.append(c)   #final list of child nodes

    # makes the parent node of each child
    for node in fchild:
        node.parent = n
        #print"---parent,child",node.parent,node.value
    for t in terrain:
        if t in fchild:
            fchild.remove(t)          #makes the terrain node ignorable by removing from child list
    return fchild

#create the matrix
for i in range(0,columns):
    row=[]
    for j in range(0,columns):
        nodes=Node(i,j,None,k)
        row.append(nodes)
        k += 1
        h += 1
    mat.append(row)
    del row

#print matrix
for i in range(0,columns):
    for j in range(0,columns):
        print mat[i][j].value,
    print

source=mat[0][0]            #source node
dest=mat[8][8]              #destionation node
open_list.append(source)       #add source to open list for the first time
#terrain=[mat[5][6],mat[3][6],mat[4][6],mat[7][6],mat[8][6],mat[9][6],mat[10][6],mat[11][6],mat[12][6],mat[2][6],mat[2][5],mat[2][4],mat[2][3],mat[2][2],mat[12][3],mat[12][2],mat[12][4],mat[12][5],mat[12][6],mat[12][7],mat[12][8],mat[12][9],mat[12][10],mat[12][11],mat[12][12],mat[12][13],mat[12][14]]
terrain=[mat[4][0],mat[4][1],mat[4][2],mat[4][3],mat[4][4],mat[4][5],mat[4][6],mat[4][7],mat[4][7],mat[4][8],mat[4][9],mat[4][10],mat[4][11]]
#terrain=[mat[1][4],mat[2][4],mat[3][4],mat[4][4],mat[5][4],mat[6][4],mat[6][4],mat[7][4],mat[8][4],mat[9][4],mat[10][4],mat[11][4]]
#terrain=[mat[4][7],mat[4][8],mat[4][1],mat[5][0],mat[4][0],mat[4][2],mat[4][3],mat[4][4],mat[4][5],mat[4][6],mat[6][5],mat[3][2],mat[6][0],mat[6][1],mat[6][2],mat[6][3],mat[6][4],mat[6][5],mat[6][6],mat[6][7],]             #Non walkable node
while True:        #pathfinding loop
    current=min(open_list,key=lambda node:node.f_cost)      #gets minimum cost node from open list
    open_list.remove(current)                         #remove from open
    if current not in close:                #if it is not in close list then add it
        close.append(current)
    if current==dest:               #if goal node found break
        break
    child=findchild(current)        #generate all the child of current node
    for child in child:
        if child not in open_list:
            open_list.append(child)     #if not in open then add it
    print "open:",open_list
    print "close:",close
mapping.append(dest)        #add destination node in mapping list

def route(dest):
    if dest==source:
        return 1
    else:
        #print dest.parent
        tmp=dest.parent         #set tmp to parent of current node
        mapping.append(tmp)         #append to mapping list
        route(tmp)              #recursive call to get the successive parents


route(dest)
print "Source:",source
print "Destination:",dest
print "Non walkable:",terrain
mapping.reverse()
print mapping
print "Matrix:"
for i in range(0,columns):
    for j in range(0,columns):
        if mat[i][j] in terrain:
            print "# ",
        elif mat[i][j] in mapping:
            print "0 ",
        else:
            print "+ ",
    print


def call():
    print "hello"
for i in range(0,columns):
    for j in range(0,columns):
        if mat[i][j]==source:
            l = Label(bg="BLUE", borderwidth=2)
            l.grid(row="%d" % i, column="%d" % j, sticky=E, padx=2, pady=2, ipadx=7, ipady=0)
        elif mat[i][j]==dest:
            l = Label(bg="RED", borderwidth=2)
            l.grid(row="%d" % i, column="%d" % j, sticky=E, padx=2, pady=2, ipadx=7, ipady=0)
        elif mat[i][j] in terrain:
            l = Label(bg="BLACK", borderwidth=2)
            l.grid(row="%d" % i, column="%d" % j, sticky=E, padx=2, pady=2, ipadx=7, ipady=0)
        elif mat[i][j] in mapping:
            l = Label(bg="GREEN", borderwidth=2)
            l.grid(row="%d" % i, column="%d" % j, sticky=E, padx=2, pady=2, ipadx=7, ipady=0)
        else:
            l = Label(bg="GREY", borderwidth=2,)
            l.grid(row="%d" % i, column="%d" % j, sticky=E, padx=2, pady=2, ipadx=7, ipady=0)
    print
root.mainloop()

del open_list
del close
del child
del terrain

