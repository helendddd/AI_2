from collections import deque


class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state  # состояние узла
        self.parent = parent  # родитель узла
        self.cost = cost  # стоимость пути до узла


class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial  # начальное состояние
        self.goal = goal  # конечное состояние
        self.graph = graph  # граф с соседями для каждого состояния

    def is_goal(self, state):
        return state == self.goal

    def expand(self, node):
        """Возвращает список соседей для текущего узла."""
        neighbors = []
        for neighbor, cost in self.graph[node.state]:
            neighbors.append(Node(neighbor, node, node.cost + cost))
        return neighbors


def breadth_first_search(problem):
    node = Node(problem.initial)

    if problem.is_goal(problem.initial):
        return node

    frontier = deque([node])  # Очередь для хранения узлов
    reached = {problem.initial}  # Множество посещенных узлов

    while frontier:
        node = frontier.popleft()  # Удаление узла из очереди

        # Проходим по соседям узла
        for child in problem.expand(node):
            s = child.state

            # Если цель найдена, возвращаем путь
            if problem.is_goal(s):
                return child

            if s not in reached:
                reached.add(s)
                frontier.append(child)

    return None  # Возвращаем None, если путь не найден


# Восстановление пути до узла
def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # Возвращаем путь в обратном порядке


if __name__ == '__main__':
    graph = {
        'Турин': [('Иврея', 51), ('Новара', 95), ('Милан', 140),
                  ('Асти', 56), ('Кунео', 98)],
        'Иврея': [('Турин', 51), ('Биелла', 25)],
        'Биелла': [('Иврея', 25), ('Верчелли', 43)],
        'Новара': [('Турин', 95), ('Милан', 52),
                   ('Генуя', 151), ('Павия', 42)],
        'Верчелли': [('Биелла', 43), ('Алессандрия', 57)],
        'Варезе': [('Милан', 60), ('Павия', 94)],
        'Милан': [('Турин', 140), ('Новара', 52), ('Варезе', 60),
                  ('Бергамо', 60), ('Брешиа', 91), ('Кремона', 91),
                  ('Пьянценца', 69), ('Генуя', 52), ('Павия', 42)],
        'Бергамо': [('Милан', 60), ('Брешиа', 51)],
        'Брешиа': [('Милан', 91), ('Верона', 73),
                   ('Кремона', 58), ('Бергамо', 51)],
        'Верона': [('Брешиа', 73), ('Модена', 105)],
        'Кремона': [('Брешиа', 58), ('Милан', 96), ('Павия', 77)],
        'Пьяченца': [('Милан', 69), ('Парма', 74), ('Генуя', 144)],
        'Парма': [('Пьяченца', 74), ('Реджо-Эмилия', 28)],
        'Реджо-Эмилия': [('Парма', 28), ('Модена', 25)],
        'Модена': [('Верона', 105), ('Реджо-Эмилия', 25)],
        'Генуя': [('Новара', 151), ('Пьячнца', 144), ('Милан', 161)],
        'Алессандрия': [('Верчелли', 57), ('Асти', 38)],
        'Асти': [('Турин', 56), ('Алессандрия', 38), ('Кунео', 104)],
        'Кунео': [('Турин', 98), ('Асти', 104)],
        'Павия': [('Варезе', 94), ('Милан', 42), ('Кремона', 77)]
    }

    problem = Problem('Кунео', 'Верона', graph)
    result = breadth_first_search(problem)

    if result:
        path = reconstruct_path(result)
        print("Минимальный путь:", path)
        print("Минимальное расстояние:", result.cost)
    else:
        print("Путь не найден")
