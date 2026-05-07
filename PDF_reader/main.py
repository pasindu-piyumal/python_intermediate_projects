import re
from collections import Counter
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)

        print('Pages:', len(reader.pages))
        print('-'*10)

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text
    
def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        # print(split_text)

        all_words += [words for words in split_text if words]
    
    return Counter(all_words)
    
def main():
    extracted_text: list[str] = extract_text_from_pdf('python_intermediate_projects/PDF_reader/sample.pdf')
    counter: Counter = count_words(text_list=extracted_text)

    for page in extracted_text:
        print(page)
        print('-'*30)

    for word, mention in counter.most_common(5):
        print(f'{word:20}: {mention}')

if __name__ == "__main__":
    main()