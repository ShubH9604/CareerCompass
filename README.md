# 🧭 CareerCompass — Intelligent Career Recommendation Chatbot

> 🚀 An AI-powered chatbot that recommends the best career paths based on your skills, interests, and goals.  
> Built with **Streamlit** and **Machine Learning (TF-IDF + Cosine Similarity)**.

🎯 **Live Demo:** [https://careercompass-cc.streamlit.app](https://careercompass-cc.streamlit.app)

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
- **pandas** – for data handling  
- **scikit-learn** – for TF-IDF + Cosine Similarity  
- **dotenv** – for environment configuration  

---

## 🧠 How It Works

1. The user describes their interests (e.g., “I like creativity and design”).  
2. The app converts the input into a **TF-IDF vector**.  
3. It compares the vector with job descriptions from `data/careers.csv`.  
4. It returns the **top 5 career roles** most relevant to the user's input.

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
