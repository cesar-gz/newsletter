# Your Personal Press
This web application has a form that you can fill to have a news letter sent to your email
with news on topics you want to know about. The email will be sent out weekly.

## How to use app
Fill out the form(in progress), click submit, and expect a email in a couple of minutes.

## How to set up the Front-End
1) git clone
2) open a terminal, cd to Front-End, and 'npm install'
3) same terminal, run 'ng serve'
4) go to localhost:4200 on a browser

## How to set up the Back-End
1) open a terminal, create a venv, activate it, then install the requirements
* `python -m venv myenv`
* `source myenv/bin/activate` or (for Windows users)`Set-ExecutionPolicy Unrestricted -Scope Process` then `myenv\Scripts\activate.ps1`
* `pip install -r requirements.txt`
2) then in the working directory run this command to run the uvicorn server
* `foreman start`
3) finally go to the following link to test the api
* `http://localhost:5000/docs`

## Background
This is a project I made for myself and for CPSC 491 as a exit project. The reason I wanted to do this project is because I wanted to have automatic news emails sent to me on various topics, so that I don't have to watch the news or research news.
