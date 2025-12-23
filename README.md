
# 🔍 Job Listing Legitimacy Lens (Demo)

A beginner-friendly Python tool that helps users quickly assess whether a job listing shows signs of legitimacy or potential fraud.  
This is **not** a verification engine; it is a **signal-based assistant** designed to highlight red flags, positive indicators, and elements that require closer attention.

---

## ✨ What This Tool Does

The Job Listing Legitimacy Lens analyzes four key components:

1. **Company Name**
2. **Job Source** (where the listing was found)
3. **Contact Email**
4. **Job Description**

Using pattern checks, keyword detection, and risk scoring, it estimates whether a job is:

- **Likely Legitimate**
- **Caution / Mixed Signals**
- **High Risk / Suspicious**

It also provides **human-readable explanations** for its decisions — helping users learn *why* something might be unsafe.

---

## ⭐ Updated & Enhanced Features

### **1. Smarter Job Source Evaluation**
- Recognizes reputable platforms such as:
  - Indeed  
  - LinkedIn  
  - Glassdoor  
  - CareerBuilder  
  - ZipRecruiter  
- Accepts unfamiliar sources *without automatically penalizing them as scams*.
- If the source is unknown or nonstandard, the tool simply flags it with:
  > “Not a common platform — double-check that the link belongs to the real company.”

This avoids false negatives while still encouraging user caution.

---

### **2. Stronger Email Validation**
The tool now checks whether an email is **properly formatted**, including:

- Must contain `@`
- Must contain a valid domain structure (`example.com`, `company.org`, `team.co`, etc.)
- Flags incomplete or malformed domains (e.g., `chef@gma`, `back@p`)
- Highlights suspicious free-mail usage in job postings

---

### **3. Critical Red-Flag Detection (New & Expanded)**

The tool now looks for high-risk patterns including:

- Payment apps used for salary:
  - Cash App  
  - Zelle  
  - Venmo  
  - PayPal  
- Unrealistic salaries or exaggerated earnings  
- Requests for:
  - Upfront payment  
  - Personal information  
- Run-on hype language (“we are so cool,” “super rad,” “better than the Arctic”)
- Repetitive nonsense strings (common in scam/bot-generated ads)
- Missing job duties or requirements  

If any major red flag is detected → **risk score automatically drops heavily**.

---

### **4. Expanded Positive Signals**
The tool now rewards job descriptions that include legitimate-looking structure, including:

- Salary ranges  
- Defined responsibilities  
- Qualifications or experience requirements  
- Benefits such as:
  - 401k
  - Insurance
  - PTO
  - Retirement plans  
  - Holidays  
- Industry-standard language that real HR teams use

Each positive keyword reduces risk slightly — up to a safe maximum.

---

### **5. Improved Scoring System (More Realistic)**

**Final Score Categories:**

| Score | Assessment |
|-------|------------|
| **90–100** | Likely Legitimate (based on provided signals) |
| **70–89**  | Caution / Mixed Signals |
| **40–69**  | Mixed Signals / Needs Verification |
| **0–39**   | High Risk / Suspicious |

Important:  
Legitimacy ≠ guaranteed safety.  
The tool assesses *patterns*, not real company identity.

---

### **6. Helpful User Guidance When Needed**
If the tool detects uncertainty — for example, an unfamiliar job board — it now gently recommends:

> “This may be legitimate, but always double-check that you are on the employer’s official site.”

This supports user education without penalizing legitimate newer platforms.

---

## 🖥️ How to Run the Tool (Mac Instructions)

1. **Download or clone the repository:**
   ```bash
   git clone https://github.com/YourRepoName/job-listing-legitimacy-lens.git
