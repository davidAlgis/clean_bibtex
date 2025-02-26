# Clean Bib Files

This tool is a fork of the repository [SFLR](https://github.com/SFRL/clean_bibtex), thanks to him for the base of the code. I only made a clean up and tried to improve the "user experience".

This tool removes unused entries from a BibTeX file based on citations found in a LaTeX file. It works as follows:

1. **Extract Citations**: The script extracts all citation keys from the LaTeX file by matching the contents of the LaTeX commands `\cite{}` and `\citeA{}`.

2. **Process Bib File**: It reads the BibTeX file line by line, identifying entries that start with `@` (e.g., `@article`).

3. **Check Citations**: For each entry, it checks if the citation key appears in the list of extracted citations.

4. **Clean Bib File**: If a citation key is not found in the LaTeX file, the script discards all lines associated with that entry until it encounters the next entry starting with `@`.

## Usage

To clean your BibTeX file, follow these steps:

1. **Prepare Your Files**: Ensure you have the paths to your BibTeX file (e.g., `/path/to/your/references.bib`) and your LaTeX file (e.g., `/path/to/your/main.tex`).

2. **Run the Script**: Open your command line, navigate to the directory containing the Python script, and execute the following command:

   ```sh
   python clean_bibtex.py -b /path/to/your/references.bib -t /path/to/your/main.tex -o /path/to/output/cleaned_references.bib
   ```

   In this example:
   - `-b /path/to/your/references.bib` specifies the full path to the input BibTeX file.
   - `-t /path/to/your/main.tex` specifies the full path to the input LaTeX file.
   - `-o /path/to/output/cleaned_references.bib` specifies the full path for the output cleaned BibTeX file.

This command will generate a new BibTeX file containing only the references cited in your LaTeX document, allowing you to keep your files organized in different directories.

## Requirements

- Python 3.x
- `argparse` (included in Python standard library)

## Testing

To ensure the script works correctly, you can run the included tests using `pytest`. Make sure you have `pytest` installed:

```sh
pip install pytest
pytest test_clean.py
```

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
