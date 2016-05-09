from PIL import Image

# resize the file to be at most 400 x 400
def resize(file):
	img = Image.open(file);
	max_size = (400, 400);
	img.thumbnail(max_size, Image.ANTIALIAS); 
	img.save(file);

# crop image to be around the torso area
def crop_image(file):
	img = Image.open(file);
	halfWidth = img.size[0]/2
	halfHeight = img.size[1] / 2
	img2 = img.crop((halfWidth - 30, halfHeight, halfWidth + 30, halfHeight+95))
	img2.save("img.jpg");

# find the main color of the file
def main_color(file):
	img = Image.open(file);
	print img.size;
	colors = img.getcolors(10000);
	max_occurence, most_present = 0, 0
	try:
		for c in colors:
			if c[0] > max_occurence:
				(max_occurence, most_present) = c
		return most_present
	except TypeError:
		raise Exception("Too many colors in the image");


# determine the color from the rgb
def determine_color(file):
	colors = main_color(file);
	r = colors[0]
	g = colors[1]
	b = colors[2]
	print (r);
	print (g);
	print (b);
	error_allowance = 45;
	error_allowance2 = 50;
	if(255-error_allowance <= r <= 255 or (0 <= g <= error_allowance2 and 0 <= b <= error_allowance2)):
		print "red"
	elif(255-error_allowance <= g <= 255 or (0 <= r <= error_allowance2 and 0 <= b <= error_allowance2)):
		print "green"
	elif(255-error_allowance <= b <= 255 or(0 <= r <= error_allowance2 and 0 <= g <= error_allowance2 )):
		print "blue";
	else:
		print "grey";

wholeFileName = "dress2.jpg";
resize(wholeFileName);
crop_image(wholeFileName);
determine_color("img.jpg");
