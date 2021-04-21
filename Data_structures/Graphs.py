class Graph:
    def __init__(self):
        self._adjacent_list = {}

    def add_vertex(self, node: str) -> bool:
        if not self._adjacent_list.get(node):
            self._adjacent_list[node] = set()
            return True
        return False

    def add_edge(self, node1: str, node2: str) -> bool:
        if not self._adjacent_list.get(node1) is None and not self._adjacent_list.get(node2) is None:
            self._adjacent_list.get(node1).add(node2)
            self._adjacent_list.get(node2).add(node1)
            return True
        return False

    def __len__(self):
        return len(self._adjacent_list.keys())

    def __repr__(self):
        result = ""
        for node, edge in self._adjacent_list.items():
            result += f'{node} --> {sorted(list(edge))}\n'
        return result


if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_vertex('0')
    my_graph.add_vertex('1')
    my_graph.add_vertex('2')
    my_graph.add_vertex('3')
    my_graph.add_vertex('4')
    my_graph.add_vertex('5')
    my_graph.add_vertex('6')
    my_graph.add_edge('3', '1')
    my_graph.add_edge('3', '4')
    my_graph.add_edge('4', '2')
    my_graph.add_edge('4', '5')
    my_graph.add_edge('1', '2')
    my_graph.add_edge('1', '0')
    my_graph.add_edge('0', '2')
    my_graph.add_edge('6', '5')
    print(my_graph)
