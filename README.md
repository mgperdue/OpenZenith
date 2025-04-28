# OpenZenith

[![CI](https://github.com/mgperdue/OpenZenith/actions/workflows/ci.yml/badge.svg)](https://github.com/mgperdue/OpenZenith/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mgperdue/OpenZenith/branch/main/graph/badge.svg)](https://codecov.io/gh/mgperdue/OpenZenith)
[![License](https://img.shields.io/github/license/mgperdue/OpenZenith)](https://github.com/mgperdue/OpenZenith/blob/main/LICENSE)

**Real-time sky awareness:**  
Visualize aircraft, satellites, and weather overhead — beautifully and seamlessly — from your desktop.

---

## ✨ Features

- 🛫 **Aircraft Tracking** – Live planes overhead via OpenSky and AviationStack APIs
- 🛰️ **Satellite Awareness** *(future)* – Real-time orbit tracking
- 🌦️ **Weather Layers** – METAR, radar overlays, conditions
- 📡 **ATC Frequencies** – Estimated tuned frequencies + LiveATC links
- 📈 **Flight Trails & Stats** – Real-time traffic analytics
- 🧠 **Machine Learning Predictions** *(future)* – Runway and procedure prediction
- 🖥️ **Cross-platform Desktop** – Linux & Windows support

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9, 3.10, 3.11, or 3.12
- Git
- API keys:
  - [OpenSky Network](https://opensky-network.org/)
  - [AviationStack](https://aviationstack.com/)
  - [Mapbox](https://mapbox.com/)
  - [OpenWeatherMap](https://openweathermap.org/)

### Install

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/OpenZenith.git
cd OpenZenith

# Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

# Install dependencies
pip install .[dev]
```

---

## 📦 Project Structure

```plaintext
src/
  core/        # Core flight, satellite, and weather tracking
  gui/         # PySide6-based tray and UI components
  renderer/    # Wallpaper/image rendering engine
  cli/         # CLI tools for data export and analysis
  ml/          # Machine learning models and training (future)
assets/
data/
tests/
docs/
.github/
```

---

## 📄 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

*Built with clarity. Tuned for the sky.*
