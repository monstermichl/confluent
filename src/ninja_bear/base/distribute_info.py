from dataclasses import dataclass


@dataclass  # https://stackoverflow.com/a/70259423
class DistributeInfo:
    file_name: str
    data: str