from collections import Counter, defaultdict
from random import choices
from re import fullmatch

from nltk.tokenize import WhitespaceTokenizer
from nltk.util import trigrams


def markov_chain(tokens):
    model = defaultdict(Counter)
    for head1, head2, tail in trigrams(tokens):
        model[f'{head1} {head2}'][tail] += 1
    return model


def make_sequence(model):
    first_word_pattern = r"[A-Z][\w\d']*"
    end_word_pattern = r"[\S]*[.!?]"

    list_keys = [*model]
    # A random capitalized word that does not end with a sentence-ending punctuation mark
    sequence = choices(list_keys)
    while not fullmatch(first_word_pattern, sequence[0].split()[0]):
        sequence = choices(list_keys)
    # Minimal sentence length 5 tokens, with a sentence-ending punctuation mark
    second = choices([*model[sequence[0]]])
    sequence.extend(second)

    key = f'{sequence[0].split()[1]} {second[0]}'

    for i in range(1, 100):  # not less then 5 tokens, till sentence-ending punctuation mark
        weights = [w for w in model[key].values()]
        next_word = choices(list(model[key]), weights)
        key = f'{sequence[i]} {next_word[0]}'
        sequence.extend(next_word)

        if i > 1 and fullmatch(end_word_pattern, next_word[0]):
            print(*sequence)
            break

def corpus_statistic(tokens):
    print('Corpus statistics')
    print('All tokens:', len(tokens))
    print('Unique tokens:', len(set(tokens)))


def main():
    with open(input(), "r", encoding="utf-8") as f:
        tokens = WhitespaceTokenizer().tokenize(f.read())

    model = markov_chain(tokens)

    for _ in range(10):
        make_sequence(model)


if __name__ == '__main__':
    main()
