
import math

# each round, scores go down by a fixed amount
# let ph = player hit points, bh = boss hit points
# let pd = damage delivered by player, bd = damage delivered by boss.
# The boss goes down in math.ceil(bh/pd) hits,
# We go down in math.ceil(ph/bd) hits.

# known variables:
# ph = 100
# bd (from input) = Hit Points: 104

# bd depends on boss damage(known) and our armor
# pd depends on our damage and boss armor(known)

# We need to find the lowest way to buy 1 weapon, 0-1 armor and 0-2 rings

class Fighter:
	def __init__(self, hitpoints, damage, armor):
		self.hitpoints = hitpoints
		self.damage = damage
		self.armor = armor

	def __repr__(self):
		return "hitpoints %d, damage %d, armor %d"%(self.hitpoints,self.damage,self.armor)
	def hit_points_to(self, other):
		return max(1, self.damage - other.armor)

	def defeats(self, other):
		""" Returns true if self defeats other (when self starts the fight) """
		our_hit_damage = self.hit_points_to(other)
		other_hit_damage = other.hit_points_to(self)

		hits_needed1 = (other.hitpoints+our_hit_damage-1) / our_hit_damage
		hits_needed2 = (self.hitpoints+other_hit_damage-1) / other_hit_damage

		return hits_needed1 <= hits_needed2


class Asset:
	def __init__(self, cost, damage, armor):
		self.cost = cost
		self.damage = damage
		self.armor = armor

	def __repr__(self):
		return "cost %d, damage %d, armor %d"%(self.cost,self.damage,self.armor)

weapons = [
	Asset(8,4,0),
	Asset(10,5,0),
	Asset(25,6,0),
	Asset(40,7,0),
	Asset(74,8,0)
]

armors = [
	Asset(13,0,1),
	Asset(31,0,2),
	Asset(53,0,3),
	Asset(75,0,4),
	Asset(102,0,5)
]

rings = [
	Asset(25,1,0),
	Asset(50,2,0),
	Asset(100,3,0),
	Asset(20,0,1),
	Asset(40,0,2),
	Asset(80,0,3)
]

def generate_asset_combos(weapons, armors, rings):
	for w in range(len(weapons)):	
		weapon = weapons[w]

		yield (weapon,)
		for a in range(len(armors)):
			armor = armors[a]

			yield (weapon, armor)

			for r1 in range(len(rings)):
				ring1 = rings[r1]
				
				yield (weapon, ring1)
				yield (weapon, armor, ring1)

				for r2 in range(len(rings)):
					if r1 == r2: continue
					ring2 = rings[r2]

					yield (weapon, ring1, ring2)
					yield (weapon, armor, ring1, ring2)

def generate_winning_combos():
	boss = Fighter(104, 8, 1)
	for combo in generate_asset_combos(weapons, armors, rings):
		cost = sum([ asset.cost for asset in combo ])
		damage = sum([ asset.damage for asset in combo ])
		armor = sum([ asset.armor for asset in combo ])

		print (cost, damage, armor)
		player = Fighter(100, damage, armor)

		if player.defeats(boss):
			yield combo,player,boss

# test with sample
#print Fighter(8, 5, 5).defeats(Fighter(12,7,2))

best = 100000
best_combo = None
for c,p,b in generate_winning_combos():
	cost = sum([a.cost for a in c])
	if cost < best:
		best_combo = (c,p,b)
		best = cost

print "Winning params:", best_combo
print "Cost:", best

#print Fighter(100,6,3).defeats(Fighter(104,8,1))
