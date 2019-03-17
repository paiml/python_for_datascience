---
redirect_from:
  - "/lessons/lesson3-python-for-data-science-basics"
interact_link: content/lessons/Lesson3_Python_For_Data_Science_Basics.ipynb
kernel_name: python3
title: 'Lesson 3 - Basics'
prev_page:
  url: /lessons/Lesson2_Python_For_Data_Science_Introduction_to_Colab
  title: 'Lesson 2 - Introduction to Colab'
next_page:
  url: /lessons/Lesson4_Python_For_Data_Science_Strings
  title: 'Lesson 4 - Strings'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson3_Python_For_Data_Science_Basics.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 3 Basics

## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 3.1 Write procedural code

 ### Procedural Statements
 Procedural statements are literally statements that  can be issued one line at a time.  Below are types of procedural statements.  These statements can be run in:
 * Jupyter Notebook
 * IPython shell
 * Python interpreter
 * Python scripts



{:.input_area}
```
three_type_of_energy = ["protein", "carbohydrates", "fat"]
```


### **Multiple procedural statements**



{:.input_area}
```
protein, carbohydrate, fat = three_type_of_energy
print(f"{carbohydrate} sure taste good")
print(f"{fat} isn't bad for you anymore?")

```


{:.output .output_stream}
```
carbohydrates sure taste good
fat isn't bad for you anymore?

```

### Adding Numbers



{:.input_area}
```
protein = 4
fat = 9
carbohydrate = 4
carbohydrate + protein
```





{:.output .output_data_text}
```
8
```



**Adding Phrases**



{:.input_area}
```
"a carbohydrate " + "has " + str(carbohydrate) + " calories" 
```





{:.output .output_data_text}
```
'a carbohydrate has 4 calories'
```



**Complex statements**

More complex statements can be created that use data structures like the belts variable, which is a list.



{:.input_area}
```
for energy_type in three_type_of_energy:
  print(energy_type)
```


{:.output .output_stream}
```
protein
carbohydrates
fat

```

## 3.2 Use simple expressions and variables

### assert



{:.input_area}
```
assert carbohydrate == 9
  
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-65-448b002ebeaf> in <module>()
    ----> 1 assert carbohydrate == 9
          2 


    AssertionError: 


```



{:.input_area}
```
assert carbohydrate == 4
```


### pass



{:.input_area}
```
class Calorie: pass
kcal = Calorie()

```




{:.input_area}
```
kcal.value = "9"
```


### del




{:.input_area}
```
class Calorie: pass
kcal = Calorie()
%who_ls
```





{:.output .output_data_text}
```
['Calorie',
 'breakfast',
 'calories',
 'carb',
 'carbohydrate',
 'carbs',
 'egg_set',
 'energy',
 'energy_type',
 'fat',
 'food',
 'ingredients',
 'kcal',
 'omelette',
 'protein',
 'snacks',
 'this',
 'three_type_of_energy',
 'too_much_food',
 'variable']
```





{:.input_area}
```
kcal.value = 9
```




{:.input_area}
```
del kcal
%who_ls
```





{:.output .output_data_text}
```
['Calorie',
 'breakfast',
 'calories',
 'carb',
 'carbohydrate',
 'carbs',
 'egg_set',
 'energy',
 'energy_type',
 'fat',
 'food',
 'ingredients',
 'omelette',
 'protein',
 'snacks',
 'this',
 'three_type_of_energy',
 'too_much_food',
 'variable']
```



### return



{:.input_area}
```
def food():
  return "whey"

print(f"Make {food()} while the sun shines")
```


{:.output .output_stream}
```
Make whey while the sun shines

```

### yield



{:.input_area}
```
def too_much_food():
  meal = ["orange", "apple", "turkey", "ham"]
  for snack in meal:
    yield snack
    
```




{:.input_area}
```
snacks = too_much_food()
print(next(snacks))
print(next(snacks))
```


{:.output .output_stream}
```
orange
apple

```



{:.input_area}
```
next(snacks)
```





{:.output .output_data_text}
```
'turkey'
```





{:.input_area}
```
next(snacks)
```





{:.output .output_data_text}
```
'ham'
```





{:.input_area}
```
next(snacks)
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-78-4cb0aa5aecce> in <module>()
    ----> 1 next(snacks)
    

    StopIteration: 


```

### break




