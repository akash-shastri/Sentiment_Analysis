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

You will also need jupyter notebook to run the notebooks. I use anaconda for this, you can use any number of options available (eg: Colab)

## To use my weights.
You can find my weights on this google drive: https://drive.google.com/drive/folders/1D1_h639KyOTlplyPzXPQCfarwmsQeo6V?usp=sharing

Download and copy these weights into the same folder as your notebooks.

#### Note: Without weights, this model is useless. To get accurate results, use my weights or train your own.

# Working
First paste the review to the review.txt file or add the path to your text file containing review in the below line.

```
rev = open('./review.txt').read()
```

To create a new review, prompt is the start of your new review and N_WORDS is the number of words in the review. You can change these parameters as needed.

