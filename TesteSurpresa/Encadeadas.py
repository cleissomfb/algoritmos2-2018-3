"""Define um no da lista encadeada."""


class No:
    def __init__(self, valor):
        """Inicializa no."""
        self.dado = valor
        self.proximo = None
        self.anterior = None


class Lista:
    """Define lista encadeada."""

    def __init__(self):
        """Inicializa uma nova lista."""
        self.head = None
        self.tail = None
        self.size = 0

    def _executaWhile(self, i):
        while i.proximo is not None:
            anterior = i
            i = i.proximo
            if i.proximo is None:
                valor = i.dado
                anterior.proximo = None
                self.tail = anterior
        return valor

    def append(self, valor):
        """Adiciona um valor ao final da lista."""
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo
        self.size += 1

    def addFirst(self, valor):
        # if self.head is not None:
            real_head = self.head
            self.head = No(valor)
            self.head.proximo = real_head
            self.size += 1

    def removeFirst(self):
        if self.head is not None:
            self.head = self.head.proximo
            self.size -= 1

    def removeLast(self):
        if self.head is not None:
            i = self.head
            anterior = None
            if self.head.proximo is None:
                self.head = self.proximo = None
            else:
                self._executaWhile(i)
            self.size -= 1

    def listSize(self):
        return (self.size)

    def remove(self, x):
        if self.head is not None:
            i = self.head
            anterior = None
            if i.dado == x:
                if i.proximo is None:
                    self.head = None
                else:
                    self.head = i.proximo
            while i.proximo is not None:
                anterior = i
                i = i.proximo
                if i.dado == x:
                    anterior.proximo = i.proximo
                    i = anterior
                    self.size -= 1

    def pop(self):
        if self.head is not None:
            i = self.head
            anterior = None
            valor = None
            if self.head.proximo is None:
                self.head = self.proximo = None
            else:
                valor = self._executaWhile(i)
            self.size -= 1
            return (valor)

    def first(self):
        if self.head is not None:
            return self.head

    def last(self):
        if self.head is not None:
            i = self.head
            while i.proximo is not None:
                i = i.proximo
                if i.proximo is None:
                    return i


x = Lista()
x.append(6)
x.append(2)
x.append(3)
x.append(3)
x.append(4)
x.append(8)
x.remove(3)
x.remove(2)
print("Valor pop:", x.pop())
x.addFirst(4)
x.addFirst(5)
x.removeFirst()
x.removeLast()
print("First:", x.first().dado)
print("Last:", x.last().dado)
print("Size:", x.listSize())
i = x.head
while i is not None:
    print(i.dado)
    i = i.proximo
