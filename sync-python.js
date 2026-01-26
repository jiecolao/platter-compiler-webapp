/**
 * Sync Python files from backend to frontend static folder
 * Run this script whenever you update Python code in backend/app/
 * 
 * Usage: node sync-python.js
 */

import { copyFileSync, mkdirSync, readdirSync, statSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const SOURCE_DIR = join(__dirname, 'backend', 'app');
const TARGET_DIR = join(__dirname, 'frontend', 'static', 'python', 'app');

function copyDirectory(source, target) {
	// Create target directory if it doesn't exist
	mkdirSync(target, { recursive: true });

	// Read all files and directories in source
	const entries = readdirSync(source);

	for (const entry of entries) {
		const sourcePath = join(source, entry);
		const targetPath = join(target, entry);
		const stat = statSync(sourcePath);

		if (stat.isDirectory()) {
			// Recursively copy subdirectories
			copyDirectory(sourcePath, targetPath);
		} else if (stat.isFile() && (entry.endsWith('.py') || entry === '__init__.py')) {
			// Copy Python files including __init__.py
			copyFileSync(sourcePath, targetPath);
			console.log(`Copied: ${entry}`);
		}
	}
}

console.log('Syncing Python files from backend to frontend...\n');
console.log(`Source: ${SOURCE_DIR}`);
console.log(`Target: ${TARGET_DIR}\n`);

try {
	copyDirectory(SOURCE_DIR, TARGET_DIR);
	console.log('\n✅ Python files synced successfully!');
} catch (error) {
	console.error('\n❌ Error syncing Python files:', error.message);
	process.exit(1);
}
