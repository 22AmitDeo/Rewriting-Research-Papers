import random
import re
from typing import List

def humanize_text(text: str, strength: str = "strong") -> str:
    """
    Post-process AI output to reduce AI-detection likelihood by injecting
    real academic writing patterns observed in human papers.
    """

    multipliers = {
        "mild": 0.02,
        "medium": 0.05,
        "strong": 0.08,
        "extreme": 0.12
    }
    chance = multipliers.get(strength, 0.08)

    # Academic hedges (tentative phrasing humans use)
    hedges = [
        "it appears that", "this may suggest", "our findings indicate",
        "could imply", "to some extent", "in certain contexts",
        "this could be interpreted as", "may point toward"
    ]

    # Human academic transition signals
    transitions = [
        "Furthermore,", "Moreover,", "In addition,", "However,",
        "On the other hand,", "Interestingly,", "Notably,", "At the same time,"
    ]

    # Academic clichés
    academic_phrases = [
        "In this study,", "The results indicate that",
        "Our findings suggest that", "This research demonstrates",
        "Overall, the evidence reveals", "The analysis shows"
    ]

    # Contribution & implication signals
    contribution_phrases = [
        "This study makes several contributions to the literature.",
        "The findings have both theoretical and practical implications.",
        "From a practical perspective, these results may inform policymakers.",
        "The study adds to ongoing debates within the field."
    ]

    # Limitations & future research signals
    limitations_phrases = [
        "This study is not without limitations.",
        "A key limitation involves the sample size.",
        "Future research could expand on these findings.",
        "Subsequent studies may adopt alternative methodologies."
    ]

    # --- Phase 1: Inject academic clichés ---
    sentences = re.split(r'(?<=[.!?]) +', text)
    if sentences and random.random() < chance * 1.5:
        insert_pos = random.randint(0, min(3, len(sentences)-1))
        sentences.insert(insert_pos, random.choice(academic_phrases))
    text = " ".join(sentences)

    # --- Phase 2: Hedge injection ---
    sentences = re.split(r'(?<=[.!?]) +', text)
    new_sentences = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 7 and random.random() < chance:
            insert_pos = random.randint(2, len(words) - 2)
            words.insert(insert_pos, random.choice(hedges) + ",")
        new_sentences.append(" ".join(words))
    text = " ".join(new_sentences)

    # --- Phase 3: Transition starters ---
    sentences = re.split(r'(?<=[.!?]) +', text)
    for i in range(1, len(sentences)):
        if random.random() < chance and not sentences[i].startswith(tuple(transitions)):
            sentences[i] = random.choice(transitions) + " " + sentences[i].lstrip()
    text = " ".join(sentences)

    # --- Phase 4: Contribution & implications ---
    if random.random() < chance:
        text += " " + random.choice(contribution_phrases)

    # --- Phase 5: Limitations & future research ---
    if random.random() < chance:
        text += " " + random.choice(limitations_phrases)

    # --- Phase 6: Sentence rhythm tweaks ---
    sentences = re.split(r'(?<=[.!?]) +', text)
    new_sentences = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        # Occasionally break into fragments
        if len(s.split()) > 18 and random.random() < chance:
            cut = len(s.split()) // 2
            words = s.split()
            s = " ".join(words[:cut]) + ". " + " ".join(words[cut:])
        new_sentences.append(s)
    text = " ".join(new_sentences)

    return text


def humanize_batch(texts: List[str], strength: str = "strong") -> List[str]:
    """Apply humanization to multiple texts"""
    return [humanize_text(text, strength) for text in texts]