{:.input_area}
```
carbohydrate = 4
calories = 0
while True:
  calories += carbohydrate
  print(f"Eating more carbohydrates {calories}")
  if calories > 8:
    print("This is all I can eat")
    break
```


{:.output .output_stream}
```
Eating more carbohydrates 4
Eating more carbohydrates 8
Eating more carbohydrates 12
This is all I can eat

```

### continue



{:.input_area}
```
three_type_of_energy = ["protein", "sugar", "fat"]
for energy in three_type_of_energy:
  if energy == "sugar":
    print(f"skipping {energy} for my health")
    continue
  print(f"eating {energy}")
```


{:.output .output_stream}
```
eating protein
skipping sugar for my health
eating fat

```

### import




{:.input_area}
```
import this
```


## 3.3 Work with the built-in types

### dict



{:.input_area}
```
omelette = {"egg": 3, "ham": "yes"}
type(omelette)
```





{:.output .output_data_text}
```
dict
```



### list



{:.input_area}
```
ingredients = ["egg", "ham", "bacon"]
type(ingredients)
```





{:.output .output_data_text}
```
list
```



### set




{:.input_area}
```
egg_set = set(["egg", "egg"])
type(egg_set)
```





{:.output .output_data_text}
```
set
```





{:.input_area}
```
egg_set
```





{:.output .output_data_text}
```
{'egg'}
```



### tuple



{:.input_area}
```
breakfast = ("egg","soup")
breakfast[0] = "turkey"
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-96-5737173ae030> in <module>()
          1 breakfast = ("egg","soup")
    ----> 2 breakfast[0] = "turkey"
    

    TypeError: 'tuple' object does not support item assignment


```



{:.input_area}
```
breakfast[1]
```





{:.output .output_data_text}
```
'soup'
```



## 3.4 Printing

### Printing



{:.input_area}
```
print("omelets are tasty")

```


{:.output .output_stream}
```
omelets are tasty

```



{:.input_area}
```
variable = "ham"
print(f"I like {variable}")
```


{:.output .output_stream}
```
I like ham

```

### Create Variable and Use Variable



{:.input_area}
```
variable = "omelets";print(variable)
```


{:.output .output_stream}
```
omelets

```

### Use print as a function



{:.input_area}
```
print("kombucha", "manuka honey", sep="+")
```


{:.output .output_stream}
```
kombucha+manuka honey

```

## 3.5 Perform basic math operations



#### Numbers and Arithmetic Operations

Python is also a built-in calculator. Without installing any additional libraries it can do many simple and complex arithmetic operations.

**Adding and Subtracting Numbers**



{:.input_area}
```
steps = (1+1)-1
print(f"Two Steps Forward:  One Step Back = {steps}")
```


{:.output .output_stream}
```
Two Steps Forward:  One Step Back = 1

```

**Multiplication with Decimals**

Can use float type to solve decimal problems



{:.input_area}
```
body_fat_percentage = 0.10
weight = 200
fat_total = body_fat_percentage * weight
print(f"I weight 200lbs, and {fat_total}lbs of that is fat")
```


{:.output .output_stream}
```
I weight 200lbs, and 20.0lbs of that is fat

```

Can also use Decimal Library to set precision and deal with repeating decimal




{:.input_area}
```
from decimal import (Decimal, getcontext)

getcontext().prec = 2
Decimal(1)/Decimal(3)


```





{:.output .output_data_text}
```
Decimal('0.33')
```



**Using Exponents**

Using the Python math library it is straightforward to call 2 to the 3rd power



{:.input_area}
```
import math
math.pow(2,3)
```





{:.output .output_data_text}
```
8.0
```



Can also use built in exponent operator to accomplish same thing



{:.input_area}
```
2**3
```





{:.output .output_data_text}
```
8
```



multiply



{:.input_area}
```
2*3
```





{:.output .output_data_text}
```
6
```



this is regular multiplication



{:.input_area}
```
2*3
```





{:.output .output_data_text}
```
6
```



**Converting Between different numerical types**

There are many numerical forms to be aware of in Python.
A couple of the most common are:

* Integers
* Floats



{:.input_area}
```
number = 100
num_type = type(number).__name__
print(f"{number} is type [{num_type}]")
```


{:.output .output_stream}
```
100 is type [int]

```



