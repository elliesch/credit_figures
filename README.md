# credit_figures
Add an author credit (or any desired text) to an existing figure or plot image using Python. Built by [Ellie Schwab](https://twitter.com/SeeTheStarsRise). Licensed under the MIT license (see LICENSE).


##Installation
Run ```pip install credit_figure``` to get the latest version.


##Usage
There is only one function credit_figure. You use it like this:
```
import credit_figure as cf

cf.credit_figure( author_name, text_color, px_from_left, px_from_top, image_to_open, save_image_as)
```
You just enter the arguments in this fashion:
```
( "Author, Year", (0,0,0), ##, ##, "image.png", "savedimage.png" )
```


##Documentation
Currently credit_figure only works with .png, .jpg and .gif files, but an update is in the works to include more files.


Text_color takes arguments as RGB number values. Just type in (0,0,0) for black and (255, 255, 255) for white, or the numbers
for any other color you choose. Here is a [useful color picker](http://www.colorpicker.com).


I have used Avenir font, but it is not a default Windows or Linux font. Here's how the code does this by default:
```
font = ImageFont.truetype("/System/Library/Fonts/Avenir.ttc", 18, index=4)

#font = ImageFont.truetype("/System/Library/Fonts/Helvetica.dfont",18, index=1)
```
If you are running this script on Windows or Linux, you can fix this by commenting out the first font line, and uncommenting
the second, like this:
```
#font = ImageFont.truetype("/System/Library/Fonts/Avenir.ttc", 18, index=4)

font = ImageFont.truetype("/System/Library/Fonts/Helvetica.dfont",18, index=1)
```


##Attribution
Feel free to use this code to credit figures, plots, images. It would be great if you could send me a note that you're using it.
If you are using the code as part of another code, please cite it.


##License
Copyright 2016, Ellie Schwab.
