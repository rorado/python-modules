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

        return {"text": data}


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

        return result


class OutputStage:

    def process(self, data: Any) -> Any:

        if not isinstance(data, dict):
            raise TypeError

        if "csv_count" in data:
            return f"CSV processed: {data['csv_count']}"

        if "event_count" in data:
            return f"Stream processed: {data['event_count']}"

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

    def process(self, data: Any):

        try:
            print("JSON pipeline")
            print(data)
            result = self.run_stages(data)
            print(result)
            return result

        except Exception:
            self.record_error()
            raise


class CSVAdapter(ProcessingPipeline):

    def process(self, data: Any):

        try:
            print("CSV pipeline")
            print(data)
            result = self.run_stages(data)
            print(result)
            return result

        except Exception:
            self.record_error()
            raise


class StreamAdapter(ProcessingPipeline):

    def process(self, data: Any):

        try:
            print("Stream pipeline")
            print(data)
            result = self.run_stages(data)
            print(result)
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

        for p in self.pipelines:

            if p.pipeline_id in payloads:

                try:
                    p.process(payloads[p.pipeline_id])

                except Exception as e:
                    print("Pipeline error")
                    print(e)

    def chain(self, pipeline_ids: List[str], data: Any):

        payload = data

        for pid in pipeline_ids:
            payload = self.by_id[pid].process(payload)

        return payload

    def print_stats(self):

        for p in self.pipelines:
            print(p.get_stats())


def main():

    stages = [
        InputStage(),
        TransformStage(),
        OutputStage()
    ]

    json_pipeline = JSONAdapter("json_pipeline", stages)
    csv_pipeline = CSVAdapter("csv_pipeline", stages)
    stream_pipeline = StreamAdapter("stream_pipeline", stages)

    manager = NexusManager()

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    manager.run_all({
        "json_pipeline": {"sensor": "temp", "value": 20},
        "csv_pipeline": "a,b,c",
        "stream_pipeline": "1|2|3|4"
    })

    result = manager.chain(
        ["json_pipeline", "csv_pipeline"],
        "x,y,z"
    )

    print(result)

    manager.print_stats()


if __name__ == "__main__":
    main()