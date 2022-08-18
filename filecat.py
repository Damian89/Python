import subprocess
result = subprocess.run(["cat", "hello.py"], stderr=subprocess.PIPE, text=True)
print(result.stderr)
