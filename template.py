import os

PROJECT_PATHS = [
    ".gitignore",
    "pyproject.toml",
    "README.md",
    "examples/simple_summarizer/main.py",
    "examples/simple_summarizer/prompts.yml",
    "prompt_forge/__init__.py",
    "prompt_forge/core.py",
    "prompt_forge/models.py",
    "prompt_forge/exceptions.py",
    "tests/__init__.py",
    "tests/test_core.py",
]


def create_structure(base_path=".", paths=PROJECT_PATHS):
    """
    Create directories and empty files from a list of relative paths.
    """
    for rel_path in paths:
        path = os.path.join(base_path, rel_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("")


if __name__ == "__main__":
    create_structure()
    print("✅ Project skeleton created successfully!")