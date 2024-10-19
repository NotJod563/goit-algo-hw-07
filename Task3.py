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

# Функція для обчислення суми всіх значень у дереві
def calculate_sum(root):
    if root is None:
        return 0
    # Рекурсивно обчислюємо суму значень лівого і правого піддерев та додаємо значення поточного вузла
    return root.val + calculate_sum(root.left) + calculate_sum(root.right)

# Функція для прямого (preorder) обходу дерева
def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Створення дерева
root = None
keys = [15, 10, 20, 8, 12, 16, 25]  # Вставляємо елементи у дерево

for key in keys:
    root = insert(root, key)

# Виведення результатів
print("Прямий обхід дерева:")
preorder_traversal(root)

# Обчислення суми всіх значень
total_sum = calculate_sum(root)
print(f"\nСума всіх значень у дереві: {total_sum}")