{:.input_area}
```
number = float(100)
num_type = type(number).__name__
print(f"{number} is type [{num_type}]")
```


{:.output .output_stream}
```
100.0 is type [float]

```



{:.input_area}
```
class Foo:pass
f = Foo()
```




{:.input_area}
```
type(f)
```





{:.output .output_data_text}
```
__main__.Foo
```



**Numbers can also be rounded**

Python Built in round 



{:.input_area}
```
too_many_decimals = 1.912345897
round(too_many_decimals, 3)
#get more info
#round?
```





{:.output .output_data_text}
```
1.912
```



Numpy round



{:.input_area}
```
import numpy as np
np.round(too_many_decimals, 3)
```





{:.output .output_data_text}
```
1.912
```



Pandas round



{:.input_area}
```
import pandas as pd
df = pd.DataFrame([too_many_decimals], columns=["A"], index=["first"])
df.round(2)

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
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>1.91</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Simple benchmark of all three (**Python**, **numpy** and **Pandas** round):   using **%timeit**

*Depending on what is getting rounded (i.e. a very large DataFrame, performance may very, so knowing how to benchmark performance is important with round) *




{:.input_area}
```
print("built in Python Round")
%timeit round(too_many_decimals, 2)

print("numpy round")
%timeit np.round(too_many_decimals, 2)

print("Pandas DataFrame round")
%timeit df.round(2)
```


{:.output .output_stream}
```
built in Python Round
The slowest run took 21.00 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 3: 486 ns per loop
numpy round
The slowest run took 9.26 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 7.62 µs per loop
Pandas DataFrame round
1000 loops, best of 3: 951 µs per loop

```

## 3.6 Use classes and objects with dot notation



#### Interacting with Special Class Methods and Other Class Techniques

Class special methods have the signature ```__method__```:

Examples include
```
__len__
__call__
__equal__

```



{:.input_area}
```
l = [1,2]
len(l)
#class Foo:pass
#f = Foo()
#len(f)
```





{:.output .output_data_text}
```
2
```





{:.input_area}
```
class JonJones:
  """Jon Jones class with customized length"""
  
  def __len__(self):
    return 84

jon_jones = JonJones()
len(jon_jones)
```





{:.output .output_data_text}
```
84
```





{:.input_area}
```
class foo():pass
f = foo()
f.red = "red"
len(f)
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-123-f0f0529fb27b> in <module>()
          2 f = foo()
          3 f.red = "red"
    ----> 4 len(f)
    

    TypeError: object of type 'foo' has no len()


```

@property decorator is a shortcut for creating a read only property



{:.input_area}
```
class JonJones:
  """Jon Jones class with read only property"""
  
  @property
  def reach(self):
    return 84

jon_jones = JonJones()
jon_jones.reach
#jon_jones.reach = 85 #cannot set
jon_jones.length = 85
jon_jones.length
```





{:.output .output_data_text}
```
85
```





{:.input_area}
```
jon_jones.reach
jon_jones.reach = 85
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-127-c873d37e7994> in <module>()
          1 jon_jones.reach
    ----> 2 jon_jones.reach = 85
    

    AttributeError: can't set attribute


```

@staticmethod bolts a function onto a class



{:.input_area}
```
class JonJones:
  """Jon Jones Class with 'bolt-on' reach method
  self isn't needed
  """
  
  @staticmethod
  def reach():
    return 84

jon_jones =JonJones()
jon_jones.reach()
```





{:.output .output_data_text}
```
84
```



#### Immutability concepts with Objects



{:.input_area}
```
class Foo:
  
  @property
  def unbreakable(self):
    return "David"


```




{:.input_area}
```
foo = Foo()
foo.unbreakable 
```





{:.output .output_data_text}
```
'David'
```





{:.input_area}
```
foo.not_unbreakable = "Elijah"
```


@property acts like an read only attribute, but it isn't



{:.input_area}
```
foo.__dict__
```





{:.output .output_data_text}
```
{'not_unbreakable': 'Elijah'}
```



You can change an attribute on the object, but not the read only property



{:.input_area}
```
foo.not_unbreakable = "Mr. Glass"
```




{:.input_area}
```
foo.unbreakable = "Bruce Willis"
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-137-4bc1ea5ae699> in <module>()
    ----> 1 foo.unbreakable = "Bruce Willis"
    

    AttributeError: can't set attribute


```

## Notes
