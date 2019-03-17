---
redirect_from:
  - "/lessons/lesson11-python-for-data-science-lazy-evaluation"
interact_link: content/lessons/Lesson11_Python_For_Data_Science_Lazy_Evaluation.ipynb
kernel_name: python3
title: 'Lesson 11 - Lazy Evaluation'
prev_page:
  url: /lessons/Lesson10_Python_For_Data_Science_Functional_Programming
  title: 'Lesson 10 - Functional Programming'
next_page:
  url: /lessons/Lesson12_Python_For_Data_Science_Pattern_Matching
  title: 'Lesson 12 - Pattern Matching'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson11_Python_For_Data_Science_Lazy_Evaluation.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 11: Lazy Evaluation

## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 11.1 Use generators

### Lists and Generators



{:.input_area}
```
l_ten = [x for x in range(10)]
g_ten = (x for x in range(10))

print(f"l_ten is a {type(l_ten)} and prints as: {l_ten}")
print(f"g_ten is a {type(g_ten)} and prints as: {g_ten}")
```


{:.output .output_stream}
```
l_ten is a <class 'list'> and prints as: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
g_ten is a <class 'generator'> and prints as: <generator object <genexpr> at 0x7fec69bbfc50>

```

### Next



{:.input_area}
```
next(g_ten)
```





{:.output .output_data_text}
```
1
```



### Iteration



{:.input_area}
```
for x in g_ten:
  print(x)

```


{:.output .output_stream}
```
0
1
2
3
4
5
6
7
8
9

```

### Indexing



{:.input_area}
```

g_ten[3]
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-95-e7b8f961aa33> in <module>()
          1 
    ----> 2 g_ten[3]
    

    TypeError: 'generator' object is not subscriptable


```

### Size



{:.input_area}
```
import sys
x = 100000000
l_big = [x for x in range(x)]
g_big = (x for x in range(x))

print( f"l_big is {sys.getsizeof(l_big)} bytes")
print( f"g_big is {sys.getsizeof(g_big)} bytes")
```


{:.output .output_stream}
```
l_big is 859724472 bytes
g_big is 88 bytes

```

## 11.2 Design generator pipelines

### Stringing generators together



{:.input_area}
```
evens = (x*2 for x in range(5000000))
three_factors = (x//3 for x in evens if x%3 == 0)
titles = (f"this number is {x}" for x in three_factors)
capped = (x.title() for x in titles)

print(f"The first call to capped: {next(capped)}")
print(f"The second call to capped: {next(capped)}")
print(f"The third call to capped: {next(capped)}")
```


{:.output .output_stream}
```
The first call to capped: This Number Is 0
The second call to capped: This Number Is 2
The third call to capped: This Number Is 4

```

### Why use lazy evaluation
Processing large datasets in smaller pieces.
Example: Salt and protein of organic foods

#### Define generator to read file line by line



{:.input_area}
```
def row_reader(file_path):
  for line in open(file_path, 'r'):
    yield line
```


####



{:.input_area}
```
file_path = './features.en.openfoodfacts.org.products.csv'

rows = row_reader(file_path)
rows
```





{:.output .output_data_text}
```
<generator object row_reader at 0x7fd2e9af5f68>
```





{:.input_area}
```
next(rows)
```





{:.output .output_data_text}
```
'3,57.14,17.86,3.57,17.86,1.22428,2540,2835.7,92.86,0,Organic Salted Nut Mix\n'
```



#### Generator pipeline to process one line at a time



{:.input_area}
```
def row_reader(file_path):
  line_reader = (x for x in open(file_path, 'r'))
  
  organics_only = (x.split(',') for x in line_reader if x.split(',')[-1].startswith('Organic'))

  name_salt_protein = ((x[-1], x[-6], x[-7]) for x in organics_only)
  
  return name_salt_protein



rows = row_reader(file_path)
```




{:.input_area}
```
next(rows)
```





{:.output .output_data_text}
```
('Organic Oat Groats\n', '0.0254', '16.67')
```





{:.input_area}
```
import pandas
organics = pandas.DataFrame(columns=['Name', 'Salt', 'Protein'])

rows = row_reader(file_path)

for new_row in rows:
  organics.loc[len(organics)] = new_row
  
organics
```





