# lunar-probe-orbital-simulation
Simulating the orbital motion of a lunar probe under dual gravitational influence from the moon and earth.

# Simulating the Orbital Motion of a Lunar Probe Under Dual Gravitational Influence

This project models the motion of a lunar probe orbiting the Moon, while the Moon itself orbits the Earth. It simulates the system using newtonian gravity and numerically integrates the resulting system of differential equations using `scipy` in python.

The simulation accounts for:
- Earth's gravity on the Moon
- Both Earth and Moon's gravity on the probe
- The conversion between the Moon's frame and Earth's frame
- Accuracy tuning via numerical tolerance

---

## Features of the Program

- Numerically solves equations of motion using `scipy.integrate.solve_ivp`
- Models a two-body (Earth–Moon) and three-body (Earth–Moon–Probe) system
- Plots the orbital paths of the Moon and the probe in 2D space
- Shows effect of varying probe altitude and initial velocities
- Achieves 99.44% accuracy compared to the Moon’s real orbital period
- Includes visual comparison of orbits at various solver tolerances

---

## Output Plots

![Probe orbiting the Moon](images/probe_and_moon_plot.png)
> Probe orbiting the Moon while both orbit the Earth. Simulated in Python with `solve_ivp`.

![Probe orbiting the Moon](images/2d_speed_probe_plot.png)
> Speed of the probe along two orthogonal axes verying with time.

---

## Theory Condensed

The Moon is treated as orbiting the Earth, modeled as a fixed origin representing the centre of Earth's mass. The probe is influenced by gravitational forces from both the Earth and the Moon. The equations of motion are:

**Moon's motion**  
![Equation of motion of the moon](images/moon_eq_motion.png)
> Equation of motion describing how the moon's position will vary with time.

**Probe's motion**               
![Equation of motion of the moon](images/probe_eq_motion.png)
> Equation of motion describing how the probe's position will vary with time.


where:
- r_m: position vector of the Moon from Earth
- r_p: position vector of the probe from Earth
- r_pm: probe's position relative to the Moon

