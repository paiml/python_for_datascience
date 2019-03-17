---
redirect_from:
  - "/lessons/lesson5-python-for-data-science-python-data-structure"
interact_link: content/lessons/Lesson5_Python_For_Data_Science_Python_Data_structure.ipynb
kernel_name: python3
title: 'Lesson 5 - Data Structures'
prev_page:
  url: /lessons/Lesson4_Python_For_Data_Science_Strings
  title: 'Lesson 4 - Strings'
next_page:
  url: /lessons/Lesson6_Python_For_Data_Science_Data_Conversion_Recipes
  title: 'Lesson 6 - Data Conversion Recipes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson5_Python_For_Data_Science_Python_Data_structure.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 5: Python Data Structures


## 5.1 Use lists and tuples

### Sequences
Lists, tuples, and strings are all Python sequences, and share many of the same methods.

### Creating an empty list



{:.input_area}
```
empty = []
empty
```





{:.output .output_data_text}
```
[]
```



### Using square brackets with initial values



{:.input_area}
```
numbers = [1, 2, 3]
numbers

```





{:.output .output_data_text}
```
[1, 2, 3]
```



### Casting an iterable
Any iterable can be cast to a list



{:.input_area}
```
numbers = list(range(10))
numbers
```





{:.output .output_data_text}
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



### Creating using multiplication



{:.input_area}
```
num_players = 10
scores = [0] * num_players
scores
```





{:.output .output_data_text}
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```



### Mixing data types
Lists can contain multple data types



{:.input_area}
```
mixed = ['a', 1, 2.0, [13], {}]
mixed
```





{:.output .output_data_text}
```
['a', 1, 2.0, [13], {}]
```



### Indexing
Items in lists can be accessed using indices in a similar fashion to strings.

#### Access first item



{:.input_area}
```
numbers[0]

```





{:.output .output_data_text}
```
0
```



#### Access last item



{:.input_area}
```
numbers[-2]
```





{:.output .output_data_text}
```
8
```



#### Access any item



{:.input_area}
```
numbers[4]
```





{:.output .output_data_text}
```
4
```



### Adding to a list

#### Append to the end of a list



{:.input_area}
```
letters = ['a']
letters.append('c')
letters
```





{:.output .output_data_text}
```
['a', 'c']
```



#### Insert at beginning of list



{:.input_area}
```
letters.insert(0, 'b')
letters
```





{:.output .output_data_text}
```
['b', 'a', 'c']
```



#### Insert at arbitrary position



{:.input_area}
```
letters.insert(2, 'c')
letters
```





{:.output .output_data_text}
```
['b', 'a', 'c', 'c']
```



#### Extending with another list



{:.input_area}
```
more_letters = ['e', 'f', 'g']
letters.extend(more_letters)
letters
```





{:.output .output_data_text}
```
['b', 'a', 'c', 'c', 'e', 'f', 'g']
```



### Change item at some position



{:.input_area}
```
letters[3] = 'd'
letters
```





{:.output .output_data_text}
```
['b', 'a', 'c', 'd', 'e', 'f', 'g']
```



### Swap two items



{:.input_area}
```
letters[0], letters[1] = letters[1], letters[0]
letters
```





{:.output .output_data_text}
```
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```



### Removing items from a list

#### Pop from the end



{:.input_area}
```
letters = ['a', 'b', 'c', 'd', 'e', 'f']
letters.pop()
letters
```





{:.output .output_data_text}
```
['a', 'b', 'c', 'd', 'e']
```



#### Pop by index



{:.input_area}
```
letters.pop(2)
letters
```





{:.output .output_data_text}
```
['a', 'b', 'd', 'e']
```



#### Remove specific item



{:.input_area}
```
letters.remove('d')
letters
```





{:.output .output_data_text}
```
['a', 'b', 'e']
```



### Create tuple using brackets



{:.input_area}
```
tup = (1, 2, 3)
tup
```





{:.output .output_data_text}
```
(1, 2, 3)
```



### Create tuple with commas



{:.input_area}
```
tup = 1, 2, 3
tup
```





{:.output .output_data_text}
```
(1, 2, 3)
```



### Create empty tuple



{:.input_area}
```
tup = ()
tup
```





{:.output .output_data_text}
```
()
```



### Create tuple with single item



{:.input_area}
```
tup = 1,
tup
```





{:.output .output_data_text}
```
(1,)
```



### Behaviours shared by lists and tuples
The following sequence behaviors are shared by lists and tuples

### Check item in sequence



{:.input_area}
```
3 in (1, 2, 3, 4, 5)
```





{:.output .output_data_text}
```
True
```



### Check item not in sequence



{:.input_area}
```
'a' not in [1, 2, 3, 4, 5]
```





{:.output .output_data_text}
```
True
```



### Slicing

#### Setting start, slice to the end



{:.input_area}
```
letters = 'a', 'b', 'c', 'd', 'e', 'f'
letters[3:4]

