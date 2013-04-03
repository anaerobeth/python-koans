#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1, 1, 1, 5, 1]) => 1150 points
# score([2, 3, 4, 6, 2]) => 0 points
# score([3, 4, 5, 3, 3]) => 350 points
# score([1, 5, 1, 2, 4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):
    # You need to write this method    
    count1 = dice.count(1)
    count2 = dice.count(2)
    count3 = dice.count(3)
    count4 = dice.count(4)
    count5 = dice.count(5)
    count6 = dice.count(6)
    #print count1
    #print count5
    bonus1 = (count1/3 *1000) + (count1%3 * 100)
    #print bonus1
    bonus2 = (count2/3 *200)
    #print bonus2
    bonus3 = (count3/3 *300)
    #print bonus3
    bonus4 = (count4/3 *400)
    #print bonus4
    bonus5 = (count5/3 *500) + (count5%3 * 50)
    #print bonus5
    bonus6 = (count6/3 *600)
    #print bonus6
    score = bonus1 + bonus2 + bonus3 + bonus4 + bonus5 + bonus6
    #print score
    return score
"""    self.s = 0
    self.s = self.b1 + self.b + self.s1 + self.s5
    return self.s
  
def bonus1(dice):
    self.b1 = (dice.count(1) / 3) * 1000
    return self.b1
def bonusOther(dice):
    self.b = (dice.count(2) / 3) * 2
    return self.b
def score1(dice):
    self.s1 = dice.count(1) % 3  * 100
    return self.s1
def score5(dice):
    self.s5 = dice.count(5)%3 * 100
    return self.s5 """
class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))
    
    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))
    
    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))
    
    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1, 5, 5, 1]))
    
    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2, 3, 4, 6]))
    
    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1, 1, 1]))
    
    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2, 2, 2]))
        self.assertEqual(300, score([3, 3, 3]))
        self.assertEqual(400, score([4, 4, 4]))
        self.assertEqual(500, score([5, 5, 5]))
        self.assertEqual(600, score([6, 6, 6]))
    
    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2, 5, 2, 2, 3]))
        self.assertEqual(550, score([5, 5, 5, 5]))
        self.assertEqual(1150, score([1, 1, 1, 5, 1]))
        
    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1, 2, 2, 2]))
        self.assertEqual(350, score([1, 5, 2, 2, 2]))
