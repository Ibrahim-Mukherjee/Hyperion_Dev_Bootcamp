import spacy

# load the spacy English model
nlp = spacy.load("en_core_web_sm")

# garden path sentences
garden_path_sentences = [
    "The old man the boat.",
    "The horse raced past the barn fell.",
    "The cotton clothing is usually made of grows in Mississippi.",
    "The dog that the man owned bit the mailman.",
    "The man who hunts ducks out on weekends."
]

# tokenize each sentence and perform entity recognition
garden_path_entities = []
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    garden_path_entities.append(entities)

# print out the identified entities for each garden path sentence
for i, entities in enumerate(garden_path_entities):
    print(f"Garden path sentence {i+1}: {garden_path_sentences[i]}")
    print(f"Identified entities: {entities}")
    print()

# print out explanations for any entities we don't understand
for entities in garden_path_entities:
    for entity in entities:
        if entity[1] == "UNKNOWN":
            print(spacy.explain(entity[1]))

# two entities I looked up: GPE and NORP
print("GPE represents geopolitical entities, e.g. countries, cities, states, etc.")
print("NORP represents nationalities or religious or political groups.")
