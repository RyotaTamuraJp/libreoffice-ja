import os
from dataclasses import dataclass

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


@dataclass(frozen=True)
class LogConfig:
    logging_conf_path = os.path.join(BASE_PATH, 'logging.conf')
