
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Measurement:

    """A class representing a measurement in the lab ontology.
    Attributes:
        value (float): The measured value.
        type (str): The type of measurement (e.g., "temperature", "pH").
        unit (str): The unit of the measurement (e.g., "Celsius", "pH units").
        sample_id (Optional[str]): An optional identifier for the sample associated with the measurement.
        time (Optional[datetime]): An optional timestamp for when the measurement was taken.
    """
    
    value: float
    type: str
    unit: str
    sample_id: Optional[str] = None
    time: Optional[datetime] = None

    