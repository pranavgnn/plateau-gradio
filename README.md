# Plateau: License Plate Detection

**Machine Learning & Deep Learning Lab Endsem Project**

## Overview

Plateau is a web application designed to automatically detect and localize vehicle license plates in real-world environments. Powered by a custom-trained YOLOv8 model and wrapped in a Gradio web interface, the application allows users to upload images and instantly view the detected bounding boxes.

This repository contains the complete pipeline, including the model weights, the interactive web application, the original Kaggle training notebook, and the continuous deployment configuration.

## Tech Stack

- **Machine Learning:** Ultralytics YOLOv8, PyTorch
- **Web Interface:** Gradio, Pillow
- **Dependency Management:** `uv`
- **Deployment & CI/CD:** Docker, GitHub Actions, GitHub Container Registry (GHCR)

## Repository Structure

- `main.py`: The Gradio web application script for model inference.
- `weights.pt`: The custom-trained YOLOv8 model weights.
- `train.ipynb`: The Kaggle notebook used to train the model on the license plate dataset.
- `pyproject.toml` & `uv.lock`: Dependency configuration files for fast, reproducible environments.
- `.github/workflows/build-and-push.yaml`: The CI/CD pipeline configuration.

## Quick Start (Docker)

The application is packaged as a Docker image and built automatically by our CD pipeline. The fastest way to run the application is to pull the latest image from the GitHub Container Registry.

1. Pull the latest image:

```bash
   docker pull ghcr.io/pranavgnn/plateau-gradio:latest
```

2.  Run the container:

```bash
    docker run -p 7860:7860 ghcr.io/pranavgnn/plateau-gradio:latest
```

3.  Open `http://localhost:7860` in your web browser to access the application.

## Local Development Setup

If you prefer to run the application locally without Docker, we recommend using `uv` for dependency management.

1.  Clone the repository:

```bash
    git clone [https://github.com/pranavgnn/plateau-gradio.git](https://github.com/pranavgnn/plateau-gradio.git)
    cd plateau-gradio
```

2.  Sync the environment (this automatically creates a `.venv` and installs exact dependencies from `uv.lock`):

```bash
    uv sync
```

3.  Run the Gradio application:

```bash
    uv run main.py
```

## Continuous Deployment (CI/CD)

This repository utilizes GitHub Actions for continuous deployment. Whenever changes are pushed to the `main` branch affecting the `Dockerfile`, `main.py`, or `weights.pt`, the workflow automatically triggers.

The pipeline builds a new Docker image utilizing caching mechanisms and pushes it to the GitHub Container Registry (`ghcr.io`). The image is tagged with both `latest` and the specific commit SHA to ensure version control and immediate availability.

## Project Team

**Plateau** is our ML & DL Lab Endsem Project.

**Submitted by:**

| Name                          | Registration Number |
| :---------------------------- | :------------------ |
| Pranav G Nayak                | 230958011           |
| Aprameya Srinivasan Tatachari | 230958006           |
| Roselin Maria T J             | 230958032           |
| Dhruva Deepak                 | 230958048           |

<br>

**Submitted to:**<br>
**Prof. Dr. Srikanth Prabhu**<br>
Professor of Machine Learning and Deep Learning<br>
MIT Manipal

## Acknowledgments & Credits

This project was made possible by utilizing publicly available data. We would like to properly credit the following dataset and reference code used to train our license plate detection model:

- **Dataset & Reference:** [License Plate Detection on Kaggle](https://www.kaggle.com/code/tustunkok/license-plate-detection)
