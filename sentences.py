import random

def main():
    # Example of generating and printing sentences
    for _ in range(5):  # Generate 5 example sentences
        quantity = random.choice(["single", "plural"])
        tense = random.choice(["past", "present", "future"])
        sentence = make_sentence(quantity, tense)
        print(sentence)

def make_sentence(quantity, tense):
    """Generate a sentence with a determiner, noun, and verb."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    return f"{determiner} {noun} {verb}."

def get_determiner(quantity):
    """Return a randomly chosen determiner based on quantity."""
    determiners = {
        "single": ["A", "One", "The"],
        "plural": ["Some", "Many", "The"]
    }
    return random.choice(determiners[quantity])

def get_noun(quantity):
    """Return a randomly chosen noun based on quantity."""
    nouns = {
        "single": ["cat", "dog", "woman", "boy", "bird"],
        "plural": ["cats", "dogs", "women", "boys", "birds"]
    }
    return random.choice(nouns[quantity])

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on quantity and tense."""
    verbs = {
        "past": {
            "single": ["ran", "jumped", "ate", "laughed", "walked"],
            "plural": ["ran", "jumped", "ate", "laughed", "walked"]
        },
        "present": {
            "single": ["runs", "jumps", "eats", "laughs", "walks"],
            "plural": ["run", "jump", "eat", "laugh", "walk"]
        },
        "future": {
            "single": ["will run", "will jump", "will eat", "will laugh", "will walk"],
            "plural": ["will run", "will jump", "will eat", "will laugh", "will walk"]
        }
    }
    return random.choice(verbs[tense][quantity])

# Entry point of the program
if __name__ == "__main__":
    main()