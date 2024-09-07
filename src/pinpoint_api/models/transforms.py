from vbl_aquarium.models.pinpoint import AffineTransformModel
from vbl_aquarium.models.unity import Vector3

qiu2018 = AffineTransformModel(
    name = "Qiu2018",
    prefix = "q18",
    scaling = Vector3(
        x = -1.031,
        y = 0.952,
        z = -0.885
    ),
    rotation = Vector3(
        x = 0,
        y = -7.5,
        z = 0
    )
)

dorr2018 = AffineTransformModel(
    name = "Dorr2008",
    prefix = "d08",
    scaling = Vector3(
        x = -1.087,
        y = 1,
        z = -0.952
    ),
    rotation = Vector3(
        x = 0,
        y = -7.5,
        z = 0
    )
)

dorr2018_ibl = AffineTransformModel(
    name = "IBL-Dorr2008",
    prefix = "id08",
    scaling = Vector3(
        x = -1.087,
        y = 1,
        z = -0.952
    ),
    rotation = Vector3(
        x = 0,
        y = 0,
        z = 0
    )
)

default = AffineTransformModel(
    name = "Default",
    prefix = "",
    scaling = Vector3(
        x = 1,
        y = 1,
        z = 1
    ),
    rotation = Vector3(
        x = 0,
        y = 0,
        z = 0
    )
)