```





{:.output .output_data_text}
```
('d',)
```



#### Set end, slice from beginning



{:.input_area}
```
letters[:4]
```





{:.output .output_data_text}
```
('a', 'b', 'c', 'd')
```



#### Index from end of sequence



{:.input_area}
```
letters[-4:]
```





{:.output .output_data_text}
```
('c', 'd', 'e', 'f')
```



#### Setting step



{:.input_area}
```
letters[1::-2]
```





{:.output .output_data_text}
```
('b',)
```



### Unpacking



{:.input_area}
```
first, middle = [1, 2, 3]

f"first = {first},  middle = {middle},  last = {last}"
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-38-c24a37f354b9> in <module>()
    ----> 1 first, middle = [1, 2, 3]
          2 
          3 f"first = {first},  middle = {middle},  last = {last}"


    ValueError: too many values to unpack (expected 2)


```

### Extended unpacking



{:.input_area}
```
first, *middle, last = (1, 2, 3, 4, 5)

f"first = {first},  middle = {middle},  last = {last}"
```





{:.output .output_data_text}
```
'first = 1,  middle = [2, 3, 4],  last = 5'
```



### Using list as Stack
A stack is a LIFO (last in, first out) data structure which can be simulated using a list

#### Push onto the stack using append



{:.input_area}
```
stack = []
stack.append('first on')
stack.append('second on')
stack.append('third on')
stack
```





{:.output .output_data_text}
```
['first on', 'second on', 'third on']
```



#### Retrieve items, last one first using **pop**



{:.input_area}
```
f"Retrieved first: {stack.pop()!r}, retrieved second: {stack.pop()!r}, retrieved last: {stack.pop()!r}"
```





{:.output .output_data_text}
```
"Retrieved first: 'third on', retrieved second: 'second on', retrieved last: 'first on'"
```



## 5.2 Explore dictionaries
Dictionaries are mappings of key value pairs.

### Create an empty dict using constructor



{:.input_area}
```
dictionary = {}
dictionary
```





{:.output .output_data_text}
```
{}
```



### Create a dictionary based on key/value pairs



{:.input_area}
```
key_values = [['key-1','value-1'], ['key-2', 'value-2']]
dictionary = dict(key_values)
dictionary
```





{:.output .output_data_text}
```
{'key-1': 'value-1', 'key-2': 'value-2'}
```



### Create an empty dict using curley braces



{:.input_area}
```
dictionary = {}
dictionary
```





{:.output .output_data_text}
```
{}
```



### Use curley braces to create a dictionary with initial key/values



{:.input_area}
```
dictionary = {'key-1': 'value-1',
              'key-2': 'value-2'}

dictionary
```





{:.output .output_data_text}
```
{'key-1': 'value-1', 'key-2': 'value-2'}
```



### Access value using key



{:.input_area}
```
dictionary['key-1']
```





{:.output .output_data_text}
```
'value-1'
```



### Add a key/value pair to an existing dictionary



{:.input_area}
```
dictionary['key-3'] = 'value-3'

dictionary
```





{:.output .output_data_text}
```
{'key-1': 'value-1', 'key-2': 'value-2', 'key-3': 'value-3'}
```



### Update value for existing key



{:.input_area}
```
dictionary['key-2'] = 'new-value-2'
dictionary['key-2']
```





{:.output .output_data_text}
```
'new-value-2'
```



### Get keys



{:.input_area}
```
list(dictionary.keys())
```





{:.output .output_data_text}
```
['key-1', 'key-2', 'key-3']
```



### Get values



{:.input_area}
```
dictionary.values()
```





{:.output .output_data_text}
```
dict_values(['value-1', 'new-value-2', 'value-3'])
```



### Get iterable keys and items



{:.input_area}
```
dictionary.items()
```





{:.output .output_data_text}
```
dict_items([('key-1', 'value-1'), ('key-2', 'new-value-2'), ('key-3', 'value-3')])
```



### Use items in for loop



{:.input_area}
```
for key, value in dictionary.items():
  print(f"{key}: {value}")
