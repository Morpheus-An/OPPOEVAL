from transformers import pipeline

generator = pipeline(
    'text-generation', model="models/opt125m", device='cuda:0')
print(
    generator("What are we having for dinner?")
)
