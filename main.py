#!/usr/bin/env python
# coding: utf-8

# In[39]:


from fastai.text.all import *
from tkinter import *


# In[8]:


path = untar_data(URLs.IMDB)


# In[27]:


path = Path('.')
learn_clas = load_learner(path/'exported_clas.pkl')
learn_lang = load_learner(path/'exported_finetuned.pkl')


# In[94]:


top = Tk()
top.title("Main")
top.geometry("250x100")

def onClassify():
    root = Tk()
    root.title("Classify Reviews")
    top.geometry("250x100")

    label1 = Label( root, text="Review file Path" )
    label1.pack()
    rev=Text(root, height=2, width=50)
    rev.pack(padx = 10, pady = 10)
    rev.insert(INSERT,"./review.txt")
    
    def onClick_classify():
        rev_i=rev.get("1.0","end-1c")
        rev_text = open(rev_i).read()
        sentiment = str(learn_clas.predict(rev_text)[0])
        label2 = Text(root, height=2, width=30)
        label2.pack()
        label2.insert(INSERT, sentiment)
        
        
    
    b_c = Button(root, text ="Classify", command = onClick_classify)
    b_c.pack(padx = 10, pady = 10)
    
    root.mainloop()


def onCreate_rev():
    root = Tk()
    root.title("Create Reviews")
    top.geometry("250x100")
    label = Text(root, height=1, width=50, bg="black", fg="white")
    label.pack(padx = 10, pady = 10)
    label.insert(INSERT, "This is a little slow. Bear with us.") 
    label.config(state=DISABLED)
    
    label1 = Label( root, text="Start Prompt" )
    label1.pack()
    rev=Text(root, height=2, width=50)
    rev.pack(padx = 10, pady = 10)
    rev.insert(INSERT,"I love this movie ")
    
    label2 = Label( root, text="number of words" )
    label2.pack()
    n_words=Text(root, height=2, width=50)
    n_words.pack(padx = 10, pady = 10)
    n_words.insert(INSERT,"80")
    
    def onClick_create():
        prompt=rev.get("1.0","end-1c")
        num_words = n_words.get("1.0","end-1c")
        review = str(learn_lang.predict(prompt, n_words = int(num_words), temperature = 0.75))
        label2 = Text(root, height=25, width=100)
        label2.pack()
        label2.insert(INSERT, review)
        
        
    
    b_c = Button(root, text ="Classify", command = onClick_create)
    b_c.pack(padx = 10, pady = 10)
    
    root.mainloop()
    
    
b1 = Button( text ="Classify Review", command = onClassify)
b1.grid(row = 0, column = 0, padx = 10, pady = 10)
b2 = Button(text ="Create Review", command = onCreate_rev)
b2.grid(row = 0, column = 2,padx = 10, pady = 10)

top.mainloop()

