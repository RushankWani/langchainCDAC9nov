import random

def actor_picker():
    actor_names = ["Chris Evens","Robert Downey Jr","Chris Hemsworth","Scarlet Johansson","Jeremy Renner","Stan Lee"]
    return random.choice(actor_names)

def location_picker():
    location_names = ["New York","Brazil","India","Tokyo","Los Angeles","Queens","Brooklyn"]
    return random.choice(location_names)

def theme_picker():
    theme_names = ["Science Fiction","Action","Comedy","Thriller","Horror","Romance"]
    return random.choice(theme_names)