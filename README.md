
Job Listing Legitimacy Lens (Demo)

A beginner-friendly Python tool that helps users assess whether a job listing shows signs of legitimacy or potential fraud.

This project is not a verification engine. It is a signal-based assistant designed to surface red flags, positive indicators, and elements that require closer human review.

The goal is awareness and education, not automated decision-making.

What This Tool Does

The Job Listing Legitimacy Lens analyzes four core components of a job posting:

Company name

Job source (where the listing was found)

Contact email

Job description

Using pattern checks, keyword detection, and weighted scoring, the tool categorizes listings as:

Likely Legitimate

Caution / Mixed Signals

High Risk / Suspicious

Each assessment includes human-readable explanations so users understand why something may appear risky or credible.

Features
Smarter Job Source Evaluation

Recognizes common job platforms such as Indeed, LinkedIn, Glassdoor, CareerBuilder, and ZipRecruiter.

Unfamiliar or nonstandard platforms are not automatically penalized. Instead, the tool flags them with a recommendation to confirm that the listing links to the employer’s official website.

Stronger Email Validation

Evaluates whether an email address:

Contains a valid @ structure

Uses a realistic domain (for example, .com, .org, .co)

Malformed or incomplete domains are flagged.
Free-mail usage in professional job postings is highlighted when appropriate.

Critical Red Flag Detection

Detects high-risk patterns including:

Salary payment via Cash App, Zelle, Venmo, or PayPal

Unrealistic salary claims

Requests for upfront payment or personal information

Excessive hype or informal language

Repetitive or nonsensical text commonly seen in scam or bot-generated ads

Missing job duties or qualification requirements

When major red flags are detected, the risk score is reduced significantly.

Expanded Positive Signals

Rewards legitimate job structure, including:

Salary ranges

Clearly defined responsibilities

Experience or qualification requirements

Benefits such as insurance, 401(k), PTO, retirement plans, and paid holidays

Industry-standard HR language

Positive indicators reduce risk incrementally, up to a safe maximum.

Scoring System

Final scores are categorized as follows:

90–100 Likely Legitimate (based on available signals)

70–89 Caution / Mixed Signals

40–69 Mixed Signals requiring verification

0–39 High Risk / Suspicious

Legitimacy does not guarantee safety. This tool evaluates patterns, not company identity.

Design Insight

This project is still a work in progress.

A key improvement came from feedback provided by a 9-year-old collaborator who emphasized the importance of balancing negative signals with positive indicators. Rebalancing the scoring model based on that insight significantly improved scoring accuracy and realism.

Sometimes clarity comes from experience. Sometimes it comes from someone who understands balance instinctively.

Getting Started
Requirements

Python 3.0 or higher

Run the Tool on macOS

Clone the repository:

git clone https://github.com/YourRepoName/job-listing-legitimacy-lens.git
cd job-listing-legitimacy-lens
python3 job_lens.py

Disclaimer

This tool does not verify employers or job listings.
It provides signal-based insights to support safer decision-making and user education.
