#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


def count_islands_bfs(matrix):
    """
    Подсчет количество островов в бинарной матрице
    с учетом диагональных соединений.
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Вверх, вниз, влево, вправо
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Диагонали
    ]

    def bfs(start_x, start_y):
        # Создаем очередь и добавляем начальную точку
        queue = deque([(start_x, start_y)])
        matrix[start_x][start_y] = 0  # Помечаем как посещенную

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Если сосед является частью суши и не посещен
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1:
                    matrix[nx][ny] = 0  # Помечаем как посещенную
                    queue.append((nx, ny))

    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:  # Новый остров найден
                island_count += 1
                bfs(i, j)

    return island_count


if __name__ == '__main__':
    binary_matrix = [
        [1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
    ]
    result = count_islands_bfs(binary_matrix)
    print(f"Количество островов: {result}")
