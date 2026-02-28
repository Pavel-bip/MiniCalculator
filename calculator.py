import datetime
import csv
from typing import List, Dict, Union, Tuple, Optional


class CalculatorWithHistory:

    def __init__(self, max_history: int = 100):
        self._history: List[Dict] = []
        self.max_history = max_history

    def _add_record(self, operation: str, args: Tuple, result: float) -> None:

        record = {
            'operation': operation,
            'args': args,
            'result': result,
            'timestamp': datetime.datetime.now().isoformat()
        }
        self._history.append(record)
        if len(self._history) > self.max_history:
            self._history.pop(0)

    def get_history(self) -> List[Dict]:

        return self._history.copy()

    def clear_history(self) -> None:
        self._history.clear()

    def undo_last(self) -> Optional[Dict]:

        if self._history:
            return self._history.pop()
        return None

    def save_history_to_file(self, filename: str) -> None:

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['operation', 'args', 'result', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for record in self._history:
                record_copy = record.copy()
                record_copy['args'] = ', '.join(str(arg) for arg in record['args'])
                writer.writerow(record_copy)


    def add(self, a: float, b: float) -> float:

        result = a + b
        self._add_record('add', (a, b), result)
        return result

    def subtract(self, a: float, b: float) -> float:

        result = a - b
        self._add_record('subtract', (a, b), result)
        return result

    def multiply(self, a: float, b: float) -> float:

        result = a * b
        self._add_record('multiply', (a, b), result)
        return result

    def divide(self, a: float, b: float) -> float:

        if b == 0:
            raise ZeroDivisionError("Деление на ноль не допускается.")
        result = a / b
        self._add_record('divide', (a, b), result)
        return result
