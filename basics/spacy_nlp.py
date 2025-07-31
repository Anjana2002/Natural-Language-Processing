#Create a simple NLP program using Python that performs basic text processing tasks such as tokenization, part-of-speech (POS) tagging, and named entity recognition (NER) using spaCy.
import spacy 
nlp = spacy.load('en_core_web_sm')
text = "Apple is looking at buying U.K"
doc = nlp(text)
print("Tokens:")
for token in doc:
    print(token.text)
print("\nPOs Tags:")
for token in doc:
    print(token.text, token.pos_)
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)