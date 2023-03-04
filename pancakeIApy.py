class Node:
    def __init__(self, estado, siguiente=None, movimiento=None):
        self.estado = estado
        self.siguiente = siguiente
        self.movimiento = movimiento

    def __repr__(self):
        return f"<Node {self.estado}>"

def obt_hijo(node):
    children = []
    for i in range(2, len(node.estado) + 1):
        flipped = node.estado[:i][::-1]
        children.append(Node(flipped + node.estado[i:], siguiente=node, movimiento=(i, len(node.estado))))
    return children

def dfs(estado_estado):
    estado_node = Node(estado_estado)
    if estado_estado == sorted(estado_estado):
        return estado_node
    pila = [estado_node]
    visited = {tuple(estado_estado)}
    while pila:
        node = pila.pop()
        for child in obt_hijo(node):
            if child.estado == sorted(estado_estado):
                return child
            if tuple(child.estado) not in visited:
                visited.add(tuple(child.estado))
                pila.append(child)

def print_solution(node):
    moves = []
    estados = []
    while node.siguiente is not None:
        moves.append(node.movimiento)
        estados.append(node.estado)
        node = node.siguiente
    moves.reverse()
    estados.reverse()
    for i in range(len(moves)-1):
        print(f"voltear {moves[i][0]}-{moves[i][1]}: {estados[i+1]}")
    print(estados[-1])

if __name__ == "__main__":
    estado_estado = [5, 3, 1, 4]
    solution_node = dfs(estado_estado)
    print_solution(solution_node)