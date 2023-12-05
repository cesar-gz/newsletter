# Your Personal Press
This web application has a form that you can fill to have a newsletter email sent to your email with news on topics you want to know about. The email will be sent out weekly.

## How to use app
Fill out the form, click subscribe, and expect an email in a five minutes.
* Frontend: Currently up, https://cesar-gz.github.io/newsletter/
* Backend: Currently down, https://newsletter.api.cesargz.com/docs

# How to set up your own
I self hosted the Back-End on a raspberry pi and used my home router to port forward api requests
to the pi. I also already have a registered domain to host my home router's IP on, as well as a registered SSL certificate, and firewalls set up for the pi. This is optional if you decide to host
the back-end on a different system or provider than a self hosted pi.

I recommend setting this up on pi. Make sure the system you decide to host on has Python and Git.

* git clone this repo onto the system you want to host on

## How to set up the Back-End
1) open a terminal, create a venv, activate it, then install the requirements
* change directory in the Back-End, and run `python -m venv myenv`
* `source myenv/bin/activate` or (for Windows users) run `Set-ExecutionPolicy Unrestricted -Scope Process`, then `myenv\Scripts\activate.ps1`
* `pip install -r requirements.txt`
2) then in the Back-End directory run this command to run the uvicorn server
* `foreman start`
3) finally go to the following link to test the api
* `http://localhost:5000/docs`
4) create the SQL tables by opening another terminal, change directory to Back-End
* create a database.db file
* run `python populate.py` to populate tables
* your back-end is ready now, it is recommended to make fake users in the database to test the api

## How to set up the Front-End
1) open a terminal, cd to Front-End, and run `npm install` to get the dependencies
2) in the same terminal, run `ng serve`
3) go to localhost:4200 on a browser
4) to deploy/host the Front-End, run `ng build --base-href /newsletter/`, to create a doc folder
5) I hosted the Front-End on GitHub pages, by setting the repo this project is on, to be hosted
by a doc folder. I did this by modifying the settings in this git repo's "Actions" section
6) run `git push` to push the front-end to your repo and have github actions deploy the doc folder

## How to set up the scripts folder
This section assumes the directions were followed correctly in the "Back-End" section of this README.
I also have a .env file where I store my credentials for sending emails. The scripts
are set up to import the environment variables as well. So you may want to create a .env file as well. The script that sends email requires you to import your email's username and password from the .env file.

1) Set up the dependencies by running, `pip install requests`, `pip install -U g4f`, `pip install smtplib`
2) with the Back-End running on one terminal, open another terminal, change directory to the scripts folder
* run `python main.py` to perform a script that will call Bing's gpt4 model to perform web searches,
and then when completed, store the searches into the database. This script takes a while based on your
hardware.

### Finished
That should be it to set up. I usually have my raspberry pi running to keep the backend up, and so that
when the form is filled out a new subscriber will be able to fill out the form successfully. I have a cron job set up on pi that will auto send emails once a week to the subscribers on my database. It does
this by automatically running the main.py script.

### Background
This is a project I made for myself and for CPSC 491 as a exit project. The reason I wanted to do this project is because I wanted to have automatic news emails sent to me on various topics, so that I don't have to watch the news or research news.
