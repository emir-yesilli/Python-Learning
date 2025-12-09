from rembg import remove
from PIL import Image
import easygui as eg
input_path = eg.fileopenbox(title='Metallica.jpeg')
output_path = eg.filesavebox(title= "")
output = remove(Image.open(input_path))
output.save(output_path)

print("completed")