
# Email Analyser

## Requirements
All you need to check this out is **Python 3.10**.<br>
Possibly, if you would like to run tests, you have to install packages from `requirements.txt`.

## Description
The application makes operations on files and fetch required data from them. The application is looking for email adresses in
`emails` by default. This is necessary that it be in the same folder as `main.py` script. We will use `main.py` script to run commands.
There is an `email_analyser` package as well, which inside are `app.py` script and another two packages: `simply_cli` and `email_analyser` - again.

Firstly a few words about `simply_cli` package. Inspired by 'Click', I made (very) simply terminal app creator :).
The main features of this package are `SimplyCLI` class and `register_command` decorator. There is in this package the logic of running commands in terminal.

Another folder is `email_analyser` package where from `app.py` script imports modules to make tasks done. `app.py` imports `SimplyCLI` and
`register_command` also. `app.py` is the most outer layer of this project, from here `main.py` imports `EmailAnalyzer` class and invoke tasks.

## Usage
Clone the repository and in direction where `main.py` script is, run it within terminal with **Python 3.10** interpreter, like this:
```
git clone https://github.com/StefanoDaReel/email-analyser.git
cd email-analyser
python3 main.py
```
There should appear help panel with instructions. From now it should be easy, enjoy :)

![Screenshot from 2022-07-31 14-31-12](https://user-images.githubusercontent.com/68772546/182026548-aaf095e2-6014-4f56-a2ea-1f04029438d5.png)
