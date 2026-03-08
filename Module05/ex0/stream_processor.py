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

        avg = total / count if count > 0 else 0

        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            return all(isinstance(v, (int, float)) for v in data)
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        base = super().format_output(result)
        return f"From numeric process {base}"


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        char_count = len(data)
        word_count = len(data.split())

        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        base = super().format_output(result)
        return f"From text process {base}"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if "ERROR" in data:
            level = "ALERT"
        elif "INFO" in data:
            level = "INFO"
        else:
            level = "UNKNOWN"

        message = data.split(":", 1)[1] if ":" in data else data
        return f"[{level}] level detected:{message}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return f"From log process output: {result}"


def main() -> None:

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    data1 = [1, 2, 3, 4, 5]
    data2 = "Hello Nexus World"
    data3 = "ERROR: Connection timeout"

    print("Initializing Numeric Processor...")
    print(f"Processing data: {data1}")

    if numeric.validate(data1):
        print("Validation: Numeric data verified")
        result = numeric.process(data1)
        print(numeric.format_output(result))
    else:
        print("Validation failed")

    print("\nInitializing Text Processor...")
    print(f'Processing data: "{data2}"')

    if text.validate(data2):
        print("Validation: Text data verified")
        result = text.process(data2)
        print(text.format_output(result))
    else:
        print("Validation failed")

    print("\nInitializing Log Processor...")
    print(f'Processing data: "{data3}"')

    if log.validate(data3):
        print("Validation: Log entry verified")
        result = log.process(data3)
        print(log.format_output(result))
    else:
        print("Validation failed")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [numeric, text, log]
    data_list: List[Any] = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]

    for i, processor in enumerate(processors):
        data = data_list[i]

        if processor.validate(data):
            result = processor.process(data)
            print(f"Result {i+1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
