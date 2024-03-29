# File(PDF/JPEG/PNG) to text using OCR

## Table of content

- Introduction
- Requirement
- Installation
- Guide
- Approach
- Challenges faced
- Learned from assignment
- Link to app working video

## Introduction

This app helps user to convert their PDF file or Images(JPGE/PNG) into text using OCR. This app is made using Django. You can login by registering to this app or you can login directly via Google SSO.

## Requirement

Following should be installed in your system

1. Python
2. Django

## Installation

1. Create a virtual environment for installing following dependencies

   - python -m venv env

2. Now activate environment

   - source env/bin/activate

3. Install following packages using pip

   - pip install django
   - pip install psycopg2-binary
   - pip install pillow
   - pip install pytesseract
   - pip install pdf2image
   - pip install django-allauth
   - pip install django-crispy-forms

4. Install this software in your system

   - sudo apt-get install tesseract-ocr

## Guide

When you runserver using

- python manage.py runserver

Then if you are a new user then you must sign-up for using this app or you can use google SSO.

If you are already a user then you can simply login.

After login/signup you will be redirected to list of files you have already upload.

Now you see the text extracted from files by clicking on file or you can navigate to upload section to upload more files.

## Approach

Firstly I have to connect my django app with Postgresql.

Then I started out finding for a library that can convert pdf to text then I understand they work with typed character. Now, I have started finding library that uses OCR for conversion.

After this I have a basic functional app. Then I added authorization.

A basic working app is ready. So, I started modifing app in such a way that it can fullfill the instruction
and added styling to the app.

Finally I implemented User Authentication / Single Sign On(SSO).

## Challenges faced

- Installation and intial set up for postgresql and pgadmin4
- Finding out better library for converting images to text using OCR
- Worked with new library for SSO.

## Learned from assignment

- Django with POSTGRES
- pdf/jpeg/png to text using OCR
- Implementation of SSO in Django

## Link to app working video

- [G-drive](https://drive.google.com/drive/folders/1HmFsxC3uximWRLvMbjeA4_Ak9qQ3itrH?usp=share_link)
- I have added comments for the logic of the application.  
