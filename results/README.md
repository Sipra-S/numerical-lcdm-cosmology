# Numerical ΛCDM Cosmology

A numerical implementation of the ΛCDM (Lambda Cold Dark Matter) cosmological model solving the Friedmann equations to study the expansion history of the Universe.

This project computes:

- The expansion history \( a(t) \)
- The age of the Universe
- Comoving distance
- Luminosity distance

# Theoretical Framework

The ΛCDM model assumes:

- Homogeneity and isotropy (FLRW metric)
- General Relativity governs gravity
- The Universe consists of:
  - Radiation (Ω_r)
  - Matter (Ω_m)
  - Dark Energy / Cosmological Constant (Ω_Λ)

For a spatially flat universe:

\[
H(a) = H_0 \sqrt{
\frac{\Omega_r}{a^4}
+ \frac{\Omega_m}{a^3}
+ \Omega_\Lambda
}
\]

Cosmic time is computed via:

\[
t_0 = \int_0^1 \frac{da}{aH(a)}
\]

Cosmological distances are computed numerically from:

\[
D_C(z) = c \int_0^z \frac{dz'}{H(z')}
\]

\[
D_L(z) = (1+z) D_C(z)
\]

# Numerical Method

- Numerical integration performed using the trapezoidal rule
- Scale factor discretized from \( a = 10^{-5} \) to \( a = 1 \)
- Cosmological parameters consistent with Planck 2018 observations

# Input Parameters Used

- H₀ = 67.4 km/s/Mpc  
- Ωₘ = 0.315  
- Ωᵣ = 9 × 10⁻⁵  
- Ω_Λ = 0.685  

---

# Results

# Expansion History

The numerical integration reproduces the expected ΛCDM expansion behavior:

- Early radiation-dominated era
- Matter-dominated intermediate phase
- Late-time accelerated expansion driven by dark energy

# Key Numerical Outputs

- Age of the Universe ≈ **13.8 Gyr**
- Comoving Distance (z=1) ≈ **3.4 Gpc**
- Luminosity Distance (z=1) ≈ **6.8 Gpc**

These values are consistent with standard ΛCDM cosmology.



