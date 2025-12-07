

This is a tiny prototype that gives a rough “trust score” for job listings using simple rule-based checks. It was inspired by a mental model our Innovation Lab explored earlier in the program: helping job seekers understand if a job posting looks legitimate or suspicious.

This demo shows how research and mental models can turn into a simple working tool.

---

## 🔍 What this tool does

- Takes in:
  - company name
  - where you found the job
  - contact email
  - full job description

- Checks for:
  - missing company details
  - vague or very short descriptions
  - suspicious phrases (like “wire money” or “earn money fast”)
  - free email domains
  - pressure-language

- Returns:
  - a **trust score** (0–100)
  - a **label** (Likely Legitimate, Needs More Info, or High Risk)
  - clear explanations for each signal

This is NOT a real security tool — it’s a teaching prototype to show how mental models and logic can support job seekers.

---

## 📂 Project structure

