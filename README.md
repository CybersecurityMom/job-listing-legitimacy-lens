
<h1 align="center"><strong>Job Listing Legitimacy Lens (Demo)</strong></h1>

<p align="center">
  A beginner-friendly Python tool that helps users assess whether a job listing shows signs of legitimacy or potential fraud.
</p>

<p align="center">
  <strong>Signal-based. Educational. Human-first.</strong>
</p>

<hr />

<p>
  <strong>This project is not a verification engine.</strong><br />
  It is a signal-based assistant designed to surface red flags, positive indicators, and areas that deserve closer human review.
</p>

<p>
  The goal is <strong>awareness and education</strong>, not automated decision-making.
</p>

<h2>What This Tool Does</h2>

<p>
  The Job Listing Legitimacy Lens evaluates four key components of a job posting:
</p>

<ul>
  <li><strong>Company name</strong></li>
  <li><strong>Job source</strong> <em>(where the listing was found)</em></li>
  <li><strong>Contact email</strong></li>
  <li><strong>Job description</strong></li>
</ul>

<p>
  Using pattern checks, keyword detection, and weighted scoring, the tool classifies listings as:
</p>

<ul>
  <li><strong>Likely Legitimate</strong></li>
  <li><strong>Caution / Mixed Signals</strong></li>
  <li><strong>High Risk / Suspicious</strong></li>
</ul>

<p>
  Each result includes <strong>plain-language explanations</strong> so users understand why something may appear risky or credible.
</p>

<h2>Key Features</h2>

<h3>Smarter Job Source Evaluation</h3>

<p>
  Recognizes well-known job platforms such as <strong>Indeed</strong>, <strong>LinkedIn</strong>, <strong>Glassdoor</strong>, <strong>CareerBuilder</strong>, and <strong>ZipRecruiter</strong>.
</p>

<p>
  Unfamiliar platforms are <strong>not automatically penalized</strong>. Instead, the tool gently recommends confirming that the listing links to the employer’s official website.
</p>

<h3>Stronger Email Validation</h3>

<ul>
  <li>Checks for a valid <strong>@</strong> structure</li>
  <li>Validates realistic domain endings such as <strong>.com</strong>, <strong>.org</strong>, and <strong>.co</strong></li>
</ul>

<p>
  Malformed domains are flagged. Free-mail usage in professional job postings is highlighted when appropriate.
</p>

<h3>Critical Red Flag Detection</h3>

<ul>
  <li>Salary payment via Cash App, Zelle, Venmo, or PayPal</li>
  <li>Unrealistic salary or earnings claims</li>
  <li>Requests for upfront payment or personal information</li>
  <li>Overly hyped or informal language</li>
  <li>Repetitive or nonsensical text common in scam or bot-generated ads</li>
  <li>Missing job duties or qualification requirements</li>
</ul>

<p>
  When major red flags are detected, the risk score is <strong>significantly reduced</strong>.
</p>

<h3>Expanded Positive Signals</h3>

<ul>
  <li>Salary ranges</li>
  <li>Clearly defined responsibilities</li>
  <li>Experience or qualification requirements</li>
  <li>Benefits such as insurance, 401(k), PTO, retirement plans, and paid holidays</li>
  <li>Industry-standard HR language</li>
</ul>

<p>
  Positive indicators reduce risk incrementally, up to a safe maximum.
</p>

<h2>Scoring System</h2>

<table>
  <tr>
    <th>Score</th>
    <th>Assessment</th>
  </tr>
  <tr>
    <td><strong>90–100</strong></td>
    <td>Likely Legitimate (based on available signals)</td>
  </tr>
  <tr>
    <td><strong>70–89</strong></td>
    <td>Caution / Mixed Signals</td>
  </tr>
  <tr>
    <td><strong>40–69</strong></td>
    <td>Mixed Signals — verification recommended</td>
  </tr>
  <tr>
    <td><strong>0–39</strong></td>
    <td>High Risk / Suspicious</td>
  </tr>
</table>

<p>
  <em>Legitimacy does not guarantee safety.</em> This tool evaluates patterns, not employer identity.
</p>

<h2>Design Insight</h2>

<p>
  This project is still a <strong>work in progress</strong>.
</p>

<p>
  A key improvement came from feedback provided by a <strong>9-year-old collaborator</strong> who emphasized the importance of balancing negative signals with positive indicators. Rebalancing the scoring model based on that insight significantly improved accuracy and realism.
</p>

<p>
  Sometimes clarity comes from experience. Sometimes it comes from someone who understands balance instinctively.
</p>

<h2>Getting Started</h2>

<h3>Requirements</h3>

<ul>
  <li>Python 3.8 or higher</li>
</ul>

<h3>Run the Tool on macOS</h3>

<pre><code>git clone https://github.com/YourRepoName/job-listing-legitimacy-lens.git
cd job-listing-legitimacy-lens
python3 job_lens.py</code></pre>

<h2>Disclaimer</h2>

<p>
  This tool does not verify employers or job listings. It provides signal-based insights to support safer decision-making and user education.
</p>
