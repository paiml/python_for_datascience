---
redirect_from:
  - "/lessons/lesson8-python-for-data-science-functions"
interact_link: content/lessons/Lesson8_Python_For_Data_Science_Functions.ipynb
kernel_name: python3
title: 'Lesson 8 - Functions'
prev_page:
  url: /lessons/Lesson7_Python_For_Datascience_Execution_Control
  title: 'Lesson 7 - Execution Control'
next_page:
  url: /lessons/Lesson9_Python_For_Data_Science_Data_Science_Libraries
  title: 'Lesson 9 - Data Science Libraries'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson8_Python_For_Data_Science_Functions.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 8: Functions

## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 8.1 Write and use functions

### Building blocks of distributed computing



{:.input_area}
```
def work(input):
  """Processes input and returns output"""
  
  output = input + 1
  return output

```




{:.input_area}
```
work(1)
```





{:.output .output_data_text}
```
2
```



### Key Components of Functions

#### Docstrings



{:.input_area}
```
def docstring():
  """Triple Quoted documentation!"""
  
```




{:.input_area}
```
docstring?
```


#### Arguments:  Keyword and Positional

* *Positional*:  Order based processing
* *Keyword*:  Key/Value processing


##### Positional



{:.input_area}
```
def positional(first,second,third):
  """Processes arguments to function in order"""
  
  print(f"Processed first {first}")
  print(f"Processed second {second}")
  print(f"Processed third {third}")
  
  
```




{:.input_area}
```
positional(1, 2, 3)
```


{:.output .output_stream}
```
Processed first 1
Processed second 2
Processed third 3

```



{:.input_area}
```
positional(2, 3, 1)
```


{:.output .output_stream}
```
Processed first 2
Processed second 3
Processed third 1

```

##### Keyword



{:.input_area}
```
def keyword(first=1, second=2, third=3):
  """Processed in any order"""
  
  print(f"Processed first {first}")
  print(f"Processed second {second}")
  print(f"Processed third {third}")
```




{:.input_area}
```
keyword(1,2,3)
```


{:.output .output_stream}
```
Processed first 1
Processed second 2
Processed third 3

```



{:.input_area}
```
keyword(second=2, third=3, first=1)
```


{:.output .output_stream}
```
Processed first 1
Processed second 2
Processed third 3

```



{:.input_area}
```
keyword(second=2)
```


{:.output .output_stream}
```
Processed first 1
Processed second 2
Processed third 3

```

#### Return

Default is None



{:.input_area}
```
def bridge_to_nowhere():pass
  
```




{:.input_area}
```
bridge_to_nowhere() == None
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
type(bridge_to_nowhere())
```





{:.output .output_data_text}
```
NoneType
```



Most useful functions return something



{:.input_area}
```
def more_than_zero():
  
  return 1
```




{:.input_area}
```
more_than_zero() == 1
```





{:.output .output_data_text}
```
True
```



Functions can return functions



{:.input_area}
```
def inner_peace():
  """A deep function"""
  
  def peace():
    return "piece"
  
  return peace
```




{:.input_area}
```
inner = inner_peace()
print(f"Hey, I need that {inner()}")
```


{:.output .output_stream}
```
Hey, I need that piece

```



{:.input_area}
```
inner2 = inner_peace()
```




{:.input_area}
```
type(inner2)
```





{:.output .output_data_text}
```
function
```



## 8.2 Write and use decorators

### Using Decorators

Very common to use for dispatching a function via:


*   Command-line tools
*   Web Routes
*   Speeding up Python code



#### Command-line Tools



{:.input_area}
```
%%python
import click

def less_than_zero():
  
  return {"iron_man": -1}

@click.command()
def run():
  
  rdj = less_than_zero()
  click.echo(f"Robert Downey Junior is versatile {rdj}")
  
if __name__== "__main__":
  run()
```


{:.output .output_stream}
```
Robert Downey Junior is versatile {'iron_man': -1}

```

#### Web App



