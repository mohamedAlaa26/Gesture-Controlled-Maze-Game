# 🧠 Gesture Control Game – Backend

This is the **backend API** for the Gesture Control Game, which processes hand gesture data sent from the frontend and returns a predicted gesture label using a trained ML model.

---

## 📦 Backend System Architecture & Workflow

This section outlines the complete backend implementation pipeline, including model integration, API development, monitoring setup, containerization, and deployment.

### 🔄 General Overview

* ✅ **Integrated a Trained ML Model**
  Loaded and served a pre-trained gesture classification model capable of predicting `left`, `right`, `up`, `down`, and `none` based on hand gesture input.

* ✅ **Experiment Tracking with MLflow**
  Logged multiple training experiments using **MLflow**, capturing metrics, parameters, and artifacts to enable better model selection and reproducibility.

* ✅ **FastAPI Integration**
  Developed a clean and modular FastAPI application:

  * `/predict` endpoint for receiving image data and returning gesture predictions.
  * `/metric` endpoint for exposing server and model metrics for monitoring.

* ✅ **Monitoring Setup**

  * Integrated **Prometheus** to scrape real-time API metrics.
  * Designed a **Grafana dashboard** to visualize these metrics.

* ✅ **Frontend Communication**
  Modified the existing frontend code to connect with the new backend API using REST calls via `api-call.js`.

* ✅ **Dockerized Application**

  * Created a `Dockerfile` to containerize the FastAPI application.
  * Built and tested the image locally to ensure smooth performance.
  * Pushed the final image to **Docker Hub** for public access.

* ✅ **Cloud Deployment**
  Deployed the Dockerized backend to a **ClawCloud Virtual Machine** using Docker and exposed it via **NodePort** for external accessibility.

---

## 🔬 API Endpoints

### `POST /predict`

* **Description**: Accepts base64-encoded image and returns predicted gesture label.
* **Payload**:

```json
{
  "image": "<base64_encoded_image>"
}
```

* **Response**:

```json
{
  "prediction": "up"
}
```

### `GET /metric`

* **Description**: Exposes model, data, and server metrics for monitoring with Prometheus.

---


## 🧪 Unit Testing

* Used `pytest` to create unit tests for:

  * Model loading
  * Prediction output
  * API route responses
* All tests are located in the `/tests` directory

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t gesture-backend .
```

### Run Container

```bash
docker run -d -p 8000:8000 gesture-backend
```

### Push to Docker Hub

```bash
docker tag gesture-backend <your-dockerhub-username>/gesture-backend

docker push <your-dockerhub-username>/gesture-backend
```

---

## ☁️ Cloud Deployment

* Provisioned a virtual machine on **ClawCloud**
* Installed Docker and Prometheus on the VM
* Pulled the image from Docker Hub and ran it
* Exposed service using NodePort

---

## 🚀 Project Requirements Fulfilled

| Requirement                   | Status     |
| ----------------------------- | ---------- |
| ML Model Integration          | ✅          |
| API Development (FastAPI)     | ✅          |
| MLflow Logging                | ✅          |
| Dockerization                 | ✅          |
| Cloud Deployment              | ✅          |
| Frontend Integration          | ✅          |
| Monitoring Setup (Prometheus) | ✅          |
| Unit Testing                  | ✅          |

---

