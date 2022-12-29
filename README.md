# sgrstreamcoords
Transformation to convert Equatorial coordinates to Sgr stream coordinate system (Belokurov et al. 2014)
$$
\tilde{\Lambda} = \text{atan2}(−0.935 953 54 \cos \alpha \cos \delta - 0.319 106 58 \sin \alpha \cos \delta + 0.148 868 95 \sin \delta,
0.212 155 55 \cos \alpha \cos \delta - 0.848 462 91 \sin \alpha \cos \delta -0.484 871 86 \sin \delta)
$$

$$
\tilde{B} = \arcsin(0.281 035 59 \cos \alpha \cos \delta - 0.422 234 15 \sin \alpha \cos \delta + 0.861 822 09 \sin \delta)
$$

Inverse transformation
$$
\alpha = \text{atan2}(-0.848 462 91 \cos \tilde{\Lambda} \cos \tilde{B} - 0.319 106 58 \sin \tilde{\Lambda}\cos \tilde{B} -0.422 234 15 \sin \tilde{B}, 0.212 155 55 \cos \tilde{\Lambda} \cos \tilde{B} - 0.935 953 54 \sin \tilde{\Lambda} \cos \tilde{B} + 0.281 035 59 \sin \tilde{B})
$$

$$
\delta = \arcsin(-0.484 871 86 \cos \tilde{\Lambda} \cos \tilde{B} + 0.148 868 95 \sin \tilde{\Lambda} \cos \tilde{B} + 0.861 822 09 \sin \tilde{B})
$$

where $\tan(\text{atan2}(y,x)) = y/x$
