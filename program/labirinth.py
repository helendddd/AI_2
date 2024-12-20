#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


def is_valid(x, y, maze, visited):
    """
    Проверяет, является ли клетка допустимой для посещения.
    """
    return (
        0 <= x < len(maze)
        and 0 <= y < len(maze[0])
        and maze[x][y] == 1
        and not visited[x][y]
    )


def bfs(maze, start, end):
    """
    Алгоритм поиска в ширину (BFS) для нахождения кратчайшего пути.
    """
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distance = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque([start])  # Очередь для BFS
    visited[start[0]][start[1]] = True
    distance[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()

        # Если достигли конечной клетки, возвращаем расстояние
        if (x, y) == end:
            return distance[x][y]

        # Проверяем соседей
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, maze, visited):
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    return None  # Если путь не найден


if __name__ == '__main__':

    # Лабиринт (где 0 — стена, 1 — свободный путь)
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    ]

    # Направления движения: вверх, вниз, влево, вправо
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Начальная и конечная позиции
    START = (0, 0)
    END = (6, 6)

    # Находим кратчайший путь
    path_weight = bfs(maze, START, END)

    # Вывод результата
    if path_weight is not None:
        print(f"Вес кратчайшего пути: {path_weight}")
    else:
        print("Путь не найден.")
