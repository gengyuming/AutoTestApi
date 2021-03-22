from enum import Enum


class TestStatus(Enum):
    Pass = 1
    Failed = 2
    Error = 3


class AssertResult(Enum):
    Pass = 1
    Failed = 2
    Error = 3


