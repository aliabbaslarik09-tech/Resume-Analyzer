# 📄 Resume Scoring & Improvement Tool

## Overview
This project is a Python-based tool that reads a resume from a plain `.txt` file, evaluates its quality, and assigns a **score out of 100**. In addition to scoring, it provides **clear, actionable feedback** on what needs to be improved to make the resume stronger and more ATS-friendly.

The tool is designed to help job seekers quickly understand how good their resume is and what specific changes can increase their chances of getting shortlisted.

---

## Features
- Reads resume content from a `.txt` file  
- Scores the resume on a **0–100 scale**  
- Evaluates structure, clarity, keywords, and impact  
- Identifies weak or missing sections  
- Suggests **what to fix and how to fix it**  
- Simple and lightweight (no heavy dependencies)

---

## How It Works
1. The program reads the resume text file.
2. It analyzes key resume factors such as:
   - Section presence (summary, experience, skills, etc.)
   - Use of action verbs and measurable achievements
   - Keyword relevance
   - Consistency and readability
3. A final score is calculated.
4. Improvement suggestions are generated based on gaps and weaknesses.

---

## Usage

```bash
python resume_scorer.py
