from typing import Callable, Dict, List

def gen_bin_tree(height: int, root: int, l_b: Callable[[int], int] = lambda x: x * 3, r_b: Callable[[int], int] = lambda x: x - 4) -> Dict[int, List[Dict[int, List]]]:
    """
    Эта функция создает бинарное дерево с заданной высотой и корнем.
    Для каждого узла в дереве вычисляются два потомка: левый и правый, с помощью переданных функций.
    Параметры:
    height (int): Высота дерева (сколько уровней будет в дереве).
    root (int): Значение, которое будет в корне дерева.
    l_b (Callable[[int], int]): Функция для вычисления левого потомка.
    r_b (Callable[[int], int]): Функция для вычисления правого потомка.
    Возвращаемое значение:
    dict: Cловарь
    """
    if height == 0:
        return {root: []}

    left_leaf = gen_bin_tree(height - 1, l_b(root))
    right_leaf = gen_bin_tree(height - 1, r_b(root))

    return {
        root: [left_leaf, right_leaf]
    }
