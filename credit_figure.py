import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def credit_figure ( member_name, text_color, px_from_left, px_from_top, image_to_open, save_image_as) :
    ''' 
    Labels plots and figures with creator's name. All plots and figures should be in
    .png, .gif, or .jpg format.
    
    For tcolor enter (0,0,0) for black and (255,255,255) for white. For other colors
    use RGB format.
    
    Enter args in this fashion: 
    credit_figure ( "Member Name, Year", (0,0,0), ##, ##, "image.png", "savedimage.png" )
    '''
    
    #Avenir is a more easily-readable font, but it might not work on everyone's systems. 
    #If so, comment out and use Helvetica code line below.
    font = ImageFont.truetype("/System/Library/Fonts/Avenir.ttc", 18, index=4)
    
    #font = ImageFont.truetype("/System/Library/Fonts/Helvetica.dfont",18, index=1)
    
    #Write BDNYC member name
    text = member_name
        
    #positions the text. 
    # First number indicates position from left edge, and second number indicates position from right edge in pixels.
    text_pos = (px_from_left, px_from_top)
    
    #opens images in .png, .jpg or .gif format
    img = Image.open(image_to_open)
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    draw.text(text_pos, text, fill=text_color, font=font)
    del draw
    
    #saves the figure
    img.save(save_image_as)