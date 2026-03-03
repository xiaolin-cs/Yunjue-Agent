from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    TODO = "todo"
    DONE = "done"
    FAILED = "failed"

class Task(BaseModel):
    task_id: str
    description: str
    status: TaskStatus
    created_at: datetime
    tools: List[str] = Field(default_factory=list)
    dependencies: List[str] = Field(default_factory=list)

