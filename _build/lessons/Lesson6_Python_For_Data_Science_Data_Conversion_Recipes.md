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

## 6.1 Convert lists to dicts, and dicts to lists

### Converting Lists to Dictionaries

#### Create basic dictionary



{:.input_area}
```
d = dict( [('one', 1), ('two', 2), ('three', 3)] )
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





{:.output .output_data_text}
```
{'accordian': 'Astor Pantaleón Piazzolla',
 'banjo': 'Noam Pikelny',
 'lute': 'Julian Bream',
 'violin': 'Anne-Sophie Mutter'}
```



#### From keys



{:.input_area}
```
racers = ['Tom', 'Bill', 'Will', 'Jill']
start_distance = 0
d = dict.fromkeys(racers, start_distance)
d
```





{:.output .output_data_text}
```
{'Bill': 0, 'Jill': 0, 'Tom': 0, 'Will': 0}
```



### Converting Dictionaries to  Lists



{:.input_area}
```
d = {'name': 'toby', 'id' : 14}
print( list(d) )
print( sorted(d) )
print( list(d.values()) )
```


{:.output .output_stream}
```
['name', 'id']
['id', 'name']
['toby', 14]

```

## 6.2 Convert dicts to pandas Dataframe

### Create dict from DataFrame



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
      <th>0</th>
      <th>1</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Edward</td>
      <td>Robert</td>
      <td>Earl</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tudor</td>
      <td>Redford</td>
      <td>Scruggs</td>
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





{:.input_area}
```
d = {'a': 'A', 'b': 'B', 'c': 'C'}
df = DataFrame(list(d.items()), columns=['lower', 'upper'])
print(df)
#Dataframe.from_record
```


{:.output .output_stream}
```
  lower upper
0     a     A
1     b     B
2     c     C

```

## 6.3 Convert characters to integers and back



{:.input_area}
```
print( float('12.3'))
# Casting to int
print( int('011') )
print( int('011', 2) )
print( int('011', 6) )
print( int('011', 6) )
print( int('011', 2) )
print( int('011', 8) ) 
print( int('011', 16) )
```


{:.output .output_stream}
```
12.3
11
3
7
7
3
9
17
161

```



{:.input_area}
```
one = str(1)
print( type(one) )
f"{one!r} is a string"
```


{:.output .output_stream}
```
<class 'str'>

```




{:.output .output_data_text}
```
"'1' is a string"
```





{:.input_area}
```
# ascii codes
```


## 6.4 Convert between hexadecimal, binary, and floats

### Conversion to and from Floats




{:.input_area}
```

a_float = str(12.4)
print( f" {a_float!r} is a {type(a_float)}" )

a_float = float(a_float)
print( f" {a_float!r} is a {type(a_float)}" )



```


{:.output .output_stream}
```
 '12.4' is a <class 'str'>
 12.4 is a <class 'float'>

```

### Hexadecimal



{:.input_area}
```
nt_hex = hex(18)
print( f" hex(18) returns the {type(int_hex)}: {int_hex!r}" )

float_hex = 12.4.hex()
print( f" 12.4.hex() returns the {type(float_hex)}: {float_hex!r}" )
```


{:.output .output_stream}
```
 hex(18) returns the <class 'str'>: '0x12'
 12.4.hex() returns the <class 'str'>: '0x1.8cccccccccccdp+3'

```

[hex function](https://docs.python.org/3/library/functions.html)

### Conversion to and from binary



{:.input_area}
```
import base64
bytes_str = b"Encode this string"
encoded_str = base64.b64encode(bytes_str)
print( encoded_str )

print( base64.b64decode(encoded_str))
```


{:.output .output_stream}
```
b'RW5jb2RlIHRoaXMgc3RyaW5n'
b'Encode this string'

```

[base64-module](https://docs.python.org/3/library/base64.html#module-base64)

# Notes
- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [More on  lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Dataframe.from_dict](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.from_dict.html)
- https://stackoverflow.com/questions/4576115/convert-a-list-to-a-dictionary-in-python
- https://thispointer.com/python-how-to-convert-a-list-to-dictionary/

