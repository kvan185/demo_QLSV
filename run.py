import sys
import os

# Thêm thư mục gốc project vào PYTHONPATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# Chạy main_window
from src.presentation.main_window import main

if __name__ == "__main__":
    main()
