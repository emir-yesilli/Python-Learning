import pyqrcode
url = input("Enter URL: ")
url = pyqrcode.create(url)
url.svg('Materials/uca-url.svg', scale=2)
url.eps('Materials/uca-url.eps', scale=2)

print(url.terminal(quiet_zone=1))

