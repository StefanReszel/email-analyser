
# Email Analyser

*Made by **Stefan Reszel***

stefanreszel@outlook.com

## Requirements
I decided to make app from scratch, so all you need to use it is **Python 3.10**.<br>
Possibly, if you would like to run tests, you have to install packages from `requirements.txt`.

## Description
There are, in the repository, `emails` direction and `email-sent.logs` file which were sent by you. The application is looking for email adresses in
`emails` by default. This is necessary that it be in the same folder as `main.py` script. We will use `main.py` script to run commands.
There is an `email_analyser` package as well, which inside are `app.py` script and another two packages: `simply_cli` and `email_analyser` - again.

Firstly a few words about `simply_cli` package. To create this the certain thought forced me, which was: "What if in the nearby future I will have to
do a similar app?". So, inspired by 'Click', I made (very) simply terminal app creator :). The main features of this package are `SimplyCLI` class and
`register_command` decorator. There is in this package the logic of running commands in terminal.

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

## Screens
![EAscreenHELP](https://user-images.githubusercontent.com/68772546/178119008-d16e34e8-fb20-495a-999f-bf17757e6ee4.png)
![EAscreenICS](https://user-images.githubusercontent.com/68772546/178119088-3061b088-449d-4962-90e4-720b4d7d491f.png)
![EAscreenERR](https://user-images.githubusercontent.com/68772546/178119226-139ededb-a31c-4c2e-ad55-80282da73093.png)
![EAscreenFEIL](https://user-images.githubusercontent.com/68772546/178119231-0e95dc60-dc5c-4f36-9504-b62991e9a578.png)
