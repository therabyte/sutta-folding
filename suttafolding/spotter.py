#!/usr/bin/python
# -*- coding: utf-8 -*-
import unicodedata
import string
import re

def normalize(input_string):
    """Discards accents, weirds chars and punctuation from a string.

    Parameters
    ----------
    input_string: {str}

    Returns
    -------
    {str}: the normalized string

    Notes
    -----
    Transforms the string in NKFD normalized string,
    ignores non ASCII chars,
    and removes all chars in string.punctuation.
    """
    nfkd_form = unicodedata.normalize('NFKD', input_string)
    text_input = str(nfkd_form.encode('ASCII', 'ignore'))
    translator = str.maketrans('', '', string.punctuation)
    out = text_input.translate(translator)
    return(out)


def tokenizer_3gram(input_string):
    """Explodes a string into letter 3 grams.

    Parameters
    ----------
    input_string: {str}

    Returns
    -------
    {list}: list of tuples of len 3 made of successive chars
    """
    w = normalize(input_string)
    return([ (w[i], w[i+1], w[i+2]) for i in range(0, len(w)-2)])


def word_spotter(sentence, wordlist):
    """Spots words in a sentence using the 3gram technique.
    - cuts words in wordlist into letter 3 grams,
    - tries to find each letter 3 gram in sentence,
    - returns the number of 3 grams found for each word in wordlist

    Parameters
    ----------
    sentence: {str} a text as string
    wordlist: {list} of {str}

    Returns
    -------
    {list}: of tuples as (w, v1, v2),
            w is the word from wordlist,
            v1 the number of 3 grams of w found in sentence
            v2 the total number of 3 grams in w
    """
    sentence_3gram = set(tokenizer_3gram(sentence))

    ret = []
    for w in wordlist:
        w_3gram = tokenizer_3gram(w)
        count = len([ mol for mol in w_3gram if mol in sentence_3gram ])
        ret.append((w, count, len(w_3gram)))
    return(ret)

def sent_tokenizer(text):
    l = re.compile("[!\?\.]").split(text)
    return([s for s in l if len(s) > 0])

def section_tokenizer(text):
    l = re.compile("[\\n]").split(text)
    return([s for s in l if len(s) > 0])


if __name__ == '__main__':
    with open('testdata/sn.56.11.txt', 'r') as ifile:
        content = ifile.read()

    sentence = """bhikkhave, dukkhaṃ"""
    testlist = ['dukkha', 'bhikkhu']

    print(tokenizer_3gram(testlist[0]))
    print(tokenizer_3gram(testlist[1]))
    print((tokenizer_3gram(sentence)))
    print(word_spotter(sentence, testlist))

    sentences = sent_tokenizer(content)
    print(len(sentences))
