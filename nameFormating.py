import os

path="./samples"

print(os.listdir(path))
i=0
# for filename in os.listdir(path):
#     if os.path.isfile(os.path.join(path, filename)):
#         form=filename.split(".")[-1]  # Replace spaces with underscores
#         new_filename = f"{i}.{form}"
#         os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
#         i+=1
