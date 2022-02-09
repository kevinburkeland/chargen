#!/usr/bin/python
#rev 0.1
#Last modified 2/8/2022
#writen by Kevin Burkeland
#imports random
import random

class Dice:
	# empty constructor
	def __init__(self):
		pass

	def roll(self, max_roll, num_dice):
		rolls = []
		for _ in range(num_dice):
			roll = random.randint(1, max_roll)
			rolls.append(roll)
		return rolls

	def roll_d4(self, num_dice):
		return self.roll(4, num_dice)

	def roll_d6(self, num_dice):
		return self.roll(6, num_dice)

	def roll_d8(self, num_dice):
		return self.roll(8, num_dice)

	def roll_d10(self, num_dice):
		return self.roll(10, num_dice)

	def roll_d12(self, num_dice):
		return self.roll(12, num_dice)

	def roll_d20(self, num_dice):
		return self.roll(20, num_dice)
