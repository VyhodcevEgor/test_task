# Тестовое задание для отправки отклика на вакансию Junior Python Backend Developer в компанию "JetLend"
В данном репозитории содержится код функции, реализующей следующую задачу: **удаление дубликатов из списка словарей на входе.** Функция находится в файле `main.py`
### Обязательное условие: функция не должна иметь сложность `O(n^2)`.

## Моё решение
В своем решении я использовал множества `set`, так как большинство атомарных операций, таких как добавление элементов или проверка на вхождение с помощью оператора in, совершаются за время `O(1)`. Для начала нам необходимо создать множество **"seen"** для хранения уникальных по своему значению словарей, а также результирующий список словарей **"result"**. Затем, в цикле пройтись по списку и достать каждый словарь в отдельности (сложность `O(N)`). Внутри цикла мы создаем кортеж, содержащий элементы словаря, являющегося текущим элементом в цикле(сложность `O(len(d)`). После этого проверяем есть ли словарь с такими элементами во множестве **"seen"** (сложность `O(1)`) - если нет, добавляем данный словарь в список **"result"** (сложность `O(1)`) и во множество **"seen"** (сложность `O(1)`), иначе - продолжаем итерацию цикла с помощью оператора **"continue"**. В конце своего выполнения функция возвращает список **"result"**.

В итоге, сложность моего решения с использованием цикла оценивается как O(N) и связана с длиной списка словарей. Ключевой проблемой являлось получение элементов словаря, так как методы `items()`, `values()`, `keys()` возвращают не сами элементы, а объекты "dict items", "dict keys" и т.п. Для работы с ними с помощью множества их нужно было перенести в другую структуру данных. Я использовал кортежи tuple, так как они занимают меньше памяти, чем списки list. Проблема использования tuple заключается в том, что создание кортежа от какого-либо набора элементов (`tuple(...)`) оценивается как `O(len(...))`, что усложняет алгоритм решения. Более лучшего способа достать элементы из словаря и сравнить их на уникальность мне не представляется возможным. Насколько мне известно, в более старых версиях Python можно было хешировать объекты dict.items() напрямую, это улучшило бы моё решение.

Пример работы функции:
![image](https://user-images.githubusercontent.com/121723410/213022612-84ba9823-2d47-42b9-96df-1bf79c0cd05b.png)
