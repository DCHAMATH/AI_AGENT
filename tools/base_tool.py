from abc import ABC, abstractmethod

class BaseTool(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass

    @abstractmethod
    def get_declaration(self):
        """Return Gemini function schema"""
        pass