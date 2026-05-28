import subprocess
import os

def run_tests():
    result = subprocess.run(
    [r"C:\code\playwright_web_framework\.venv\Scripts\python.exe", "-m", "pytest", "tests/", "--override-ini=addopts="],
    capture_output=True,
    text=True,
    )
    print(result.stdout + result.stderr)

def list_test_files():
    test_files = []
    for file in os.listdir("tests"):
        if file.startswith("test_") and file.endswith(".py"):
            test_files.append(file)
    return test_files

if __name__ == "__main__":
    print("Test files:", list_test_files())
    print("\nRunning tests...\n")
    run_tests()