def draw_triangle(height):
    for i in range(height):
        if i == 0:
            print(' ' * (height - i - 1) + '/\\')
        elif i == height - 1:
            print(' ' * (height - i - 1) + '/' + '_' * (2 * i) + '\\')  
        else:
            print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')

def draw_base(width):
    print('\\' + '_' * (width - 2) + '/')

draw_triangle(5)
