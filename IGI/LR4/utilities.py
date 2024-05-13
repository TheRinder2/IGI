from abc import ABC, abstractmethod
import re
from entities import Tree

class DictToStudentMixin:
    def convert(self, d: dict) -> Tree:
        '''Converts dict objectd to Tree.'''
        try:
            tree = Tree(
            d.get('name'), 
            int(d.get('count')),
            float(d.get('countOfNorm')))
        except TypeError as err:
            print(f'Incorrect type: {err}')
        except ValueError as err:
            print(f'Incorrect value: {err}')
        else:
            return tree


class Serializer(ABC):
    @abstractmethod
    def serialize(self, fileName: str, data: list, columns=None):
        '''Serializes given data to fileName.csv.'''
        pass

    @abstractmethod
    def deserialize(self, fileName: str) -> list:
        '''Deserializes data from fileName.csv.'''
        pass


class CsvSerializer(Serializer,  DictToStudentMixin):
    def serialize(self, fileName: str, data: list, columns=None):
        import csv

        with open(fileName, "w") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)

    def deserialize(self, fileName: str) -> list:
        import csv

        with open(fileName, newline='\n') as f:
            reader = csv.DictReader(f)
            return [self.convert(obj) for obj in list(reader)]


class PickleSerializer(Serializer,  DictToStudentMixin):
    def serialize(self, fileName: str, data: list, columns=None):
        import pickle

        with open(fileName, "wb") as f:
            pickle.dump(data, f)

    def deserialize(self, fileName: str) -> list:
        import pickle

        with open(fileName, "rb") as f:
            return [self.convert(obj) for obj in pickle.load(f)]
        

class TextParser:
    regex = {
    'sentences'     : r'\s*[\w,;\()\'"\s]+(?:\.|\?|!)\s*',
    'sentences_pov' : r'\s*[\w,;\()\'"\s]+\.\s*',
    'sentences_vop' : r'\s*[\w,;\()\'"\s]+\?\s*',
    'sentences_pob' : r'\s*[\w,;\()\'"\s]+!\s*',
    'words'         : r'\s*\b([a-zA-Z\']+)\b\s*',
    'smiles'        : r'[;:]-*(?:\(+|\)+|\[+|\]+)',
    'lcase_words'   : r'\b[a-z]\w*\b',
    'punctuation'   : r'(\.\.\.|\.|\?!|!|\?|,)',
    'auto'          : r'[A-Z]{2}\d{4}',
    'сoms'          : r'[a-zA-Z]+[,]',
    'equal_letters' : r'\b\w*(?P<letter>\w)(?P=letter)\w*\b'
    }

    @classmethod
    def get_sentences(cls, text: str) -> list:
        '''Find all sentences in text.'''
        return re.findall(cls.regex.get('sentences'), text)
    
    @classmethod
    def get_narrative_sentences(cls, text: str) -> list:
        '''Find all narrative sentences in text.'''
        return re.findall(cls.regex.get('sentences_pov'), text)
    
    @classmethod
    def get_interrogative_sentences(cls, text: str) -> list:
        '''Find all interrogative sentences in text.'''
        return re.findall(cls.regex.get('sentences_vop'), text)
    
    @classmethod
    def get_incentive_sentences(cls, text: str) -> list:
        '''Find all incentive sentences in text.'''
        return [word.strip() for word in re.findall(cls.regex.get('sentences_pob'), text)]

    @classmethod
    def get_words(cls, text: str) -> list:
        '''Find all words in text.'''
        return re.findall(cls.regex.get('words'), text)
    
    @classmethod
    def get_smiles(cls, text: str) -> list:
        '''Find all smiles in text.'''
        return re.findall(cls.regex.get('smiles'), text)   

    @classmethod
    def get_lcase_words(cls, text: str) -> list:
        '''Find all words that start with lowercase letter in text.'''
        return re.findall(cls.regex.get('lcase_words'), text) 
    
    @classmethod
    def get_punctuation(cls, text: str) -> list:
        '''Find all punctuation signs in text.'''
        return re.findall(cls.regex.get('punctuation'), text)
    
    @classmethod
    def get_auto_numbers(cls, text: str) -> list:
        '''Find all auto numbers in text.'''
        return re.findall(cls.regex.get('auto'), text)
    
    @classmethod
    def get_words_with_coms(cls, text: str) -> list:
        '''Find all words with commas in text.'''
        return re.findall(cls.regex.get('сoms'), text)

    
    @classmethod
    def get_longest_word(cls, text: str) -> list:
        '''Find the longest word in text.'''
        return max(cls.get_words(text), key=len)
