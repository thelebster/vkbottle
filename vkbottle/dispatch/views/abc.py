from abc import ABC, abstractmethod
from typing import Any, List

from vkbottle.api.abc import ABCAPI
from vkbottle.dispatch.handlers import ABCHandler
from vkbottle.dispatch.middlewares import BaseMiddleware


class ABCView(ABC):
    handlers: List["ABCHandler"]
    middlewares: List["BaseMiddleware"]

    @abstractmethod
    async def process_event(self, event: dict) -> bool:
        pass

    @abstractmethod
    async def handle_event(self, event: dict, ctx_api: "ABCAPI") -> Any:
        pass

    def register_middleware(self, middleware: "BaseMiddleware"):
        self.middlewares.append(middleware)
