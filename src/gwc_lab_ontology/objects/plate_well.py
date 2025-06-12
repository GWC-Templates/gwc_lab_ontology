from typing import Optional, List
from dataclasses import dataclass
from gwc_lab_ontology.objects.measurement import Measurement
from datetime import datetime

@dataclass
class Well:
    position: str  # e.g. "A1"
    measurements: List[Measurement]