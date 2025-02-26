# 🚀 Sentiment Analysis using Flask & Gemini API

This is a simple web-based **Sentiment Analysis App** that uses **Google's Gemini API** to classify tweets as **POSITIVE, NEGATIVE, or NEUTRAL**. The app is built with **Flask** and is containerized using **Docker**.

---

## 📌 Features
- ✅ Analyze tweet sentiment (**POSITIVE, NEGATIVE, NEUTRAL**)  
- ✅ User-friendly web interface  
- ✅ Uses **Google Gemini API** for NLP processing  
- ✅ **Dockerized** for easy deployment  

---

---

## ⚡ Installation & Setup

## **Clone the Repository**
```bash
git clone https://github.com/yourusername/sentiment-analysis.git
cd sentiment-analysis
```
---
## ** Install Dependencies **
If you want to run the app locally (without Docker), install dependencies:

```bash
pip install -r requirements.txt

```
## ** Set up the API Key **
You need a Google Gemini API Key.
Set it as an environment variable:
```bash
$env:GEMINI_API_KEY="your_api_key"

```
## **Running with Docker**
Build the Docker Image
```bash
docker build -t sentiment-analysis .
```
## **Run the Docker Container**
```bash
docker run -p 5000:5000 --env GEMINI_API_KEY=your_api_key sentiment-analysis

```
## Open the Web App
Go to http://localhost:5000/ in your browser.
