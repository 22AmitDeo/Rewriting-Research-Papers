import random
import re
from typing import List, Dict

def humanize_text(text: str, strength: str = "strong") -> str:
    """
    Post-process AI output to significantly reduce AI-detection likelihood.
    Adds imperfections, varied phrasing, and natural human writing patterns.
    strength: "mild", "medium", "strong", "extreme"
    """
    
    multipliers = {
        "mild": 0.02,
        "medium": 0.05,
        "strong": 0.08,
        "extreme": 0.12  # Maximum humanization
    }
    chance = multipliers.get(strength, 0.08)

    # Expanded hedging and conversational phrases
    hedges = [
        "to some extent", "arguably", "it is worth noting", "in practice", 
        "in certain cases", "from another perspective", "at times", 
        "in reality", "sometimes overlooked", "generally speaking",
        "for the most part", "in many instances", "under certain circumstances",
        "it could be argued that", "from my perspective", "based on experience",
        "in my observation", "what I've found is", "interestingly enough"
    ]

    # Expanded synonyms with more natural variations
    synonyms = {
        "important": ["crucial", "significant", "vital", "paramount", "essential", "key"],
        "many": ["numerous", "several", "countless", "a multitude of", "a variety of"],
        "show": ["demonstrate", "reveal", "illustrate", "exhibit", "display", "suggest"],
        "make": ["create", "formulate", "develop", "construct", "produce", "generate"],
        "need": ["require", "demand", "call for", "necessitate", "compel"],
        "impact": ["effect", "influence", "consequence", "repercussion", "ramification"],
        "change": ["shift", "transition", "transformation", "alteration", "modification"],
        "however": ["nevertheless", "nonetheless", "that said", "on the other hand"],
        "therefore": ["thus", "consequently", "as a result", "hence", "accordingly"],
        "additionally": ["furthermore", "moreover", "also", "what's more", "besides"],
    }

    # Common AI phrases to target for replacement
    ai_phrases = {
        "it is important to": ["crucially, we should", "a key consideration is", "we must"],
        "in conclusion": ["to sum up", "ultimately", "in summary", "finally"],
        "this suggests that": ["this implies", "this indicates", "this points to"],
        "research has shown": ["studies demonstrate", "evidence reveals", "findings indicate"],
        "it can be seen that": ["we observe that", "it becomes apparent", "one can see"],
        "as previously mentioned": ["as noted earlier", "building on earlier points", "returning to"],
    }

    # --- Phase 1: AI phrase replacement ---
    for ai_phrase, replacements in ai_phrases.items():
        if ai_phrase in text.lower():
            if random.random() < chance * 1.5:
                replacement = random.choice(replacements)
                text = re.sub(re.escape(ai_phrase), replacement, text, flags=re.IGNORECASE)

    # --- Phase 2: Synonym replacements with context awareness ---
    words = text.split()
    for i, word in enumerate(words):
        clean_word = word.lower().strip('.,!?;:"')
        if clean_word in synonyms and random.random() < chance * 2:
            replacement = random.choice(synonyms[clean_word])
            # Preserve original capitalization
            if word[0].isupper():
                replacement = replacement.capitalize()
            words[i] = replacement + word[len(clean_word):]
    text = " ".join(words)

    # --- Phase 3: Strategic hedge injections ---
    sentences = re.split(r'(?<=[.!?]) +', text)
    new_sentences = []
    
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 5 and random.random() < chance:
            insert_pos = random.randint(1, len(words) - 2)
            hedge = random.choice(hedges)
            words.insert(insert_pos, hedge + ",")
        new_sentences.append(" ".join(words))
    
    text = " ".join(new_sentences)

    # --- Phase 4: Advanced sentence restructuring ---
    sentences = re.split(r'(?<=[.!?]) +', text)
    new_sentences = []
    
    i = 0
    while i < len(sentences):
        current = sentences[i].strip()
        if not current:
            i += 1
            continue
            
        # Split very long sentences
        if len(current.split()) > 20 and random.random() < chance * 2:
            parts = re.split(r'[,;:]', current)
            if len(parts) > 1:
                current = parts[0] + "." + " ".join(parts[1:])
        
        # Merge short related sentences
        if (i < len(sentences) - 1 and len(current.split()) < 8 and 
            random.random() < chance and len(new_sentences) > 0):
            next_sent = sentences[i + 1].strip()
            if next_sent and len(next_sent.split()) < 15:
                connector = random.choice(["and", "while", "though", "although"])
                new_sentences[-1] = new_sentences[-1] + f" {connector} " + next_sent.lower()
                i += 2
                continue
        
        new_sentences.append(current)
        i += 1

    text = ". ".join(new_sentences)

    # --- Phase 5: Add natural human imperfections ---
    if random.random() < chance:
        # Add a conversational aside
        asides = [
            "This is something I've personally observed in my work.",
            "From my experience, this tends to hold true.",
            "I've found this approach particularly effective.",
            "This perspective has served me well in practice.",
            "In my view, this deserves more attention."
        ]
        text += " " + random.choice(asides)

    if random.random() < chance / 2:
        # Add a minor grammatical "error" that humans make
        errors = [
            "Their are multiple perspectives on this.",
            "This effects how we approach the problem.",
            "We should of considered this earlier.",
            "Its important to note these limitations.",
            "This principle applies irregardless of context."
        ]
        if random.random() < 0.3:  # Only add errors occasionally
            text = text + " " + random.choice(errors)

    # --- Phase 6: Final polishing ---
    # Ensure proper capitalization after sentence breaks
    text = re.sub(r'\. ([a-z])', lambda match: '. ' + match.group(1).upper(), text)
    
    # Add varied sentence starters
    starters = ["Moreover,", "Additionally,", "Interestingly,", "Surprisingly,", "Notably,"]
    if random.random() < chance and len(text.split('. ')) > 2:
        sentences = text.split('. ')
        if len(sentences) > 1:
            sentences[1] = random.choice(starters) + " " + sentences[1].lower()
            text = '. '.join(sentences)

    return text

# Additional utility function for batch processing
def humanize_batch(texts: List[str], strength: str = "strong") -> List[str]:
    """Humanize multiple texts with consistent settings"""
    return [humanize_text(text, strength) for text in texts]