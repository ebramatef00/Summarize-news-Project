# News Summarizer Analyzer

The **News Summarizer Analyzer** is a Streamlit application that allows users to input the URL of a news article and receive a summary along with sentiment analysis. It leverages the `newspaper` library for article extraction and the `textblob` library for sentiment analysis.

## Installation

1. Make sure you have Python installed (preferably Python 3.6 or later).
2. Install the required packages using pip:

```bash
pip install streamlit newspaper3k textblob nltk
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/news-summarizer-analyzer.git
cd news-summarizer-analyzer
```

2. Run the Streamlit app:

```bash
streamlit run main.py
```


## How It Works

1. **Input URL**: Enter the URL of a news article in the provided text input.

2. **Summarize**: Click the "Summarize" button to extract the article content, display its title, authors, publication date, and a summary.

3. **Sentiment Analysis**: The app also performs sentiment analysis on the article text, providing a polarity score and sentiment label (positive, negative, or neutral).

## Customization

Feel free to customize the app by improving the UI, adding more features, or enhancing the summarization algorithm.

