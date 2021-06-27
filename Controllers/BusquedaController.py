import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection

db = connection()

class BSTNode:
# Creacion de nodo
    def __init__(self, precio, marca, color):
        self.left = None
        self.right = None
        self.marca = marca
        self.color = color
        self.precio = precio

def insertNode(root, node):
    if root == None:
        root = node
    else:
        if root.precio > node.precio:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        elif root.precio == node.precio:
            if root.left == None:
                root.left = node
            else:
                node.left = root.left
                root.left = node
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

def buildBSTFromArray(list):
    root = None

    for item in list:
        if list.index(item) == 0:
            root = BSTNode(item, "Toyota", "rojo")
        else:
            insertNode(root, BSTNode(item, "Toyota", "rojo"))
    return root

def buildBST(bd):
    root = None
    n = True
    for documento in bd:
        if n:
            root = BSTNode(documento["Precio"], documento["Marca"], documento["Color"])
            n = False
        else:
            insertNode(root, BSTNode(documento["Precio"], documento["Marca"], documento["Color"]))
    return root
    
def inOrderRecursive(nodo, lista):

  if not nodo :
    return
  
  tupla = (str(nodo.marca), str(nodo.color), str(nodo.precio))
  lista.append(tupla)
  #print(str(nodo.precio) + " - "  + str(nodo.marca) + " - "  + str(nodo.color))
  inOrderRecursive(nodo.left, lista)
  inOrderRecursive(nodo.right, lista)
  return lista
  
def find(root, precio):

    currentNode = root

    if currentNode == None:
        return None
    else:
        if precio == currentNode.precio:
            return currentNode
        if precio < currentNode.precio:
            return find(currentNode.left,precio)
        else:
            return find(currentNode.right,precio)

def Mayores(nodo, root, lista):
    if not nodo :
        return
    if nodo.right:
        tupla = (str(nodo.right.marca), str(nodo.right.color), str(nodo.right.precio))
        lista.append(tupla)
        #print(str(nodo.right.precio) + " - "  + str(nodo.right.marca) + " - "  + str(nodo.right.color))
        inOrderRecursive(nodo.right.left, lista)
        inOrderRecursive(nodo.right.right, lista)
        return lista
    else: 
        if root.precio > nodo.precio:
            tupla = (str(root.marca), str(root.color), str(root.precio))
            lista.append(tupla)
        inOrderRecursive(root.right, lista)
        return lista

def Menores(nodo, root, lista):
    if not nodo :
        return
    if nodo.left:
        tupla = (str(nodo.marca), str(nodo.color), str(nodo.precio))
        lista.append(tupla)
        tupla = (str(nodo.left.marca), str(nodo.left.color), str(nodo.left.precio))
        lista.append(tupla)
        '''print(str(nodo.precio) + " - "  + str(nodo.marca) + " - "  + str(nodo.color))
        print(str(nodo.left.precio) + " - "  + str(nodo.left.marca) + " - "  + str(nodo.left.color))'''
        inOrderRecursive(nodo.left.left, lista)
        inOrderRecursive(nodo.left.right, lista)
        return lista
    else: 
        if root.precio < nodo.precio:
            tupla = (str(root.marca), str(root.color), str(root.precio))
            lista.append(tupla)
        #print(root.precio)
        inOrderRecursive(root.left, lista)
        return lista

def ConstruirArbol():
    basedatos = db.Autos.find()
    root = buildBST(basedatos)
    return root

class BusquedaController():

    def __init__(self, principal):
        self.root = ConstruirArbol()
        self.principal = principal
    
    def listProducts(self):
        lista = []
        table = self.principal.table_auto
        table.setRowCount(0)
        products = inOrderRecursive(self.root, lista)
        for row_number, row_data in enumerate(products):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def BuscarMayor(self, precio):
        lista = []
        table = self.principal.table_auto
        table.setRowCount(0)
        nodo = find(self.root, int(precio))
        products = Mayores(nodo, self.root, lista)
        for row_number, row_data in enumerate(products):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def BuscarMenor(self, precio):
        lista = []
        table = self.principal.table_auto
        table.setRowCount(0)
        nodo = find(self.root, int(precio))
        products = Menores(nodo, self.root, lista)
        for row_number, row_data in enumerate(products):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


'''lista = []
root = ConstruirArbol()
lista = inOrderRecursive(root, lista)
print(lista)
Menores(root, root)'''
