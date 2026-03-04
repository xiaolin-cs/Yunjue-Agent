from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    TODO = "todo"
    DONE = "done"
    FAILED = "failed"

class Task(BaseModel):
    task_id: str = Field(description="The unique identifier for the task.")
    description: str = Field(description="The description of the task.")
    status: TaskStatus = Field(description="The status of the task.")
    created_at: datetime = Field(description="The timestamp when the task was created.")
    tools: List[str] = Field(default_factory=list, description="The tools used to complete the task.")
    dependencies: List[str] = Field(default_factory=list, description="The dependencies of the task.")

class ClaimStatus(Enum):
    PROPOSED = "proposed"
    VALIDATED = "validated"
    REFUTED = "refuted"

class ClaimType(Enum):
    FACT = "fact"
    THEORY = "theory"
    HYPOTHESIS = "hypothesis"
    METRIC = "metric"
    INTERPRETATION = "interpretation"
    OTHER = "other"

class Source(BaseModel):
    url: str = Field(description="The Utype: SRL of the source.")
    title: str = Field(description="The title of the source.")
    content: str = Field(description="The content of the source.")
    

class Claim(BaseModel):
    claim_id: str = Field(description="The unique identifier for the claim.")
    statement: str = Field(description="The statement of the claim.")
    scope: str = Field(description="The scope of the claim.")
    type: ClaimType = Field(description="The type of the claim.")
    status: ClaimStatus = Field(description="The status of the claim.")
    created_at: datetime = Field(description="The timestamp when the claim was created.")
    sources: List[Source] = Field(default_factory=list, description="The sources of the claim.")