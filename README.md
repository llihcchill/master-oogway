# master-oogway
'*If she leaves you for another, there is always their mother,*' we all need advice like that and so here is a discord bot that gives advice in Master Oogway's voice.

# Overview:
Discord bot that gives advice using the discord.py library, with a seperate branch for the AI version of this which creates it's own quotes.
To ask for a quote, all you gotta do is type a question mark ("?") before your question, and the bot will answer with a quote:
```
| • ?why did she leave me?                  |
|                          l bozo + ratio • |
```
In an attempt to find an appropriate quote to output, Master Oogway will call the [ZenQuotes](https://zenquotes.io/api/quotes) API and check what verbs and nouns are common among both of them, and if there's a match, it will send the quote through to the channel the question was asked in.
# Installation
After I build a server to host this on, I will put the project up on [top.gg](top.gg) so you can try it out with no hassles, but otherwise you can put it on a hosting server or build one yourself, all it requires is a desktop of some kind (not a table) like an old PC or raspberry pi, and you want to create a web server using either [Django](https://djangoproject.com) or [Flask](https://flask.palletsprojects.com/en/2.2.x/) (which is what I'll develop next) and just run it on your localserver 24/7 :)
