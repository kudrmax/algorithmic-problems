with open('input.txt', 'r') as file:
    lines = file.readlines()

w, h, c = map(int, lines[0].split())
lines = lines[1:]

doc = []

for line in lines:
    # last = 0
    while line != '\n':
        first = line[:].find('(')
        last = line[first:].find(')')

        words = line[0:first].split(' ')
        for word in words:
            if word != '':
                doc.append(word)

        params = line[first:first+last].split(' ')
        p = {}
        for param in params:
            if param.startswith("layout"):
                p['layout'] = param.split('=')[1]
            if param.startswith("width"):
                p['width'] = int(param.split('=')[1].rstrip('\n').rstrip(')'))
            if param.startswith("height"):
                p['height'] = int(param.split('=')[1].rstrip('\n').rstrip(')'))
            if param.startswith("dx"):
                p['dx'] = int(param.split('=')[1].rstrip('\n').rstrip(')'))
            if param.startswith("dy"):
                p['dy'] = int(param.split('=')[1].rstrip('\n').rstrip(')'))
        if p != {}:
            doc.append(p)
        line = line[first + last + 1:]

print(doc)
