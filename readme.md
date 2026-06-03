# Matplotlib

### What is Matplotlib?
- Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
- Matplotlib was created by John D. Hunter.
- Matplotlib is open source and we can use it freely.
- Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

## Matplotlib Pyplot
### Pyplot
- Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:  
`import matplotlib.pyplot as plt`

### Anatomy of Mtplotlib Plot
- A Matplotlib plot is made up of several components. Understanding these parts helps you customize and create professional visualizations.

#### Image:
![alt text](image.png)

```
Figure
│
├── Axes
│   ├── Title
│   ├── X-Axis
│   │   ├── Ticks
│   │   └── Tick Labels
│   ├── Y-Axis
│   │   ├── Ticks
│   │   └── Tick Labels
│   ├── Grid
│   ├── Legend
│   ├── Spines
│   └── Plot Data (Line, Bar, Scatter, etc.)
```

#### 1. Figure:
- The Figure is the entire window or canvas that contains all plot elements.

#### 2. Axes
- The Axes is the actual plotting area where data is displayed.

#### 3. Axis
- An Axis represents the scale of the plot.
- There are typically:
    - X-Axis (horizontal)
    - Y-Axis (vertical)

#### 4. Title
- Describes the plot. (Heading of plot/graph)

#### 5. Labels (X-Label and Y-Label)
- Used to describe the meaning of each axis.

#### 6. Ticks
- Ticks are the marks along the axes.

#### 7. Tick Labels
- Values displayed beside the ticks.

#### 8. Grid
- Reference lines that improve readability.
- Horizontal and vertical guide lines appear.

#### 9. Plot Area
- Region where data points, lines, bars, etc. are drawn.

#### 10. Legend
- Explains different plotted datasets.

#### 11. Spines
- The borders around the plot area.
- Spines:
    - Top
    - Bottom
    - Left
    - Right

#### 12. Text and Annotations
- Used to add notes on the graph.



