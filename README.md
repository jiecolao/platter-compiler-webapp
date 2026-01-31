# Platter Compiler Webapp

A browser-based IDE for the Platter programming language, featuring lexical and syntax analysis powered by Pyodide (Python WebAssembly runtime).

## ✨ Features

- **Browser-Based**: Runs completely in your browser, no server required
- **Lexical Analysis**: Tokenize Platter code with detailed token information
- **Syntax Analysis**: Parse and validate code structure
- **Fast**: Python analysis runs client-side via WebAssembly
- **File Operations**: Open and save `.platter` files
- **Modern UI**: Dark/light theme with syntax highlighting
- **Static Deployment**: Works on GitHub Pages, Netlify, Vercel, etc.

## 🚀 Quick Start

### Windows
```cmd
Platter-Start.bat
```

### Command Line
```bash
npm start
```

Then open http://localhost:5173

### First Time Setup
```bash
npm run install-all
```

## 📦 Project Structure

```
platter-compiler-webapp/
├── platter-compiler-sveltejs/     # SvelteKit application
│   ├── src/                       # Frontend source code
│   ├── static/python/app/         # Python compiler (runs via Pyodide)
│   ├── python-dev/                # Tests & development files
│   └── package.json
├── Platter-Start.bat              # Quick start script
└── package.json                   # Root scripts
```

## 💻 Development

### Edit Python Code
```bash
# Edit files in:
platter-compiler-sveltejs/static/python/app/lexer/
platter-compiler-sveltejs/static/python/app/parser/

# Refresh browser to see changes - no build needed!
```

### Testing
```bash
npm run test              # Python unit tests (runs automatically)
npm run test:frontend     # E2E tests
```

**Note**: The test command automatically runs Python unit tests using unittest. No Python environment setup required!

### Building
```bash
npm run build            # Build for production
npm run preview          # Preview build locally
```

Deploy `platter-compiler-sveltejs/build/` to any static host.

## 🛠️ Technology Stack

- **Frontend**: SvelteKit 2.x, Tailwind CSS 4.x
- **Editor**: CodeMirror 5
- **Python Runtime**: Pyodide 0.29.x (WebAssembly)
- **Build Tool**: Vite 7.x

## 📖 Documentation

- [Architecture.md](Architecture.md) - Technical architecture details
- [platter-compiler-sveltejs/README.md](platter-compiler-sveltejs/README.md) - Frontend docs
- [platter-compiler-sveltejs/python-dev/README.md](platter-compiler-sveltejs/python-dev/README.md) - Python development

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes in `platter-compiler-sveltejs/static/python/app/`
4. Test your changes
5. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## ❓ FAQ

**Q: Do I need Python installed?**  
A: Not for running the app! Pyodide runs Python in the browser. Python is only needed for running tests.

**Q: Why is the first analysis slow?**  
A: Pyodide loads ~6-10MB on first use (cached after). This only happens once per browser session.

**Q: Can I deploy to GitHub Pages?**  
A: Yes! Run `npm run build` and deploy the `platter-compiler-sveltejs/build/` directory.

**Q: Where is the backend?**  
A: There isn''t one! Everything runs client-side via Pyodide.
