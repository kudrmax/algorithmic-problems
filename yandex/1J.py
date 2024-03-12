with open('input.txt', 'r') as file:
    lines = file.readlines()

W, H, C = map(int, lines[0].split())
lines = lines[1:]

doc = []

for line in lines:
    # last = 0
    if line == '\n':
        doc.append({'type': 'n'})
    else:
        while line != '\n':
            first = line[:].find('(')
            last = line[first:].find(')')

            words = line[0:first].split(' ')
            for word in words:
                if word != '':
                    word_d = {
                        'type': 'w',
                        'data': word
                    }
                    doc.append(word_d)

            params = line[first:first + last].split(' ')
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
                p['type'] = 'i'
                doc.append(p)
            line = line[first + last + 1:]
        doc.append({
            'type': 'new_line'
        })
print(doc)

this_x, this_y = 0, 0 # коретка

res = []

for obj in doc:
    if obj['type'] == 'w':
        size = C * len(obj['data'])
        was_inserted = False
        while not was_inserted:

            this_size = 0
            if this_x == 0:
                this_size = size
            else:
                this_size += C

            if this_x + this_size <= W:
                this_x += this_size
                was_inserted = True
            else:
                this_x = 0
                this_y += H
    if obj['type'] == 'i':
        if obj['layout'] == 'embedded':
            size = obj['width']
            was_inserted = False
            while not was_inserted:

                this_size = 0
                if this_x == 0:
                    this_size = size
                else:
                    this_size += C

                if this_x + this_size <= W:
                    this_x += this_size
                    was_inserted = True
                else:
                    this_x = 0
                    this_y += max(obj['height'], H)
            res.append([this_x, this_y])

print(res)

