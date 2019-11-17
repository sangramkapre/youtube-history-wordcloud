import os
import sqlite3
import re
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import sys


################################################################
# YOUR CHANGES HERE #

# chrome history file path
history_file = "<< ENTER CHROME HISTORY FILE PATH HERE >>"
# e.g. history_file = "/home/sangram/.config/google-chrome/Default/History"

# list of words you want to ignore (leave empty if no such words)
unwanted_words = []
# e.g unwanted_words = ["enter", "words", "you", "want", "to", "ignore", "in", "this", "list"]

# name of the output file (can provide full path if requried)
output_image_name = "<< ENTER OUTPUT FILE PATH HERE >>"
# e.g. output_image_name = "youtube_history_wordcloud.png"

################################################################
# to check if inputs are provided
if history_file == "<< ENTER CHROME HISTORY FILE PATH HERE >>":
    sys.exit("\n\nError! Path to Chrome browser's history file is not updated.\n\n")

if output_image_name == "<< ENTER OUTPUT FILE PATH HERE >>":
    sys.exit("\n\nError! Path to WordCloud output image is not updated.\n\n")

if not unwanted_words:
    print ("\n\nWarning: List of unwanted words to be ignored from WordCloud is empty.\n\n")

################################################################

# get chrome history (make sure to close all CHROME tabs before executing)
con = sqlite3.connect(history_file)
c = con.cursor()
try:
    c.execute("select url, title, visit_count, last_visit_time from urls") #Change this to your prefered query
except sqlite3.OperationalError:
    sys.exit("\n\nError! Please close Chrome browser and run again.\n\n")

results = c.fetchall()

# filter youtube history
youtube_topics = [result[1] for result in results if 'youtube' in result[0]]

# remove special chars and numbers
youtube_topics = [re.sub('[^A-Za-z]+', ' ', t) for t in youtube_topics]

# remove single letter words
youtube_topics = [' '.join([x for x in line.split(' ') if len(x)>1]) for line in youtube_topics]

# remove YouTube word (present in every title)
youtube_topics = ' '.join(youtube_topics)
youtube_topics = ' '.join([t for t in youtube_topics.split(" ") if t.lower()!="youtube"])

# ignore unwanted words 
youtube_topics = ' '.join([t for t in youtube_topics.split(" ") if t.lower() not in unwanted_words])

# create word cloud
def create_word_cloud(string):
    cloud = WordCloud(width=1600, height=1600, background_color = "white", max_words = 1000, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file(output_image_name)

print ("\n\nCreating the word cloud...\n\n")
create_word_cloud(youtube_topics)
print ("\n\nThe word cloud is created: " + output_image_name + "\n\n")
