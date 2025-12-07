"""
job_trust_checker.py

Job Listing Legitimacy Lens (Demo)

A tiny rule-based tool that gives a rough "trust score" for a job listing.
This is for teaching and demo purposes only, not real-world verification.
"""

import re

# Phrases that often show up in obvious scams or shady posts
GENERAL_RED_FLAGS = [
    "wire money",
    "wire transfer",
    "bank details",
    "bank account",
    "routing number",
    "gift card",
    "gift cards",
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

# Direct payment apps (bad sign for a "job")
PAYMENT_APP_RED_FLAGS = [
    "venmo",
    "cash app",
    "cashapp",
    "paypal",
    "zelle",
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
    critical_flags = 0  # count “this is really not okay” signals

    company_clean = company.strip()
    source_clean = source.strip()
    email_clean = email.strip()
    desc_clean = description.strip()
    desc_lower = desc_clean.lower()

    # --- Company name ---
    if not company_clean:
        risk += 20
        critical_flags += 1
        reasons.append("No company name provided.")
    else:
        reasons.append("Company name provided.")

    # --- Source site / platform ---
    if not source_clean:
        risk += 20
        critical_flags += 1
        reasons.append("No source site provided (e.g., LinkedIn, company site).")
    else:
        reasons.append(f"Job source provided: {source_clean}.")
        src_lower = source_clean.lower()
        if not any(site in src_lower for site in KNOWN_JOB_SITES):
            risk += 30
            critical_flags += 1
            reasons.append(
                "Job source is not a common job platform or clear company site; review carefully."
            )

    # --- Description length / clarity ---
    desc_len = len(desc_clean)
    if desc_len == 0:
        risk += 50
        critical_flags += 1
        reasons.append("No job description provided at all.")
    elif desc_len < 50:
        risk += 30
        critical_flags += 1
        reasons.append("Description is extremely short/vague (less than 50 characters).")
    elif desc_len < 120:
        risk += 15
        reasons.append("Description is short and may be missing important details.")
    elif desc_len < 400:
        reasons.append("Description has reasonable length.")
    else:
        reasons.append("Description is detailed and provides plenty of information.")

    # --- All caps check (shouty / spammy tone) ---
    if desc_len > 0 and desc_clean.isupper():
        risk += 15
        reasons.append("Description is written in all caps (unprofessional / spam-like tone).")

    # --- General scammy phrases ---
    gen_hits = [p for p in GENERAL_RED_FLAGS if p in desc_lower]
    if gen_hits:
        risk += 40
        critical_flags += 1
        reasons.append("Potential scam signals found: " + ", ".join(gen_hits) + ".")

    # --- Too-good-to-be-true promises ---
    tgood_hits = [p for p in TOO_GOOD_TO_BE_TRUE if p in desc_lower]
    if tgood_hits:
        risk += 25
        critical_flags += 1
        reasons.append(
            "Unrealistic earning claims detected: " + ", ".join(tgood_hits) + "."
        )

    # --- Payment app red flags (e.g., Venmo) ---
    pay_hits = [p for p in PAYMENT_APP_RED_FLAGS if p in desc_lower]
    if pay_hits:
        risk += 35
        critical_flags += 1
        reasons.append(
            "Direct payment via apps detected (unusual for legitimate jobs): "
            + ", ".join(pay_hits)
            + "."
        )

    # --- Salary validity check (unrealistic high salaries) ---
    # Look for dollar amounts and "million" indicators
    salary_pattern = re.findall(
        r"\$?(\d{1,3}(?:,\d{3})+|\d+)(?:\s*(million|billion))?", desc_lower
    )
    unrealistic_salary = False

    for amount, multiplier in salary_pattern:
        amount_value = int(amount.replace(",", ""))

        # If "million" or "billion" is present, or the word appears anywhere, unrealistic
        if multiplier in ("million", "billion") or "million" in desc_lower or "billion" in desc_lower:
            unrealistic_salary = True

        # Salary above $500k is unrealistic for typical postings
        if amount_value > 500000:
            unrealistic_salary = True

    if unrealistic_salary:
        risk += 40
        critical_flags += 1
        reasons.append("Salary appears unrealistic or inflated for this job posting.")

    # --- Pressure language ---
    pressure_hits = [p for p in PRESSURE_PHRASES if p in desc_lower]
    if pressure_hits:
        risk += 15
        reasons.append(
            "High-pressure language detected: " + ", ".join(pressure_hits) + "."
        )

    # --- Compensation red flags (exploitative terms) ---
    comp_hits = [p for p in COMPENSATION_RED_FLAGS if p in desc_lower]
    if comp_hits:
        risk += 40
        critical_flags += 1
        reasons.append(
            "Compensation red flags detected (potentially exploitative terms): "
            + ", ".join(comp_hits)
            + "."
        )

    # --- Email checks ---
    if email_clean:
        reasons.append(f"Contact email provided: {email_clean}.")
        if "@" in email_clean:
            domain = email_clean.split("@")[-1].lower()
            if "." not in domain:
                # no .com / .org / etc.
                risk += 35
                critical_flags += 1
                reasons.append(
                    "Contact email domain is missing a dot (e.g., .com); format looks invalid."
                )
            elif domain in FREE_EMAIL_DOMAINS:
                risk += 10
                reasons.append(
                    "Email uses a free domain (may be fine, but slightly less professional)."
                )
        else:
            risk += 35
            critical_flags += 1
            reasons.append("Contact email format looks invalid (no @ symbol).")
    else:
        risk += 25
        critical_flags += 1
        reasons.append("No contact email provided.")

    # --- Simple positive signals (tiny risk reduction) ---
    positive_hits = 0
    # NOTICE: we do NOT include "salary" here so wild salary claims never look positive.
    POSITIVE_KEYWORDS = [
        "health insurance",
        "medical insurance",
        "401k",
        "benefits",
        "paid time off",
        "pto",
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

    # --- Base trust score ---
    trust_score = max(0, min(100, 100 - risk))

    # --- Clamp score based on how many critical flags we saw ---
    # If there are multiple major problems, the score should never look "okay".
    if critical_flags >= 3 and trust_score > 25:
        trust_score = 25
    elif critical_flags == 2 and trust_score > 45:
        trust_score = 45
    elif critical_flags == 1 and trust_score > 65:
        trust_score = 65

    # --- Label based on final score ---
    if trust_score >= 85:
        label = "Likely Legitimate (based on these checks)"
    elif trust_score >= 60:
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
