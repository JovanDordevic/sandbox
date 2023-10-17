import os

print("Hello from tmp.py")
print()
# Returns `default_value` if the key doesn't exist
print(f"ENV_NUM = {os.getenv('ENV_NUM', 'it does not exist!')}")
print()
print(f"whole env:\n {os.environ}")