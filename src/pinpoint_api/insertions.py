from vbl_aquarium.models.unity import Vector3
from vbl_aquarium.models.pinpoint import InsertionModel

# Coordinates are in (ap, ml, dv)
# Coordinates are in mm

BREGMA_DICT = {
    'allen_mouse_25um': Vector3(
        x = 5.2,
        y = 5.7,
        z = 0.33
    )
}

class Insertion():

    def __init__(self, atlas: str = 'allen_mouse_25um', transform: str = 'null',
        entry_coordinate: Vector3 = None, depth: float = None,
        tip_coordinate: Vector3 = None,
        angles: Vector3 = None,
        reference_coordinate: Vector3 = BREGMA_DICT['allen_mouse_25um']):
        """Create an insertion
        """
        pass

    def 