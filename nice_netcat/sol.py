
with open('output.txt', 'r') as f:
	text = f.readlines()

out_text = ''
for i in text:
	one, two = i.split(' ')
	out_text += chr(int(one))

print(out_text)
