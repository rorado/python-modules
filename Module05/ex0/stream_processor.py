from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"



class NumericProcessor(DataProcessor):
    def process(self, data):

        daatlen = 0
        for i in data:
            daatlen += 1

        dataTotal = 0
        for i in data:
            dataTotal += i

        return f"Sum: {dataTotal}, Count: {daatlen}"


class TextProcessor(DataProcessor):
    def process(self, data):
        return f"Length: {len(data)} characters"

class LogProcessor(DataProcessor):
    pass
