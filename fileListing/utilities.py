import os

def cleanListings():
    base_string = os.path.join(os.getcwd(),'Listings')
    walk_results = os.walk(os.path.join(base_string))
    listing_list = walk_results.next()[-1]
    for f in listing_list:
        os.remove(os.path.join(base_string,f))
    print("Listings Cleaned")
    
def cleanTemps():
    base_string = os.path.join(os.getcwd(),'Temp')
    walk_results = os.walk(os.path.join(base_string))
    listing_list = walk_results.next()[-1]
    for f in listing_list:
        os.remove(os.path.join(base_string,f))
    print("Temps Cleaned")
    