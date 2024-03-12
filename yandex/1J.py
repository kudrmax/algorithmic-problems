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
h = 0
insert_arr = [[0, 1000000000], [W, 1000000000]]
res = []

def find_place(this_x, this_y, size, h):
    was_inserted = False
    i_min = 0
    while not was_inserted:
        x_min, x_max = insert_arr[i_min][0], insert_arr[i_min + 1][0]

        this_size = size
        if this_x != 0:
            this_size += C

        x_first = this_x
        x_second = this_x + this_size
        if x_first >= x_min and x_second <= x_max:
            this_x += this_size
            was_inserted = True
        else:
            if i_min + 1 != len(insert_arr) - 1:
                i_min += 2
            else:

                this_x = 0
                this_y += max(H, h)
                if h != 0:
                    h = 0

                list_to_remove = []
                for l in range(len(insert_arr)):
                    hh = insert_arr[l][1]
                    if hh < this_y:
                        list_to_remove.append(insert_arr[l])

                while len(list_to_remove) > 0:
                    el = list_to_remove.pop()
                    insert_arr.remove(el)

                insert_arr.sort(key=lambda x: x[0])
                i_min = 0

        return this_x, this_y, h

for obj in doc:

    if obj['type'] == 'w':
        size = C * len(obj['data'])
        this_x, this_y, h = find_place(this_x, this_y, size, h)


    if obj['type'] == 'i':
        if obj['layout'] == 'embedded':
            size = obj['width']
            this_x, this_y, h = find_place(this_x, this_y, size, h)
            h = obj['height']
            res.append([this_x - size, this_y])

        if obj['layout'] == 'surrounded':
            this_size = obj['width']
            this_x, this_y, h = find_place(this_x, this_y, size, h)

            insert_arr.append([this_x - this_size, this_y + obj['height']])
            insert_arr.append([this_x, this_y + obj['height']])
            insert_arr.sort(key=lambda x: x[0])
            res.append([this_x, this_y])
        if obj['layout'] == 'floating':
            dx = obj['dx']
            dy = obj['dy']
            width = obj['width']
            height = obj['height']

            coord_x_right = this_x + dx + width
            coord_x_left = this_x + dx
            if coord_x_right > W:
                coord_x_right = W
                res.append([coord_x_right - width, this_y + dy])
            elif coord_x_left < 0:
                coord_x_right = 0
                res.append([0, this_y + dy])
            res.append([coord_x_left, this_y + dy])

    if obj['type'] == 'new_line':
        this_y += C

print(res)

