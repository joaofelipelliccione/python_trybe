class Node:
    def __init__(self, value):
        self.value = value  # ๐ฒ Valor a ser armazenado.
        self.next = None  # ๐ Forma de apontar para outro nรณ. Default = None.

    def __str__(self):
        return f"Node(value={self.value}, next={self.next})"
