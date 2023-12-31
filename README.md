# UltraCrew
#### UltraCrew is a Django web app for ultramarathon crews to track their runners and predict when runners will arrive at aid stations.
Often ultramarathon runners have friends or family act as their crew, providing them with water, food, and other supplies at aid stations along the race course. However, considering the long distances involved, it can be difficult for crew members to guess when their runner will arrive at each aid station. UltraCrew projects when the runner will arrive at future aid stations and makes it simple for crews to log the runner's progress. UltraCrew makes crew's job easier and can also provide race strategy insights since crews can let runners how they are doing compared with their goal.
I coded UltraCrew for my final project for Harvard's excellent CS50 course.
#### Check out the demo here: https://ricecodes.pythonanywhere.com/
#### Video Demo: https://youtu.be/dQhCoqGzgHE

## Stack
I chose to use a Django backend to leverage its built-in admin and authentication systems, convenient database access using Django models, and simplified data validation using Django model forms. I considered Flask, which was used in CS50 and would have been simpler in some respects, but decided on Django since its security features would allow me to confidently offer the app to other users (although I also designed it to minimize any sensitive information that could be leaked in a security flaw). On the frontend, I used some Bootstrap CSS components to provide a modern and responsive appearance while also defining custom CSS to help organize forms generated by Django and give a unique theme with a trail running aesthetic. I currently decided to deploy using Python Anywhere since it is free and made deploying a Django app relatively simple. In the future I hope to learn how to deploy using AWS.

## Apps
My Django project includes three apps that I added:
1. The **accounts** app manages the create account and login pages
2. The **home** app manages the homepage
3. The **runner** app includes the core functionality of the website. The main views it provides are
   - **addRace** to create a new race
   - **runnerPage** to display all of a given users races, provide time projects, and allow for logging checkpoints by authorized crew
   - **crewPage** to view all of the races a given user has been asked to crew and give links to the corresponding runnerPages

## Models in the runner app
I tried to structure the Django models, which provide convenient access to a sqlite3 database, so allow for expansion of the app beyond its current feature set. The models are:
1. **Race** A user agnostic definition of a race. In the future, a user could join a race defined by a different user instead of creating their own, although this has not been implemented yet.
2. **AidStation** Many aid stations may be associated with one race and each must have a name and its distance.
3. **RaceRegistration** This model lets a user set their goal and their crew for a given race.
4. **Checkpoints** Checkpoints contain the logged time when I user arrives at a given aid station. They are associated with one user and one race. The time is automatically set in the backend so that the crew only has to click one button. Times in the backend are all in GM time to account for the possibility of a race that transcends timezones.

## Languages Used
### Python
As a Django app, UltraCrew is coded primarily in Python. I used Django's models for database access and model forms for recieviing and validating data. Pace calculations were also done in Python and the results were provided as dictionaries to the HTML template renderer.
### HTML, CSS
I designed the template html pages using Django's templating system. Within the root template folder I made layout.html which provides a consistent Navbar through all of the pages while the individual apps include the pages that utilize that template. I especially strove in testing to ensure that the site would be responsive on mobile devices since the crew members are expected to track and log their runners using phones.
### Javascript
A few of the desired frontend behaviors required Javascript. 
1. The collapseable race tables in the runner page retain their state after refresh or logging a station in runnerPage.html by storing their state in local storage.
2. Users can dynamically create or remove aid station forms in addRace.html so that any number of aid stations can be accommodated.
Currently the javascript is included within the .html templates.
3. GM time times from the backend are converted into the user's local time zone.
## Acknowledgements
I want to especially thank the entire CS50 team, particlarly Professor Malan and Brian Yu. I would also like to thank my Dad, who has been my crew for all seven of my ultramarathons and who was the inspiration (and intended user) for this app.
