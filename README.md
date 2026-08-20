<div align="center">

# 🔗 URL Shortener API

**A simple, fast URL shortening service built with FastAPI, SQLAlchemy, and PostgreSQL.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## ✨ Features

- 🔗 Shorten any valid URL into a unique 6-character short code
- ↪️ Instant redirect from short code to original URL
- 🔐 Cryptographically secure code generation (via Python's `secrets` module)
- ✅ Request/response validation with Pydantic
- 🗄️ PostgreSQL-backed persistence

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Server | Uvicorn |

---

## 📁 Project Structure

```
.
├── main.py         # API routes and app entry point
├── crud.py         # Database operations (create/read logic)
├── models.py       # SQLAlchemy models (URL table schema)
├── database.py     # Database connection and session setup
├── schemas.py      # Pydantic request/response schemas
└── __init__.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL running locally or remotely

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/adarsh-ach/<your-repo-name>.git
cd <your-repo-name>
```

**2. Install dependencies**
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pydantic
```

**3. Set up your environment variables**

Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<db_name>
```

**4. Run the server**
```bash
uvicorn main:app --reload
```

The API will be live at **http://localhost:8000** 🎉

---

## 📡 API Endpoints

### `GET /`
Health check — confirms the API is running.

<details>
<summary>Response</summary>

```json
{ "message": "URL Shortener API is running" }
```
</details>

---

### `POST /shorten`
Creates a shortened URL.

<details open>
<summary><b>Request Body</b></summary>

```json
{ "url": "https://example.com/some/very/long/link" }
```
</details>

<details open>
<summary><b>Response</b></summary>

```json
{
  "short_code": "aZ3xQ9",
  "short_url": "http://localhost:8000/aZ3xQ9"
}
```
</details>

---

### `GET /{short_code}`
Redirects to the original URL associated with the short code.

| Status | Meaning |
|---|---|
| `307` | Redirects to original URL |
| `404` | Short code not found |

---

## 📖 Interactive API Docs

FastAPI auto-generates interactive documentation out of the box:

- **Swagger UI** → `http://localhost:8000/docs`
- **ReDoc** → `http://localhost:8000/redoc`

---

## 🗺️ Roadmap

- [ ] Click tracking / analytics
- [ ] Custom short code aliases
- [ ] Link expiration
- [ ] Rate limiting

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Built by **[Adarsh Acharya](https://github.com/adarsh-ach)**

</div>
