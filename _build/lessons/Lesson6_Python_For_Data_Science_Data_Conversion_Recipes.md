---
redirect_from:
  - "/lessons/lesson6-python-for-data-science-data-conversion-recipes"
interact_link: content/lessons/Lesson6_Python_For_Data_Science_Data_Conversion_Recipes.ipynb
kernel_name: python3
title: 'Lesson 6 - Data Conversion Recipes'
prev_page:
  url: /lessons/Lesson5_Python_For_Data_Science_Python_Data_structure
  title: 'Lesson 5 - Data Structures'
next_page:
  url: /lessons/Lesson7_Python_For_Datascience_Execution_Control
  title: 'Lesson 7 - Execution Control'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson6_Python_For_Data_Science_Data_Conversion_Recipes.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 6: Data Conversion Recipes

## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 6.1 Convert lists to dicts, and dicts to lists

### Converting Lists to Dictionaries

#### Create basic dictionary



{:.input_area}
```
key_values = [('one', 1), ('two', 2), ('three', 3)]
d = dict( key_values )
d
```





{:.output .output_data_text}
```
{'one': 1, 'three': 3, 'two': 2}
```



#### Zip two lists



{:.input_area}
```
instruments = [ 'violin', 'lute', 'banjo', 'accordian']
players = [ 'Anne-Sophie Mutter', 'Julian Bream', 'Noam Pikelny', 'Astor Pantaleón Piazzolla']

d = dict(zip(instruments, players))
d
```


#### From keys



{:.input_area}
```
racers = ['Tom', 'Bill', 'Will', 'Jill']
start_distance = 0
d = dict.fromkeys(racers, start_distance)
d
```


### Converting Dictionaries to  Lists



{:.input_area}
```
d = {'name': 'toby', 'id' : 14}
```


#### Get a list of keys



{:.input_area}
```
list(d)
```


#### Get keys in sorted order



{:.input_area}
```
sorted(d)
```


#### Get list of values



{:.input_area}
```
list(d.values())
```


## 6.2 Convert dicts to pandas Dataframe

### Create DataFrame using data parameter



{:.input_area}
```
from pandas import DataFrame

d = {'first': ['Jill', 'Solma', 'Elizabeth'], 'last': ['Stein', 'Smith', 'Tudor']}
DataFrame(data=d)
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
      <th>first</th>
      <th>last</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jill</td>
      <td>Stein</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Solma</td>
      <td>Smith</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Elizabeth</td>
      <td>Tudor</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Use class from_dict method



{:.input_area}
```
DataFrame.from_dict(d)
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
      <th>first</th>
      <th>last</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jill</td>
      <td>Stein</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Solma</td>
      <td>Smith</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Elizabeth</td>
      <td>Tudor</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Create DataFrame with index orientation



{:.input_area}
```
d = {0: ['Edward', 'Tudor'], 1: ['Robert', 'Redford'], 3: ['Earl', 'Scruggs']}
df = DataFrame.from_dict(d, orient='index')
df.columns=['first', 'last']
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
      <th>first</th>
      <th>last</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Edward</td>
      <td>Tudor</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Robert</td>
      <td>Redford</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Earl</td>
      <td>Scruggs</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Assign column names



{:.input_area}
```
d = {'a': 'A', 'b': 'B', 'c': 'C'}
df = DataFrame(list(d.items()), columns=['lower', 'upper'])
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
      <th>lower</th>
      <th>upper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>
</div>



## 6.3 Convert characters to integers and back

### Cast str to int

#### Base 10



{:.input_area}
```
int('011')
```





{:.output .output_data_text}
```
11
```



#### Base 2



{:.input_area}
```
int('011', 2)
```





{:.output .output_data_text}
```
3
```



#### Base 6



{:.input_area}
```
int('011', 6)
```





{:.output .output_data_text}
```
7
```



#### Base 8



{:.input_area}
```
int('011', 8)
```





{:.output .output_data_text}
```
9
```



#### Base 16



{:.input_area}
```
int('011', 16)
```





{:.output .output_data_text}
```
17
```



### Cast int to string



{:.input_area}
```
one = str(1)
type(one)

```





{:.output .output_data_text}
```
str
```



## 6.4 Convert between hexadecimal, binary, and floats

### Cast to str from float




{:.input_area}
```
a_str = str(12.4)
f" {a_str!r} is a {type(a_str)}"
```





{:.output .output_data_text}
```
" '12.4' is a <class 'str'>"
```



### Cast to float from str



{:.input_area}
```
a_str = "12.3"
a_float = float(a_str)
f" {a_float!r} is a {type(a_float)}"
```





{:.output .output_data_text}
```
" 12.3 is a <class 'float'>"
```



### Hexadecimal

#### Int to hex str



{:.input_area}
```
int_hex = hex(18)
f" hex(18) returns the {type(int_hex)}: {int_hex!r}"

```





{:.output .output_data_text}
```
" hex(18) returns the <class 'str'>: '0x12'"
```



#### Float to hex str



{:.input_area}
```
float_hex = 12.0.hex()
f" 12.4.hex() returns the {type(float_hex)}: {float_hex!r}"
```





{:.output .output_data_text}
```
" 12.4.hex() returns the <class 'str'>: '0x1.8000000000000p+3'"
```



[hex function](https://docs.python.org/3/library/functions.html)

### Conversion to and from binary

#### Bytes literal
Similar to strings, but limited to ASCII characters.



{:.input_area}
```
bytes_str = b"some bytes literal"
type(bytes_str)
```





{:.output .output_data_text}
```
bytes
```



#### Encode to bytes



{:.input_area}
```
import base64
bytes_str = b"Encode this string"
encoded_str = base64.b64encode(bytes_str)
f"The encoded string {encoded_str!r} is of type {type(encoded_str)}"


```





{:.output .output_data_text}
```
"The encoded string b'RW5jb2RlIHRoaXMgc3RyaW5n' is of type <class 'bytes'>"
```



#### Decode from bytes



{:.input_area}
```
base64.b64decode(encoded_str)
```





{:.output .output_data_text}
```
b'Encode this string'
```



[base64-module](https://docs.python.org/3/library/base64.html#module-base64)

# Notes
- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [More on  lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Dataframe.from_dict](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.from_dict.html)
- https://stackoverflow.com/questions/4576115/convert-a-list-to-a-dictionary-in-python
- https://thispointer.com/python-how-to-convert-a-list-to-dictionary/

