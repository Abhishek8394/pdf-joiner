from argparse import ArgumentParser
from pypdf import PdfMerger
import logging

logging.basicConfig(level=logging.INFO)

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('files', nargs='+', help='PDF File list in order')
    parser.add_argument('-o', '--out-file', help='output file', required=True)
    return parser

def merge_files(files, out_file):
    merger = PdfMerger()
    for pdf in files:
        logging.info("Adding file: %s", pdf)
        merger.append(pdf)

    merger.write(out_file)
    merger.close()

def main():
    args = get_parser().parse_args()

    merge_files(args.files, args.out_file)

if __name__ == '__main__':
    main()

