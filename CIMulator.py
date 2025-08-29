# Interactive Memristor simulator with ipywidgets (works in Jupyter/Colab)
# Requirements: ipywidgets (usually preinstalled on Colab/JupyterLab); if not, run: pip install ipywidgets

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import FloatSlider, FloatLogSlider, IntSlider, HBox, VBox, Button, Output, Layout, Dropdown
from IPython.display import display, clear_output

# ---- Core simulation function ----
def run_memristor_sim(R0=100.0, k=10.0, I0=1e-3, freq=50.0, duration=0.1, steps=1000, wave="sine"):
    t = np.linspace(0.0, duration, steps)
    omega = 2.0 * np.pi * freq
    
    if wave == "sine":
        i_t = I0 * np.sin(omega * t)
    elif wave == "square":
        i_t = I0 * np.sign(np.sin(omega * t))
    elif wave == "triangle":
        i_t = (2*I0/np.pi) * np.arcsin(np.sin(omega * t))
    else:
        i_t = I0 * np.sin(omega * t)

    dt = t[1] - t[0]
    q_t = np.cumsum(i_t) * dt  # integral of current
    M_t = R0 + k * q_t         # linear memristor model
    v_t = M_t * i_t
    
    return t, i_t, q_t, M_t, v_t

# ---- Widgets ----
R0_w = FloatSlider(value=100.0, min=1.0, max=1000.0, step=1.0, description='R0 (Ω)', readout_format='.1f', continuous_update=False)
k_w  = FloatSlider(value=10.0,  min=0.0, max=100.0, step=0.5, description='k (Ω/C)', readout_format='.1f', continuous_update=False)
I0_w = FloatLogSlider(value=1e-3, base=10, min=-6, max=-1, step=0.1, description='I0 (A)', continuous_update=False)
f_w  = FloatSlider(value=50.0,  min=1.0, max=500.0, step=1.0, description='freq (Hz)', readout_format='.1f', continuous_update=False)
dur_w= FloatSlider(value=0.1,   min=0.01, max=2.0, step=0.01, description='duration (s)', readout_format='.2f', continuous_update=False)
N_w  = IntSlider(value=1000,    min=200, max=5000, step=100, description='steps', continuous_update=False)
wave_w = Dropdown(options=[('sine','sine'), ('square','square'), ('triangle','triangle')], value='sine', description='wave')

run_btn = Button(description='Run Simulation', button_style='')
out = Output()

def on_run_clicked(_):
    with out:
        clear_output(wait=True)
        t, i_t, q_t, M_t, v_t = run_memristor_sim(R0=R0_w.value, k=k_w.value, I0=I0_w.value,
                                                  freq=f_w.value, duration=dur_w.value,
                                                  steps=N_w.value, wave=wave_w.value)
        # Plot (each chart separate, no specific colors)
        fig, axs = plt.subplots(3, 1, figsize=(10, 8))
        
        axs[0].plot(t, i_t)
        axs[0].set_title('Input Current i(t)')
        axs[0].set_ylabel('A')
        axs[0].grid(True)
        
        axs[1].plot(t, q_t)
        axs[1].set_title('Accumulated Charge q(t)')
        axs[1].set_ylabel('C')
        axs[1].grid(True)
        
        axs[2].plot(t, M_t)
        axs[2].set_title('Memristance M(t)')
        axs[2].set_ylabel('Ohm')
        axs[2].set_xlabel('Time (s)')
        axs[2].grid(True)
        
        plt.tight_layout()
        plt.show()

run_btn.on_click(on_run_clicked)

ui = VBox([
    HBox([R0_w, k_w, I0_w]),
    HBox([f_w, dur_w, N_w]),
    HBox([wave_w, run_btn]),
    out
])

display(ui)

print("Tip: Adjust sliders, choose a waveform, then click 'Run Simulation'.")