```


{:.output .output_stream}
```
key-1: value-1
key-2: new-value-2
key-3: value-3

```

### Check if dictionary has key
The 'in' syntax we used with sequences checks the dicts keys for membership.



{:.input_area}
```
'key-5' in dictionary
```





{:.output .output_data_text}
```
False
```



### Get method



{:.input_area}
```
dictionary.get("bad key", "default value")
```





{:.output .output_data_text}
```
'default value'
```



### Remove item



{:.input_area}
```
del(dictionary['key-1'])
dictionary
```





{:.output .output_data_text}
```
{'key-2': 'new-value-2', 'key-3': 'value-3'}
```



### Keys must be immutable

#### List as key
Lists are mutable and not hashable



{:.input_area}
```
items = ['item-1', 'item-2', 'item-3']

map = {}

map[items] = "some-value"
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-66-25faa77a670a> in <module>()
          3 map = {}
          4 
    ----> 5 map[items] = "some-value"
    

    TypeError: unhashable type: 'list'


```

#### Tuple as a key
Tuples are immutable and hence hashable



{:.input_area}
```
items = 'item-1', 'item-2', 'item-3'
map = {}
map[items] = "some-value"

map
```





{:.output .output_data_text}
```
{('item-1', 'item-2', 'item-3'): 'some-value'}
```



## 5.3 Dive into sets

### Create set from tuple or list



{:.input_area}
```
letters = 'a', 'a', 'a', 'b', 'c'
unique_letters = set(letters)
unique_letters
```





{:.output .output_data_text}
```
{'a', 'b', 'c'}
```



### Create set from a string



{:.input_area}
```
unique_chars = set('mississippi')
unique_chars
```





{:.output .output_data_text}
```
{'i', 'm', 'p', 's'}
```



### Create set using curley braces



{:.input_area}
```
unique_num = {1, 1, 2, 3, 4, 5, 5}
unique_num
```





{:.output .output_data_text}
```
{1, 2, 3, 4, 5}
```



### Adding to a set



{:.input_area}
```
unique_num.add(6)
unique_num
```





{:.output .output_data_text}
```
{1, 2, 3, 4, 5, 6}
```



### Popping from a set
Pop method removes and returns a random element of the set



{:.input_area}
```
unique_num.pop()
```





{:.output .output_data_text}
```
2
```



### Indexing
Sets have no order, and hence cannot be accessed via indexing



{:.input_area}
```
unique_num[4]
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-75-c928415e5703> in <module>()
    ----> 1 unique_num[4]
    

    TypeError: 'set' object does not support indexing


```

### Checking membership



{:.input_area}
```
3 in unique_num
```





{:.output .output_data_text}
```
True
```



### Set operations



{:.input_area}
```
s1 = { 1 ,2 ,3 ,4, 5, 6, 7}
s2 = { 0, 2, 4, 6, 8 }
```


#### Items in first set, but not in the second



{:.input_area}
```
s1 - s2
```





{:.output .output_data_text}
```
{1, 3, 5, 7}
```



#### Items in either or both sets



{:.input_area}
```
s1 | s2
```





{:.output .output_data_text}
```
{0, 1, 2, 3, 4, 5, 6, 7, 8}
```



#### Items in both sets



{:.input_area}
```
s1 & s2
```





{:.output .output_data_text}
```
{2, 4, 6}
```



#### Items in either set, but not both



{:.input_area}
```
s1 ^ s2
```





{:.output .output_data_text}
```
{0, 1, 3, 5, 7, 8}
```



## 5.4 Work with the numpy array


Numpy is an opened source numerical computing libary for python. The numpy array is a datastructure representing multidimension arrays which is optimized for both memory and performance.

### Create a numpy array from a list of lists



{:.input_area}
```
import numpy as np
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

np_array = np.array(list_of_lists)

