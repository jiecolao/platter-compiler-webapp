"""
Test runner for Platter Compiler
Runs unittest with correct PYTHONPATH
"""
import sys
import unittest
from pathlib import Path

# Get the project root
project_root = Path(__file__).parent
python_source = project_root / "platter-compiler-sveltejs" / "static" / "python"
test_dir = project_root / "platter-compiler-sveltejs" / "python-dev"

# Add Python source to path
sys.path.insert(0, str(python_source))
sys.path.insert(0, str(test_dir))

if __name__ == "__main__":
    # Discover and run tests
    loader = unittest.TestLoader()
    tests = loader.discover(str(test_dir / "tests"), pattern="ga_*.py")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(tests)
    
    # Exit with proper code
    sys.exit(0 if result.wasSuccessful() else 1)
