# Archived - Backend Server Files

This directory contains the **archived backend server implementation** that is **no longer used** in production.

## ⚠️ Important Notice

The Platter Compiler Webapp now runs **entirely in the browser** using [Pyodide](https://pyodide.org/). The FastAPI server in this directory is **not required** and **not maintained**.

## Migration Status

- ✅ **Migrated**: All functionality now runs client-side via Pyodide
- ✅ **Archived**: `main.py` and server code kept for reference only
- ✅ **Active**: Python modules in `app/` are still the source of truth (synced to frontend)

## What's Here

- **`main.py`**: Archived FastAPI server (not used)
- **`test_main.http`**: HTTP test file for the old API (not used)
- **`app/`**: ✅ **ACTIVE** - Python compiler modules (source of truth)
- **`tests/`**: ✅ **ACTIVE** - Unit tests for Python modules

## Active vs Archived

| File/Directory | Status | Purpose |
|----------------|--------|---------|
| `app/` | ✅ **ACTIVE** | Source of truth for Python code |
| `tests/` | ✅ **ACTIVE** | Unit tests for modules |
| `requirements.txt` | ✅ **ACTIVE** | Development dependencies |
| `main.py` | ❌ **ARCHIVED** | Old FastAPI server (reference only) |
| `test_main.http` | ❌ **ARCHIVED** | Old API tests (reference only) |

## Why Was It Archived?

We migrated from a client-server architecture to a **pure frontend** approach:

### Old Architecture (Archived)
```
Browser → HTTP → FastAPI Server → Python Lexer/Parser → JSON Response
```

### New Architecture (Current)
```
Browser → Pyodide (WebAssembly) → Python Lexer/Parser → Results
```

### Benefits of Migration

✅ **No Server Required**: Runs entirely in the browser  
✅ **Easier Deployment**: Static hosting (GitHub Pages, Netlify, etc.)  
✅ **Offline Capable**: Works without internet connection  
✅ **No CORS Issues**: All processing is client-side  
✅ **Faster for Users**: No network latency  
✅ **Lower Costs**: No server hosting needed  

## If You Need the Server

The server code is preserved but not actively maintained. If you need to run it:

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload

# Server runs on http://localhost:8000
```

However, **the frontend no longer calls this server**. The frontend uses Pyodide exclusively.

## Current Workflow

See the main [README.md](../README.md) for the current development workflow:

1. Edit Python code in `backend/app/`
2. Run tests: `python -m pytest tests/`
3. Sync to frontend: `npm run sync-python`
4. Test in browser: `npm start`

## Questions?

- See [README.md](README.md) for Python module documentation
- See [../MIGRATION_TO_PYODIDE.md](../MIGRATION_TO_PYODIDE.md) for migration details
- See [../README.md](../README.md) for overall project documentation
