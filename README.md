This is a short script to quickly create a fun Word-Cloud from the titles of the YouTube videos watched (fetched from the Chrome browser's history).
I never imagined such a simple word-cloud could imply so much about one's personality (likes, interests, mood, etc.) !


### Getting Started

Clone this repository (or download and extract the ZIP) and navigate to **youtube-history-wordcloud** folder.

```
git clone https://github.com/sangramkapre/youtube-history-wordcloud.git
cd youtube-history-wordcloud
```

### Prerequisites

This script has been tested on Python3 so far. If you prefer to create a virtual environment (*highly recommended*):

```
virtualenv --python /usr/bin/python3 venv
source venv/bin/activate
```

Install required packages from **requirements.txt**:
```
pip install -r requirements.txt
```

### Create word cloud from YouTube watched videos!

```
python youtube_history_wordcloud.py
```

### Example Output

Here is what I got from my YouTube history:

![Youtube History WordCloud]
(https://github.com/sangramkapre/youtube-history-wordcloud/blob/master/youtube_history_wordcloud.png)