np_array
```





{:.output .output_data_text}
```
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
```



### Initialize an array of zeros



{:.input_area}
```
zeros_array = np.zeros( (4, 5) )
zeros_array
```





{:.output .output_data_text}
```
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
```



### Initialize and array of ones



{:.input_area}
```
ones_array = np.ones( (6, 6) )
ones_array
```





{:.output .output_data_text}
```
array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.]])
```



### Using arrange



{:.input_area}
```
nine = np.arange( 9 )
nine
```





{:.output .output_data_text}
```
array([0, 1, 2, 3, 4, 5, 6, 7, 8])
```



### Using reshape



{:.input_area}
```
nine.reshape(3,3)
```





{:.output .output_data_text}
```
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```



### Introspection

#### Get the data type



{:.input_area}
```
np_array.dtype
```





{:.output .output_data_text}
```
dtype('int64')
```



#### Get the array's shape



{:.input_area}
```
np_array.shape
```





{:.output .output_data_text}
```
(4, 4)
```



#### Get the number of items in the array



{:.input_area}
```
np_array.size
```





{:.output .output_data_text}
```
16
```



#### Get the size of the array in bytes



{:.input_area}
```
np_array.nbytes
```





{:.output .output_data_text}
```
128
```



### Setting the data type

#### dtype parameter



{:.input_area}
```
np_array = np.array(list_of_lists, dtype=np.int8)
np_array
```





{:.output .output_data_text}
```
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]], dtype=int8)
```



#### Size reduction



{:.input_area}
```
np_array.nbytes
```





{:.output .output_data_text}
```
16
```



#### The data type setting is immutible
Data may be truncated if the data type is restrictive.



{:.input_area}
```
np_array[0][0] = 1.7344567
np_array[0][0]
```





{:.output .output_data_text}
```
1
```



### Array Slicing


*   Slicing can be used to get a view reprsenting a sub-array. 
*   The slice is a view to the original array, the data is not copied to a new data structure
*   The slice is taken in the form: array[ rows, columns ]








{:.input_area}
```
np_array
```





{:.output .output_data_text}
```
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]], dtype=int8)
```





{:.input_area}
```
np_array[2:, :3]
```





{:.output .output_data_text}
```
array([[ 9, 10, 11],
       [13, 14, 15]], dtype=int8)
```



### Math operations


*   Unlike a unlike nested lists, matrix operations perform mathimatical operations on data



#### Create two 3 x 3 arrays



{:.input_area}
```
np_array_1 = np.arange(9).reshape(3,3)
np_array_1

```





{:.output .output_data_text}
```
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```





{:.input_area}
```
np_array_2 = np.arange(10, 19).reshape(3,3)
np_array_2
```





{:.output .output_data_text}
```
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
```



#### Multiply the arrays



{:.input_area}
```
np_array_1 * np_array_2
```





{:.output .output_data_text}
```
array([[  0,  11,  24],
       [ 39,  56,  75],
       [ 96, 119, 144]])
```



#### Add the arrays



{:.input_area}
```
np_array_1 + np_array_2
```





{:.output .output_data_text}
```
array([[10, 12, 14],
       [16, 18, 20],
       [22, 24, 26]])
```



### Matrix operations

#### Transpose



{:.input_area}
```
np_array.T
```





{:.output .output_data_text}
```
array([[ 1,  5,  9, 13],
       [ 2,  6, 10, 14],
       [ 3,  7, 11, 15],
       [ 4,  8, 12, 16]], dtype=int8)
```



#### Dot product



{:.input_area}
```
np_array_1.dot(np_array_2)

```





{:.output .output_data_text}
```
array([[ 45,  48,  51],
       [162, 174, 186],
       [279, 300, 321]])
```



## 5.5 Use the Pandas DataFrame
*   One of the most highly leveraged data structures for data science
*   A table-like two dimensional data structure. 


### Create a DataFrame



{:.input_area}
```
import pandas as pd
first_names = ['henry', 'rolly', 'molly', 'frank', 'david', 'steven', 'gwen', 'arthur']
last_names = ['smith', 'brocker', 'stein', 'bach', 'spencer', 'de wilde', 'mason', 'davis']
ages = [43, 23, 78, 56, 26, 14, 46, 92]

df = pd.DataFrame({ 'first': first_names, 'last': last_names, 'age': ages})
df
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
      <th>age</th>
      <th>first</th>
      <th>last</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>43</td>
      <td>henry</td>
      <td>smith</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>rolly</td>
      <td>brocker</td>
    </tr>
    <tr>
      <th>2</th>
      <td>78</td>
      <td>molly</td>
      <td>stein</td>
    </tr>
    <tr>
      <th>3</th>
      <td>56</td>
      <td>frank</td>
      <td>bach</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26</td>
      <td>david</td>
      <td>spencer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>14</td>
      <td>steven</td>
      <td>de wilde</td>
    </tr>
    <tr>
      <th>6</th>
      <td>46</td>
      <td>gwen</td>
      <td>mason</td>
    </tr>
    <tr>
      <th>7</th>
      <td>92</td>
      <td>arthur</td>
      <td>davis</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Head - looking at the top



