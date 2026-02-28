CalculatorWithHistory
=====================

.. autoclass:: calculator.CalculatorWithHistory
   :members:
   :undoc-members:
   :show-inheritance:

Структура данных истории
------------------------
История хранится в виде списка словарей. Каждый элемент списка содержит:
* **operation** (str) – название выполненной операции;
* **args** (tuple) – кортеж аргументов, переданных в операцию;
* **result** (float) – результат вычисления;
* **timestamp** (str) – время выполнения в формате ISO (YYYY-MM-DDTHH:MM:SS.mmmmmm).

Пример записи истории:
.. code-block:: python

    {
        'operation': 'add',
        'args': (5, 3),
        'result': 8.0,
        'timestamp': '2025-03-01T12:00:00.123456'
    }

Формат сохранения в файл
-------------------------
Метод :meth:`save_history_to_file` сохраняет историю в CSV-файл со следующими полями:

* ``operation`` – название операции;
* ``args`` – аргументы, объединённые в строку через запятую;
* ``result`` – результат;
* ``timestamp`` – временная метка.

Пример содержимого файла ``history.csv``:
.. code-block:: text

    operation,args,result,timestamp
    add,"5, 3",8.0,2025-03-01T12:00:00.123456
    subtract,"10, 4",6.0,2025-03-01T12:00:01.234567

Примеры работы с историей
-------------------------
Ниже показан типичный сценарий использования калькулятора с историей.

.. code-block:: python

    from calculator import CalculatorWithHistory

    # Создаём калькулятор с максимальным размером истории 3
    calc = CalculatorWithHistory(max_history=3)

    # Выполняем несколько операций
    calc.add(5, 3)
    calc.subtract(10, 4)
    calc.multiply(2, 6)

    # Просматриваем всю историю
    history = calc.get_history()
    for entry in history:
        print(f"{entry['timestamp']}: {entry['operation']}{entry['args']} = {entry['result']}")

    # Отменяем последнюю операцию
    last = calc.undo_last()
    print(f"Отменена операция: {last['operation']}")

    # Сохраняем историю в файл
    calc.save_history_to_file('my_history.csv')

    # Очищаем историю
    calc.clear_history()

Вывод программы (примерный):
.. code-block:: text

    2025-03-01T12:00:00.123456: add(5, 3) = 8.0
    2025-03-01T12:00:01.234567: subtract(10, 4) = 6.0
    2025-03-01T12:00:02.345678: multiply(2, 6) = 12.0
    Отменена операция: multiply

Ограничения
-----------
* Максимальный размер истории задаётся параметром ``max_history`` при создании объекта (по умолчанию 100).  
* При превышении лимита самая старая запись автоматически удаляется.  
* История хранится только в оперативной памяти и теряется при завершении программы (если не была сохранена в файл).
