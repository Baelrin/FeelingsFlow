# FeelingsFlow

FeelingsFlow is a sentiment analysis tool that leverages the TextBlob library to perform semantic analysis and determine the sentiment of a given text.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use FeelingsFlow, execute the `master.py` script with command-line arguments or enter text interactively:

```bash
python master.py --text "Your text here" --threshold  0.3
```

Or in interactive mode:

```bash
python master.py
```

After entering the text, you will receive an emoji representing the sentiment of the text.

## Testing

To run tests, use the following command:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
