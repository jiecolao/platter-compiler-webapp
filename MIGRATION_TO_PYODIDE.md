# Migration to Pyodide (Static Hosting)

## Overview

The Platter IDE has been migrated from a FastAPI backend to a fully client-side implementation using Pyodide. This allows the entire application to be hosted as a static site without requiring a backend server.

## What Changed

### Before (FastAPI Backend)
- **Backend**: Python FastAPI server running on `localhost:8000`
- **Frontend**: SvelteKit app making HTTP requests to the backend
- **Deployment**: Required hosting both frontend and backend separately
- **Dependencies**: Python virtual environment, uvicorn, FastAPI

### After (Pyodide)
- **Backend**: Removed entirely
- **Frontend**: SvelteKit app with Pyodide running Python directly in the browser
- **Deployment**: Can be hosted as a static site (GitHub Pages, Netlify, Vercel, etc.)
- **Dependencies**: Only Node.js for development

## Technical Details

### Pyodide Integration

1. **Loading Pyodide**: The Python runtime is loaded from CDN on page mount
2. **Python Files**: All Python modules are copied to `frontend/static/python/app/`
3. **Virtual Filesystem**: Python files are loaded into Pyodide's virtual filesystem
4. **Execution**: Python code runs directly in the browser via WebAssembly

### File Structure

```
frontend/
├── static/
│   └── python/
│       └── app/
│           ├── lexer/          # Lexer modules
│           └── parser/         # Parser modules
├── src/
│   └── routes/
│       └── +page.svelte       # Main IDE with Pyodide integration
└── package.json
```

### How It Works

1. **Initialization** (`onMount`):
   - Load Pyodide from CDN
   - Fetch all Python files from `/python/app/`
   - Create directory structure in Pyodide's virtual filesystem
   - Write Python files to virtual filesystem

2. **Lexical Analysis**:
   ```javascript
   pyodide.globals.set('code_input', codeInput);
   const tokensProxy = await pyodide.runPythonAsync(`
     from app.lexer.lexer import Lexer
     lexer = Lexer(code_input)
     # ... tokenize and return results
   `);
   ```

3. **Syntax Analysis**:
   ```javascript
   pyodide.globals.set('code_input', codeInput);
   const result = await pyodide.runPythonAsync(`
     from app.parser.parser import Parser
     # ... parse and return results
   `);
   ```

## Benefits

✅ **No Backend Required**: Entire app runs in the browser
✅ **Easy Deployment**: Deploy to any static hosting service
✅ **Offline Capable**: Works offline once loaded
✅ **No Server Costs**: No need to pay for backend hosting
✅ **Same Python Code**: All original Python code remains unchanged

## Trade-offs

⚠️ **Initial Load Time**: ~6-10MB Pyodide download on first visit
⚠️ **First Run Delay**: Python interpreter startup takes a moment
⚠️ **Browser Only**: Requires modern browser with WebAssembly support

## Development

### Running Locally

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:5173`

### Building for Production

```bash
cd frontend
npm run build
npm run preview
```

### Deploying

The built files in `frontend/build/` can be deployed to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

## Removed Files/Dependencies

- `backend/main.py` (FastAPI server) - No longer needed
- `backend/requirements.txt` - No longer needed for frontend
- Backend-related npm scripts (`start:dev`, `stop:dev`, etc.)
- Server manager scripts

## Python Files Location

All Python files are now in:
- **Source**: `backend/app/` (original location)
- **Static**: `frontend/static/python/app/` (copied for Pyodide)

When updating Python code, you need to:
1. Update files in `backend/app/`
2. Copy to `frontend/static/python/app/`
3. Rebuild/restart dev server

## Browser Compatibility

Requires browsers with WebAssembly support:
- Chrome 57+
- Firefox 52+
- Safari 11+
- Edge 79+

## Performance Notes

- **First Load**: 6-10 seconds (Pyodide download + initialization)
- **Subsequent Loads**: Instant (cached)
- **Analysis Speed**: Similar to backend (Python runs at ~50% native speed in WebAssembly)
