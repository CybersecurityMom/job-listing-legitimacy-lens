RED_FLAG_PHRASES = [
    "wire money", "quick money", "earn money fast", "no experience needed",
    "upfront fee", "training fee", "gift cards", "crypto", "bitcoin",
    "urgent hire", "immediately hired"
]

FREE_EMAIL_DOMAINS = [
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"
]


def analyze_job(company, source, description, email):
    reasons = []
    risk = 0

    if not company:
        risk += 20
        reasons.append("No company name provided.")
    else:
        reasons.append("Company name provided.")

    if not source:
        risk += 10
        reasons.append("No source site provided.")
    else:
        reasons.append(f"Source: {source}")

    if len(description) < 80:
        risk += 15
        reasons.append("Description is very short.")
    elif len(description) < 200:
        risk += 5
        reasons.append("Description is somewhat short.")
    else:
        reasons.append("Description has enough detail.")

    found = [p for p in RED_FLAG_PHRASES if p in description.lower()]
    if found:
        risk += min(30, 10 + len(found)*5)
        reasons.append(f"Red-flag phrases: {', '.join(found)}")

    if email:
        if "@" in email:
            domain = email.split("@")[-1].lower()
            if domain in FREE_EMAIL_DOMAINS:
                risk += 10
                reasons.append("Email uses free domain (less professional).")
        else:
            risk += 10
            reasons.append("Email format looks invalid.")
    else:
        risk += 10
        reasons.append("No contact email provided.")

    score = max(0, 100 - risk)

    if score >= 70:
        label = "Likely Legitimate"
    elif score >= 40:
        label = "Needs More Info"
    else:
        label = "High Risk"

    return score, label, reasons


def main():
    print("\n=== Job Listing Legitimacy Lens ===\n")

    company = input("Company name: ")
    source = input("Where did you find this job?: ")
    email = input("Contact email: ")

    print("\nPaste job description. Type END on a new line when finished.\n")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    desc = "\n".join(lines)

    score, label, reasons = analyze_job(company, source, desc, email)

    print("\n=== RESULT ===")
    print(f"Score: {score}/100")
    print(f"Assessment: {label}\n")
    print("Reasons:")
    for r in reasons:
        print(f"- {r}")


if __name__ == "__main__":
    main()
