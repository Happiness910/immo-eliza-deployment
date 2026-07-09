from pydantic import BaseModel

class Property(BaseModel):
    livable_surface: float
    bedrooms: int
    bathrooms: int
    state_of_property: str
    epc_score: str
    province: str
    city : str