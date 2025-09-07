from app.utils.openrouter import call_openrouter

STYLE_JSON = {
    "tone": "Formal, academic, professional, but approachable and natural",
    "style": "Engaging, avoids robotic phrasing, varies sentence structure",
    "avoid": [
        "Overly casual language",
        "AI-sounding disclaimers",
        "Excessive repetition",
        "Inventing citations",
        "Overly complex jargon"
    ],
    "structure": [
        "Abstract", "Introduction", "Literature Review",
        "Methodology", "Results", "Discussion",
        "Conclusion", "References"
    ],
    "extra_rules": [
        "Ensure logical flow",
        "Vary rhythm",
        "Keep length ±10%",
        "Mark unclear sentences as [Check: unclear]",
        "Allow slight imperfections so text doesn’t sound AI-generated"
    ]
}

async def rewrite_paper(paper: str) -> str:
    prompt = f"STYLE_JSON: {STYLE_JSON}\n\nPAPER:\n{paper}"
    return await call_openrouter(prompt)
