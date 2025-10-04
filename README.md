# [❓] Insert Project Name

<div align="center">
  <img src="assets/project-logo.png" alt="Project Logo" style="width: min(200px, 50vw); height: auto; max-width: 100%;">
</div>

<!-- The description of your project would go here... -->
Insert project description here...

## [📋] Table of Contents

<table width="100%">
  <tr>
    <th style="width: auto; white-space: nowrap;">Section</th>
    <th style="width: 100%;">Description</th>
  </tr>
  <tr>
    <td style="white-space: nowrap;">🧑‍💻 Contributors</td>
    <td>Meet the team behind this project</td>
  </tr>
  <tr>
    <td style="white-space: nowrap;">⚙️ Tech Stack</td>
    <td>Technologies, frameworks, APIs used in development</td>
  </tr>
  <tr>
    <td style="white-space: nowrap;">📁 Project Structure</td>
    <td>Organization of the codebase and purposes of different directories</td>
  </tr>
  <tr>
    <td style="white-space: nowrap;">🔰 Getting Started</td>
    <td>Local setup instructions and prerequisites</td>
  </tr>
</table>

## [🧑‍💻] Contributors

<table width="100%">
  <tr>
    <th style="width: auto; white-space: nowrap;">Name</th>
    <th style="width: auto; white-space: nowrap;">Role</th>
    <th style="width: 100%;">GitHub</th>
  </tr>
  <tr>
    <td style="white-space: nowrap;">Jason Matthew Suhari</td>
    <td style="white-space: nowrap;">Frontend, Backend, Data</td>
    <td><a href="https://github.com/username">@jasonmatthewsuhari</a></td>
  </tr>
  <tr>
    <td style="white-space: nowrap;">Person B</td>
    <td style="white-space: nowrap;">Role</td>
    <td><a href="https://github.com/username">@username</a></td>
  </tr>
  <tr>
    <td style="white-space: nowrap;">Person C</td>
    <td style="white-space: nowrap;">Role</td>
    <td><a href="https://github.com/username">@username</a></td>
  </tr>
  <tr>
    <td style="white-space: nowrap;">Person D</td>
    <td style="white-space: nowrap;">Role</td>
    <td><a href="https://github.com/username">@username</a></td>
  </tr>
</table>

## [⚙️] Tech Stack
<!-- Make sure to use and remove these badges as required  -->

### Frontend
[![Next.js][Next.js]][Next-url]
[![React][React.js]][React-url]
[![TypeScript][TypeScript]][TypeScript-url]
[![TailwindCSS][TailwindCSS]][TailwindCSS-url]
[![ESLint][ESLint]][ESLint-url]
[![PNPM][PNPM]][PNPM-url]

### Backend
[![FastAPI][FastAPI]][FastAPI-url]
[![Python][Python]][Python-url]
[![Pytest][Pytest]][Pytest-url]

### Databases & Storage
[![PostgreSQL][PostgreSQL]][PostgreSQL-url]
[![MongoDB][MongoDB]][MongoDB-url]
[![Neo4j][Neo4j]][Neo4j-url]
[![Supabase][Supabase]][Supabase-url]
[![ChromaDB][ChromaDB]][ChromaDB-url]
[![FAISS][FAISS]][FAISS-url]

### Data Warehouses
[![BigQuery][BigQuery]][BigQuery-url]
[![Snowflake][Snowflake]][Snowflake-url]

### External APIs & Services
[![Google Auth][Google-Auth]][Google-Auth-url]
[![Telegram][Telegram]][Telegram-url]
[![Alpha Vantage][Alpha-Vantage]][Alpha-Vantage-url]
[![Yahoo Finance][Yahoo-Finance]][Yahoo-Finance-url]
[![NewsAPI][NewsAPI]][NewsAPI-url]

### AI/ML & OCR
[![OpenAI][OpenAI]][OpenAI-url]
[![PyMuPDF][PyMuPDF]][PyMuPDF-url]
[![EasyOCR][EasyOCR]][EasyOCR-url]

## [📁] Project Structure

