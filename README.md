# Sierpiński triangle SVG generator

Simple command line tool to generate [Sierpiński
triangles](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) in
SVG.

## Usage

You give a base width in pixels (the height is computed to make an
equilateral triangle), and the number of times to recurse (`0` for a
single triangle, `1` for a triangle with a triangle cut out, etc.)

Output is to standard output.

```
./sierpinski.py basewidth recursiondepth [svgattrs]
```

The third argument is passed as-is to the SVG polygon, and you can use
it to control styling.

```
./sierpinski.py 100 2 'fill="red"' > striangle.svg
./sierpinski.py 1000 8 'fill="none" stroke="black"' > striangle.svg
```

## Complexity

`O(4ⁿ)` (over depth) in space, time, and resultant SVG size. Don't mess
around with large depth values. 😅

