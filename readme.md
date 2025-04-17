# ⚡ FastAPI SaaS Starter

A production-ready, modular, and scalable **FastAPI starter project** — designed for SaaS, AI tools, microservices, and clean architecture lovers.

> 🔥 Built to be your **go-to backend base** — whether you're launching a startup, hacking a side project, or contributing to open source.

---

## 🚀 Features

- ✅ Clean architecture with modular `domains/`
- ✅ Global exception handling + standardized responses
- ✅ Built-in request logging middleware
- ✅ Flexible service/repository pattern
- ✅ Pydantic-based input validation
- ✅ Response formatting for success & error payloads
- ✅ Ready for AI, LangChain, OpenAI, Weaviate, etc.
- ✅ Open-source friendly — fork and start building now

---

## 🧱 Project Structure

```
app/
├── config/              # App settings & environment
├── domains/             # Feature modules (auth, user, file, etc.)
├── infrastructure/      # DB, LangChain, OpenAI, storage, vector
├── server/              # Runtime layer: exceptions, middlewares, routers
├── shared/              # Reusable logic, dependencies, shared repos
├── main.py              # FastAPI app entrypoint
```

> 🧠 Designed for clarity, extensibility, and open-source scale.

---

## 📆 Tech Stack

- **FastAPI** – blazing-fast web framework
- **Pydantic** – powerful validation & serialization
- **Starlette** – high-performance ASGI toolkit
- **Optional AI Stack** – LangChain, OpenAI, Weaviate (optional integrations)

---

## 🛠️ Getting Started

```bash
git clone https://github.com/your-username/fastapi-saas-starter.git
cd fastapi-saas-starter

# Install dependencies
poetry install
# or
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```

> ⚙️ Make sure to configure your environment in `app/config/settings.py`

---

## 🎯 Example API Response

### ✅ Success

```json
{
  "success": true,
  "data": { "id": 1, "name": "John Doe" },
  "message": "User retrieved successfully"
}
```

### ❌ Error

```json
{
  "success": false,
  "error": {
    "message": "Invalid token",
    "status_code": 401,
    "type": "UNAUTHORIZED"
  }
}
```

---

## 📁 Modular Domains Example

```bash
app/
└── domains/
    └── user/
        ├── router.py
        ├── schema.py
        ├── service.py
        └── repository.py
```

> 💡 Add new features by creating a new folder in `domains/`

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -am 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a pull request 🙌

---

## 📄 License

MIT License — free to use, modify, and build on.

---

## 💬 Need Help?

Open an issue or reach out on [LinkedIn](https://linkedin.com/in/developeranku)

---

## ⭐️ Like This?

Give it a star — and help others discover clean FastAPI apps!
