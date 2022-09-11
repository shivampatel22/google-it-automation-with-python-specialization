Week6 - 
=======
Writing a Script from the bottom up
-----------------------------------

<h3>Problem Statement</h3>
<p>Create a daily report that tracks the use of machines. Specifically, create report that generates which users are currently connected to which machines.</p>

<h3>Criteria</h3>
<p>Input-
An instance of the event class which will contains the following:

- The date when the event happened
- The name of the machine where it happened
- The user involved.
- The event type, which includes the login and logout event type
- The event types are strings and the ones we care about are login and logout
</p>

The class event has the following attributes:

- date
- user
- machine
- type
<p>
Output-
Print the machine name followed by all the current users separated by commas.
</p>

<h3>Approach</h3>

- Sort the list of events chronologically.
- Store the data in a dictionary of sets.
- We need keep track of who's logged into which machine.

*Set provides O(n) search*
- Print the dictionary


Final Project-
=============

Problem Statement
-----------------

Create a "word cloud" from a text by procssing the text and return a dictionary that outputs the frequency of each words.

<h3>Criteria</h3>

- Input
- Processing the text
- Remove punctuation
- Ignore case and words that do not contain all alphabets
- Count the frequencies
- Ignore uninteresting or irrelevant words
- Output
  
*A dictionary is the output of the calculate_frequencies function. The wordcloud module will then generate the image from your dictionary.*

<h3>Approach</h3>

- Browse and upload a text to be processed
- Remove puntuations and normalize the letters
- Create a set to store the uninteresting words
- Create a dictionary that uses a word as a key and frequencies of the word as a value
- Use WordCloud framework to generate a image of world cloud
  
> Output - 

 ![wordcloud](/assets/wordcloud.png)