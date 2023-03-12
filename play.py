
import os

# load text from input.txt unicode
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('’', '\'')
text = text.replace('-', ' ')

text = text.replace('\n', ' ')
text = text.replace('\r', ' ')

#escape double quotes
text = text.replace('"', ' ')



#replace ^ with "to the power of"
text = text.replace('^', ' to the power of ')

# remove numbers between [ and ] (e.g. [1]) with regex
import re
text = re.sub(r'\[[0-9]*\]', '', text)

# replace  O( any ) (e.g. O(n^2)) with `O of $1` using regex
text = re.sub(r'O\((.{1,6})\)', r'O of \1', text)

#replace ( and ) with spaces
text = text.replace('(', ' ')
text = text.replace(')', ' ')

print(text)

# trim text
text = text.strip()

command = "tts --text \"" + text + "\""
os.system(command)

# play me.wav on windows using windows media player
os.system("start tts_output.wav")
