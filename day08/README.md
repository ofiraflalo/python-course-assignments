# Day 08 - PubChem Web Application

## Description

This project is based on my Day 6 PubChem Compound Analyzer project.  
The program uses the PubChem database to download chemical information about selected compounds and process the data.

In this version, I created a web application using FastAPI.  
The business logic is separated into a different file, so the same functions can be used by both the program and the web application.

## Project Structure

```text
day08/
├── app.py
├── pubchem_logic.py
├── test_pubchem_logic.py
├── test_app.py
├── requirements.txt
└── README.md
```

## Business Logic

The business logic is in:

```text
pubchem_logic.py
```

This file includes functions that:

- Download compound data from PubChem
- Analyze several compounds
- Calculate the average molecular weight
- Find the heaviest compound
- Find the most hydrophobic compound based on XLogP

## Web Application

The web application is written with FastAPI in:

```text
app.py
```

The application has two routes:

```text
GET /
POST /analyze
```

The `/analyze` route receives a list of compound names and returns the analyzed data.

Example input:

```json
{
  "compounds": ["caffeine", "aspirin", "glucose"]
}
```

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the web application:

```bash
uvicorn app:app --reload
```

Then open the browser at:

```text
http://127.0.0.1:8000
```

To use the automatic API page, open:

```text
http://127.0.0.1:8000/docs
```

## How to Run the Tests

Run:

```bash
pytest
```

The tests check both the business logic and the web application.

## AI Use

I used CHAT GPT to help me adapt my Day 6 project into a web application.  
AI helped me separate the business logic from the web application, write FastAPI routes, and create tests for both the logic functions and the web application.

Examples of prompts I used:

```text
I have a Python project that downloads chemical data from PubChem. Help me separate the business logic into a separate file.
```

```text
Help me create a FastAPI web application that uses my existing PubChem analysis functions.
```

```