{:.input_area}
```
%%writefile run.py
from flask import Flask
app = Flask(__name__)

def less_than_zero():
  
  return {"iron_man": -1}

@app.route('/')
def runit():
  return less_than_zero()
  

```


{:.output .output_stream}
```
Overwriting run.py

```

curl localhost:5000/ {'iron_man': -1}



#### Using Numba

Using numba Just in Time Compiler (JIT) can dramatically speed up code



{:.input_area}
```
def crunchy_normal():
  count = 0
  num = 10000000
  for i in range(num):
    count += num  
  return count
```




{:.input_area}
```
%%time
crunchy_normal()
```


{:.output .output_stream}
```
CPU times: user 906 ms, sys: 581 µs, total: 907 ms
Wall time: 908 ms

```




{:.output .output_data_text}
```
100000000000000
```





{:.input_area}
```
from numba import jit

@jit(nopython=True)
def crunchy():
  count = 0
  num = 10000000
  for i in range(num):
    count += num  
  return count
```




{:.input_area}
```
%%time
crunchy()
```


{:.output .output_stream}
```
CPU times: user 113 ms, sys: 15.9 ms, total: 129 ms
Wall time: 194 ms

```




{:.output .output_data_text}
```
100000000000000
```



### Writing Decorators

#### Instrumentation Decorator

Using a decorator to time, debug or instrument code is very common



{:.input_area}
```
from functools import wraps
import time

def instrument(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print(f"function: {f.__name__}, args: [{args}, {kw}] took: {te-ts} sec")
        return result
    return wrap
```


Using decorator to time execution of a function



{:.input_area}
```
from time import sleep

@instrument
def simulated_work(count, task):
  """simulates work"""
  
  print("Starting work")
  sleep(count)
  processed = f"one {task} leap"
  return processed
  
```




{:.input_area}
```
simulated_work(3, task="small")  
```


{:.output .output_stream}
```
Starting work
function: simulated_work, args: [(3,), {'task': 'small'}] took: 3.0027008056640625 sec

```




{:.output .output_data_text}
```
'one small leap'
```



## 8.3 Compose closure functions

### Functions with state



{:.input_area}
```
def calorie_counter():
    """Counts calories"""
    
    protein = 0
    fat = 0
    carbohydrate = 0
    total = 0
    def calorie_counter_inner(food):
        nonlocal protein
        nonlocal fat
        nonlocal carbohydrate
        if food == "protein":
          protein += 4
        elif food == "carbohydrate":
          carbohydrate += 4
        elif food == "fat":
          fat += 9
        total = protein + carbohydrate + fat
        print(f"Consumed {total} calories of protein: {protein}, carbohydrate: {carbohydrate}, fat: {fat}")
    return calorie_counter_inner
```




{:.input_area}
```
meal = calorie_counter()
type(meal)

```





{:.output .output_data_text}
```
function
```





{:.input_area}
```
meal("carbohydrate")
```


{:.output .output_stream}
```
Consumed 4 calories of protein: 0, carbohydrate: 4, fat: 0

```



{:.input_area}
```
meal("fat")
```


{:.output .output_stream}
```
Consumed 13 calories of protein: 0, carbohydrate: 4, fat: 9

```



{:.input_area}
```
meal("protein")
```


{:.output .output_stream}
```
Consumed 17 calories of protein: 4, carbohydrate: 4, fat: 9

```

## 8.4 Use lambda

### YAGNI


**Y**ou **A**in't **G**onna **N**eed** I**t




{:.input_area}
```
import this
```


{:.output .output_stream}
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```



{:.input_area}
```
func = lambda x: x**x
func(4)
```





{:.output .output_data_text}
```
256
```





{:.input_area}
```
def expo(x):
  return x**x

expo(4)
```





{:.output .output_data_text}
```
256
```



### Close Encounters with Lambdas

Used in series or DataFrame 



{:.input_area}
```
import pandas as pd

