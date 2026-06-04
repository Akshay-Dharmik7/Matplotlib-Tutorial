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

#

## Types of Data in Matplotlib and Seaborn

- Before creating visualizations in Matplotlib or Seaborn, it is important to understand the type of data you are working with.
- The choice of plot depends on whether your data is Numerical or Categorical.

```
Data
│
├── Numerical Data
│
└── Categorical Data
    │
    ├── Ordinal Data
    │
    └── Nominal (Non-Ordinal) Data
```

### 1. Numerical Data:

- Numerical data consists of values that can be measured, counted, or used in mathematical calculations.

#### Characteristics

- Represented by numbers.
- Arithmetic operations can be performed.
- Can be sorted naturally from smallest to largest.

### 2. Categorical Data

- Categorical data represents groups, labels, or categories rather than numeric measurements.
- Examples:
  - Gender
  - Department
  - City
  - Product Category

Categorical data is divided into two types:

```
Categorical Data
│
├── Ordinal
│
└── Nominal
```

#### A. Ordinal Data

- Ordinal data consists of categories that have a meaningful order or ranking.
- Characteristics
  - Categories can be arranged in order.
  - The difference between categories is not necessarily measurable.

- Examples
  - Education Level: `High School < Bachelor's < Master's < PhD`
  - Customer Satisfaction: `Poor < Average < Good < Excellent`
  - T-Shirt Size: `Small < Medium < Large < XL`
  - Rating System: `1 Star < 2 Star < 3 Star < 4 Star < 5 Star`

#### B. Nominal (Non-Ordinal) Data

- Nominal data consists of categories that do not have any natural order or ranking.
- Characteristics
  - Categories are simply labels.
  - One category is not greater or smaller than another.
  - Only classification is possible.

- Examples
  - Gender: `Male, Female`
  - Blood Group: `A, B, AB, O`
  - Department: `IT, HR, Finance, Marketing`
  - City: `Pune, Mumbai, Delhi, Bangalore`

### Comparison: Ordinal vs Nominal:

| Feature                            | Ordinal               | Nominal         |
| ---------------------------------- | --------------------- | --------------- |
| Categories                         | Yes                   | Yes             |
| Natural Order                      | Yes                   | No              |
| Ranking Possible                   | Yes                   | No              |
| Mathematical Difference Meaningful | No                    | No              |
| Example                            | Poor, Good, Excellent | IT, HR, Finance |

### Which Plots to Use?

| Data Type                 | Matplotlib                | Seaborn                               |
| ------------------------- | ------------------------- | ------------------------------------- |
| Numerical                 | plot(), scatter(), hist() | lineplot(), scatterplot(), histplot() |
| Ordinal                   | bar()                     | countplot(), barplot()                |
| Nominal                   | bar(), pie()              | countplot(), barplot()                |
| Numerical + Numerical     | scatter()                 | scatterplot()                         |
| Numerical + Categorical   | boxplot()                 | boxplot(), violinplot()               |
| Categorical + Categorical | bar()                     | countplot()                           |

### Quick Summary

```
Data
│
├── Numerical Data
│   ├── Discrete
│   └── Continuous
│
└── Categorical Data
    │
    ├── Ordinal
    │   ├── Low
    │   ├── Medium
    │   └── High
    │
    └── Nominal
        ├── IT
        ├── HR
        └── Finance
```

### Rule of Thumb:

- If the values are numbers and calculations make sense → **Numerical Data.**
- If the values are labels/categories → **Categorical Data.**
- If categories have a ranking → **Ordinal Data**.
- If categories are just names without ranking → **Nominal Data.**

#

## Univariate, Bivariate, and Multivariate Analysis

- In data analysis and visualization (Matplotlib/Seaborn), data can be analyzed based on the number of variables involved.

```
Data Analysis
│
├── Univariate Analysis
│   └── 1 Variable
│
├── Bivariate Analysis
│   └── 2 Variables
│
└── Multivariate Analysis
    └── More than 2 Variables
```

### 1. Univariate Analysis

- Univariate means analyzing one variable at a time.
- Purpose:
  - Understand the distribution of a single variable.
  - Find minimum, maximum, average, spread, and outliers.

#### Example Dataset:

| Age |
| --- |
| 21  |
| 25  |
| 22  |
| 28  |
| 30  |

- Only Age is being analyzed.

#### Questions Answered

- What is the average age?
- What is the highest age?
- How are ages distributed?

### 2. Bivariate Analysis

- Bivariate means analyzing two variables together.
- Purpose:
  - Identify relationships between two variables.
  - Compare one variable against another.
  - Find correlations and trends.

#### Example Dataset

| Height | Weight |
| ------ | ------ |
| 150    | 50     |
| 160    | 60     |
| 170    | 70     |
| 180    | 80     |

#### Variables:

- Height
- Weight

#### Questions Answered

- Does weight increase with height?
- Is there a positive or negative relationship?
- How strong is the correlation?

#### Types of Bivariate Analysis

- Numerical vs Numerical
- Categorical vs Numerical
- Categorical vs Categorical

### 3. Multivariate Analysis

- Multivariate means analyzing more than two variables simultaneously.
- Purpose:
  - Discover complex relationships.
  - Compare multiple factors together.
  - Perform advanced data analysis.

#### Example Dataset

| Age | Salary | Experience |
| --- | ------ | ---------- |
| 25  | 30000  | 2          |
| 30  | 50000  | 5          |
| 35  | 70000  | 8          |

#### Variables:

- Age
- Salary
- Experience

#### Questions Answered

- Does experience affect salary?
- How do age and experience together influence salary?
- Which factors are related?

#### Comparison Table

| Feature             | Univariate              | Bivariate                                | Multivariate                  |
| ------------------- | ----------------------- | ---------------------------------------- | ----------------------------- |
| Number of Variables | 1                       | 2                                        | More than 2                   |
| Purpose             | Understand one variable | Study relationship between two variables | Analyze complex relationships |
| Example             | Age                     | Height vs Weight                         | Age vs Salary vs Experience   |
| Seaborn Plots       | histplot(), boxplot()   | scatterplot(), barplot()                 | pairplot(), heatmap()         |
| Matplotlib Plots    | hist(), boxplot()       | scatter(), plot()                        | heatmap, 3D scatter           |

#### Visual Summary

```
UNIVARIATE
-----------
Age

BIVARIATE
----------
Height ──► Weight

MULTIVARIATE
-------------
Age
 │
 ├── Salary
 │
 └── Experience
```

#### Easy Way to Remember

- **Univariate** = 1 Variable → Analyze a single column.
- **Bivariate** = 2 Variables → Analyze the relationship between two columns.
- **Multivariate** = 3 or More Variables → Analyze multiple columns together.

For example, in an employee dataset:

- Age → Univariate
- Age vs Salary → Bivariate
- Age, Salary, Experience → Multivariate


## Bar Plot in Matplotlib
- A bar plot uses rectangular bars to represent data categories, with bar length or height proportional to their values.
- It compares discrete categories, with one axis for categories and the other for values.
- A Bar Plot (Bar Chart) is used to compare values across different categories using rectangular bars.
- The height (or length) of each bar represents the value of a category.
- The x-axis typically shows the categories being compared, while the y-axis shows the values associated with those categories.
- This visual format makes it easy to compare quantities across different groups.
- This function takes several parameters:
    - **x:** The categories (e.g., fruits).
    - **height:** The corresponding values (e.g., sales).
    - **width:** The width of the bars (default is 0.8).
    - **bottom:** The baseline for the bars (default is 0).
    - **align:** How to align bars ('center' or 'edge')

![alt text](image-1.png)

