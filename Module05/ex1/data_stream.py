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
        try:
            count = 0
            total_temp = 0.0

            for record in data_batch:
                if isinstance(record, dict) and "temp" in record:
                    total_temp += record["temp"]
                    count += 1

            avg_temp = total_temp / count if count > 0 else 0

            return f"{count} readings processed, avg temp: {avg_temp}°C"

        except Exception as e:
            return f"Error processing sensor data: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        if criteria == "high_temp":
            return [
                r for r in data_batch
                if isinstance(r, dict) and r.get("temp", 0) > 22
            ]

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data"
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
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

        if criteria == "large":
            return [
                t for t in data_batch
                if isinstance(t, dict) and t.get("amount", 0) > 100
            ]

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Financial Data"
        }


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
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
            f"Critical: {critical}, "
            f"Warning: {warning}, "
            f"Info: {info}"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        if criteria == "critical":
            return [e for e in data_batch if e == "error"]

        if criteria == "warning":
            return [e for e in data_batch if e == "warning"]

        if criteria == "info":
            return [e for e in data_batch if e not in ("error", "warning")]

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "System Events"
        }



class StreamProcessor:

    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_streams(self, batches: List[List[Any]], len: int) -> None:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

        i = 0
        while i < len:
            try:
                stream = self.streams[i]
                batch = batches[i]

                if isinstance(stream, SensorStream):
                    print("Initializing Sensor Stream...")
                    stats = stream.get_stats()
                    print("Stream ID: " + stats["stream_id"] + ", Type: " + stats["type"])
                    filtered = stream.filter_data(batch)
                    result = stream.process_batch(filtered)
                    print("Sensor analysis: " + result + "\n")

                elif isinstance(stream, TransactionStream):
                    print("Initializing Transaction Stream...")
                    stats = stream.get_stats()
                    print("Stream ID: " + stats["stream_id"] + ", Type: " + stats["type"])
                    filtered = stream.filter_data(batch)
                    result = stream.process_batch(filtered)
                    print("Transaction analysis: " + result + "\n")

                elif isinstance(stream, EventStream):
                    print("Initializing Event Stream...")
                    stats = stream.get_stats()
                    print("Stream ID: " + stats["stream_id"] + ", Type: " + stats["type"])
                    filtered = stream.filter_data(batch)
                    result = stream.process_batch(filtered)
                    print("Event analysis: " + result + "\n")

            except Exception as e:
                stats = stream.get_stats()
                print(f"Error processing stream {stats.get('stream_id', 'Unknown')}: {e}\n")
            i += 1

    def process_polymorphic(self, batches: List[List[Any]], len: int) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch Results:")

        i = 0
        while i < len:
            try:
                stream = self.streams[i]
                batch = batches[i]

                filtered = stream.filter_data(batch)
                result = stream.process_batch(filtered)
                stats = stream.get_stats()

                print("- " + stats["type"] + ": " + result)
            except Exception as e:
                print(f"Error processing stream {stats.get('stream_id', 'Unknown')}: {e}\n")

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

    print("\nAll streams processed successfully. Nexus throughput optimal.")