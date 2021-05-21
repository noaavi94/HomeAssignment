import requests
from bs4 import BeautifulSoup
import re
import nltk as nltk


def print_most_common_per_len(most_common, i):
    for (a, b) in most_common:
        if len(a) == i:
            print("length ", i, ": ", a)
            break


def is_valid(word):
    return len(word) > 1 and not word.isnumeric()


def get_words(urls):
    words = []
    for url in urls:
        r = requests.get(url)
        html = r.text
        word_lengths = []

        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        tokens = re.findall('\w+', text)

        for word in tokens:
            word = word.lower()
            if is_valid(word):
                words.append(word)
                if (len(word) not in word_lengths):
                    word_lengths.append(len(word))
        return words


def get_common_words_by_len(urls):
    words = get_words(urls)
    freqdist = nltk.FreqDist(words)
    for i in range(10):
        print_most_common_per_len(freqdist.most_common(), i)


def main():
    urls = ["http://he.wikipedia.org",
            "http://ynet.co.il",
            "https://www.mako.co.il/",
            "https://www.bbc.com/"]

    get_common_words_by_len(urls)


if __name__ == "__main__":
    main()
