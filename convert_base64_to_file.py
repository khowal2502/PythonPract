import base64

data = ""

file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
path = "file.pdf"

with open(path, 'w') as f:
    f.write(file_data)
