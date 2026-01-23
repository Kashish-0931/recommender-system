
```python
import os
import pickle

def load_movies_dict(file_path):
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"File {file_path} not found. Creating a new one.")
        return {}
    except Exception as e:
        print(f"Error loading file: {e}")
        return {}

# Usage
file_path = 'movies_dict.pkl'
movies_dict = load_movies_dict(file_path)
```