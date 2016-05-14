import Image
import random

class ad(object):
	def __init__(self, gender, item, pattern, color, link):
		self.gender = gender
		self.item = item
		self.pattern = pattern
		self.color = color
		self.link = link

	def open_image(self):
		print "OPEN IMAGE FUNCTION "
		image = Image.open(self.link)
		image.show()

	def get_item(self):
		return self.item

	def get_color(self):
		return self.color

	def get_gender(self):
		return self.gender
		
	def get_link(self):
		return self.link

#library of images
def create_ads_list():
	ads_list = []
	ads_list.append(ad("female", "dress", "solid", "red", "Awesome-Red-Dress.jpg"))
	ads_list.append(ad("female", "shirt", "polkadots", "black", "black_polka_dot_womens_shirt.jpg"))
	ads_list.append(ad("female", "dress", "solid", "blue", "blue_dress.jpg"))
	ads_list.append(ad("female", "pants", "solid", "blue", "blue_pants_womens.jpg"))
	ads_list.append(ad("female", "shirt", "solid", "green", "green_shirt_womens.jpg"))
	ads_list.append(ad("female", "pants", "solid", "yellow", "How-to-Wear-Bright-Yellow-Pants-Stylishlyme.jpg"))
	ads_list.append(ad("male", "pants", "solid", "black", "mens_black_pants.jpg"))
	ads_list.append(ad("male", "pants", "solid", "black", "mens_black_pants_blue_shirt.jpg"))
	ads_list.append(ad("male", "shirt", "solid", "blue", "mens_black_pants_blue_shirt.jpg"))
	ads_list.append(ad("male", "shorts", "solid", "black", "mens_black_shorts_grey_shirt.jpg"))
	ads_list.append(ad("male", "shirt", "solid", "grey", "mens_black_shorts_grey_shirt.jpg"))
	ads_list.append(ad("male", "shorts", "solid", "white", "mens_blue_shirt.jpg"))
	ads_list.append(ad("male", "shirt", "solid", "blue", "mens_blue_shirt.jpg"))
	ads_list.append(ad("male", "pants", "solid", "red", "mens_red_pants.jpg"))
	ads_list.append(ad("male", "shirt", "solid", "red", "mens_red_shirt.jpg"))
	ads_list.append(ad("male", "pants", "solid", "red", "mens_red_pants.jpg"))
	ads_list.append(ad("male", "shorts", "solid", "red", "mens_red_shorts.jpg"))
	ads_list.append(ad("male", "shorts", "solid", "red", "mens_red_shorts2.jpg"))
	ads_list.append(ad("male", "shirt", "stripes", "blue", "mens-shirts-sky-blue-stripes-striped-short.jpg"))
	ads_list.append(ad("male", "shirt", "solid", "pink", "pink_jacket.jpg"))
	ads_list.append(ad("male", "shirt", "stripes", "pink", "pink_stripe_mens.jpeg"))
	ads_list.append(ad("female", "dress", "solid", "red", "red-dress-11.jpg"))
	ads_list.append(ad("female", "pants", "solid", "red", "redpants.jpg"))
	ads_list.append(ad("male", "pants", "solid", "red", "red-pants-mens.jpg"))
	ads_list.append(ad("male", "shirt", "solid", "blue", "red-pants-mens.jpg"))
	ads_list.append(ad("female", "shirt", "polkadots", "red", "red_polka_dot_womens_shirt.jpg"))
	ads_list.append(ad("female", "shorts", "solid", "red", "red-shorts-urban-style01.jpg"))
	ads_list.append(ad("female", "shorts", "solid", "white", "white_shorts_white_shirt_womens.jpg"))
	ads_list.append(ad("female", "shirt", "solid", "white", "white_shorts_white_shirt_womens.jpg"))
	ads_list.append(ad("female", "pants", "solid", "white", "womens_white_pants.jpg"))
	ads_list.append(ad("female", "shorts", "solid", "white", "womens_white_shorts_red_shirt.jpg"))
	ads_list.append(ad("female", "shirt", "solid", "red", "womens_white_shorts_red_shirt.jpg"))
	ads_list.append(ad("male", "shorts", "solid", "yellow", "mens_yellow_shorts.jpg"))
	ads_list.append(ad("female", "dress", "solid", "yellow", "yellow_dress.jpg"))
	ads_list.append(ad("female", "dress", "polkadots", "yellow", "yellow_polka_dot_womens_shirt.jpg"))
	ads_list.append(ad("male", "shirt", "solid", "brown", "brown_shirt_mens.jpg"))


	return ads_list


def searched_failed():
	print "Sorry, there is no suggested ad available"
	exit()

def search_attribute(attribute, ads_list):
	x = 0
	listcopy = list(ads_list)
	for i in listcopy:
		print attribute, i.get_attribute(attribute)
		if attribute != i.get_attribute(attribute):
			ads_list.remove(i)
			x +=1

def search_color(ads_list, color):
	listcopy = list(ads_list)
	for i in listcopy:
		if (color != i.get_color()):
			ads_list.remove(i)

def search_gender(ads_list, gender):
	listcopy = list(ads_list)
	for i in listcopy:
		if (gender != i.get_gender()):
			print gender, i.get_gender()
			ads_list.remove(i)

def search_item(ads_list, item):
	listcopy = list(ads_list)
	for i in listcopy:
		if (item != i.get_item()):
			print item, i.get_item()
			ads_list.remove(i)

def search_pattern(ads_list, pattern):
	listcopy = list(ads_list)
	for i in listcopy:
		if (pattern != i.get_pattern()):
			ads_list.remove(i)

def find_ad(gender, item, pattern, color, all_ads):
	ads_list = all_ads
	print "ads list size ", len(ads_list)
	#keep temp list so that if one step leads to the list being empty, we can 
	#use temp list to go back a step
	temp_list = ads_list
	#find clothing for specified gender
	if (gender != '0'):
		search_gender(ads_list, gender)

	#make sure there are still options
	if (len(ads_list) == 0):
		searched_failed()
	temp_list = ads_list

	#find similar clothing items
	if (item != '0'):
		search_item(ads_list, item)
	print "ads list size ", len(ads_list)

	#make sure there are still options
	if not ads_list:
		searched_failed()
	temp_list = ads_list

	#find similar clothing items
	if (pattern != '0'):
		search_pattern(ads_list, pattern)

	print "ads list size ", len(ads_list)

	#make sure there are still options
	if not ads_list:
		searched_failed()
	temp_list = ads_list

		#find similar clothing items
	if (color != '0'):
		search_color(ads_list, color)

	#make sure there are still options
	if not ads_list:
		searched_failed()
	temp_list = ads_list

	return ads_list


#choose a random image from the list
def return_image(ads_list):
	list_size = len(ads_list) - 1
	if (list_size == -1):
		print "Sorry, no matches were found"
	else:
		num = random.randint(0, list_size)
		ads_list[num].open_image()




if __name__ == '__main__':

	all_ads = create_ads_list()
	c = raw_input("Color: ")
	g = raw_input("Gender: ")
	ads_list = 	find_ad(g.lower(), '0', '0', c.lower(), all_ads)
	return_image(ads_list)
