from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from datetime import datetime
import nltk # nltk.download('punkt')

def summarize_text(input_file, output_file_prefix='summary', summary_percentage=0.1):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    # calculate the number of sentences based on the percentage of the original text
    sentences_count = int(len(parser.document.sentences) * summary_percentage)
    summary = summarizer(parser.document, sentences_count=sentences_count)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'{output_file_prefix}_{timestamp}.txt'

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(" ".join(str(sentence) for sentence in summary))

    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    input_file_path = 'input.txt'
    summarize_text(input_file_path)
