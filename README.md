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
![Sentiment analysis home](https://github.com/akash-shastri/Images/blob/main/Sentiment%20analysis%20home.PNG)
Select whichever option you want to perform

![Pre Classify](https://github.com/akash-shastri/Images/blob/main/classify.PNG)
add the path to your review text file

![Post Classify](https://github.com/akash-shastri/Images/blob/main/post%20clasify.PNG) 
This is what the result looks like. pos is positive sentiment and neg is negative sentiment

![Pre Create](https://github.com/akash-shastri/Images/blob/main/Create%20pre.PNG)
Add the starting prompt and the number of words for the review

![Post Create](https://github.com/akash-shastri/Images/blob/main/create%20post.PNG)
This is what the result looks like.



