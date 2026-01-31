# Installing

prerequisites:
* python3
* python3-venv
  
```sh
git clone 'https://github.com/ThereAre12Months/dutch-dictionary-scraper.git'
cd dutch-dictionary-scraper

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt --upgrade
deactivate
```

# Using

```sh
source .venv/bin/activate
python3 scrape.py
deactivate
```

In the `words/` directory you will now find an `all.txt` file and a .json file for every letter of the alphabet.

The .json files are further subdivided by the second letter of the word for easier searching. Every word entry has it's unicode-normalised, lower-case version as the key and it's canonical form (=with upper-cases and diacritics) as the value.  

How a small sample of a `words/a.json` could look like:
```json
{
	"a": {..., "aalst":"Aalst", ...},
	"b": {..., "abrupt":"abrupt", ...},
	...
}
```

If you wanted to list all words starting with 'am' you would do it the following way.  
```py
import json

with open("words/a.json", "r") as f:
	words = json.load(f)["m"].values()

for word in words:
	print(word)
```
