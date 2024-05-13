import re
from statistics import mean
from decorators import try_again_decorator
from utilities import TextParser
@try_again_decorator
def task2():
    '''Parses text in input.txt file.'''
    try:
        with open('input.txt', encoding='utf-8', newline='\n') as file:
            text = file.read()
            sentences     = TextParser.get_sentences(text)
            nar_sentences = TextParser.get_narrative_sentences(text)
            int_sentences = TextParser.get_interrogative_sentences(text)
            inc_sentences = TextParser.get_incentive_sentences(text)
            out = open('task2_result.txt', 'w', encoding='utf-8')
            out.write('Number of sentences:')
            out.write(f'All: {len(sentences)}')
            out.write(f'Narrative(.): {len(nar_sentences)}')
            out.write(f'Interrogative(?): {len(int_sentences)}')
            out.write(f'Incentive(!): {len(inc_sentences)}\n')
            word_lens = []

            for sentence in sentences:
                words = TextParser.get_words(sentence)
                word_lens.append(sum([len(word.strip()) for word in words]))

            out.write(f'Average sentence len: {mean(word_lens)}\n')
            words = TextParser.get_words(text)
            out.write(f'Average word len: {mean([len(word.strip()) for word in words])}\n')
            smiles = TextParser.get_smiles(text)
            out.write(f'Smiles count: {len(smiles)}\n')
            lcase_words = TextParser.get_lcase_words(text)
            out.write(f'Words starting with a lowercase letter: {lcase_words}\n')
            punctuation = TextParser.get_punctuation(text)
            out.write(f'Punctuation: {punctuation}\n')
            auto = TextParser.get_auto_numbers(text)
            out.write(f'Auto numbers: {auto}\n')
            cons = TextParser.get_words_with_coms(text)
            out.write('Words with a commas:')
            out.write(f'\nCount: {len(cons)}\n')
            out.write(' '.join(cons))
            out.write(f'\nLongest word:\n{TextParser.get_longest_word(text)}\n')
            out.close()
            f = open('task2_result.txt', encoding='utf-8')
            print(f.read())
            f.close()
            from zipfile import ZipFile
            with ZipFile('result2.zip', 'a') as zip_file:
                try:
                    zip_file.write('task2_result.txt')
                except UserWarning as err:
                    print(f'Warning: {err}')
                finally:
                    print('task2_result.txt info:')
                    print(zip_file.getinfo('task2_result.txt'))
    except FileNotFoundError as err:
        print(f'File error: {err}')
    except OSError as err:
        print(f'OS error: {err}')