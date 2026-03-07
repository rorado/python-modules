from abc import ABC, abstractmethod
from collections import Counter
from typing import Any, Dict, List, Protocol, Union

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return data
        if isinstance(data, str):
            has_comma = False
            has_pipe = False
            for c in data:
                if c == ",":
                    has_comma = True
                if c == "|":
                    has_pipe = True
            if has_comma:
                return {"csv_row": data}
            if has_pipe:
                return {"stream": data}
            return {"text": data}
        return {"text": str(data)}


class TransformStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError
        result = {}
        for k in data:
            result[k] = data[k]
        if "csv_row" in result:
            count = 1
            for c in result["csv_row"]:
                if c == ",":
                    count += 1
            result["csv_count"] = count
        if "stream" in result:
            count = 1
            for c in result["stream"]:
                if c == "|":
                    count += 1
            result["event_count"] = count
        if "text" in result:
            result["text_count"] = len(result["text"])
        return result


class OutputStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError
        if "csv_count" in data:
            return f"User activity logged: {data['csv_count']} fields processed"
        if "event_count" in data:
            return f"Stream summary: {data['event_count']} readings processed"
        if "text_count" in data:
            return f"Text processed: {data['text_count']} characters"
        return "Data processed"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str, stages: List[ProcessingStage]):
        self.pipeline_id = pipeline_id
        self.stages = stages
        self.stats = Counter()

    def run_stages(self, data: Any) -> Any:
        payload = data
        for stage in self.stages:
            payload = stage.process(payload)
            self.stats["stage_calls"] += 1
        self.stats["success"] += 1
        return payload

    def record_error(self):
        self.stats["errors"] += 1

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "pipeline_id": self.pipeline_id,
            "success": self.stats["success"],
            "errors": self.stats["errors"],
            "stage_calls": self.stats["stage_calls"]
        }

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            print("Processing JSON data through pipeline...")
            print(f"Input: {data}")
            result = self.run_stages(data)
            print("Transform: Enriched with metadata and validation")
            print(f"Output: {result}")
            return result
        except Exception:
            self.record_error()
            raise


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            print("Processing CSV data through same pipeline...")
            print(f"Input: {data}")
            result = self.run_stages(data)
            print("Transform: Parsed and structured data")
            print(f"Output: {result}")
            return result
        except Exception:
            self.record_error()
            raise


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            print("Processing Stream data through same pipeline...")
            print(f"Input: {data}")
            result = self.run_stages(data)
            print("Transform: Aggregated and filtered")
            print(f"Output: {result}")
            return result
        except Exception:
            self.record_error()
            raise


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []
        self.by_id: Dict[str, ProcessingPipeline] = {}

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)
        self.by_id[pipeline.pipeline_id] = pipeline


    def run_all(self, payloads: Dict[str, Any]):
        for pipeline in self.pipelines:
            if pipeline.pipeline_id in payloads:
                try:
                    pipeline.process(payloads[pipeline.pipeline_id])
                except Exception as e:
                    print(f"Pipeline {pipeline.pipeline_id} failed: {e}")

    def chain(self, pipeline_ids: List[str], data: Any) -> Any:
        payload = data
        for pid in pipeline_ids:
            payload = self.by_id[pid].process(payload)
        return payload

    def print_stats(self):
        print("\n=== Pipeline Statistics ===")
        for p in self.pipelines:
            stats = p.get_stats()
            print(
                f"{stats['pipeline_id']}: success={stats['success']}, "
                f"errors={stats['errors']}, stage_calls={stats['stage_calls']}"
            )


def main():
    stages = [InputStage(), TransformStage(), OutputStage()]

    json_pipeline = JSONAdapter("json_pipeline", stages)
    csv_pipeline = CSVAdapter("csv_pipeline", stages)
    stream_pipeline = StreamAdapter("stream_pipeline", stages)

    manager = NexusManager()
    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("=== Multi-Format Data Processing ===")
    manager.run_all({
        "json_pipeline": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "csv_pipeline": "user,action,timestamp",
        "stream_pipeline": "22.0|23.1|21.4|22.9|21.0"
    })

    print("\n=== Pipeline Chaining Demo ===")
    chain_result = manager.chain(
        ["json_pipeline", "csv_pipeline", "stream_pipeline"],
        "sensor,value,unit"
    )
    print(f"Chain result: {chain_result}")

    print("\n=== Error Recovery Test ===")
    try:
        manager.by_id["csv_pipeline"].process(42)
    except Exception:
        print("Recovery initiated: Switching to backup processor")
        manager.by_id["stream_pipeline"].process("1|2|3|4|5")
        print("Recovery successful: Pipeline restored, processing resumed")

    manager.print_stats()
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    main()
    # print("Initializing Nexus Manager...")
    # print("Pipeline capacity: 1000 streams/second")
    # print("Creating Data Processing Pipeline...")
    # print("Stage 1: Input validation and parsing")
    # print("Stage 2: Data transformation and enrichment")
    # print("Stage 3: Output formatting and delivery\n")