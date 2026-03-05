from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: {data_batch}")

        try:
            count = 0
            total_temp = 0.0

            for record in data_batch:
                if isinstance(record, dict) and "temp" in record:
                    total_temp += record["temp"]
                    count += 1

            if count == 0:
                return "No valid sensor readings"

            avg_temp = total_temp / count

            return f"{count} readings processed, avg temp: {avg_temp}°C"

        except Exception as e:
            return f"Error processing sensor data: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        data = []

        if criteria == "high_temp":
            for d in data_batch:
                if isinstance(d, dict) and "temp" in d:
                    if d["temp"] > 22:
                        data.append(d)

        return data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Sensor data"
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing transaction batch: {data_batch}")

        count = 0
        net_flow = 0

        for transaction in data_batch:
            if isinstance(transaction, dict):
                if transaction.get("type") == "buy":
                    net_flow += transaction.get("amount", 0)
                elif transaction.get("type") == "sell":
                    net_flow -= transaction.get("amount", 0)

                count += 1

        sign = "" if net_flow < 0 else "+"

        return f"{count} operations processed, net flow: {sign}{net_flow} units"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        data = []

        if criteria == "large":
            for d in data_batch:
                if isinstance(d, dict) and "amount" in d:
                    if d["amount"] > 100:
                        data.append(d)

        return data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Transaction data"
        }


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing event batch: {data_batch}")

        total_count = 0
        critical = 0
        warning = 0
        info = 0

        for event in data_batch:
            total_count += 1

            if event == "error":
                critical += 1
            elif event == "warning":
                warning += 1
            else:
                info += 1

        return (
            f"{total_count} events processed | "
            f"Critical: {critical}, Warning: {warning}, Info: {info}"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        data = []

        if criteria == "alerts":
            for d in data_batch:
                if d == "error":
                    data.append(d)

        return data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Event Events"
        }


class StreamProcessor:

    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_streams(self, batches: List[List[Any]], length: int) -> None:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

        i = 0
        while i < length:

            try:
                stream = self.streams[i]
                batch = batches[i]

                stats = stream.get_stats()

                if isinstance(stream, SensorStream):
                    print("Initializing Sensor Stream...")

                elif isinstance(stream, TransactionStream):
                    print("Initializing Transaction Stream...")

                elif isinstance(stream, EventStream):
                    print("Initializing Event Stream...")

                print("Stream ID: " + stats["stream_id"] +
                      ", Type: " + stats["type"])

                result = stream.process_batch(batch)

                print("Analysis: " + result + "\n")

            except Exception as e:
                print(f"Error processing stream: {e}\n")

            i += 1

    def process_polymorphic(self, batches: List[List[Any]], length: int) -> None:

        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch Results:")

        i = 0

        while i < length:

            try:
                stream = self.streams[i]
                batch = batches[i]

                result = stream.process_batch(batch)

                stats = stream.get_stats()

                print("- " + stats["type"] + ": " + result)

            except Exception as e:
                print(f"Error processing stream: {e}")

            i += 1

    def filter_streams(self, batches: List[List[Any]], length: int) -> None:

        print("\nStream filtering active: High-priority data only")

        i = 0

        while i < length:

            try:
                stream = self.streams[i]
                batch = batches[i]

                if isinstance(stream, SensorStream):
                    filtered = stream.filter_data(batch, "high_temp")
                    name = "critical sensor alerts"

                elif isinstance(stream, TransactionStream):
                    filtered = stream.filter_data(batch, "large")
                    name = "large transactions"

                elif isinstance(stream, EventStream):
                    filtered = stream.filter_data(batch, "alerts")
                    name = "critical system events"

                count = 0
                for _ in filtered:
                    count += 1

                print(f"{count}  {name}, ", end="")

            except Exception as e:
                print(f"Error processing stream: {e}")

            i += 1


if __name__ == "__main__":

    streams: List[DataStream] = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001")
    ]

    batches: List[List[Any]] = [
        [{"temp": 22.5}, {"temp": 25.0}, {"temp": 20.0}],
        [
            {"type": "buy", "amount": 100},
            {"type": "sell", "amount": 150},
            {"type": "buy", "amount": 75}
        ],
        ["login", "error", "warning", "logout"]
    ]

    processor = StreamProcessor(streams)

    processor.process_streams(batches, 3)
    processor.process_polymorphic(batches, 3)
    processor.filter_streams(batches, 3)

    print("\nAll streams processed successfully. Nexus throughput optimal.")