# 🧠 Chatbot with User Login (MySQL)

A secure, memory-augmented **Generative AI Chatbot** powered by **Google Gemini Pro** using **LangChain**, with full user login/registration backed by **XAMPP-based MySQL** database. The chatbot remembers conversations using **LangChain’s ConversationBufferMemory**, enabling contextual follow-up questions.

---

## 🚀 Demo

<img width="1366" height="614" alt="Image" src="https://github.com/user-attachments/assets/716e2a56-7a34-4d12-8521-f5fa17b9fc66" />

---

## 📌 Key Features

✅ Gemini-Pro API integration via LangChain
✅ Secure login & registration with MySQL (via XAMPP/phpMyAdmin)
✅ Per-user conversation memory (LangChain's `ConversationBufferMemory`)
✅ Fully interactive chatbot built with Streamlit
✅ Modular codebase for easy extension
✅ Environment-variable based secret management (`.env`)
✅ Extendable for LangGraph or multi-agent agentic workflows

---

## 🛠️ Tech Stack

| Layer      | Technology                                        |
| ---------- | ------------------------------------------------- |
| 💬 LLM     | [Gemini-2.5-Pro](https://ai.google.dev) via LangChain |
| 🧠 Memory  | LangChain `ConversationBufferMemory`              |
| 🌐 UI      | Streamlit                                         |
| 🔐 Auth    | MySQL (XAMPP) + SHA256 hashing                    |
| 🔌 Backend | Python + LangChain + mysql-connector-python       |

---

## 🧱 Project Structure

```bash
chatbot/
├── app.py                 # Main Streamlit App
├── db.py                  # MySQL login/register functions
├── langchain_gemini.py    # LLM + memory integration
├── .env                   # Secure Gemini API key
├── requirements.txt       # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. ✅ Clone Repository

```bash
git clone https://github.com/your-username/Chatbot-with-User-Login.git
cd Chatbot-with-User-Login
```

### 2. ✅ Install Requirements

```bash
pip install -r requirements.txt
```

### 3. ✅ Configure Gemini API Key

Create a `.env` file:

```bash
GEMINI_API_KEY=your_actual_gemini_api_key
```

### 4. ✅ Setup MySQL DB via XAMPP

1. Launch XAMPP → Start **Apache** & **MySQL**
2. Visit: [http://localhost/phpmyadmin](http://localhost/phpmyadmin)
3. Run SQL:

```sql
CREATE DATABASE chatbot;
USE chatbot;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) UNIQUE,
  password VARCHAR(255)
);
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 👤 User Flow

1. User registers/login via MySQL database.
2. On successful login, a personalized LangChain memory session starts.
3. Gemini LLM answers the user queries with context.
4. Chat memory persists for the session (can be extended for long-term storage).
5. User can logout anytime.

---

## 🔒 Security Notes

* Passwords are hashed with SHA256 (upgradeable to bcrypt/argon2).
* Gemini API key is stored in `.env` file (never commit this).
* No chat history is stored in database (unless you extend memory to MySQL).

---

## 📈 Possible Extensions

| Feature                          | Status      |
| -------------------------------- | ----------- |
| LangGraph orchestration          | 🔜 Planned  |
| Multi-agent Planner-Executor     | 🔜 Planned  |
| Chat history storage (MySQL)     | 🔜 Optional |
| Admin dashboard                  | 🔜 Optional |
| Tool-augmented answers (PDF/API) | 🔜 Future   |
| Multi-user chat insights         | 🔜 Future   |

---

## 🤝 Contribution

Pull requests, feature suggestions, and feedback are welcome!

---

## 📄 License

[MIT License](LICENSE)

---

## 📬 Contact

**👤 Developed by:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan-695483237/)
**📧 Email:** [iconicemon01@gmail.com](mailto:iconicemon01@gmail.com)
**💬 WhatsApp:** [+8801834363533](https://wa.me/8801834363533)
**💻 GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)

---
