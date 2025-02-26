import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=
        'Clean a .bib file by removing unused references from a .tex file.')
    parser.add_argument('-b',
                        '--bib',
                        type=str,
                        default='references.bib',
                        help='Path to the .bib file (default: references.bib)')
    parser.add_argument('-t',
                        '--tex',
                        type=str,
                        default='main.tex',
                        help='Path to the .tex file (default: main.tex)')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=None,
        help=
        'Output filename for cleaned .bib file (default: cleaned_<input>.bib)')
    return parser.parse_args()


def load_file(filename):
    """Load the content of a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def extract_citations(tex_content):
    """Extract citation keys from \\cite{} and \\citeA{} commands."""
    tex_content = re.sub(r'\\citeA\{\}', '', tex_content)
    tex_content = re.sub(r'\\cite\{\}', '', tex_content)
    citations = re.findall(r'\\cite\{(.*?)\}', tex_content) + re.findall(
        r'\\citeA\{(.*?)\}', tex_content)

    extracted_citations = set()
    for citation in citations:
        extracted_citations.update(map(str.strip, citation.split(',')))

    return extracted_citations


def clean_bib_file(bib_content, citations):
    """Remove unused references from the .bib file."""
    cleaned_bib = []
    delete_flag = True
    for line in bib_content.splitlines():
        if line.strip().startswith('@'):
            citation_name = line.split('{', 1)[1].split(',', 1)[0].strip()
            delete_flag = citation_name not in citations
        if not delete_flag:
            cleaned_bib.append(line)

    return '\n'.join(cleaned_bib) + '\n'


def main():
    args = parse_arguments()

    bib_content = load_file(args.bib)
    tex_content = load_file(args.tex)

    citations = extract_citations(tex_content)
    cleaned_bib = clean_bib_file(bib_content, citations)

    output_filename = args.output if args.output else f'cleaned_{args.bib}'
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(cleaned_bib)

    print(f'Cleaned .bib file saved as {output_filename}')


if __name__ == '__main__':
    main()
