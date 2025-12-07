

# Job Listing Legitimacy Lens

Job Listing Legitimacy Lens is a tiny, rule-based prototype that gives a rough “trust score” for job postings. It was inspired by an early Innovation Lab mental model exploring how job seekers evaluate whether a job opportunity feels legitimate or potentially fraudulent. This project is not a real security product. It is a teaching prototype showing how research and mental models can be translated into simple working logic.

---

## 🌱 Why This Exists

During the Innovation Lab, our group explored the question: **“How do job seekers know whether a posting is real?”**  
Even though our team ultimately selected a different idea for the final project, this concept stayed with me.

I built this tool as an **additional exploration** to demonstrate how a mental model can evolve into a working prototype using simple rules and transparent reasoning.

This project highlights:

- How UX thinking can support user trust  
- How mental models turn into decision frameworks  
- How logic pathways can help job seekers make sense of risk  

---

## 🔍 What the Tool Does

The tool asks the user for:

- Company name  
- Where the job was found  
- Contact email  
- Full job description  

Then it checks for:

- Missing or unclear company information  
- Extremely short or vague descriptions  
- Suspicious red-flag phrases (e.g., “earn money fast,” “wire money,” “training fee required,” “urgent hire,” “no experience needed”)  
- Free or unprofessional email domains  
- Pressure-style scam wording  

---

## 🎯 What the Tool Returns

The script produces:

- A **trust score** (0–100)  
- A **risk category**:
  - Likely Legitimate  
  - Needs More Info  
  - High Risk / Suspicious  
- A list of **reasons** explaining why the score was generated  

This keeps the scoring transparent and easy to understand.

---

## 🛠️ How to Run the Tool

### 1. Make sure Python 3 is installed.

### 2. Download or clone this repository:
```
git clone https://github.com/YOURUSERNAME/job-listing-legitimacy-lens.git
cd job-listing-legitimacy-lens
```

### 3. Run the script:
```
python3 job_trust_checker.py
```

### 4. Follow the prompts:
- Enter company name  
- Enter where you found the job  
- Enter contact email  
- Paste the full job description  
- Type **END** on a new line when finished  

The tool will output the trust score, risk label, and reasons.

---

## 🧪 Example (Shortened)

**Input:**
```
Company: Best Careers LLC
Source: Facebook
Email: jobsnow@gmail.com

Description:
Earn money fast from home! No experience needed.
Training fee required. Apply immediately.
END
```

**Output:**
```
Score: 21/100
Assessment: High Risk / Suspicious

Reasons:
- Very short description
- Multiple red-flag phrases detected
- Free email domain
- Missing company details
```

---

## 📂 Project Structure

```
job-listing-legitimacy-lens/
├─ README.md
├─ job_trust_checker.py
└─ data/
   └─ sample_job_listings.json
```

---

## ⚠️ Limitations

This prototype:

- Does NOT validate whether a job is actually real or fake  
- Uses simple rules, not machine learning  
- Should not be used as an official verification tool  
- Exists purely for learning and demonstration  

A real system would require:

- Verified employer databases  
- Scam intelligence sources  
- Text analysis models  
- API-based validation  

---

## 🙏 Credits & Inspiration

Created by **Aqueelah Emanuel** as a bonus exploration during the Innovation Lab.  
This prototype demonstrates how UX research, mental models, and transparent logic can evolve into early functional tools, even in their simplest form.
