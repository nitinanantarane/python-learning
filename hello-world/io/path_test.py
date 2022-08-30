from pathlib import Path

# path = Path()
# files = path.glob("*")
# for file in files:
#     print(file)

path = Path("../ecommerce")
files = path.glob("*.py")
for file in files:
    print(file)

# path = Path("emails")
# print(path.exists())
# path.mkdir()
# print(path.exists())

# path = Path("emails")
# print(path.exists())
# path.rmdir()
# print(path.exists())
