from typing import Optional, List, Dict
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sample:
    
    """
    A class representing a sample in the lab ontology.
    
    Attributes:
        identifier (str): A unique identifier for the sample.
        metadata (dict): A dictionary containing metadata about the sample, such as source, date collected, etc.
    """

    identifier: str
    metadata: dict


@dataclass
class Measurement:

    """
    A class representing a measurement in the lab ontology.
    
    Attributes:
        value (float): The measured value.
        type (str): The type of measurement (e.g., "temperature", "pH").
        unit (str): The unit of the measurement (e.g., "Celsius", "pH units").
        sample_id (Optional[str]): An optional identifier for the sample associated with the measurement.
        time (Optional[datetime]): An optional timestamp for when the measurement was taken.
    """
    
    value: float
    measurement_type: str
    instrument_source: str
    unit: str
    sample: Optional[Sample] = None
    timestamp: Optional[datetime] = None


class Well:

    """
    A class representing a well in a microplate.
    
    Attributes:
        position (str): The position of the well in the microplate (e.g., "A1").
        measurements (List[Measurement]): A list of measurements taken from this well.
    """

    def __init__(
        self, 
        position: str, 
        measurements: Optional[List[Measurement]] = []
    ):
        self.position = position
        
        # Ensure all measurements in a well have the same sample
        if measurements: 
            first_sample = measurements[0].sample if measurements[0].sample else None
            if first_sample:
                for measurement in measurements:
                    assert measurement.sample == first_sample, "All measurements in a well must have the same sample."

        self.measurements = measurements
            

    @property
    def sample(self):
        """Returns the sample associated with the first measurement in the well, if available."""
        if self.measurements:
            return self.measurements[0].sample
        return None
    
    
    def add_measurement(self, measurement: Measurement):
        """Adds a measurement to the well."""
        if self.measurements:
            assert measurement.sample == self.sample, "Measurement sample does not match well sample."
            self.measurements.append(measurement)
        else:
            self.measurements = [measurement]



@dataclass
class Microplate:

    """
    A class representing a microplate in the lab ontology.
    
    Attributes:
        identifier (Optional[str]): An optional identifier for the microplate.
        wells (Dict[str, Well]): A dictionary mapping well positions (e.g., "A1") to Well objects.
        n_rows (int): The number of rows in the microplate.
        n_columns (int): The number of columns in the microplate.
    """
    
    identifier: Optional[str]
    wells: Dict[str, Well] 
    n_rows: int
    n_columns: int





