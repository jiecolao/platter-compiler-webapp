# Architecture Documentation

## Overview

Platter Compiler Webapp is a fully client-side application that runs Python code in the browser using Pyodide (WebAssembly). This architecture eliminates the need for a backend server and enables static hosting.

## System Architecture

```
┌─────────────────────────────────────────┐
│         Browser (localhost:5173)        │
│  ┌───────────────────────────────────┐  │
│  │     SvelteKit Frontend            │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │   Pyodide (WebAssembly)     │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │  Python Modules       │  │  │  │
│  │  │  │  - app.lexer.*       │  │  │  │
│  │  │  │  - app.parser.*      │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## Technology Stack

### Frontend Layer
- **Framework**: SvelteKit 2.x
  - Server-side rendering (SSR) for static generation
  - File-based routing
  - Built-in TypeScript support
- **Styling**: Tailwind CSS 4.x
  - Utility-first CSS framework
  - Custom theme configuration
- **Code Editor**: CodeMirror 5
  - Syntax highlighting for Platter language
  - Error markers and line highlighting
- **Build Tool**: Vite 7.x
  - Fast HMR (Hot Module Replacement)
  - Optimized production builds

### Python Runtime
- **Pyodide 0.29.x**
  - Python 3.11 compiled to WebAssembly
  - Runs Python directly in the browser
  - No backend server required
  - Virtual filesystem for Python modules

## Component Architecture

### Frontend Components

```
src/
├── routes/
│   ├── +page.svelte          # Main IDE interface
│   ├── +layout.svelte        # App layout wrapper
│   └── +layout.ts            # Layout configuration
└── lib/
    ├── assets/               # Static assets
    └── utils/
        └── browser.ts        # Browser utilities
```

### Python Modules

```
static/python/app/
├── lexer/                    # Lexical analyzer
│   ├── lexer.py             # Main lexer
│   ├── token.py             # Token definitions
│   ├── keywords.py          # Keyword handling
│   ├── operators.py         # Operator tokenization
│   ├── numericals.py        # Number literals
│   ├── identifiers.py       # Variable names
│   └── char_com.py          # Characters & comments
└── parser/                   # Syntax analyzer
    ├── parser.py            # Main parser
    ├── first_set.py         # First set computation
    ├── follow_set.py        # Follow set computation
    ├── predict_set.py       # Predictive parsing table
    └── token_map.py         # Token mapping
```

## Data Flow

### Lexical Analysis Flow

```
User Input (Platter Code)
    ↓
JavaScript (SvelteKit)
    ↓
Pyodide Runtime
    ↓
Python Lexer (app.lexer)
    ↓
Token List
    ↓
JavaScript/Svelte UI
    ↓
Display Results
```

### Syntax Analysis Flow

```
Token List
    ↓
Python Parser (app.parser)
    ↓
Parse Tree / Error Messages
    ↓
JavaScript/Svelte UI
    ↓
Display Parse Results
```

## Pyodide Integration

### Initialization

1. **Load Pyodide**: CDN or local bundle (~6-10MB)
2. **Fetch Python Files**: Load from `/static/python/app/`
3. **Create Virtual Filesystem**: Write files to Pyodide's virtual FS
4. **Import Modules**: Import lexer and parser modules

### Execution

```javascript
// Example: Running lexical analysis
const code = "int main() { return 0; }";
const result = await pyodide.runPythonAsync(`
from app.lexer.lexer import Lexer
lexer = Lexer('''${code}''')
tokens = lexer.tokenize()
tokens
`);
```

## Deployment Architecture

### Local Development

```
npm start → Vite Dev Server (port 5173) → Browser
```

### Production Deployment

```
npm run build
    ↓
Static Files (platter-compiler-sveltejs/build/)
    ↓
Static Host (GitHub Pages, Netlify, Vercel)
    ↓
Users' Browsers
```

## GitHub Actions Workflow

### Build & Deploy Pipeline

```yaml
Python Tests → Frontend Build → Deploy to GitHub Pages
```

**Steps**:
1. Run Python unit tests (`platter-compiler-sveltejs/python-dev/tests/`)
2. Build SvelteKit app with `BASE_PATH=/Platter`
3. Upload artifacts
4. Deploy to GitHub Pages

## Security Considerations

### Client-Side Execution
- All Python code runs in WebAssembly sandbox
- No server-side code execution
- No data sent to external servers
- User code never leaves the browser

### Dependencies
- Pyodide from official CDN (integrity verified)
- npm packages from official registry
- SvelteKit security best practices

## Performance Characteristics

### Initial Load
- **First Visit**: ~6-10MB Pyodide download + app bundle
- **Cached Visit**: Instant (service worker caching)
- **Pyodide Initialization**: ~2-3 seconds

### Runtime Performance
- **Lexical Analysis**: < 100ms for typical code
- **Syntax Analysis**: < 200ms for typical code
- **Memory Usage**: ~50-100MB (Pyodide + app)

### Optimization Strategies
- Lazy Pyodide loading (only on first analysis)
- Browser caching for Pyodide and Python modules
- Code splitting for SvelteKit app
- Minified production builds

## File System Layout

### Production Build

```
build/
├── _app/
│   ├── immutable/         # Versioned assets
│   └── version.json       # Build version
├── python/
│   └── app/              # Python modules
├── index.html            # Main entry point
└── favicon.png           # App icon
```

## Development Workflow

### Edit-Refresh Cycle

1. Edit Python files in `static/python/app/`
2. Refresh browser (Vite HMR for frontend changes)
3. For Python changes: Hard refresh (Ctrl+Shift+R)

### Testing Workflow

```bash
# Python tests (pytest)
npm run test

# Frontend E2E tests (Playwright)
npm run test:frontend
```

## Browser Compatibility

### Supported Browsers
- **Chrome/Edge**: 90+ ✅
- **Firefox**: 88+ ✅
- **Safari**: 14+ ✅

### Requirements
- WebAssembly support
- ES6+ JavaScript support
- LocalStorage API

## Limitations

### Pyodide Limitations
- First load is slow (~6-10MB download)
- Limited Python package support (pure Python only)
- No C extensions without compilation

### Application Limitations
- No server-side persistence
- No multi-user collaboration features
- Limited to browser memory constraints

## Future Enhancements

### Potential Improvements
- Progressive Web App (PWA) for offline use
- WebWorker for Python execution (non-blocking UI)
- Code completion and IntelliSense
- Multi-file project support
- Export to executable formats

## Troubleshooting

### Common Issues

**Pyodide fails to load**
- Check browser console for CORS errors
- Verify CDN connectivity
- Clear browser cache

**Python changes not reflected**
- Hard refresh browser (Ctrl+Shift+R)
- Clear Pyodide cache
- Verify file paths in `/static/python/app/`

**Slow first analysis**
- Normal behavior (Pyodide initialization)
- Subsequent analyses are fast
- Consider showing loading indicator

## References

- [Pyodide Documentation](https://pyodide.org/)
- [SvelteKit Documentation](https://kit.svelte.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
