EMERGENCY_RESPONSE = (
    "MEDICAL EMERGENCY  \n"
    "Call an ambulance immediately.\n\n"
    "India Emergency Numbers:\n"
    "• 112 (National Emergency)\n"
    "• 108 (Ambulance)\n\n"
    "Do NOT delay. Get medical help NOW."
)

CRITICAL_KEYWORDS = [
    # Heart / Chest
    "heart attack",
    "heart pain",
    "chest pain",
    "chest tightness",
    "pressure in chest",
    "pain in chest",

    # Breathing
    "shortness of breath",
    "breathing problem",
    "difficulty breathing",
    "can't breathe",
    "cannot breathe",

    # Radiating pain
    "left arm pain",
    "jaw pain",
    "shoulder pain",

    # Neurological / collapse
    "collapse",
    "unconscious",
    "fainted",
    "stroke",
    "seizure",

    # Bleeding
    "severe bleeding",
    "heavy bleeding"
]

def is_critical_medical_query(text: str) -> bool:
    text = text.lower().strip()
    return any(keyword in text for keyword in CRITICAL_KEYWORDS)
