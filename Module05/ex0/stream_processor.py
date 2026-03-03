from abc import ABC, abstractmethod
from typing import Any, List


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

    def process(self, data: Any) -> str:
        count = 0
        total = 0
        for value in data:
            total += float(value)
            count += 1
        avg = total / count if count > 0 else 0
        return f"Processed {count} numeric values, sum={int(total)}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            for value in data:
                float(value)
        except (ValueError, TypeError):
            return False
        return True


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        char_count = len(data)
        word_count = 0
        inside_word = False
        for char in data:
            if char != " " and not inside_word:
                word_count += 1
                inside_word = True
            elif char == " ":
                inside_word = False
        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        try:
            data.upper()
        except AttributeError:
            return False
        return True


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if "ERROR" in data:
            level = "ALERT"
        elif "INFO" in data:
            level = "INFO"
        else:
            level = "UNKNOWN"
        message = data.split(":", 1)[1].strip() if ":" in data else data
        return f"[{level}] {data.split(':')[0]} level detected: {message}"

    def validate(self, data: Any) -> bool:
        try:
            data.upper()
        except AttributeError:
            return False
        return True


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("\nInitializing Numeric Processor...")
    data1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data1}")
    if numeric.validate(data1):
        print(numeric.format_output(numeric.process(data1)))

    print("\nInitializing Text Processor...")
    data2 = "Hello Nexus World"
    print(f'Processing data: "{data2}"')
    if text.validate(data2):
        print(text.format_output(text.process(data2)))

    print("\nInitializing Log Processor...")
    data3 = "ERROR: Connection timeout"
    print(f'Processing data: "{data3}"')
    if log.validate(data3):
        print(log.format_output(log.process(data3)))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [numeric, text, log]
    demo_data = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    for i, (processor, data) in enumerate(zip(processors, demo_data), start=1):
        if processor.validate(data):
            result = processor.process(data)
            print(f"Result {i}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")