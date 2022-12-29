from astropy.coordinates import BaseCoordinateFrame
from astropy.coordinates import frame_transform_graph
from astropy.coordinates import RepresentationMapping
import astropy.coordinates.representation as r


class SgrCoords(BaseCoordinateFrame):
    # Specify how coordinate values are represented when outputted
    default_representation = r.SphericalRepresentation

    # Override component bames
    frame_specific_representation_info = {
        r.SphericalRepresentation: [
            RepresentationMapping("lon", "Λ"),
            RepresentationMapping("lat", "B"),
        ]
    }