{:.input_area}
```
df.head(10)
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
      <th>age</th>
      <th>first</th>
      <th>last</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>43</td>
      <td>henry</td>
      <td>smith</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>rolly</td>
      <td>brocker</td>
    </tr>
    <tr>
      <th>2</th>
      <td>78</td>
      <td>molly</td>
      <td>stein</td>
    </tr>
    <tr>
      <th>3</th>
      <td>56</td>
      <td>frank</td>
      <td>bach</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26</td>
      <td>david</td>
      <td>spencer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>14</td>
      <td>steven</td>
      <td>de wilde</td>
    </tr>
    <tr>
      <th>6</th>
      <td>46</td>
      <td>gwen</td>
      <td>mason</td>
    </tr>
    <tr>
      <th>7</th>
      <td>92</td>
      <td>arthur</td>
      <td>davis</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Setting number of rows returned with head



{:.input_area}
```
df.head(3)
```


### Tail - looking at the bottom



{:.input_area}
```
df.tail(2)
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
      <th>age</th>
      <th>first</th>
      <th>last</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>46</td>
      <td>gwen</td>
      <td>mason</td>
    </tr>
    <tr>
      <th>7</th>
      <td>92</td>
      <td>arthur</td>
      <td>davis</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Describe - descriptive statistics



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
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>47.250000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>27.227874</td>
    </tr>
    <tr>
      <th>min</th>
      <td>14.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>25.250000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>44.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>61.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>92.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Access one column



{:.input_area}
```
df['first']
```





{:.output .output_data_text}
```
0     henry
1     rolly
2     molly
3     frank
4     david
5    steven
6      gwen
7    arthur
Name: first, dtype: object
```



### Slice a column



{:.input_area}
```
df['first'][4:]
```





{:.output .output_data_text}
```
4     david
5    steven
6      gwen
7    arthur
Name: first, dtype: object
```



### Use conditions to filter



{:.input_area}
```
df[df['age'] > 50]
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
      <th>age</th>
      <th>first</th>
      <th>last</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>78</td>
      <td>molly</td>
      <td>stein</td>
    </tr>
    <tr>
      <th>3</th>
      <td>56</td>
      <td>frank</td>
      <td>bach</td>
    </tr>
    <tr>
      <th>7</th>
      <td>92</td>
      <td>arthur</td>
      <td>davis</td>
    </tr>
  </tbody>
</table>
</div>
</div>



## 5.6 Use the pandas Series


*   A one dimensional labeled array
*   Contains data of only one type
*   Similar to a column in a spreedsheet




### Create a series



{:.input_area}
```
pd_series = pd.Series( [1, 2, 3 ] )
pd_series
```





{:.output .output_data_text}
```
0    1
1    2
2    3
dtype: int64
```



### Series introspection methods



{:.input_area}
```
f"This series is made up of {pd_series.size} items whose data type is {pd_series.dtype}"
```





{:.output .output_data_text}
```
'This series is made up of 3 items whose data type is int64'
```



### A Pandas DataFrame is composed of Pandas Series.



{:.input_area}
```
age = df.age
type( age )
```





{:.output .output_data_text}
```
pandas.core.series.Series
```



### Some useful helper methods of a Series

#### mean



{:.input_area}
```
pd_series = pd.Series([ 1, 2, 3, 5, 6, 6, 6, 7, 8])
pd_series.mean()
```





{:.output .output_data_text}
```
4.888888888888889
```



#### Unique



{:.input_area}
```
pd_series.unique()
```





{:.output .output_data_text}
```
array([1, 2, 3, 5, 6, 7, 8])
```



#### Max



{:.input_area}
```
pd_series.min()
```





{:.output .output_data_text}
```
1
```



# Notes:
[Lists](https://docs.python.org/3/tutorial/datastructures.html)

[Tuples and sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

[Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

[Numpy arrays](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)

[Pandas DataFrame](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html)

[Pandas Series](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.Series.html)


