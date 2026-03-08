
from abc import ABC, abstractmethod
from collections import Counter
from typing import Any, Dict, List, Protocol, Union, Optional


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return data
        if isinstance(data, str):
            has_comma = "," in data
            has_pipe = "|" in data
            if has_comma:
                return {"csv_row": data}
            if has_pipe:
                return {"stream": data}
            return {"text": data}
        raise TypeError("Unsupported data format")


class TransformStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError("Invalid data format")
        result = data.copy()
        if "csv_row" in result:
            result["csv_count"] = result["csv_row"].count(",") + 1
        if "stream" in result:
            numbers = [float(v) for v in result["stream"].split("|")]
            result["event_count"] = len(numbers)
            result["avg"] = sum(numbers) / len(numbers)
        if "text" in result:
            result["text_count"] = len(result["text"])
        if "sensor" in result and "value" in result:
            if result["value"] < 30:
                result["status"] = "Normal range"
            else:
                result["status"] = "High"
        return result


class OutputStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError("Invalid data format")
        if "csv_count" in data:
            return (f"User activity logged: "
                    f"{data['csv_count']} actions processed")
        if "event_count" in data:
            avg = data.get("avg", 0)
            return (f"Stream summary: "
                    f"{data['event_count']} readings, avg: {round(avg,1)}°C")
        if "text_count" in data:
            return f"Text processed: {data['text_count']} characters"
        if "sensor" in data and "value" in data:
            return (
                f"Processed temperature reading: "
                f"{data['value']}{data.get('unit','')} "
                f"({data.get('status','Unknown')})"
            )
        return "Data processed"


class ProcessingPipeline(ABC):
    def __init__(
        self,
        pipeline_id: str,
        stages: Optional[List[ProcessingStage]] = None
    ) -> None:
        self.pipeline_id = pipeline_id
        if stages is None:
            stages = [InputStage(), TransformStage(), OutputStage()]
        self.stages: List[ProcessingStage] = stages
        self.stats: Counter = Counter()

    def run_stages(self, data: Any) -> Any:
        try:
            payload = data
            for stage in self.stages:
                payload = stage.process(payload)
                self.stats["stage_calls"] += 1
            self.stats["success"] += 1
            return payload
        except Exception:
            self.record_error()
            raise

    def record_error(self) -> None:
        self.stats["errors"] += 1

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "pipeline_id": self.pipeline_id,
            "success": self.stats["success"],
            "errors": self.stats["errors"],
            "stage_calls": self.stats["stage_calls"]
        }

    @abstractmethod
    def process(self, data: Any) -> Any:
        ...


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            print("Processing JSON data through pipeline...")
            print(f"Input: {data}")
            result = self.run_stages(data)
            print("Transform: Enriched with metadata and validation")
            print(f"Output: {result}")
            return result
        except Exception as e:
            print(f"Error detected : {e}")
            self.record_error()
            raise


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            print("\nProcessing CSV data through same pipeline...")
            print(f"Input: \"{data}\"")
            result = self.run_stages(data)
            print("Transform: Parsed and structured data")
            print(f"Output: {result}")
            return result
        except Exception as e:
            print(f"Error detected : {e}")
            self.record_error()
            raise


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            print("\nProcessing Stream data through same pipeline...")
            print(f"Input: \"{data}\"")
            result = self.run_stages(data)
            print("Transform: Aggregated and filtered")
            print(f"Output: {result}")
            return result
        except Exception as e:
            print(f"Error detected : {e}")
            self.record_error()
            raise


class NexusManager:
    def __init__(self) -> None:
        print("\nInitializing Nexus Manager...")
        self.pipelines: List[ProcessingPipeline] = []
        self.by_id: Dict[str, ProcessingPipeline] = {}

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)
        self.by_id[pipeline.pipeline_id] = pipeline

    def run_all(self, payloads: Dict[str, Any]) -> None:
        print("\n=== Multi-Format Data Processing ===")
        for p in self.pipelines:
            if p.pipeline_id in payloads:
                try:
                    p.process(payloads[p.pipeline_id])
                except Exception as e:
                    print(f"Pipeline {p.pipeline_id} failed: {e}")
            print(f"Pipeline {p.pipeline_id} stats: {p.get_stats()}")

    def chain(self, pipeline_ids: List[str], data: Any) -> str:
        print("\n=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")
        payload = data
        for pid in pipeline_ids:
            payload = self.by_id[pid].process(payload)
        return "Final output after chaining: " + str(payload)

    def error_recovery(self) -> None:
        print("\n=== Error Recovery Test ===")
        print("Simulating pipeline failure...")
        try:
            self.by_id["csv_pipeline"].process(1337)
        except Exception:
            print("Recovery initiated: Switching to backup processor")

    def print_stats(self) -> None:
        print("\nNexus Integration complete. All systems operational.")


def main() -> None:
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    stages = [InputStage(), TransformStage(), OutputStage()]

    json_pipeline = JSONAdapter("json_pipeline", stages)
    csv_pipeline = CSVAdapter("csv_pipeline", stages)
    stream_pipeline = StreamAdapter("stream_pipeline", stages)

    manager = NexusManager()
    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    manager.run_all({
        "json_pipeline": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "csv_pipeline": "user,action,timestamp",
        "stream_pipeline": "22.0|23.1|21.4|22.9|21.0"
    })

    chain_result = manager.chain(
        ["json_pipeline", "csv_pipeline", "stream_pipeline"],
        "sensor,value,unit"
    )
    print(f"\nChain result: {chain_result}")

    manager.error_recovery()
    manager.print_stats()


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    main()
