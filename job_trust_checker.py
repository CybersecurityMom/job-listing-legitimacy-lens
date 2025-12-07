"""
job_trust_checker.py

Job Listing Legitimacy Lens (Demo)

A tiny rule-based tool that gives a rough "trust score" for a job listing.
This is for teaching and demo purposes only, not real-world verification.
"""

# Phrases that often show up in obvious scams or shady posts
GENERAL_RED_FLAGS = [
    "wire money",
    "wire transfer",
    "bank details",
    "bank account",
    "routing number",
    "gift card",
    "gift cards",
    "crypto",
    "cryptocurrency",
    "bitcoin",
    "training fee",
    "processing fee",
    "upfront fee",
    "send payment",
]

# Phrases that signal hype or unrealistic promises
TOO_GOOD_TO_BE_TRUE = [
    "earn money fast",
    "get rich",
    "quick money",
    "work from home and get rich",
    "make thousands a day",
]

# Phrases that signal pressure / urgency
PRESSURE_PHRASES = [
    "urgent hire",
    "apply immediately",
    "apply now",
    "start today",
    "limited spots",
    "act now",
]

# Phrases that suggest bad or exploitative compensation
COMPENSATION_RED_FLAGS = [
    "pay in peanuts",
    "paid in peanuts",
    "for exposure only",
    "no pay",
    "unpaid role",
    "unpaid internship",
    "no salary",
    "no compensation",
]

FREE_EMAIL_DOMAINS = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "proton.me",
    "icloud.com",
]

# Common places you’d reasonably find legit listings
KNOWN_JOB_SITES = [
    "linkedin",
    "indeed",
    "glassdoor",
    "ziprecruiter",
    "monster",
    "usajobs",
    "usa jobs",
    "career page",
    "careers page",
    "company site",
    "company website",
    "workday",
    "greenhouse",
    "lever",
]


def analyze_job(company, source, description, email):
    """
    Take job details and return:
    - trust_score (0–100)
    - label (Likely Legitimate / Mixed Signals / High Risk)
    - reasons (list of human-readable strings)
    """
    reasons = []
    risk = 0

    company_clean = company.strip()
    source_clean = source.strip()
    email_clean = email.strip()
    desc_clean = description.strip()
    desc_lower = desc_clean.lower()

    # --- Company name ---
    if not company_clean:
        risk += 20
        reasons.append("No company name provided.")
    else:
        reasons.append("Company name provided.")

    # --- Source site / platform ---
    if not source_clean:
        risk += 15
        reasons.append("No source site provided (e.g., LinkedIn, company site).")
    else:
        reasons.append(f"Job source provided: {source_clean}.")
        src_lower = source_clean.lower()
        if not any(site in src_lower for site in KNOWN_JOB_SITES):
            risk += 12
            reasons.append(
                "Job source is not a common job platform or clear company site; review carefully."
            )

    # --- Description length / clarity ---
    desc_len = len(desc_clean)
    if desc_len == 0:
        risk += 40
        reasons.append("No job description provided at all.")
    elif desc_len < 50:
        risk += 30
        reasons.append("Description is extremely short/vague (less than 50 characters).")
    elif desc_len < 120:
        risk += 12
        reasons.append("Description is short and may be missing important details.")
    elif desc_len < 400:
        reasons.append("Description has reasonable length.")
    else:
        reasons.append("Description is detailed and provides plenty of information.")

    # --- All caps check (shouty / spammy tone) ---
    if desc_len > 0 and desc_clean.isupper():
        risk += 12
        reasons.append("Description is written in all caps (unprofessional / spam-like tone).")

    # --- General scammy phrases ---
    found_general = [p for p in GENERAL_RED_FLAGS if p in desc_lower]
    if found_general:
        risk += min(32, 8 * len(found_general))
        reasons.append("Potential scam signals found: " + ", ".join(found_general) + ".")

    # --- Too-good-to-be-true promises ---
    found_too_good = [p for p in TOO_GOOD_TO_BE_TRUE if p in desc_lower]
    if found_too_good:
        risk += min(24, 10 + 5 * len(found_too_good))
        reasons.append("Unrealistic earning claims detected: " + ", ".join(found_too_good) + ".")

    # --- Pressure language ---
    found_pressure = [p for p in PRESSURE_PHRASES if p in desc_lower]
    if found_pressure:
        risk += min(20, 6 * len(found_pressure))
        reasons.append("High-pressure language detected: " + ", ".join(found_pressure) + ".")

    # --- Compensation red flags (your “peanuts” case lives here) ---
    found_comp = [p for p in COMPENSATION_RED_FLAGS if p in desc_lower]
    if found_comp:
        risk += 30  # strong penalty
        reasons.append(
            "Compensation red flags detected (potentially exploitative terms): "
            + ", ".join(found_comp) + "."
        )

    # --- Email checks ---
    if email_clean:
        reasons.append(f"Contact email provided: {email_clean}.")
        if "@" in email_clean:
            domain = email_clean.split("@")[-1].lower()
            if domain in FREE_EMAIL_DOMAINS:
                risk += 8
                reasons.append(
                    "Email uses a free domain (may be fine, but slightly less professional)."
                )
        else:
            risk += 18
            reasons.append("Contact email format looks invalid.")
    else:
        risk += 12
        reasons.append("No contact email provided.")

    # --- Simple positive signals (tiny risk reduction) ---
    positive_hits = 0
    POSITIVE_KEYWORDS = [
        "health insurance",
        "medical insurance",
        "401k",
        "benefits",
        "paid time off",
        "pto",
        "salary",
        "full-time",
        "competitive pay",
    ]
    for kw in POSITIVE_KEYWORDS:
        if kw in desc_lower:
            positive_hits += 1

    if positive_hits:
        reduction = min(10, 3 * positive_hits)
        risk = max(0, risk - reduction)
        reasons.append(
            f"Some structured compensation/benefits language present ({positive_hits} positive signals)."
        )

    # --- Compute trust score ---
    trust_score = max(0, min(100, 100 - risk))

    if trust_score >= 80:
        label = "Likely Legitimate (based on these checks)"
    elif trust_score >= 55:
        label = "Mixed Signals / Needs More Info"
    else:
        label = "High Risk / Suspicious"

    return trust_score, label, reasons


def main():
    print("\n=== Job Listing Legitimacy Lens (Demo) ===\n")

    company = input("Company name: ")
    source = input("Where did you find this job?: ")
    email = input("Contact email: ")

    print("\nPaste job description. Type END on a new line when finished.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    description = "\n".join(lines)

    score, label, reasons = analyze_job(company, source, description, email)

    print("\n=== RESULT ===")
    print(f"Score: {score}/100")
    print(f"Assessment: {label}\n")
    print("Reasons:")
    for r in reasons:
        print(f"- {r}")

    print("\nReminder: This is a simple demo, not a real-world verification tool.")


if __name__ == "__main__":
    main()