```
├── frontend/          # Next.js frontend application
│   ├── src/
│   │   ├── app/       # App Router pages
│   │   └── components/ # Reusable UI components
│   └── .json
├── backend/           # FastAPI backend application
│   ├── apps/          # Application modules
│   │   ├── app-a/     # Sample app module
│   │   └── shared_utils/ # Shared utilities and connectors
│   ├── main.py        # FastAPI entry point
│   └── tests/         # Test suite
└── data/              # Data storage
```

## [🔰] Getting Started

### Prerequisites
- **Conda/Miniconda**: [Install here](https://docs.anaconda.com/miniconda/install/)
- **Node.js 18+**: [Install here](https://nodejs.org/)
- **Git**: For cloning the repository

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd hackathon-template
   ```

2. **Run the setup script** (handles Python environment & backend dependencies)
   ```bash
   bash setup.bash
   ```

3. **Setup Frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Start Backend** (in a separate terminal)
   ```bash
   # Make sure conda environment is activated
   conda activate hackathon-template-env
   cd backend
   python main.py
   ```

### What setup.bash does:
- Creates a conda environment with Python 3.10
- Installs and upgrades pip, setuptools, wheel, and pip-tools
- Compiles `requirements.in` to `requirements.txt`
- Installs all Python dependencies using pip-sync

<!-- MARKDOWN LINKS & IMAGES -->
[Next.js]: https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[TypeScript]: https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white
[TypeScript-url]: https://www.typescriptlang.org/
[TailwindCSS]: https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white
[TailwindCSS-url]: https://tailwindcss.com/
[ESLint]: https://img.shields.io/badge/ESLint-4B3263?style=for-the-badge&logo=eslint&logoColor=white
[ESLint-url]: https://eslint.org/
[PNPM]: https://img.shields.io/badge/pnpm-F69220?style=for-the-badge&logo=pnpm&logoColor=white
[PNPM-url]: https://pnpm.io/
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Pytest]: https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[MongoDB]: https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/
[Neo4j]: https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white
[Neo4j-url]: https://neo4j.com/
[Supabase]: https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white
[Supabase-url]: https://supabase.com/
[ChromaDB]: https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMSA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDMgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K&logoColor=white
[ChromaDB-url]: https://www.trychroma.com/
[FAISS]: https://img.shields.io/badge/FAISS-4285F4?style=for-the-badge&logo=meta&logoColor=white
[FAISS-url]: https://faiss.ai/
[BigQuery]: https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white
[BigQuery-url]: https://cloud.google.com/bigquery
[Snowflake]: https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white
[Snowflake-url]: https://www.snowflake.com/
[Google-Auth]: https://img.shields.io/badge/Google_Auth-4285F4?style=for-the-badge&logo=google&logoColor=white
[Google-Auth-url]: https://developers.google.com/identity
[Telegram]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://telegram.org/
[Alpha-Vantage]: https://img.shields.io/badge/Alpha_Vantage-1E3A8A?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIgMkwyMiAyTDIwIDIyTDIgMjJMMiAyWiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+&logoColor=white
[Alpha-Vantage-url]: https://www.alphavantage.co/
[Yahoo-Finance]: https://img.shields.io/badge/Yahoo_Finance-720E9E?style=for-the-badge&logo=yahoo&logoColor=white
[Yahoo-Finance-url]: https://finance.yahoo.com/
[NewsAPI]: https://img.shields.io/badge/NewsAPI-FF6B35?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQgNkg5VjExSDRWNlpNMTEgNkgxNlYxMUgxMVY2Wk00IDEzSDlWMThINFYxM1pNMTEgMTNIMTZWMThIMTFWMTNaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K&logoColor=white
[NewsAPI-url]: https://newsapi.org/
[OpenAI]: https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white
[OpenAI-url]: https://openai.com/
[PyMuPDF]: https://img.shields.io/badge/PyMuPDF-FF4B4B?style=for-the-badge&logo=python&logoColor=white
[PyMuPDF-url]: https://pymupdf.readthedocs.io/
[EasyOCR]: https://img.shields.io/badge/EasyOCR-00D2FF?style=for-the-badge&logo=python&logoColor=white
[EasyOCR-url]: https://github.com/JaidedAI/EasyOCR
