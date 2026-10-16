<div align="center">

# ⚡ CYBERPUNK SYSTEM HUD ⚡

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=4,11,20&height=120&section=header&text=SYSTEM%20TELEMETRY%20HUD&fontSize=35&fontColor=00ff66&animation=fadeIn" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg?style=for-the-badge&logo=python&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
[![Status](https://img.shields.io/badge/Status-Active%20Development-success.svg?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge)]()

*An uncompromising, high-performance cyberpunk-styled system monitoring dashboard built with Python.*

</div>

---

## 🚀 About The Project

**Cyberpunk System HUD** is a real-time system telemetry and environment monitoring desktop application. Designed with a sleek futuristic aesthetic, it tracks critical hardware performance metrics (CPU, RAM, Disk) alongside live atmospheric weather data, dynamic background city visualization, and tactile audio feedback.

---

## 🛠️ Tech Stack & Architecture

Built with modern Python libraries and structured with modular architecture:

* **GUI Framework:** `CustomTkinter` for a modern, hardware-accelerated dark-mode interface.
* **Telemetry Core:** `psutil` for precise, low-overhead hardware performance tracking.
* **Audio Engine:** `pygame.mixer` (`SoundManager`) for immersive tactile sound effects on user interaction.
* **Data Integration:** Custom `ApiClient` for fetching live global weather telemetry.
* **Configuration:** Modular `ConfigManager` for centralized settings control.

---

## 🔥 Key Features

* **⚡ Real-Time Telemetry:** Live monitoring loops tracking CPU load, RAM utilization percentage (with used/total megabytes), and Disk usage.
* **🌆 Dynamic City & Visual Switcher:** Instantly switch between global hubs (Berlin, Tokyo, London, Paris) with automated dynamic UI image loading and weather updates.
* **🔊 Tactile Sound Feedback:** Integrated audio cues powered by custom WAV sound triggers on every interface action.
* **⚙️ Custom Configuration Layer:** Flexible setup management for refresh rates and display parameters.

---

## ⚡ Quick Start

### Prerequisites
Make sure you have Python 3.10+ installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ScuizzyBytes/Smart-Projects.git](https://github.com/ScuizzyBytes/Smart-Projects.git)
   cd Smart-Projects
