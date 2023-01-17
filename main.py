def remove_duplicates(d_list):
    seen = set() # Множество для проверки словарей на дубликаты
    result = [] # Список, составляющий результат работы функции
    for d in d_list: # Проходим в цикле по списку словарей (O(N))
        check = tuple(d.items()) # Создаем кортеж из элементов словаря для проверки. Сложность метода items() - O(1), Создание кортежа - O(len(d))
        if check in seen: # Сверяем есть ли во множестве "seen" такие же элементы (O(1))
            continue # Продолжаем цикл, игнорируя добавление в результирующий массив
        result.append(d) # Добавляем уникальный словарь в результирующий массив (O(1))
        seen.add(check) # Добавляем элементы уникального словаря во множество для проверки (O(1))

    return result


if __name__ == '__main__':
    input_list = [
        [
            {"key1": "value1"},
            {"k1": "v1", "k2": "v2", "k3": "v3"},
            {},
            {},
            {"key1": "value1"},
            {"key1": "value1"},
            {"key2": "value2"}
        ],
        [
            {},
            {},
            {},
        ],
        [
            {"k1": "v1"},
            {"k1": "value1"},
            {"key3": "val3"}
        ]
    ]
    for dict_list in input_list:
        print(remove_duplicates(dict_list))

