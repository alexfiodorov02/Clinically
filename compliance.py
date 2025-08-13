import re

RISK_PATTERNS = {
    "No consent": r"(no consent|consent not obtained|refused consent)",
    "Missing allergy info": r"(no allergy info|allergy history unknown|unknown allergy)",
    "Medication dose issue": r"(wrong dose|dose error|overdose|underdose)",
    "Missing follow-up": r"(no follow-up|not scheduled|follow-up unclear)"
}

def flag_compliance_issues(note_text):
    """Scan text for compliance-related issues."""
    flags = []

    for label, pattern in RISK_PATTERNS.items():
        if re.search(pattern, note_text, re.IGNORECASE):
            flags.append(label)
    
    return flags
