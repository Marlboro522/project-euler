#if the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#if all the numbers from 1 to 1000(One Thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342(Three Hundred and Forty-Two) contains 23 letters and 115(One Hundred and Fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

# Answer: 21124 how ?
# 1-9: 36
# 10-19: 70
# 20-99: 748
# 100-999: 20259
# 1000: 11
# 36 + 70 + 748 + 20259 + 11 = 21124

#let's get the numbers in range 1 to 1000 into words and then worry about lengths. 
#ah-ha found this moddule called the inflect module. Used it to get the answer and later do it myself. 
import inflect
p=inflect.engine()
total_sum=0
for i in range(1,1001):
    total_sum+=len(p.number_to_words(i).replace(" ","").replace("-",""))
print(total_sum) #27 is the length of "and" which is not counted in the inflect module.
print(p.number_to_words(342))
print(len("Threehundredandfortytwo"))
    