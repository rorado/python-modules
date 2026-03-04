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
            if isinstance(value, (int, float)):
                total += value
                count += 1
            else:
                print(f"Skipping non-numeric value: {value}")
        return f"Processed {count} numeric values, sum={total}"

    def validate(self, data: Any) -> bool:
        try:
            for value in data:
                if not isinstance(value, (int, float)):
                    return False
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        message = super().format_output(result)
        return f"From numeric process {message}"


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not isinstance(data, str):
            print(f"Warning: Non-text data received: {data}")
            return "Invalid data"

        char_count = 0
        word_count = 0
        inside_word = False

        for char in data:
            char_count += 1
            if char != " " and not inside_word:
                word_count += 1
                inside_word = True
            elif char == " ":
                inside_word = False

        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        try:
            return isinstance(data, str)
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        message = super().format_output(result)
        return f"From text process {message}"


class LogProcessor:

    def process(self, data: Any) -> str:
        if "ERROR" in data:
            level = "ALERT"
        elif "INFO" in data:
            level = "INFO"
        else:
            level = "UNKNOWN"

        j = 0
        for i in data:
            if i == ':':
                break
            j += 1
        return f"[{level}] level detected{data[j:]}"

    def validate(self, data: Any) -> bool:
        try:
            return isinstance(data, str)
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"From log process output: {result}"


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("\nInitializing Numeric Processor...")
    data1 = {5}
    print(f"Processing data: {data1}")
    if numeric.validate(data1):
        print(numeric.format_output(numeric.process(data1)))
    else:
        print("Data is not validate")

    print("\nInitializing Text Processor...")
    data2 = "Hello Nexus World"
    print(f'Processing data: "{data2}"')
    if text.validate(data2):
        print(text.format_output(text.process(data2)))
    else:
        print("Data is not validate")

    print("\nInitializing Log Processor...")
    data3 = "ERROR: Connection timeout"
    print(f'Processing data: "{data3}"')
    if log.validate(data3):
        print(log.format_output(log.process(data3)))
    else:
        print("Logs is not validate")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [numeric, text, log]
    demo_data = [
        data1,
        data2,
        data3
    ]

processors = [numeric, text, log]
demo_data = [data1, data2, data3]

i = 0
while i < 3:
    processor = processors[i]
    data = demo_data[i]

    if processor.validate(data):
        result = processor.process(data)
        print(f"Result {i+1}: {result}")
    i += 1

print("\nFoundation systems online. Nexus ready for advanced streams.")
