from rembg import remove
input_path = "Materials/Metallica.jpeg"
output_path = "Materials/output.png"

with open(input_path, "rb") as input_file:
    with open(output_path,"wb") as output_file:
        inputF = input_file.read()
        output = remove(inputF)
        output_file.write(output)
