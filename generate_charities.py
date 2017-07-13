from webapp.models import Charity

names = ["kids for kangaroos", "Fidget spinners for humanity", "Blue cross", "Red aid", "Mothers against Mcdonalds"]
descriptions = ["cats and gods", "dogs and pickles", "bicycles", "random seed generator", "DJANGO"]

for i in xrange(len(names)):
    charityEntry = Charity(name=names[i], description=descriptions[i])
    charityEntry.save()