<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Salt</th>
      <th>Protein</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Organic Salted Nut Mix\n</td>
      <td>1.22428</td>
      <td>17.86</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Organic Muesli\n</td>
      <td>0.1397</td>
      <td>14.06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Organic Hazelnuts\n</td>
      <td>0.01016</td>
      <td>14.29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Organic Oat Groats\n</td>
      <td>0.0254</td>
      <td>16.67</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Organic Quinoa Coconut Granola With Mango\n</td>
      <td>0.02286</td>
      <td>10.91</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Organic Unswt Berry Coconut Granola\n</td>
      <td>0.28194</td>
      <td>12.96</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Organic Red Quinoa\n</td>
      <td>0.01016</td>
      <td>13.33</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Organic Blueberry Almond Granola\n</td>
      <td>0.04572</td>
      <td>10.91</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Organic Coconut Chips\n</td>
      <td>0.09398</td>
      <td>6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Organic Garbanzo Beans\n</td>
      <td>0.05334</td>
      <td>17.02</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Organic Yellow Split Peas\n</td>
      <td>0.05588</td>
      <td>28.89</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Organic Trail Mix\n</td>
      <td>0.127</td>
      <td>13.33</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Organic Raw Pumpkin Seeds\n</td>
      <td>0.04318</td>
      <td>30</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Organic Tamari Pumpkin Seed\n</td>
      <td>0.97028</td>
      <td>26.47</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Organic Harvest Pilaf\n</td>
      <td>0.02794</td>
      <td>15.56</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Organic Salted Pistachios\n</td>
      <td>1.45034</td>
      <td>21.43</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Organic Medjool Dates\n</td>
      <td>0.0127</td>
      <td>2.2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Organic Whole Cashews\n</td>
      <td>0.0381</td>
      <td>14.71</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Organic Flourless Sprouted 7-Grain Bread\n</td>
      <td>0.6731</td>
      <td>11.76</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Organic Sunny Days Snack Bars\n</td>
      <td>0.60198</td>
      <td>5.26</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Organic Nine Grain All Natural Bread\n</td>
      <td>1.0033</td>
      <td>11.63</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Organic 100% Whole Wheat\n</td>
      <td>0.82804</td>
      <td>9.3</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Organic Great Seed\n</td>
      <td>0.88646</td>
      <td>11.63</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Organic Tortellini Pasta\n</td>
      <td>0.381</td>
      <td>10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Organic Ravioli\n</td>
      <td>0.5588</td>
      <td>9</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Organic Broccoli Florets\n</td>
      <td>0.07366</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Organic Creamy Tomato Bisque\n</td>
      <td>0.75692</td>
      <td>1.22</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Organic Green Peas\n</td>
      <td>0.5715</td>
      <td>5.62</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Organic Mixed Vegetable\n</td>
      <td>0.19304</td>
      <td>2.35</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Organic Beef Burger\n</td>
      <td>0.14224</td>
      <td>17.88</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>855</th>
      <td>Organic Gummy Bears &amp; Worms\n</td>
      <td>0</td>
      <td>2.38</td>
    </tr>
    <tr>
      <th>856</th>
      <td>Organic Fruit Flavored Snacks\n</td>
      <td>0.10922</td>
      <td>4.35</td>
    </tr>
    <tr>
      <th>857</th>
      <td>Organic Gummy Bears\n</td>
      <td>0</td>
      <td>4.35</td>
    </tr>
    <tr>
      <th>858</th>
      <td>Organic Lollipops\n</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>859</th>
      <td>Organic Sour Head\n</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>860</th>
      <td>Organic Buttermilk Pancake Mix\n</td>
      <td>2.27838</td>
      <td>7.69</td>
    </tr>
    <tr>
      <th>861</th>
      <td>Organic Yellow Cake Mix\n</td>
      <td>1.905</td>
      <td>4.55</td>
    </tr>
    <tr>
      <th>862</th>
      <td>Organic Double Chocolate Brownie Mix\n</td>
      <td>1.08966</td>
      <td>3.57</td>
    </tr>
    <tr>
      <th>863</th>
      <td>Organic Whole Grain Muffin Mix\n</td>
      <td>2.04724</td>
      <td>5.56</td>
    </tr>
    <tr>
      <th>864</th>
      <td>Organic 1% Lowfat Milk\n</td>
      <td>0.14478</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>865</th>
      <td>Organic Whole Milk\n</td>
      <td>0.1397</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>866</th>
      <td>Organic 2% Reduced Fat Milk\n</td>
      <td>0.1397</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>867</th>
      <td>Organic Fat Free Skim Milk\n</td>
      <td>0.14478</td>
      <td>3.81</td>
    </tr>
    <tr>
      <th>868</th>
      <td>Organic Fruit\n</td>
      <td>0</td>
      <td>1.43</td>
    </tr>
    <tr>
      <th>869</th>
      <td>Organic Vegetable Chili\n</td>
      <td>0.63246</td>
      <td>2.45</td>
    </tr>
    <tr>
      <th>870</th>
      <td>Organic Salted Butter Made With Organic Sweet ...</td>
      <td>1.63322</td>
      <td>0</td>
    </tr>
    <tr>
      <th>871</th>
      <td>Organic Whole Milk\n</td>
      <td>0.127</td>
      <td>3.33</td>
    </tr>
    <tr>
      <th>872</th>
      <td>Organic 2% Reduced Fat Milk\n</td>
      <td>0.13208</td>
      <td>3.33</td>
    </tr>
    <tr>
      <th>873</th>
      <td>Organic Lowfat Milk\n</td>
      <td>0.13208</td>
      <td>3.33</td>
    </tr>
    <tr>
      <th>874</th>
      <td>Organic Milk\n</td>
      <td>0.13208</td>
      <td>3.33</td>
    </tr>
    <tr>
      <th>875</th>
      <td>Organic Milk\n</td>
      <td>0.13462</td>
      <td>3.38</td>
    </tr>
    <tr>
      <th>876</th>
      <td>Organic Brown Flax Seeds\n</td>
      <td>0.07874</td>
      <td>15.38</td>
    </tr>
    <tr>
      <th>877</th>
      <td>Organic Raw Shelled Pumpkin Seed\n</td>
      <td>0.04572</td>
      <td>25</td>
    </tr>
    <tr>
      <th>878</th>
      <td>Organic Raw Sunflower Meat\n</td>
      <td>0.02794</td>
      <td>21.43</td>
    </tr>
    <tr>
      <th>879</th>
      <td>Organic Maple Syrup\n</td>
      <td>0.02032</td>
      <td>0</td>
    </tr>
    <tr>
      <th>880</th>
      <td>Organic Super Sweet Whole Kernel Corn\n</td>
      <td>0.4064</td>
      <td>1.6</td>
    </tr>
    <tr>
      <th>881</th>
      <td>Organic Sweet Peas\n</td>
      <td>0.6096</td>
      <td>3.2</td>
    </tr>
    <tr>
      <th>882</th>
      <td>Organic Cut Green Beans\n</td>
      <td>0.61468</td>
      <td>0.83</td>
    </tr>
    <tr>
      <th>883</th>
      <td>Organic Black Beans\n</td>
      <td>0.254</td>
      <td>6.15</td>
    </tr>
    <tr>
      <th>884</th>
      <td>Organic Dark Red Kidney Beans\n</td>
      <td>0.27432</td>
      <td>6.92</td>
    </tr>
  </tbody>
