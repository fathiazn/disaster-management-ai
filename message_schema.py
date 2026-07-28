from dataclasses import dataclass
from typing import Dict


@dataclass
class AgentMessage:
    sender: str
    receiver: str
    task: str
    data: Dict
    status: str = "success"