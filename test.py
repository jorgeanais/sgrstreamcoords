import numpy as np

atan2 = np.arctan2
asin = np.arcsin
cos = np.cos
sin = np.sin


def equatorial_to_sgr(ra: float, dec: float):
    """
    Transform equatorial coordinates into Sgr Coordinates
    From appendix A of Belokurov et al. (2014)
    """

    lambda_tilde = atan2(
        -0.935_953_54 * cos(ra) * cos(dec) - 0.319_106_58 * sin(ra) * cos(dec) + 0.148_868_95 * sin(dec),
         0.212_155_55 * cos(ra) * cos(dec) - 0.848_462_91 * sin(ra) * cos(dec) - 0.484_871_86 * sin(dec)
    )

    b_tilde = asin(
        0.281_035_59 * cos(ra) * cos(dec) - 0.422_234_15 * sin(ra) * cos(dec) + 0.861_822_09 * sin(dec)
    )

    return lambda_tilde, b_tilde


def sgr_to_equatorial(lambda_tilde: float, b_tilde: float):
    """
    Transform Sgr Coordinates into equatorial coordinates
    From appendix A of Belokurov et al. (2014)
    """

    ra = atan2(
        -0.848_462_91 * cos(lambda_tilde) * cos(b_tilde) + 0.319_106_58 * sin(lambda_tilde) * cos(b_tilde) + 0.422_234_15 * sin(b_tilde),
        -0.212_155_55 * cos(lambda_tilde) * cos(b_tilde) - 0.935_953_54 * sin(lambda_tilde) * cos(b_tilde) - 0.281_035_59 * sin(b_tilde)
    )

    dec = asin(
        -0.484_871_86 * cos(lambda_tilde) * cos(b_tilde) + 0.148_868_95 * sin(lambda_tilde) * cos(b_tilde) + 0.861_822_09 * sin(b_tilde)
    )

    return ra, dec