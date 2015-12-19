
import operator

class Ingredient:
	def __init__(self, name, properties):
		self.name = name
		self.properties = properties

def load_ingredients():
	ingr = []
	for l in open('day15.input','r').readlines():
		parts = l.strip().split(":")
		name = parts[0]
		properties = dict()
		for prop in parts[1].split(", "):
			prop = prop.strip().split(" ")
			propname, propval = prop[0].strip(), int(prop[1])
			properties[propname] = propval

		ingr.append(Ingredient(name, properties))
	return ingr

def generate_amounts(n, total=100):
	if n == 0:
		yield []
	elif n == 1:
		yield [total]
	else:
		for v in range(total):
			for am in generate_amounts(n-1, total - v):
				yield [v] + am

propnames = ['capacity', 'durability', 'flavor','texture']
def amounts_to_propscores_and_calories(am, ingredients):
	score = [sum([a*i.properties[p] for a,i in zip(am, ingredients) ]) for p in propnames ]
	calories = sum([a*i.properties['calories'] for a,i in zip(am, ingredients)])
	return (score, calories)

ingredients = load_ingredients()

propscores_with_calories = map(lambda am: amounts_to_propscores_and_calories(am, ingredients), generate_amounts(len(ingredients)))

propscores = map(lambda pair: pair[0], filter(lambda pair: pair[1] == 500, propscores_with_calories))

all_positive_propscores = filter(lambda p: min(p) > 0, propscores)

scores = [ reduce(operator.mul, s, 1) for s in all_positive_propscores ]
print max(scores)


