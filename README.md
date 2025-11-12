# 🧭 CareerCompass — Intelligent Career Recommendation Chatbot

![CareerCompass Banner](https://i.imgur.com/MFh3VwR.png)

> 🚀 An AI-powered chatbot that recommends the best career paths based on your skills, interests, and goals.  
> Built with **Streamlit** and **Machine Learning (TF-IDF + Cosine Similarity)**.

---

## 🌟 Features

- 💬 Chat-style conversational UI  
- 🎯 Personalized career recommendations  
- 🧠 Intelligent matching using NLP similarity  
- ⚡ Fast, lightweight, and API-free (offline model)  
- 📊 Clean modular architecture (`model/`, `data/`, etc.)  

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Streamlit** – for frontend UI  
- **pandas** – data handling  
- **scikit-learn** – TF-IDF + Cosine Similarity  
- **dotenv** – for environment config  

---

## 🧠 How It Works

1. The user describes their interests (e.g., “I like creativity and design”).  
2. The app converts the text into a **TF-IDF vector**.  
3. It compares the input vector with career descriptions in `data/careers.csv`.  
4. It shows the top 5 career roles that best match the user's description.

---

## ⚙️ Setup Instructions (Run Locally)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/ShubH9604/CareerCompass.git
cd CareerCompass

# 2️⃣ (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit app
streamlit run app.py
