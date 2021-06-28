import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
 

db = connection()

print("--------------------------MARCA-------------------------------")
variable21 = []
for nuevo70 in db.Autos.find():
    convertir = nuevo70['Marca']
    sdf = str(convertir)
    variable21.append(sdf)
 #   lista_marcas = (variable21)
 
print(variable21)
#[1]

print("--------------------------_id-------------------------------")
variable22 = []
for nuevo71 in db.Autos.find():
    convertir = nuevo71['_id']
    sdf = str(convertir)
    variable22.append(sdf)

print(variable22)

print("--------------------------Precio-------------------------------")
variable23 = []
for nuevo72 in db.Autos.find():
    convertir = nuevo72['Precio']
    sdf = str(convertir)
    variable23.append(sdf)

print(variable23)

print("----------------------------------------------------------")

# Node of a Single Linked List
class Node(object):

    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None

    # Method for setting the data
    def setData(self, data):
        self.data = data

    # Method for getting the data
    def getData(self):
        return self.data

    # Method for setting the next
    def setNext(self, next):
        self.next = next

    # Method for getting the next
    def getNext(self):
        return self.next

    # return true if thenode point to another node
    def hasNext(self):
        return self.next != None

class QueueLinkedListsCircular(object):

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        self.lastNode = self.rear
        self.rear = Node(data)

        if self.lastNode:
            self.lastNode.setNext(self.rear)

        if self.front is None:
            self.front = self.rear

        self.size +=1

    def deQueue(self):
        if self.front is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        result = self.front.getData()
        self.front = self.front.next
        self.size -=1
        return result;

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        return self.rear.getData()

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            raise IndexError
        return self.front.getData()

    def getSize(self):
        return self.size

    def print( self ):
        node = self.front
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("NULL")


# Execution
que = QueueLinkedListsCircular()
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
for item in variable21:
    print("--------------------------------")
    que.enQueue(item)
    #print("Que    --> " , que.getQue())
    marca_primera =  que.queueFront()
    marca_ultima = que.queueRear()
print(marca_primera)
print(marca_ultima)
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")

print("-------------------------------------------------------------------------------------------------")
que2 = QueueLinkedListsCircular()
for item in variable22:
    print("--------------------------------")
    que2.enQueue(item)
    #print("Que    --> " , que.getQue())

    id_primero =  que2.queueFront()
    id_ultimo = que2.queueRear()
print(id_primero)
print(id_ultimo)

print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
que3 = QueueLinkedListsCircular()
for item3 in variable23:
    print("--------------------------------")
    que3.enQueue(item3)
    #print("Que    --> " , que.getQue())

    precio_primero =  que3.queueFront()
    precio_ultimo = que3.queueRear()
print("-------------------------------------------------------------------------------------------------")
print(precio_primero)
print(precio_ultimo)
print("-------------------------------------------------------------------------------------------------")


