from pydantic import BaseModel

class Property(BaseModel):
    livable_surface: float
    bedrooms: int
    bathrooms: int
    state_of_property: str
    epc_score: str
    province: str
    city : str
    postal_code : int
    facades : int
    toilets : int
    terrace : int
    garden : int
    garage : int
    swimming_pool : int
    distance_from_train_stations_by_foot : float
    distance_from_elementary_school_by_foot : float
    distance_from_high_school_by_foot : float
    type_property : str
    subtype_property : str
    heating_type : str
    sun_exposure : str
    flooding_area_type : str