series = pd.Series([1, 5, 10])
series.apply(lambda x: x**x)
```





{:.output .output_data_text}
```
0              1
1           3125
2    10000000000
dtype: int64
```





{:.input_area}
```
def expo(x):
  return x**x

expo(4)
```




{:.input_area}
```
import pandas as pd

series = pd.Series([1, 5, 10])
series.apply(expo)
```





{:.output .output_data_text}
```
0              1
1           3125
2    10000000000
dtype: int64
```



## 8.5 Advanced Use of Functions

### Applying a Function to a Pandas DataFrame



{:.input_area}
```
import pandas as pd
df = pd.read_csv(
    "https://raw.githubusercontent.com/noahgift/food/master/data/features.en.openfoodfacts.org.products.csv")
df.drop(["Unnamed: 0", "exceeded", "g_sum", "energy_100g"], axis=1, inplace=True) #drop two rows we don't need
df.head()
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
      <th>fat_100g</th>
      <th>carbohydrates_100g</th>
      <th>sugars_100g</th>
      <th>proteins_100g</th>
      <th>salt_100g</th>
      <th>reconstructed_energy</th>
      <th>product</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>28.57</td>
      <td>64.29</td>
      <td>14.29</td>
      <td>3.57</td>
      <td>0.00000</td>
      <td>2267.85</td>
      <td>Banana Chips Sweetened (Whole)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>17.86</td>
      <td>60.71</td>
      <td>17.86</td>
      <td>17.86</td>
      <td>0.63500</td>
      <td>2032.23</td>
      <td>Peanuts</td>
    </tr>
    <tr>
      <th>2</th>
      <td>57.14</td>
      <td>17.86</td>
      <td>3.57</td>
      <td>17.86</td>
      <td>1.22428</td>
      <td>2835.70</td>
      <td>Organic Salted Nut Mix</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.75</td>
      <td>57.81</td>
      <td>15.62</td>
      <td>14.06</td>
      <td>0.13970</td>
      <td>1953.04</td>
      <td>Organic Muesli</td>
    </tr>
    <tr>
      <th>4</th>
      <td>36.67</td>
      <td>36.67</td>
      <td>3.33</td>
      <td>16.67</td>
      <td>1.60782</td>
      <td>2336.91</td>
      <td>Zen Party Mix</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```
def high_protein(row):
  """Creates a high or low protein category"""
  
  if row > 80:
    return "high_protein"
  return "low_protein"
```




{:.input_area}
```
df["high_protein"] = df["proteins_100g"].apply(high_protein)
df.head()
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
      <th>fat_100g</th>
      <th>carbohydrates_100g</th>
      <th>sugars_100g</th>
      <th>proteins_100g</th>
      <th>salt_100g</th>
      <th>reconstructed_energy</th>
      <th>product</th>
      <th>high_protein</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>28.57</td>
      <td>64.29</td>
      <td>14.29</td>
      <td>3.57</td>
      <td>0.00000</td>
      <td>2267.85</td>
      <td>Banana Chips Sweetened (Whole)</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>1</th>
      <td>17.86</td>
      <td>60.71</td>
      <td>17.86</td>
      <td>17.86</td>
      <td>0.63500</td>
      <td>2032.23</td>
      <td>Peanuts</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>2</th>
      <td>57.14</td>
      <td>17.86</td>
      <td>3.57</td>
      <td>17.86</td>
      <td>1.22428</td>
      <td>2835.70</td>
      <td>Organic Salted Nut Mix</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.75</td>
      <td>57.81</td>
      <td>15.62</td>
      <td>14.06</td>
      <td>0.13970</td>
      <td>1953.04</td>
      <td>Organic Muesli</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>4</th>
      <td>36.67</td>
      <td>36.67</td>
      <td>3.33</td>
      <td>16.67</td>
      <td>1.60782</td>
      <td>2336.91</td>
      <td>Zen Party Mix</td>
      <td>low_protein</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```
