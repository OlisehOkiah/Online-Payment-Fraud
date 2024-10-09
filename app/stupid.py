import os

print(os.getcwd())

model_path = os.path.join(os.getcwd(), 'model.pkl')

# Print the full path
print(model_path)