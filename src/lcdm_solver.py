"""
Numerical ΛCDM Cosmology Simulator
-----------------------------------
Solves the Friedmann equation numerically to compute:
- Expansion history a(t)
- Age of the Universe
- Comoving distance
- Luminosity distance

Author: Sipra Subhadarsini Sahoo
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# Cosmology Class
# ==========================================================

class LCDMModel:
    def __init__(self, H0=70.0, Omega_m=0.3, Omega_r=8.4e-5, Omega_L=0.7):
        """
        Initialize cosmological parameters.

        H0: Hubble constant (km/s/Mpc)
        Omega_m: Matter density parameter
        Omega_r: Radiation density parameter
        Omega_L: Dark energy density parameter
        """

        self.H0 = H0
        self.Omega_m = Omega_m
        self.Omega_r = Omega_r
        self.Omega_L = Omega_L
        self.c = 299792.458  # km/s

        # Convert H0 to SI units (1/s)
        self.H0_SI = H0 * 1000 / (3.0857e22)

    # ------------------------------------------------------
    # Hubble Parameter
    # ------------------------------------------------------
    def H(self, a):
        return self.H0_SI * np.sqrt(
            self.Omega_r / a**4 +
            self.Omega_m / a**3 +
            self.Omega_L
        )

    # ------------------------------------------------------
    # Compute Cosmic Age
    # ------------------------------------------------------
    def compute_age(self, n_points=10000):
        a = np.linspace(1e-5, 1, n_points)
        integrand = 1 / (a * self.H(a))

        t = np.trapz(integrand, a)

        seconds_in_Gyr = 3.1536e16
        return t / seconds_in_Gyr, a

    # ------------------------------------------------------
    # Comoving Distance
    # ------------------------------------------------------
    def comoving_distance(self, z, n_points=5000):
        a_z = 1 / (1 + z)
        a_vals = np.linspace(a_z, 1, n_points)

        integrand = 1 / (a_vals**2 * self.H(a_vals))
        integral = np.trapz(integrand, a_vals)

        D_meters = self.c * integral / self.H0_SI
        D_Mpc = D_meters / (3.0857e22)

        return D_Mpc

    # ------------------------------------------------------
    # Luminosity Distance
    # ------------------------------------------------------
    def luminosity_distance(self, z):
        return (1 + z) * self.comoving_distance(z)

    # ------------------------------------------------------
    # Expansion History Plot
    # ------------------------------------------------------
    def plot_expansion(self):
        age, a = self.compute_age()
        t_vals = np.linspace(0, age, len(a))

        plt.figure()
        plt.plot(t_vals, a)
        plt.xlabel("Cosmic Time (Gyr)")
        plt.ylabel("Scale Factor a(t)")
        plt.title("ΛCDM Expansion History")
        plt.show()


# ==========================================================
# User Interaction
# ==========================================================

def main():
    print("\n=== Numerical ΛCDM Cosmology Simulator ===\n")

    try:
        H0 = float(input("Enter H0 (km/s/Mpc) [default 70]: ") or 70)
        Omega_m = float(input("Enter Ω_m [default 0.3]: ") or 0.3)
        Omega_r = float(input("Enter Ω_r [default 8.4e-5]: ") or 8.4e-5)
        Omega_L = float(input("Enter Ω_Λ [default 0.7]: ") or 0.7)
    except ValueError:
        print("Invalid input. Using default Planck-like parameters.")
        H0, Omega_m, Omega_r, Omega_L = 70, 0.3, 8.4e-5, 0.7

    model = LCDMModel(H0, Omega_m, Omega_r, Omega_L)

    # Compute age
    age, _ = model.compute_age()
    print(f"\nAge of the Universe ≈ {age:.2f} Gyr")

    # Distance calculation
    try:
        z = float(input("\nEnter redshift z for distance calculation: "))
        D_C = model.comoving_distance(z)
        D_L = model.luminosity_distance(z)

        print(f"Comoving Distance ≈ {D_C:.2f} Mpc")
        print(f"Luminosity Distance ≈ {D_L:.2f} Mpc")

    except ValueError:
        print("Invalid redshift input. Skipping distance calculation.")

    # Plot
    model.plot_expansion()


if __name__ == "__main__":
    main()