df.describe()
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
      <th>fat_100g</th>
      <th>carbohydrates_100g</th>
      <th>sugars_100g</th>
      <th>proteins_100g</th>
      <th>salt_100g</th>
      <th>reconstructed_energy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>45028.000000</td>
      <td>45028.000000</td>
      <td>45028.000000</td>
      <td>45028.000000</td>
      <td>45028.000000</td>
      <td>45028.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>10.765910</td>
      <td>34.054788</td>
      <td>16.005614</td>
      <td>6.619437</td>
      <td>1.469631</td>
      <td>1111.332304</td>
    </tr>
    <tr>
      <th>std</th>
      <td>14.930087</td>
      <td>29.557017</td>
      <td>21.495512</td>
      <td>7.936770</td>
      <td>12.794943</td>
      <td>791.621634</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-1.200000</td>
      <td>-3.570000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>7.440000</td>
      <td>1.570000</td>
      <td>0.000000</td>
      <td>0.063500</td>
      <td>334.520000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.170000</td>
      <td>22.390000</td>
      <td>5.880000</td>
      <td>4.000000</td>
      <td>0.635000</td>
      <td>1121.540000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>17.860000</td>
      <td>61.540000</td>
      <td>23.080000</td>
      <td>9.520000</td>
      <td>1.440180</td>
      <td>1678.460000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>2032.000000</td>
      <td>4475.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Partial Functions



{:.input_area}
```
from functools import partial

def multiple_sort(column_one, column_two):
  """Performs multiple sort on a pandas DataFrame"""
  
  sorted_df = df.sort_values(by=[column_one, column_two], 
                 ascending=[False, False])
  return sorted_df
  
multisort = partial(multiple_sort, "sugars_100g")
type(multisort)
```





{:.output .output_data_text}
```
functools.partial
```



Find sugary and fatty food



{:.input_area}
```
df = multisort("fat_100g")
df.head()
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
      <th>fat_100g</th>
      <th>carbohydrates_100g</th>
      <th>sugars_100g</th>
      <th>proteins_100g</th>
      <th>salt_100g</th>
      <th>reconstructed_energy</th>
      <th>product</th>
      <th>high_protein</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8254</th>
      <td>25.00</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00000</td>
      <td>2675.00</td>
      <td>Princess Mix Decorations</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>8255</th>
      <td>25.00</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00000</td>
      <td>2675.00</td>
      <td>Frosted Mix</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>8253</th>
      <td>12.50</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00000</td>
      <td>2187.50</td>
      <td>Holiday Happiness Mix</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>9371</th>
      <td>1.79</td>
      <td>85.71</td>
      <td>100.0</td>
      <td>7.14</td>
      <td>0.04572</td>
      <td>1648.26</td>
      <td>Organic Just Cherries</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>222</th>
      <td>0.00</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00000</td>
      <td>1700.00</td>
      <td>Tnt Exploding Candy</td>
      <td>low_protein</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Find sugary and salty food



{:.input_area}
```
df = multisort("salt_100g")
df.head()
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
      <th>fat_100g</th>
      <th>carbohydrates_100g</th>
      <th>sugars_100g</th>
      <th>proteins_100g</th>
      <th>salt_100g</th>
      <th>reconstructed_energy</th>
      <th>product</th>
      <th>high_protein</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33151</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>71.120</td>
      <td>0.0</td>
      <td>Turkey Brine Kit, Garlic &amp; Herb</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>24783</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>24.130</td>
      <td>1700.0</td>
      <td>Seasoning</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>4073</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>7.620</td>
      <td>1700.0</td>
      <td>Seasoning Rub, Sweet &amp; Spicy Seafood</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>10282</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>2.540</td>
      <td>1700.0</td>
      <td>Instant Pectin</td>
      <td>low_protein</td>
    </tr>
    <tr>
      <th>17880</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.635</td>
      <td>1700.0</td>
      <td>Cranberry Cosmos Cocktail Rimming Sugar</td>
      <td>low_protein</td>
    </tr>
  </tbody>
</table>
</div>
</div>


