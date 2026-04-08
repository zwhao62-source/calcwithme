# UTF-8 Environment Setup for Windows
import sys
import io
import os

# Set UTF-8 encoding for stdout/stderr
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Set environment variables
os.environ['PYTHONIOENCODING'] = 'utf-8'

print("UTF-8 environment configured")
