# 🌱 Soil & Crop Optimization API

The **Soil-Crop API** is a FastAPI-powered backend that analyzes soil nutrient levels, predicts deficiencies, and recommends suitable crops and fertilizers. This project includes complete API support, MySQL integration, and a Dockerized deployment for easy scalability.

---

## 🚀 Features

- 📊 **Soil Nutrient Analysis**  
  Calculates NPK & micronutrient levels from uploaded soil test data.

- 🌾 **Crop Recommendation System**  
  Suggests best crops based on soil type, nutrient profile, and region.

- 🧪 **Nutrient Deficiency Detection**  
  Automatically identifies lacking nutrients and categorizes them.

- 🧮 **Fertilizer Recommendation System**  
  Gives organic + inorganic fertilizer suggestions with **specific quantities**.

- 🗄️ **MySQL Database**  
  Stores soil types, crop data, nutrient standards, fertilizer tables.

- 🐳 **Docker Support**  
  API is fully containerized with prebuilt Docker image on Docker Hub.

---

## 🛠️ Technologies Used

- **FastAPI**
- **Python**
- **MySQL**
- **SQLAlchemy**
- **Pydantic**
- **Docker**
- **Uvicorn**

---

## 📁 Project Structure

```
soil-crop-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── routers/
│   │   ├── soil.py
│   │   ├── crop.py
│   │   └── fertilizer.py
│   ├── schemas/
│   └── utils/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ▶️ Running the API Locally

Install dependencies:
```bash
pip install -r requirements.txt
```

Start FastAPI:
```bash
uvicorn app.main:app --reload
```

Open docs:
```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Usage

### **Pull image from Docker Hub**
```bash
docker pull malkhedchetan/soil-crop-api-fastapi
```

### **Run the container**
```bash
docker run -p 8000:8000 malkhedchetan/soil-crop-api-fastapi
```

### **Or build locally**
```bash
docker build -t soil-crop-api-fastapi .
docker run -p 8000:8000 soil-crop-api-fastapi
```

---

## 🌾 API Endpoints Overview

### ✓ Soil Module
- `POST /soil/analyze`
- `POST /soil/upload-report`
- `GET /soil/types`

### ✓ Crop Module
- `GET /crop/recommend/{soil_type}`
- `POST /crop/by-nutrients`

### ✓ Fertilizer Module
- `POST /fertilizer/recommend`
- `GET /fertilizer/list`

---

## 🧪 Sample JSON Input

```json
{
  "nitrogen": 45,
  "phosphorus": 15,
  "potassium": 20,
  "ph": 6.5,
  "soil_type": "Loamy"
}
```

---

## 📦 Deployment

- **Docker Hub Image:** [malkhedchetan/soil-crop-api-fastapi](https://hub.docker.com/repository/docker/malkhedchetan/soil-crop-api-fastapi/general)  
- Compatible with: AWS, Azure, GCP, Heroku (container), Render, Railway

---

## 👨‍💻 Author

**Chetan Malkhed**  
Python Backend Developer | ML & IoT Enthusiast

🔗 GitHub: [@Malkhedchetan](https://github.com/Malkhedchetan)

---

## ⭐ Acknowledgements

This project originates from:  
**Smart Soil and Crop Optimization System: Precision, Sustainability, and Farmer-Centric Innovation.**
