**PYTHON EMAIL EXTRACTION AND ANALYZER PROJECT**



**## 1. PROJECT OERVIEW**



This Python project uses python to automate the analysis and tracking of Freelancer job emails. It was undertaken as a way to address a personal need to determine some of the most demanded tech skills. This project demonstrates back-end and data engineering skills using python as the main language. It sources data from emails received from Freelancer and converts them into structured datasets for analysis, filtering, and future automation.



The project demonstrates practical skills in:



 Python automation and programming

 Email processing

 ETL pipeline development

 Data cleaning and transformation

 CSV data engineering and storage

 PostgreSQL integration

 Task scheduling

 Back end development fundamentals

 Data pipeline design

 Application and use of Python libraries and packages such as imaplib and Pandas 

 Data cleaning

 HTML parsing

 Email parsing

 IMAP email access



**## 2. BUSINESS PROBLEM / PROBLEM STATEMENT**



Freelance platforms send large numbers of job notifications by email. Manually reviewing and organizing these opportunities is time-consuming and inefficient.



This project automates the process by:



1\. Reading job notification emails.

2\. Extracting relevant job details

3\. Converting unstructured email content into structured data.

4\. Saving results into CSV files and databases.

5\. Supporting automated filtering and ranking of opportunities



The email data extracted can be used to:



 Analyze demand for specific technologies

 Identify frequently requested skills

 Track job opportunities over time

 Compare job budgets

 Monitor job categories

 Identify suitable jobs for applications

 Measure the frequency of incoming opportunities



The extracted and analyzed data can be used to answer questions such as:



 How many job opportunities were received?

 Which skills are most frequently requested?

 What types of projects are most common?

 What is the typical project budget?

 Which technologies are in demand?

 How many jobs match a specific skill set?

 How does demand change over time?



**## 3. PROJECT FEATURES**



1\. Connect directly to email inbox using IMAP.

2\. Read saved email files

3\. Process already received job emails automatically by extract key job details

4\. Create a dataframe or matrix of job details

5\. Store data in csv to be uploaded into PostgreSQL

6\. Generate reports and dashboards using data extracted



**## 4. PROJECT ARCHITECTURE AND WORKFLOW**



Connect directly to email inbox using IMAP.

&#x20;   ↓

Email Inbox

&#x20;   ↓

Read emails using IMAP

&#x20;   ↓

Filter only Freelancer.com emails

&#x20;   ↓

Extract job information from email body

(data extraction and validation)

&#x20;   ↓

Store in Python dictionary

&#x20;   ↓

Convert to Pandas DataFrame

&#x20;   ↓

Export to CSV

&#x20;   ↓

Export csv to PostgreSQL

&#x20;   ↓

Develop analytics: dashboard and reports



**## 5. PROJECT STRUCTURE**



freelancer\_job\_tracker/



|------ data/

|	 |------raw/

|	 |------processed/

|	 |------job.csv

|

|------ docs/

|       |------architecture.md

|	 |------assumptions.md

|	 |------data\_dictionary.md

|	 |------screenshots/

|

|------ logs/

|

|------notebooks/

|

|------src/

|	|------email\_reader.py

|      |------extractor.py

|	|------main.py

|	|------scheduler.py

|	|------storage.py

|	|------screenshots/parser.py

|	|------validator.py

|

|-----tests/

|

|-----.env

|-----requirements.txt

|----README.md

|\_\_\_ LICENSE



**## 6. TECHNOLOGIES / TOOLS USED**



 Python

 Python libraries / packages

&#x09; Pandas

&#x09; BeautifulSoup

&#x09; IMAP

&#x09; email

&#x09; os

&#x09; re

&#x09; email.utils

 Gmail

 PostgreSQL

 Git / GitHub

 Visual Studio Code

