from pydantic import BaseModel

class Property(BaseModel):
    livable_surface: float
    bedrooms: int
    bathrooms: int
    latitude: float
    longitude: float
    state_of_property: str
    epc_score: str
    province: str