import sys
import argparse
import urllib.request
from bs4 import BeautifulSoup

def translate(lang_pair, word):
    req = urllib.request.Request(
        url=f"https://www.wordreference.com/{lang_pair}/{word}",
        headers={
            # It is mandatory to set the User-Agent otherwise wordreference will
            # not respond
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        }
    )
    res = urllib.request.urlopen(req)
    data = res.read().decode("utf-8")

    soup = BeautifulSoup(data, 'html.parser')
    main_translations = soup.find_all("table", {"class": "WRD"})[0]

    print("Translation:", end="\n\n")

    for tr in main_translations.find_all("tr")[2:]:
        from_word = tr.find("td", {"class", "FrWrd"})
        if from_word:
            from_word = from_word.find("strong").get_text()

        to_word = tr.find("td", {"class", "ToWrd"})
        if to_word:
            to_word = to_word.contents[0]

        if from_word and to_word:
            from_word = from_word.strip()
            to_word = to_word.strip()
            print(f"{from_word}: {to_word}")

arg_parser = argparse.ArgumentParser(
    description="Get wordreference word translation")
arg_parser.add_argument("languages", metavar="LANGUAGES",
                        help="Language pair to use for translation (ex: enfr)")
arg_parser.add_argument("word", metavar="WORD", help="Word to translate")

args = arg_parser.parse_args()

lang_pair = args.languages
word = args.word
translate(lang_pair, word)
