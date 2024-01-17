from flask import Flask, render_template, request, jsonify
import random
from openai import OpenAI
import re

app = Flask(__name__)
client = OpenAI()

# Predefined set of words
@app.route('/')
def index():
   words_string = newwords()  # Assuming newwords() returns a comma-separated string
   words_list = words_string.split(',')  # Split the string into a list
   random_words = random.sample(words_list, min(100, len(words_list)))  # Shuffle and pick 100 words
   return render_template('index.html', words=random_words)


def newwords():
   messages = [
      {"role": "user", "content": "give me a comma separated string of 100 random words for a fridge poetry we need varied types of word so that we can build sentences. This what i need: Nouns (20-30 Words), Verbs (20-30 Words),Adjectives (15-25 Words),Adverbs (10-15 Words),Pronouns (5-10 Words):,Conjunctions (5-10 Words), Prepositions (10-15 Words), Articles (2-3 Words), Interjections (5-10 Words), Miscellaneous (5-10 Words). don't say anything else."},
   ]
   model = "gpt-4-1106-preview"
   
   chat_completion = client.chat.completions.create(
      model=model, 
      messages=messages,
      temperature=0.7
   )
   
   reply = chat_completion.choices[0].message.content
   
   print (reply)
   
   return reply

@app.route('/construct', methods=['POST'])
def construct():
   availableWords = request.json['availableWords']
   placedWords = request.json['placedWords']
   available_words_string = ','.join(availableWords)
   
   messages = [
      {"role": "user", "content": f"'{available_words_string}'.\n\n\
Use one of the word above to extend this sentence:\
'{placedWords}'.\n\n\
You can only select one word an dit must be spelled exactly the same way as in the list of allowed words. Only reply with the select word, nothing else.\
You must select one of the following words to add to the sentence and reply with that word only, nothing else."},
   ]
   model = "gpt-4-1106-preview"
   model = "gpt-3.5-turbo"
   model = "gpt-4"
   print (messages)
   chat_completion = client.chat.completions.create(
      model=model, 
      messages=messages,
      temperature=0.7
   )
   
   reply = chat_completion.choices[0].message.content
   
   reply = re.sub(r'[^a-z]', '', reply)
   
   print (reply)
   
   return jsonify(reply)

def frippe_says(message):
   print (messages)
   print (message)
   #message = input("User : ")
   if message:
      messages.append(
         {"role": "user", "content": message},
      )
      model = "gpt-3.5-turbo"
      
      chat_completion = client.chat.completions.create(
         model=model, 
         messages=messages,
         temperature=0.7
      )
      
      reply = chat_completion.choices[0].message.content
      print (reply)
      
      messages.append({"role": "assistant", "content": reply})
      
      return reply
   else:
      return "huh?"

if __name__ == '__main__':
    app.run(debug=True)
   
