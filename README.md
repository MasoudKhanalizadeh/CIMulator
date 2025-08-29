<p align="center">
  <img src="assets/CIMulator-v1.png" alt="CIMulator Logo" width="640"/>
</p>

# 🧠 CIMulator — Computation-In-Memory Simulator

CIMulator is an interactive Jupyter-based simulator for **memristor devices** and **crossbar arrays**. It lets researchers, students, and engineers explore **in-memory computing (CIM)** with adjustable parameters, real-time plotting, and an intuitive GUI.

## ✨ Features

- **Single-cell memristor simulation** with adjustable parameters (R0, k, I0, f, duration/resolution, waveform)
- **Waveforms:** *sine*, *square*, *triangle*
- **Interactive GUI with sliders** (ipywidgets)
- **Real-time plots:** input current *i(t)*, accumulated charge *q(t)*, memristance *M(t)*
- Built for **education, research, and prototyping** in neuromorphic/CIM

## 🚀 Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/MasoudKhanalizadeh/CIMulator.git
cd CIMulator
```

### 2) Install requirements

```bash
pip install numpy matplotlib ipywidgets
```

Enable widgets in Jupyter:

```bash
jupyter nbextension enable --py widgetsnbextension
```

### 3) Run in Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook and adjust parameters with sliders.

## 📊 Example Output

After running a simulation, you’ll see plots such as:
- Input current over time
- Accumulated charge curve
- Dynamic memristance response

## 🧩 Future Roadmap

- [ ] **Crossbar Array Mode:** simulate N×N memristor crossbars  
- [ ] **Matrix–Vector Multiplication:** demonstrate `Y = W × X` in CIM hardware  
- [ ] **AI Integration:** prototype small neural networks on crossbar arrays  
- [ ] **Export Tools:** CSV/JSON outputs for analysis  
- [ ] **Variability & Noise Models:** non-idealities for realism  
- [ ] **Unified GUI:** switch between Single-Cell / Crossbar / AI modes

## 🔍 Related Tools

- **NeuroPack:** Python GUI for memristor-based neuromorphic computing (MNIST, learning rules). (arXiv: 2201.03339)  
- **CrossSim (Sandia Labs):** GPU-accelerated crossbar simulator integrated with ML frameworks. (cross-sim.sandia.gov)

**CIMulator** fills a niche by being **interactive, educational, and Jupyter-friendly** for learning, experimentation, and rapid prototyping.

## 📬 Contact

- Author: **Masoud Khanalizadeh Imani**  
- Email: masoud.khanalizadehimani@gmail.com

## ❤️ Support This Project

If you find **CIMulator** useful, please consider supporting its development:

- ⭐ Star this repository on GitHub  
- 🐦 Share it with your network  
- ☕ For Iran: http://www.coffeete.ir/masoud.khanalizadehimani  
- ☕ International: https://buymeacoffee.com/masoudkhanalizadeh

Your support helps me add **crossbar arrays, AI integration, and advanced CIM tools**.

## 📝 License

MIT License © 2025 Masoud Khanalizadeh Imani
