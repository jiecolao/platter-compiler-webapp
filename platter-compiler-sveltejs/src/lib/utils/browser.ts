/* eslint-disable @typescript-eslint/no-explicit-any */
// Small browser utility helpers used by the editor UI
export function loadScript(url: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = url;
    s.onload = () => resolve();
    s.onerror = (e) => reject(e);
    document.head.appendChild(s);
  });
}

export function loadCSS(url: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const l = document.createElement('link');
    l.rel = 'stylesheet';
    l.href = url;
    l.onload = () => resolve();
    l.onerror = (e) => reject(e);
    document.head.appendChild(l);
  });
}

export async function readFileAsText(file: File): Promise<string> {
  // modern API
  return await file.text();
}

export async function saveContent(content: string, suggestedName = 'program.platter') {
  // Try File System Access API first
  try {
    if ((window as any).showSaveFilePicker) {
      const opts = {
        types: [
          {
            description: 'Platter files',
            accept: { 'text/plain': ['.platter'] }
          }
        ]
      };
      const handle = await (window as any).showSaveFilePicker(opts);
      const writable = await handle.createWritable();
      await writable.write(content);
      await writable.close();
      return `Saved ${handle.name ?? suggestedName}`;
    }
  } catch (err) {
    // fall through to fallback
    // some browsers may reject permission; allow fallback
    console.warn('FS Access API failed or was rejected, falling back to download', err);
  }

  // Fallback: trigger a download
  const blob = new Blob([content], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = suggestedName;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
  return `Downloaded ${suggestedName}`;
}

export async function copyToClipboard(content: string): Promise<void> {
  await navigator.clipboard.writeText(content);
}
