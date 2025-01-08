import spacy

nlp = spacy.load("en_core_web_sm")

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

doc = nlp(text)

# print(doc)
# print(len(doc))
# print(len(text))

words = text.split()[:10]

i=5
for token in doc[i:8]:
    print (f"SpaCy Token {i}:\n{token}\nWord Split {i}:\n{words[i]}\n\n")
    i=i+1
    