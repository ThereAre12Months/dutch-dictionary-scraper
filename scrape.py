import requests as req
from json import dump
from unidecode import unidecode

base_url = "https://woordenlijst.org/MolexServe/lexicon/get_suggestions?database=gig_pro_wrdlst&wordform="
letters = sorted("abcdefghijklmnopqrstuvwxyz0123456789")

all_words = open("words/all.txt", "w")

for l in letters:
    words = {}

    url = base_url + l + "%25"
    resp = req.get(url)

    content = resp.content

    start_match = b"<suggestions>"
    start_idx = content.find(start_match) + len(start_match)

    end_match = b"</suggestions>"
    end_idx = content.find(end_match)

    content = content[start_idx:end_idx]

    for w in content.split(b" | "):
        word = w.decode("utf-8").strip()
        all_words.write(word + "\n")

        norm = unidecode(word).lower()
        
        if len(norm) > 1:
            l2 = norm[1]
        else:
            l2 = ""

        if l2 not in words:
            words.update({l2:{}})
            
        words[l2].update({norm:word})

    with open(f"words/{l}.json", "w") as out:
        dump(words, out)
        
    print(f"finished {l}")

all_words.close()
