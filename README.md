# Sentiment_Analysis
This is my sentiment analysis model trained on IMDB reviews.

# Installations
You will need to install fastai. 
You can find it installation instructions here: https://docs.fast.ai/ 

Note: The conda install on the link doesn't work perfectly (at least for me), what worked for me was to clone github repo and pip install.

```
git clone https://github.com/fastai/fastai
pip install -e "fastai[dev]"
```

# Working
First paste the review to the review.txt file or add the path to your text file containing review in the below line.

```
rev = open('./review.txt').read()
```

To create a new review, prompt is the start of your new review and N_WORDS is the number of words in the review. You can change these parameters as needed.

