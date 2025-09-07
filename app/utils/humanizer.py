import random

def humanize_text(text: str) -> str:
    """
    Post-process AI output to reduce AI-detection likelihood.
    Adds imperfections, varied phrasing, and natural breaks.
    """

    # Hedge phrases to insert occasionally
    hedges = [
        "to some extent",
        "arguably",
        "it is worth noting",
        "in practice",
        "in certain cases",
        "from another perspective"
    ]

    # Randomly inject hedges
    words = text.split()
    for i in range(len(words)):
        if random.random() < 0.02:  # ~2% chance per word
            hedge = random.choice(hedges)
            words.insert(i, hedge + ",")
    text = " ".join(words)

    # Break long sentences
    sentences = text.split(". ")
    new_sentences = []
    for s in sentences:
        if len(s.split()) > 25 and random.random() < 0.3:
            parts = s.split(",")
            if len(parts) > 2:
                # turn first part into a standalone sentence
                s = parts[0] + "." + " ".join(parts[1:])
        new_sentences.append(s)
    text = ". ".join(new_sentences)

    return text