</table>
<p>885 rows × 3 columns</p>
</div>
</div>



## 11.3 Implement lazy evaluation functions

### Generator functions



{:.input_area}
```
def square_them(numbers):
  for number in numbers:
    yield number * number
    
  
s = square_them(range(10000))

print(next(s))
print(next(s))
print(next(s))
print(next(s))
```


{:.output .output_stream}
```
0
1
4
9

```

### Infinite generators



{:.input_area}
```
def counter(d):
  
  while True:
    d += 1
    yield d
```




{:.input_area}
```
c = counter(10)

print(next(c))
print(next(c))
print(next(c))
```


{:.output .output_stream}
```
11
12
13

```

### Other forms of lazy evaluation



{:.input_area}
```
def some_expensive_connection():
  import time
  time.sleep(10)
  return {}

_DB = None

def DB():
  global _DB
  if _DB is None:
    _DB = some_expensive_connection()
    
    
    
    

  
```


# File setup



{:.input_area}
```
from google.colab import files
# /Users/kbehrman/Google-Drive/projects/pragailabs/python-for-data-science/food/data
files.upload()
!ls
```



<div markdown="0" class="output output_html">

     <input type="file" id="files-5e8da7e1-ea08-4b0a-8071-4a72725bb825" name="files[]" multiple disabled />
     <output id="result-5e8da7e1-ea08-4b0a-8071-4a72725bb825">
      Upload widget is only available when the cell has been executed in the
      current browser session. Please rerun this cell to enable.
      </output>
      <script src="/nbextensions/google.colab/files.js"></script> 
</div>


{:.output .output_stream}
```
'features.en.openfoodfacts.org.products (1).csv'
'features.en.openfoodfacts.org.products (2).csv'
 features.en.openfoodfacts.org.products.csv
 sample_data

```
