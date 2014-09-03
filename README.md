# Pypas

## Summary

-hy- Python pastebin clone along the lines of ix.io

# History

This is a fork from [Pastas](http://github.com/Willyfrog/pastas) which is
currently being used at work for passing along snippets of code and general text.

Some coworkers wanted to contribute and knew Python, but where *afraid* of Hy's
lispy syntax, so this fork was born.

It is also an exercise on how easy is to migrate from a Hy application into a
Python one. An I must say it is pretty easy!

# How to install

* clone the repository:

    git clone https://github.com/Willyfrog/pypas.git

* Create a virtual environment for it (not neccessary but it's good practice)

    mkvirtualenv pypas

* install the requirements:

    pip install -r requirements.txt

* create the configuration (optional). Make a config.json file on the root of the project. You can specify the following keys:

   + secretkey: needed to keep the client-side sessions secure
   + debug: True or False (defaults to false)
   + dbstring: string to connect to the database, if not specified it'll create a sqlite database. Check the dataset library documentation to know the different options

* run the server

    python pypaste.py

# Notice

    runing flask as is is not recommended for production, but pypas as is is not recommended to be exposed to the public.
