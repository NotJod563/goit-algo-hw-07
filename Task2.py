# Клас вузла дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для вставки нового вузла у дерево
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Функція для пошуку найменшого значення у двійковому дереві пошуку
def find_min_value(root):
    current = root
    # Найменше значення завжди буде у лівому піддереві
    while current.left is not None:
        current = current.left
    return current.val

# Функція для прямого (preorder) обходу дерева
def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Створення дерева
root = None
keys = [20, 8, 22, 4, 12, 10, 14]  # Вставляємо елементи у дерево

for key in keys:
    root = insert(root, key)

# Виведення результатів
print("Прямий обхід дерева:")
preorder_traversal(root)

# Пошук найменшого значення
min_value = find_min_value(root)
print(f"\nНайменше значення у дереві: {min_value}")