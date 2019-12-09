class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class AplicacionDeListasEnlazadas:
    def __init__(self):
        self.head = None

    # Se agrega elementos al frente de la lista
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)

    # Agrega un nuevo nodo entre dos nodos existentes
    def add_between(self, posicion, elemento):
        curr = self.head
        count = 1
        nodoPrevio = None
        if elemento > 0:
            while count != posicion:
                nodoPrevio = curr
                curr = curr.next
                count += 1
            if nodoPrevio is None:
                self.head = curr.next
            elif curr:
                nodoPrevio.next = node(data=elemento, next=curr)
        else:
            return False

    # Se agregan elementos al final de la lista enlazada
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    # Evalua la lista en caso de que se encuentra vacia
    def is_empty(self):
        return self.head == None
    # Imprime la lista con los nodos
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end=" => ")
            node = node.next

s = AplicacionDeListasEnlazadas()
s.add_at_front(-3)
s.add_at_end(7)
s.add_at_front(-8)
s.add_between(3, -4)
s.print_list()