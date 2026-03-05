
from abc import ABC, abstractmethod
from typing import Dict, Any, List

class ProcessingPipeline(ABC):
    @abstractmethod
    def process(self, data: List[Dict[str, Any]]) -> None:
        pass
