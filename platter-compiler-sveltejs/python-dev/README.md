# Backend - Python Compiler Modules

**Note**: This directory contains the **source of truth** for Python compiler code, but does **NOT** run as a backend server.

## Purpose

The `backend/` directory serves as:

1. **Python Code Repository**: The canonical source for all compiler logic
2. **Development Environment**: Where Python modules are edited and tested
3. **Testing Suite**: Unit tests for lexer and parser modules

## Directory Structure

```
backend/
├── app/                    # Core compiler modules (SOURCE OF TRUTH)
│   ├── lexer/             # Lexical analysis
│   │   ├── lexer.py       # Main lexer
│   │   ├── token.py       # Token definitions
│   │   ├── keywords.py    # Keyword handling
│   │   └── ...
│   └── parser/            # Syntax analysis
│       ├── parser.py      # Main parser
│       ├── first_set.py   # First set computation
│       └── ...
├── tests/                 # Unit tests
│   ├── test_parser.py    # Parser tests
│   └── ...
├── requirements.txt       # Python dependencies
└── main.py               # [ARCHIVED] FastAPI server (not used)
```

## Development Workflow

### 1. Edit Python Code

Make changes directly in `backend/app/`:

```bash
backend/app/lexer/lexer.py
backend/app/parser/parser.py
```

### 2. Run Tests

```bash
cd backend
python -m pytest tests/
```

### 3. Sync to Frontend

After making changes, sync to the frontend:

```bash
# From project root
npm run sync-python

# This copies backend/app/ → frontend/static/python/app/
```

### 4. Test in Browser

Start the frontend and test your changes:

```bash
npm start
```

## Setting Up Python Environment

### Create Virtual Environment

```bash
cd backend
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# From backend directory
python -m pytest tests/

# With verbose output
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_parser.py -v
```

## Module Overview

### Lexer (`app/lexer/`)

- **lexer.py**: Main lexical analyzer
- **token.py**: Token type definitions and Token class
- **keywords.py**: Platter language keywords
- **operators.py**: Operator tokenization
- **numericals.py**: Number literal handling
- **identifiers.py**: Identifier/variable name handling
- **char_com.py**: Character and comment handling

### Parser (`app/parser/`)

- **parser.py**: Main syntax parser
- **first_set.py**: First set computation for LL(1) parsing
- **follow_set.py**: Follow set computation
- **predict_set.py**: Predictive parsing table generation
- **token_map.py**: Token type mapping utilities

## Architecture

```
┌──────────────────────────────────────┐
│  backend/app/                        │
│  (Edit Here)                         │
│  ┌────────────┐    ┌──────────────┐ │
│  │   lexer/   │    │   parser/    │ │
│  └────────────┘    └──────────────┘ │
└──────────────┬───────────────────────┘
               │
               │ sync-python.js
               ↓
┌──────────────────────────────────────┐
│  frontend/static/python/app/         │
│  (Auto-synced)                       │
│  ┌────────────┐    ┌──────────────┐ │
│  │   lexer/   │    │   parser/    │ │
│  └────────────┘    └──────────────┘ │
└──────────────┬───────────────────────┘
               │
               │ Loaded by Pyodide
               ↓
┌──────────────────────────────────────┐
│  Browser (WebAssembly)               │
│  Runs Python in-browser              │
└──────────────────────────────────────┘
```

## Why Not Run as a Server?

Previously, this directory contained a FastAPI server (`main.py`). We've migrated to a **frontend-only architecture** using Pyodide:

✅ **No server setup required**  
✅ **Easier deployment** (static hosting)  
✅ **Offline capable**  
✅ **No CORS issues**  
✅ **Same functionality**

The `main.py` file remains for reference but is not used in production.

## Testing New Features

1. Write Python code in `backend/app/`
2. Add tests in `backend/tests/`
3. Run `pytest` to verify
4. Sync to frontend: `npm run sync-python`
5. Test in browser: `npm start`

## Python Dependencies

See `requirements.txt` for development dependencies. For production (Pyodide), only pure Python packages are supported.

## Best Practices

- ✅ Always edit code in `backend/app/`, not `frontend/static/python/`
- ✅ Run tests before syncing to frontend
- ✅ Keep modules pure Python (no binary dependencies)
- ✅ Use type hints for better IDE support
- ✅ Document complex algorithms

## Common Tasks

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_parser.py

# Sync to frontend after changes
cd ..
npm run sync-python

# Start frontend for testing
npm start
```
