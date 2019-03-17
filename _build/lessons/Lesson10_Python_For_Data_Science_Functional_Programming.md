---
redirect_from:
  - "/lessons/lesson10-python-for-data-science-functional-programming"
interact_link: content/lessons/Lesson10_Python_For_Data_Science_Functional_Programming.ipynb
kernel_name: python3
title: 'Lesson 10 - Functional Programming'
prev_page:
  url: /lessons/Lesson9_Python_For_Data_Science_Data_Science_Libraries
  title: 'Lesson 9 - Data Science Libraries'
next_page:
  url: /lessons/Lesson11_Python_For_Data_Science_Lazy_Evaluation
  title: 'Lesson 11 - Lazy Evaluation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson10_Python_For_Data_Science_Functional_Programming.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 10: Functional Programming


## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 10.1 Understand functional programming



### Depending on state



{:.input_area}
```
wind = 'Southeast'

def describe_the_wind():
  return f'The wind blows from the {wind}'

describe_the_wind()
```





{:.output .output_data_text}
```
'The wind blows from the Southeast'
```



### Functional approach



{:.input_area}
```
def describe_the_wind(wind):
  return f'The wind blows from the {wind}'

describe_the_wind('Northeast')
```





{:.output .output_data_text}
```
'The wind blows from the Northeast'
```



### Changing state



{:.input_area}
```
WINDS = ['Northeast', 'Northwest', 'Southeast', 'Southwest']
WIND = WINDS[0]

def change_wind():
  global WIND
  WIND = WINDS[(WINDS.index(WIND) + 1)%3]
  
WIND
```





{:.output .output_data_text}
```
'Northeast'
```





{:.input_area}
```
change_wind()
WIND
```





{:.output .output_data_text}
```
'Northeast'
```





{:.input_area}
```
for _ in WINDS:
  print(WIND)
  change_wind()

```


### Functional approach



{:.input_area}
```
def change_wind(wind_index):
  winds = ['Northeast', 'Northwest', 'Southeast', 'Southwest']
  return winds[wind_index]

print( change_wind(0) )
print( change_wind(1) )
print( change_wind(2) )
print( change_wind(3) )
```


{:.output .output_stream}
```
Northeast
Northwest
Southeast
Southwest

```

### Changing state




{:.input_area}
```
def change_mutable_data(data):
  '''A function which changes
  mutable data.'''
  data['owner'] = 'White Star Line'

  
d = {"vehicle": "ship", "owner": "Joseph Bruce Ismay"}

change_mutable_data(d)
d

```





{:.output .output_data_text}
```
{'owner': 'White Star Line', 'vehicle': 'ship'}
```



### Functional approach



{:.input_area}
```
d = {"vehicle": "ship", "owner": "Joseph Bruce Ismay"}

def change_owner(data):
  new_data = data.copy()
  new_data['owner'] = 'White Star Line'
  return new_data


changed = change_owner(d)
changed
```





{:.output .output_data_text}
```
{'owner': 'White Star Line', 'vehicle': 'ship'}
```



## 10.2 Apply functions to data science workflows




{:.input_area}
```
import pandas as pd
moby_dick_quotes = [
    """It is not down on any map; true places never are.""",
    """
    Consider the subtleness of the sea; how its most dreaded creatures glide under water, unapparent for the most part, and treacherously hidden beneath the loveliest tints of azure. Consider also the devilish brilliance and beauty of many of its most remorseless tribes, as the dainty embellished shape of many species of sharks. Consider, once more, the universal cannibalism of the sea; all whose creatures prey upon each other, carrying on eternal war since the world began. 
    Consider all this; and then turn to the green, gentle, and most docile earth; consider them both, the sea and the land; and do you not find a strange analogy to something in yourself? For as this appalling ocean surrounds the verdant land, so in the soul of man there lies one insular Tahiti, full of peace and joy, but encompassed by all the horrors of the half-known life. God keep thee! Push not off from that isle, thou canst never return!
    """,
    """
    The sea had jeeringly kept his finite body up, but drowned the infinite of his soul. Not drowned entirely, though. Rather carried down alive to wondrous depths, where strange shapes of the unwarped primal world glided to and fro before his passive eyes; and the miser-merman, Wisdom, revealed his hoarded heaps; and among the joyous, heartless, ever-juvenile eternities, Pip saw the multitudinous, God-omnipresent, coral insects, that out of the firmament of waters heaved the colossal orbs. He saw God’s foot upon the treadle of the loom, and spoke it; and therefore his shipmates called him mad. So man’s insanity is heaven’s sense; and wandering from all mortal reason, man comes at last to that celestial thought, which, to reason, is absurd and frantic; and weal or woe, feels then uncompromised, indifferent as his God.
    """
]
df = pd.DataFrame(moby_dick_quotes)
df.columns = ["quotes"]
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
      <th>quotes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>It is not down on any map; true places never are.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>\n    Consider the subtleness of the sea; how ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>\n    The sea had jeeringly kept his finite bo...</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```
def classify_religious(column):
  """Creates Religion Feature"""
  
  if "God" in column:
    return "Religious"
  return "Secular"

```




{:.input_area}
```
df["quote_type"] = df["quotes"].apply(classify_religious)
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
      <th>quotes</th>
      <th>quote_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>It is not down on any map; true places never are.</td>
      <td>Secular</td>
    </tr>
    <tr>
      <th>1</th>
      <td>\n    Consider the subtleness of the sea; how ...</td>
      <td>Religious</td>
    </tr>
    <tr>
      <th>2</th>
      <td>\n    The sea had jeeringly kept his finite bo...</td>
      <td>Religious</td>
    </tr>
  </tbody>
</table>
</div>
</div>



## 10.3 Use map/reduce/filter


