# Password-Strength-Checker

 Project Overview
 
Password Strength Checker is a Python-based GUI application that evaluates the strength of user-entered passwords and provides real-time feedback with suggestions for improvement. Weak passwords are a leading cause of data breaches — this tool helps users create strong, secure passwords by analyzing common vulnerabilities.

Objective

To help users identify whether their password is weak, medium, or strong using a rule-based evaluation system. It also offers suggestions and generates stronger alternatives.

Features :

Graphical User Interface (Tkinter)

Password analysis based on:

Length

Uppercase, lowercase letters

Digits and special characters

(Optional) Dictionary word detection using NLTK

Real-time strength feedback

Suggestions to improve weak passwords

 Generates a strong password if needed


 Technologies Used :
 
Python 3

Tkinter – for GUI

Regex (re module) – for pattern matching

NLTK (optional) – to check dictionary words


Password Strength Criteria :

Criteria	Requirement

Length	At least 8 characters

Uppercase	At least 1 uppercase letter

Lowercase	At least 1 lowercase letter

Digit	At least 1 number

Special Characters	At least 1 symbol (e.g., @, #, !)

Dictionary Word	Avoid common words (if using NLTK)

Example Output :

Entered Password: Password123

Strength: Medium

Suggestions:

Add a special character (e.g., !, @, #)

Avoid using dictionary words

Suggested Strong Password: Z#k2P@m9W!rT
