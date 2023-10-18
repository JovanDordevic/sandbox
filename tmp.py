import os

print("Hello from tmp.py")
print()
# Returns `default_value` if the key doesn't exist
ENV_NUM = os.getenv('ENV_NUM', 'it does not exist!')
print(f"ENV_NUM = {ENV_NUM}")
print()
print(f"whole env:\n {os.environ}")

for i in range(ENV_NUM):
    print(f"-- {i}")