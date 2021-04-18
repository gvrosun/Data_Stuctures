class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if current_node.value > value:
                if not current_node.left:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right

    def lookup(self, value) -> bool:
        if not self.root:
            return False
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return True
            elif current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def delete(self, value):
        if not self.root:
            return
        current_node = self.root
        previous_node = current_node
        while current_node:
            if current_node.value > value:
                previous_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                previous_node = current_node
                current_node = current_node.right
            elif current_node.value == value:
                if current_node.right is None and current_node.left is None:
                    if previous_node.left == current_node:
                        previous_node.left = None
                        return
                    previous_node.right = None
                    return
                # elif current_node.right is None and current_node.left:
                #     if previous_node.left == current_node:
                #         previous_node.left = current_node.left
                #         return
                #     previous_node.right = current_node.left
                #     return
                # elif current_node.right and current_node.left is None:
                #     if previous_node.left == current_node:
                #         previous_node.left = current_node.right
                #         return
                #     previous_node.right = current_node.right
                #     return
                # elif current_node.right and current_node.left:
                #     right_node = current_node.right
                #     if right_node.left is None and right_node.right is None:
                elif current_node.right:
                    next_right_node = current_node.right
                    next_left_node = current_node.left
                    if next_right_node:
                        if previous_node.right == current_node:
                            previous_node.right = next_right_node
                        else:
                            previous_node.left = next_right_node
                        if next_left_node:
                            pass


if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(9)
    binary_tree.insert(4)
    binary_tree.insert(6)
    binary_tree.insert(20)
    binary_tree.insert(170)
    binary_tree.insert(15)
    binary_tree.insert(1)
    binary_tree.delete(1)
    binary_tree.delete(4)
    print(binary_tree.lookup(1))
    print(binary_tree.lookup(4))
    print(binary_tree.lookup(6))
