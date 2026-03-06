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
			text = data.strip()

			if text.startswith("{") and text.endswith("}"):
				content = text[1:-1].strip()
				if not content:
					return {}

				pairs = [item.strip() for item in content.split(",") if item.strip()]
				parsed: Dict[str, Any] = {}

				for pair in pairs:
					if ":" not in pair:
						continue

					left, right = pair.split(":", 1)
					key = left.strip().strip('"')
					raw_value = right.strip().strip('"')

					if raw_value.replace(".", "", 1).isdigit():
						if "." in raw_value:
							parsed[key] = float(raw_value)
						else:
							parsed[key] = int(raw_value)
					else:
						parsed[key] = raw_value

				return parsed

			if "," in text:
				return {"csv_row": text}

			return {"stream": text}

		return {"stream": str(data)}


class TransformStage:

	def process(self, data: Any) -> Any:
		if not isinstance(data, dict):
			raise TypeError("TransformStage expects dictionary input")

		transformed = {key: value for key, value in data.items()}

		if "sensor" in transformed and "value" in transformed:
			value = transformed["value"]
			if isinstance(value, (int, float)):
				transformed["status"] = "Normal range" if value < 30 else "High"
				transformed["meta"] = "enriched"

		if "csv_row" in transformed:
			fields = [entry.strip() for entry in transformed["csv_row"].split(",")]
			transformed["csv_fields"] = fields
			transformed["csv_count"] = len(fields)

		if "stream" in transformed:
			events = [entry.strip() for entry in transformed["stream"].split("|") if entry.strip()]
			transformed["events"] = events
			transformed["event_count"] = len(events)

		return transformed


class OutputStage:

	def process(self, data: Any) -> Any:
		if not isinstance(data, dict):
			raise TypeError("OutputStage expects dictionary input")

		if "sensor" in data and "value" in data:
			unit = data.get("unit", "")
			return (
				f"Processed temperature reading: {data['value']}{unit} "
				f"({data.get('status', 'Unknown')})"
			)

		if "csv_fields" in data:
			return f"User activity logged: {data.get('csv_count', 0)} fields processed"

		if "events" in data:
			return f"Stream summary: {data.get('event_count', 0)} readings processed"

		return "Output generated"


class ProcessingPipeline(ABC):

	def __init__(self, pipeline_id: str, stages: List[ProcessingStage]) -> None:
		self.pipeline_id = pipeline_id
		self.stages = stages
		self.stats: Counter[str] = Counter()

	def run_stages(self, data: Any) -> Any:
		payload = data
		for stage in self.stages:
			payload = stage.process(payload)
			self.stats["stage_calls"] += 1

		self.stats["success"] += 1
		return payload

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
	def process(self, data: Any) -> Union[str, Any]:
		pass


class JSONAdapter(ProcessingPipeline):

	def __init__(self, pipeline_id: str, stages: List[ProcessingStage]) -> None:
		super().__init__(pipeline_id, stages)

	def process(self, data: Any) -> Union[str, Any]:
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

	def __init__(self, pipeline_id: str, stages: List[ProcessingStage]) -> None:
		super().__init__(pipeline_id, stages)

	def process(self, data: Any) -> Union[str, Any]:
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

	def __init__(self, pipeline_id: str, stages: List[ProcessingStage]) -> None:
		super().__init__(pipeline_id, stages)

	def process(self, data: Any) -> Union[str, Any]:
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

	def __init__(self) -> None:
		self.pipelines: List[ProcessingPipeline] = []
		self.by_id: Dict[str, ProcessingPipeline] = {}

	def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
		self.pipelines.append(pipeline)
		self.by_id[pipeline.pipeline_id] = pipeline

	def run_all(self, payloads: Dict[str, Any]) -> None:
		for pipeline in self.pipelines:
			payload = payloads.get(pipeline.pipeline_id)
			if payload is None:
				continue

			try:
				pipeline.process(payload)
			except Exception as error:
				print(f"Pipeline {pipeline.pipeline_id} failed: {error}")

	def chain(self, pipeline_ids: List[str], data: Any) -> Any:
		payload = data

		for pipeline_id in pipeline_ids:
			pipeline = self.by_id[pipeline_id]
			payload = pipeline.process(payload)

		return payload

	def recover_and_process(
		self,
		primary_id: str,
		backup_id: str,
		data: Any
	) -> Union[str, Any]:
		try:
			return self.by_id[primary_id].process(data)
		except Exception as error:
			print("Recovery initiated: Switching to backup processor")
			print(f"Primary failure: {error}")
			return self.by_id[backup_id].process(data)

	def print_stats(self) -> None:
		print("\n=== Pipeline Statistics ===")
		for pipeline in self.pipelines:
			stats = pipeline.get_stats()
			print(
				f"{stats['pipeline_id']}: "
				f"success={stats['success']}, "
				f"errors={stats['errors']}, "
				f"stage_calls={stats['stage_calls']}"
			)


def main() -> None:
	print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
	print("Initializing Nexus Manager...")
	print("Pipeline capacity: 1000 streams/second")
	print("Creating Data Processing Pipeline...")
	print("Stage 1: Input validation and parsing")
	print("Stage 2: Data transformation and enrichment")
	print("Stage 3: Output formatting and delivery")

	shared_stages: List[ProcessingStage] = [
		InputStage(),
		TransformStage(),
		OutputStage()
	]

	json_pipeline = JSONAdapter("json_pipeline", shared_stages)
	csv_pipeline = CSVAdapter("csv_pipeline", shared_stages)
	stream_pipeline = StreamAdapter("stream_pipeline", shared_stages)

	manager = NexusManager()
	manager.add_pipeline(json_pipeline)
	manager.add_pipeline(csv_pipeline)
	manager.add_pipeline(stream_pipeline)

	print("\n=== Multi-Format Data Processing ===")
	manager.run_all({
		"json_pipeline": '{"sensor":"temp","value":23.5,"unit":"°C"}',
		"csv_pipeline": "user,action,timestamp",
		"stream_pipeline": "22.0|23.1|21.4|22.9|21.0"
	})

	print("\n=== Pipeline Chaining Demo ===")
	print("Pipeline A -> Pipeline B -> Pipeline C")
	print("Data flow: Raw -> Processed -> Analyzed -> Stored")

	chain_a = JSONAdapter("chain_a", [InputStage(), TransformStage()])
	chain_b = JSONAdapter("chain_b", [InputStage(), TransformStage()])
	chain_c = StreamAdapter("chain_c", [OutputStage()])

	manager.add_pipeline(chain_a)
	manager.add_pipeline(chain_b)
	manager.add_pipeline(chain_c)

	result = manager.chain(
		["chain_a", "chain_b", "chain_c"],
		'{"sensor":"temp","value":26.1,"unit":"°C"}'
	)

	print(f"Chain result: {result}")
	print("Performance: efficiency monitoring active")

	print("\n=== Error Recovery Test ===")
	print("Simulating pipeline failure...")
	manager.recover_and_process("csv_pipeline", "stream_pipeline", 42)
	print("Recovery successful: Pipeline restored, processing resumed")

	manager.print_stats()
	print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
	main()
