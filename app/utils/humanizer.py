import random

def humanize_text(text: str, strength: str = "strong") -> str:
    """
    Post-process AI output to reduce AI-detection likelihood.
    Adds imperfections, varied phrasing, and natural rhythm.
    strength: "mild", "medium", "strong"
    """

    multipliers = {
        "mild": 0.01,
        "medium": 0.03,
        "strong": 0.06   # stronger modifications
    }
    chance = multipliers.get(strength, 0.03)

    hedges = [
        "to some extent", "arguably", "it is worth noting",
        "in practice", "in certain cases", "from another perspective",
        "at times", "in reality", "sometimes overlooked"
    ]

    synonyms = {
        "important": ["crucial", "significant", "vital"],
        "many": ["numerous", "several", "countless"],
        "show": ["demonstrate", "reveal", "illustrate"],
        "make": ["create", "formulate", "develop"],
        "need": ["require", "demand", "call for"],
        "impact": ["effect", "influence", "consequence"],
        "change": ["shift", "transition", "transformation"],
    }

    # --- Hedge injections ---
    words = text.split()
    for i in range(len(words)):
        if random.random() < chance:
            hedge = random.choice(hedges)
            words.insert(i, hedge + ",")
    text = " ".join(words)

    # --- Synonym replacements ---
    for word, choices in synonyms.items():
        if random.random() < chance * 2:  # stronger synonym chance
            replacement = random.choice(choices)
            text = text.replace(f" {word} ", f" {replacement} ")

    # --- Sentence splitting / merging ---
    sentences = text.split(". ")
    new_sentences = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        if len(s.split()) > 25 and random.random() < chance * 2:
            parts = s.split(",")
            if len(parts) > 2:
                s = parts[0] + "." + " ".join(parts[1:])
        if len(s.split()) < 10 and random.random() < chance:
            # merge with next sentence
            if new_sentences:
                new_sentences[-1] = new_sentences[-1] + ", " + s.lower()
                continue
        new_sentences.append(s)
    text = ". ".join(new_sentences)

    # --- Add natural pauses ---
    fillers = ["after all", "as such", "in essence", "to illustrate", "in short"]
    if random.random() < chance:
        text += f". {random.choice(fillers).capitalize()}, this highlights the point clearly."

    return text
