import numpy as np

def get_matrix(theta: float, phi: float, psi: float):
    """
    Returns the rotation matrix for the given Euler angles.
    Extracted from Goldstein, Classical Mechanics, 3rd edition, p. 153.
    """
    cosθ = np.cos(theta)
    sinθ = np.sin(theta)
    cosϕ = np.cos(phi)
    sinϕ = np.sin(phi)
    cosψ = np.cos(psi)
    sinψ = np.sin(psi)
    
    # Rotation about z-axis
    D = np.array(
        [
            [cosθ, sinϕ, 0],
            [-sinθ, cosϕ, 0],
            [0, 0, 1]
        ]
    )

    # Rotation about ξ-axis
    C = np.array(
        [
            [1, 0, 0],
            [0, cosθ, sinθ],
            [0, -sinθ, cosθ]
        ]
    )

    # Rotation about ζ'-axis
    B = np.array(
        [
            [cosψ, sinψ, 0],
            [-sinψ, cosψ, 0],
            [0, 0, 1]
        ]
    )

    # Product matrix A
    return B * C * D
