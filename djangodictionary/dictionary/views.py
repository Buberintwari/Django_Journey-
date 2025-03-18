# importing the render function from django.shortcuts
# the render function renders templates
from django.shortcuts import render
# importing the PyDictionary library
from nltk.corpus import wordnet as wn

# this is the view that will render the index page
def homeView(request):
    return render(request, 'dictionary/index.html')

# this is the view that will render search page
def searchView(request):
    word = request.GET.get('search', '').strip()  # Get word and remove extra spaces
    context = {'word': word}  # Initialize context

    if word:  # Only proceed if a word is provided
        meanings = {synset.pos(): synset.definition() for synset in wn.synsets(word)}
        synonyms = {lemma.name() for synset in wn.synsets(word) for lemma in synset.lemmas()}
        antonyms = {ant.name() for synset in wn.synsets(word) for lemma in synset.lemmas() for ant in lemma.antonyms()}


        context.update({
            'meanings': meanings,
            'synonyms': list(synonyms),
            'antonyms': list(antonyms)
        })

    return render(request, 'dictionary/search.html', context)
