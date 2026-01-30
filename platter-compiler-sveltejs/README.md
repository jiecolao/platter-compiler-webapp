# Platter IDE Frontend

A SvelteKit-based IDE for the Platter programming language, running Python analysis directly in the browser via Pyodide.

## Features

- **Lexical Analysis**: Tokenize Platter code
- **Syntax Analysis**: Parse and validate Platter syntax
- **Code Editor**: CodeMirror integration with syntax highlighting
- **Error Highlighting**: Visual error markers in the editor
- **Dark/Light Theme**: Toggle between themes
- **File Operations**: Open and save `.platter` files
- **Python in Browser**: Uses Pyodide to run Python analysis without a backend

## Developing

Install dependencies and start the development server:

```sh
npm install
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

The app will be available at `http://localhost:5173`

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

## Deployment

The built app is fully static and can be deployed to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

The `build/` directory contains all necessary files.

## Python Integration

Python code from `../backend/app/` is copied to `static/python/app/` and loaded into Pyodide's virtual filesystem at runtime. The Python modules are:

- `app.lexer.*` - Lexical analysis
- `app.parser.*` - Syntax analysis

## Technical Stack

- **Framework**: SvelteKit
- **Styling**: Tailwind CSS
- **Editor**: CodeMirror 5
- **Python Runtime**: Pyodide (WebAssembly)
- **Build Tool**: Vite
