Excellent. Since the Gemini API is working, Phase 1 is about building the foundation correctly. Most AI projects become messy because people start with agents before establishing architecture.

# Phase 1 Goal

At the end of Phase 1 you should have:

```text
devforge-ai/
│
├── backend/
│
├── frontend/
│
├── docs/
│
├── .gitignore
│
├── README.md
│
└── requirements.txt
```

No agents yet.

No LangGraph yet.

Just a clean foundation.

---

# Step 1: Create Repository

```bash
mkdir devforge-ai
cd devforge-ai

git init
```

Create GitHub repository:

```text
devforge-ai
```

Push initial commit:

```bash
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

---

# Step 2: Create Backend

Inside root:

```bash
mkdir backend
cd backend
```

Create virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python -m venv venv
source venv/bin/activate
```

---

# Step 3: Install Core Dependencies

For Version 1:

```bash
pip install fastapi
pip install uvicorn
pip install langgraph
pip install langchain
pip install langchain-google-genai
pip install python-dotenv
pip install pydantic
pip install sqlalchemy
```

Freeze:

```bash
pip freeze > requirements.txt
```

Move requirements file to root later.

---

# Why These Packages?

### FastAPI

Backend API.

```text
React
  ↓
FastAPI
  ↓
LangGraph
  ↓
Gemini
```

---

### LangGraph

Agent orchestration.

```text
PM
 ↓
Architect
 ↓
Backend
 ↓
Frontend
 ↓
QA
```

---

### Pydantic

Structured data validation.

Without it:

```python
{
  "requirements": "..."
}
```

can break unexpectedly.

With Pydantic:

```python
class Requirements(BaseModel):
    ...
```

you get validation and type safety.

---

### SQLAlchemy

SQLite integration.

Needed later for:

* history
* workflow runs
* report storage

---

# Step 4: Backend Folder Structure

Create:

```text
backend/
│
├── agents/
│
├── graph/
│
├── prompts/
│
├── services/
│
├── api/
│
├── database/
│
├── schemas/
│
├── tests/
│
├── .env
│
├── config.py
│
└── main.py
```

---

# Why This Structure?

A common beginner mistake:

```text
app.py
agent.py
agent2.py
agent3.py
```

Everything eventually becomes tangled.

Instead:

### agents/

Only agent logic.

### graph/

Only LangGraph workflow.

### services/

External services.

Example:

```python
Gemini
OpenRouter
PDF generation
```

---

# Step 5: Environment Variables

Create:

```text
backend/.env
```

```env
GOOGLE_API_KEY=xxxxxxxx
```

Never commit this file.

---

Add root `.gitignore`

```gitignore
venv/
.env
__pycache__/
*.pyc
node_modules/
dist/
```

---

# Step 6: Configuration Layer

Create:

```text
backend/config.py
```

Purpose:

```python
load_dotenv()
read API keys
provide settings
```

Why?

So agents never directly access environment variables.

Bad:

```python
os.getenv(...)
```

inside every file.

Good:

```python
settings.google_api_key
```

through a central config.

---

# Step 7: Build Gemini Service First

Create:

```text
backend/services/
    gemini_client.py
```

This should be the **only place** talking to Gemini.

Future architecture:

```text
Agent
 ↓
LLM Service
 ↓
Gemini
```

NOT

```text
Agent
 ↓
Gemini
```

This abstraction is critical.

Later you can swap:

```text
Gemini
↓
OpenRouter
↓
Claude
↓
DeepSeek
```

without touching agents.

---

# Step 8: Create FastAPI Skeleton

Create:

```text
backend/main.py
```

with a single endpoint:

```text
GET /
```

Expected response:

```json
{
  "message": "DevForge AI Backend Running"
}
```

Verify:

```bash
uvicorn main:app --reload
```

Open:

```text
http://localhost:8000
```

and

```text
http://localhost:8000/docs
```

FastAPI Swagger should appear.

---

# Step 9: Frontend Setup

Return to root:

```bash
npm create vite@latest frontend
```

Choose:

```text
React
JavaScript
```

Install:

```bash
cd frontend
npm install
```

Run:

```bash
npm run dev
```

Verify:

```text
http://localhost:5173
```

works.

---

# Step 10: Create Docs Folder

Create:

```text
docs/
```

Inside:

```text
docs/
│
├── architecture/
│
├── screenshots/
│
└── diagrams/
```

Recruiters love visual documentation.

Most students skip this.

---

# Deliverable for End of Phase 1

You should have:

```text
✓ GitHub repository

✓ FastAPI running

✓ React running

✓ Gemini API tested

✓ Virtual environment

✓ Folder structure

✓ .env setup

✓ Configuration layer

✓ Gemini service skeleton

✓ Documentation folders
```

Do **not** build any agents yet.

The next phase should start with designing the shared workflow state (`WorkflowState`) and agent contracts. Those two decisions determine the entire LangGraph architecture and are much harder to change later than code.
