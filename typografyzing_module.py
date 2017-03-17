import re


class Typograph():
    def __init__(self, text):
        self.typographed_text = self.typografy_text(text)

    def replace_commas(self, text):
        return re.sub(r'([\'"])(.*?)(\1)', r'«\2»', text)

    def delete_extra_spaces(self, text):
        return re.sub(r'\s{2,}', r' ', text)

    def delete_extra_lines(self, text):
        return re.sub(r'\n{2,}', r'\n', text)

    def replace_telephone_number_delimiters(self, text):
        return re.sub(r'(\d)?-(\d)', r'\1–\2', text)

    def chain_numbers_with_words(self, text):
        return re.sub(r'[^0-9]([а-яА-Яa-zA-Z.]+)\s?(\d+)', r' \1{}\2'.format('\u00A0'), text)

    def chain_short_words_with_next_word(self, text):
        return re.sub(r'\b([\w]{1,2}\s+)\b', r'\1{}'.format('\u00A0'), text)

    def typografy_text(self, text):
        text = self.replace_commas(text)
        text = self.delete_extra_spaces(text)
        text = self.delete_extra_lines(text)
        text = self.replace_telephone_number_delimiters(text)
        text = self.chain_numbers_with_words(text)
        text = self.chain_short_words_with_next_word(text)
        return text