### map



{:.input_area}
```
def count_flower_petals(d):
  return f"{d} petals counted so far"

counts = map(count_flower_petals, [0,1,2,3,4,5])


list(counts)
```





{:.output .output_data_text}
```
['0 petals counted so far',
 '1 petals counted so far',
 '2 petals counted so far',
 '3 petals counted so far',
 '4 petals counted so far',
 '5 petals counted so far']
```



### mapping with multiple inputs



{:.input_area}
```
l1 = [0,1,2,3,4]
l2 = [10,9,8,7,6]

def multi(d1, d2):
  return d1 * d2

result = map(multi, l1, l2)
print( list(result) )
```


{:.output .output_stream}
```
[0, 9, 16, 21, 24]

```

### reduce



{:.input_area}
```
initial_balance = 10000
debits = [20, 40, 300, 3000, 1, 234]


balance = initial_balance

for debit in debits:
  balance -= debit
  
balance

```





{:.output .output_data_text}
```
6405
```





{:.input_area}
```
inital_balance = 10000
debits = [20, 40, 300, 3000, 1, 234]
from functools import reduce

def minus(a, b):
  return a - b

balance = reduce(minus, debits, initial_balance)
balance
```





{:.output .output_data_text}
```
6405
```





{:.input_area}
```
inital_balance = 10000
debits = [20, 40, 300, 3000, 1, 234]

from functools import reduce
import operator

print( reduce(operator.sub, debits, initial_balance) )
```


{:.output .output_stream}
```
6405

```

### filter



{:.input_area}
```
characters = ['C', 'b', 'c', 'A', 'b','P', 'g', 'S']

def cap(a):
  return a.isupper()

retval = filter(cap, characters)

list(retval)
```





{:.output .output_data_text}
```
['C', 'A', 'P', 'S']
```



## 10.4 Use list comprehensions


### For loop



{:.input_area}
```
names = ['tim', 'tiger', 'tabassum', 'theodora', 'tanya']

capd = []

for name in names:
  capd.append(name.title())
  
capd
```





{:.output .output_data_text}
```
['Tim', 'Tiger', 'Tabassum', 'Theodora', 'Tanya']
```



### Basic list comprehension



{:.input_area}
```
names = ['tim', 'tiger', 'tabassum', 'theodora', 'tanya']

capd = [x.title() for x in names]

capd
```





{:.output .output_data_text}
```
['Tim', 'Tiger', 'Tabassum', 'Theodora', 'Tanya']
```



#### Mapping

##### map example



{:.input_area}
```
def count_flower_petals(d):
  return f"{d} petals counted so far"

counts = map(count_flower_petals, [0,1,2,3,4,5])

list(counts)
```





{:.output .output_data_text}
```
['0 petals counted so far',
 '1 petals counted so far',
 '2 petals counted so far',
 '3 petals counted so far',
 '4 petals counted so far',
 '5 petals counted so far']
```



##### mapping using list comprehension



{:.input_area}
```
[f"{x} petals counted so far" for x in [0,1,2,3,4,5]]
```





{:.output .output_data_text}
```
['0 petals counted so far',
 '1 petals counted so far',
 '2 petals counted so far',
 '3 petals counted so far',
 '4 petals counted so far',
 '5 petals counted so far']
```



#### Filtering

##### filter function



{:.input_area}
```
characters = ['C', 'b', 'c', 'A', 'b','P', 'g', 'S']

def cap(a):
  return a.isupper()

retval = filter(cap, characters)

list(retval)
```





{:.output .output_data_text}
```
['C', 'A', 'P', 'S']
```



##### filtering in list comprehension



{:.input_area}
```
characters = ['C', 'b', 'c', 'A', 'b','P', 'g', 'S']

[x for x in characters if x.isupper()]
```





{:.output .output_data_text}
```
['C', 'A', 'P', 'S']
```



#### Multiple variables



{:.input_area}
```
horts = [ 32.0, 54.12, 12.4, 89.09]
verts = [ 15.9, -34.21, 45.54, 90]

[ f'x: {x} y: {y}' for x,y in zip(horts, verts) ]
```





{:.output .output_data_text}
```
['x: 32.0 y: 15.9', 'x: 54.12 y: -34.21', 'x: 12.4 y: 45.54', 'x: 89.09 y: 90']
```





{:.input_area}
```
list(zip(horts, verts))
```





{:.output .output_data_text}
```
[(32.0, 15.9), (54.12, -34.21), (12.4, 45.54), (89.09, 90)]
```



#### Flatten a list of lists



{:.input_area}
```
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]


[x for y in list_of_lists for x in y]
```





{:.output .output_data_text}
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```



#### Nested



{:.input_area}
```
# Integers greater than and with 3 as a factor divided by 2


[y for y in range(20)]
```





{:.output .output_data_text}
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```





{:.input_area}
```
[y for y in range(20) if y%3==0]
```





{:.output .output_data_text}
```
[0, 3, 6, 9, 12, 15, 18]
```





{:.input_area}
```
[x//2 for x in [y for y in range(20) if y%3==0] if x > 3]
```





{:.output .output_data_text}
```
[3, 4, 6, 7, 9]
```



## 10.5 Use dictionary comprehensions



{:.input_area}
```
rows = [{'name': 'barry', 'id': 1},
        {'name': 'henry', 'id': 3},
        {'name': 'suzy', 'id': 2}]

{ x['name']: x['id'] for x in rows}

```





{:.output .output_data_text}
```
{'barry': 1, 'henry': 3, 'suzy': 2}
```



# Notes
[Functional Programming](https://en.wikipedia.org/wiki/Functional_programming)

[Functional Programming Python](https://docs.python.org/3/howto/functional.html)
