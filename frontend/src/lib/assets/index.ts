// Centralized asset exports so components can import from `$lib/assets`
// Each variable holds the Vite-resolved URL string for the static file

import check from './check.png';
import copy from './copy.png';
import darkmode from './darkmode.png';
import darkBg from './dark_bg.png';
import editor from './editor.svg';
import errorIcon from './error.png';
import errors from './errors.png';
import favicon from './favicon.svg';
import lightmode from './lightmode.png';
import logo from './logo.png';
import newFile from './new_file.png';
import openFile from './open_file.png';
import refresh from './refresh.png';
import saveFile from './save_file.png';
import synSemLexIcon from './SynSemLexIcon.png';
import table from './table.png';
import warning from './warning.png';

export {
    check,
    copy,
    darkmode,
    darkBg,
    editor,
    errorIcon,
    errors,
    favicon,
    lightmode,
    logo,
    newFile,
    openFile,
    refresh,
    saveFile,
    synSemLexIcon,
    table,
    warning
};

// Aggregate object if you prefer programmatic access
export const assets = {
    check,
    copy,
    darkmode,
    darkBg,
    editor,
    errorIcon,
    errors,
    favicon,
    lightmode,
    logo,
    newFile,
    openFile,
    refresh,
    saveFile,
    synSemLexIcon,
    table,
    warning
};
