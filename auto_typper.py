import re
import pyautogui


string = str()
words = list()

try:
    with open("WordsHTML.txt") as file:
        for line in file.readlines():
            string = line
except Exception as e:
    print(e)


regex = re.sub("<span class=\"\">", "", string)
regex = re.sub("<\/span>", " ", regex)
regex = re.sub("<div class=\"place\" style=\"top: 4px;\"><span class=\"highlight\">", "", regex)
regex = re.sub(" <\/div>", "", regex)
regex = re.sub(" ", "\n", regex)
for word in regex.split("\n"):
    words.append(word)

for word in words:
    pyautogui.write(word)
    pyautogui.press("space")
