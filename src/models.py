import time
import uuid
from enum import Enum

from pydantic import BaseModel, Field


class Status(str, Enum):
    pending = 'PENDING'
    started = 'STARTED'
    succeeded = 'SUCCEEDED'
    failed = 'FAILED'
    partially_failed = 'PARTIALLY_FAILED'
    blocked = 'BLOCKED'
    deferred = 'DEFERRED'
    revoked = 'REVOKED'


class GenericEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_name: str = Field(min_length=3, max_length=15, pattern=r'[a-z][a-z0-9_]+[a-z0-9]')
    status: Status
    timestamp: int = Field(default_factory=lambda: int(time.time()))
    data: dict | None
