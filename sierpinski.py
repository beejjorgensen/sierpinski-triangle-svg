#!/usr/bin/env python

import sys, math

def svg_begin(width, height):
    width = math.ceil(width)
    height = math.ceil(height)
    print(f'<svg version="1.1" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')

def svg_group_begin():
    print('<g>')

def svg_group_end():
    print('</g>')

def svg_end():
    print('</svg>')

def svg_polygon(points, attrs):
    attrs = 'fill="black"' if attrs is None else attrs
    pstr = " ".join([f'{x},{y}' for x,y in points])
    print(f'<polygon points="{pstr}" {attrs}/>')

def bisect(p0, p1):
    """Bisect a line between two points"""
    x0, y0 = p0
    x1, y1 = p1

    return (x0+x1) / 2, (y0+y1) / 2

def sierpinski(depth, width, height, attrs):

    def triangle(points):
        """Scale the unit triangle and make SVG polys"""
        nonlocal width, height
        
        scaled_points = []

        for p in points:
            x, y = p
            x *= width
            y *= width
            y += height
            scaled_points.append((x,y))

        svg_polygon(scaled_points, attrs)

    def sr(p0, p1, p2, depth):
        """Recursive triangle generator"""
        if depth == 0:
            triangle((p0, p1, p2))
            return

        b01 = bisect(p0, p1)
        b12 = bisect(p1, p2)
        b20 = bisect(p2, p0)
        
        sr(b20, p0, b01, depth-1)
        sr(b01, p1, b12, depth-1)
        sr(b12, p2, b20, depth-1)

    # initial unit triangle
    p0 = (0,0)
    p1 = (1,0)
    p2 = (0.5,-math.sqrt(0.75))

    svg_group_begin()
    sr(p0, p1, p2, depth)
    svg_group_end()

def parse_cl(argv):
    width = depth = attrs = error = None

    try:
        while len(argv) > 0:
            a = argv.pop(0)

            if width is None:
                width = int(a)

            elif depth is None:
                depth = int(a)

            elif attrs is None:
                attrs = a

            else:
                error = ""

    except ValueError:
        error = "invalid numeric value"

    if width is None or depth is None or len(argv) > 0:
        error = ""

    return width, depth, attrs, error

def main(argv):
    scriptname = argv.pop(0)

    width, depth, attrs, error = parse_cl(argv)

    if error is not None:
        if error == "":
            print(f'usage: {scriptname} width depth [attrs]', file=sys.stderr)
        else:
            print(f'{scriptname}: {error}', file=sys.stderr)
        sys.exit(1)

    height = math.sqrt(0.75) * width  # unit height, *width to scale it up

    svg_begin(width, height)
    sierpinski(depth, width, height, attrs)
    svg_end()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
