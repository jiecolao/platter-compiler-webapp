# Quick Start - Platter Compiler Webapp

## 🚀 Running the Application

The Platter IDE now runs entirely in your browser using Pyodide (Python in WebAssembly). No backend server needed!

### Start Development Server

```bash
cd frontend
npm install
npm run dev
```

Then open: **http://localhost:5173**

That's it! 🎉

## 📍 What Changed?

✅ **No Backend Server**: Python runs directly in the browser via Pyodide  
✅ **Static Hosting**: Can be deployed to GitHub Pages, Netlify, Vercel, etc.  
✅ **Offline Capable**: Works offline once loaded  
✅ **Same Features**: All lexical and syntax analysis works the same

## 🛠️ First Time Setup

```bash
# Install frontend dependencies  
cd frontend
npm install
```

## 🏗️ Building for Production

```bash
cd frontend
npm run build
npm run preview
```

The built files in `frontend/build/` can be deployed to any static hosting service.

## 📚 More Information

- See `MIGRATION_TO_PYODIDE.md` for technical details about the migration
- The original Python code in `backend/app/` is still used, but copied to `frontend/static/python/app/`
- Pyodide downloads ~6-10MB on first load (cached afterwards)

## ⚠️ Note

The first time you click "Lexical" or "Syntax", there will be a brief delay while Pyodide initializes. This is normal and only happens once per session.