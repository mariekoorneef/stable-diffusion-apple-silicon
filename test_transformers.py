from transformers import pipeline

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')

print(classifier('We are very happy to introduce pipeline to the transformers repository.'))
# {'label': 'POSITIVE', 'score': 0.9996980428695679}]
