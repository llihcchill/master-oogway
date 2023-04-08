# master-oogway
'*If she leaves you for another, there is always their mother,*' we all need advice like that and so here is a discord bot that gives advice in Master Oogway's voice.

# Overview:
Discord bot that gives advice using machine learning and the discord.py library. This is going to be my first machine learning project ever so hopefully this thing works and I don't upset literally every machine learning engineer/data scientist with my documentation :)

# How the machine learning algorithm works:
## *Note: Before the algorithm is used the question in question (hehe) gets separated into its nouns and its verbs to be put into the algorithm, and also if possible, get only the quotes that contain most to all of the nouns and verbs or something along those lines.*
The machine learning algorithm in question is called the [Long Short-Term Memory (LSTM)](https://www.youtube.com/watch?v=YCzL96nL7j0) algorithm.
There are two inputs to the algorithm, of which one takes in the nouns and the other takes in the verbs:
```
code that is yet to be written
```
After it gets all the inputs, it will find all the synonyms of the verbs and nouns, and go through the noun and verb API's and find quotes containing those synonyms and original verbs and nouns:
```
code that is yet to be written
```
Now the algorithm should have an understanding of what it's trying to answer, so it will compare it's combinations to the quotes from the api that contain the verbs and maybe some of the nouns in the question.
```
even more code that is yet to be written
```
At this point, the algorithm will be trained using Gradient Descent to learn from itself and make new quotes from the ones it gets from [ZenQuotes](https://zenquotes.io/api/quotes)
---------------------------------------------
*picture of algorithm looking all cool*
