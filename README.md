# 🧠 CIMulator — Computation-In-Memory Simulator

CIMulator is an interactive Jupyter-based simulator for **memristor devices** and **crossbar arrays**.  
It allows researchers, students, and engineers to explore **in-memory computing (CIM)** concepts with adjustable parameters, real-time plotting, and an intuitive graphical interface.

---

## ✨ Features
- **Single-cell memristor simulation** with customizable parameters:
  - Initial resistance **R0 (Ω)**
  - Sensitivity constant **k (Ω/C)**
  - Peak current **I0 (A)**
  - Input frequency **f (Hz)**
  - Duration and resolution
  - Waveform: *sine*, *square*, *triangle*
- **Interactive GUI with sliders** (via ipywidgets).
- **Real-time plots**:
  - Input current *i(t)*
  - Accumulated charge *q(t)*
  - Memristance *M(t)*
- Designed for **education, research, and prototyping** in neuromorphic and CIM domains.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/USERNAME/CIMulator.git
cd CIMulator

###2. Install requirements
pip install numpy matplotlib ipywidgets
Enable widgets in Jupyter (if not already enabled):

jupyter nbextension enable --py widgetsnbextension

###3. Run in Jupyter Notebook
jupyter notebook
Open the notebook and adjust parameters with sliders.

##📊 Example Output
After running a simulation, you will see plots like:

Input current over time

Accumulated charge curve

Dynamic memristance response

##🧩 Future Roadmap
 Crossbar Array Mode: simulate N×N memristor crossbars.

 Matrix–Vector Multiplication: demonstrate Y = W × X in CIM hardware.

 AI Integration: prototype small neural networks running on crossbar arrays.

 Export Tools: numerical outputs (CSV/JSON) for analysis.

 Variability & Noise Models: include non-idealities for realistic behavior.

 Unified GUI: choose between Single-Cell, Crossbar, or AI mode from one dashboard.

##🔍 Related Tools
NeuroPack: Python-based GUI tool for memristor-based neuromorphic computing (focus on MNIST and learning rules). (arxiv.org)

CrossSim (Sandia Labs): GPU-accelerated crossbar simulator for modeling analog in-memory computing integrated with ML frameworks. (cross-sim.sandia.gov)

CIMulator fills a niche by being interactive, educational, and Jupyter-friendly, designed for learning, experimentation, and rapid prototyping.

##📬 Contact
Author: Masoud Khanalizadeh Imani

Email: masoud.khanalizadehimani@gmail.com

LinkedIn: https://www.linkedin.com/in/masoud-khanalizadeh-imani-b17ab41bb/

GitHub: https://github.com/USERNAME

##❤️ Support This Project
If you find CIMulator useful, please consider supporting its development:

###⭐ Star this repository on GitHub

###🐦 Share it with your network

###☕ Buy Me a Coffee: https://www.buymeacoffee.com/YOURNAME

###💰 GitHub Sponsors: https://github.com/sponsors/USERNAME

Your support helps me continue adding features such as crossbar arrays, AI integration, and advanced CIM simulation tools.

##📝 License
MIT License © 2025 Masoud Khanalizadeh Imani
