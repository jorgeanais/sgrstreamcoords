import numpy as np

atan2 = np.arctan2
asin = np.arcsin
cos = np.cos
sin = np.sin


def lambda_sgr(ra: float, dec: float):
    """Transform equatorial coordinates into Sgr Coordinates"""

    lambda_sgr = atan2(
        -0.935_953_54 * cos(ra) * cos(dec) - 0.319_106_58 
    )

    return 