

## Continuous Integration

Travis CI was used.

https://travis-ci.com/

Travis CI is a web service which links to a Github account to provide continuous
integration. Travis CI is notified when your Github repository is updated and
then clones the repository and runs the instructions in the .travis.yml file
to download the required dependencies and run the tests for
your application.

I followed the following steps to set up Travis CI and activate continuous
integration with my project's repository.

I created a .travis.yml file in my repository's base directory. The travis.yml
had the following content:

I set the language to Python so Travis knows which interpreter to use.

    language: python
    
Tell Travis the Python version. This is very important as between Python versions
especially version 2 to 3 code may become invalid.
    
    python:
      - "3.4"
    
The following tells Travis to install the required libraries for my project. The
requirements.txt file is in the base folder of the repository and is simply a list
of my required libraries and their versions.

    install:
      - pip install -r tribe/requirements.txt
    
The next section tells Travis what it has to do to run my tests. Each line of 
this represents a command to be run.

    script:
      - cd tribe
      - python manage.py test

Signing up for a Travis account was quite straightforward. It is important to 
note that for my purposes travis-ci.com was used and not travis-ci.org, because
travis-ci.org only allows for public accounts and for academic purposes I needed
to keep my builds private.

I signed up for the free trial using my Github account. This was a one-click 
operation. I was then able to navigate to the billing settings and notify Travis
that I had a Github student account. Travis are part of this plan so I was
then allowed free access to a private account.

I was then able to switch on or off repositories from my Github account.

![Activating repositories in Travis-CI](screenshots/travis-repos.png)
