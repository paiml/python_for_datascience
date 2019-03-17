---
redirect_from:
  - "/lessons/lesson4-python-for-data-science-strings"
interact_link: content/lessons/Lesson4_Python_For_Data_Science_Strings.ipynb
kernel_name: python3
title: 'Lesson 4 - Strings'
prev_page:
  url: /lessons/Lesson3_Python_For_Data_Science_Basics
  title: 'Lesson 3 - Basics'
next_page:
  url: /lessons/Lesson5_Python_For_Data_Science_Python_Data_structure
  title: 'Lesson 5 - Data Structures'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson4_Python_For_Data_Science_Strings.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 4 Strings

## 4.1 Use string methods



### Case Manipulation



{:.input_area}
```
captain = "Patrick Tayluer"
captain.capitalize()

```





{:.output .output_data_text}
```
'Patrick tayluer'
```





{:.input_area}
```
captain.lower()
```





{:.output .output_data_text}
```
'patrick tayluer'
```





{:.input_area}
```
captain.swapcase()
```





{:.output .output_data_text}
```
'pATRICK tAYLUER'
```





{:.input_area}
```
captain.title()
```





{:.output .output_data_text}
```
'Patrick Tayluer'
```





{:.input_area}
```
captain.upper()
```





{:.output .output_data_text}
```
'PATRICK TAYLUER'
```





{:.input_area}
```


```


#### Remove Whitespace



{:.input_area}
```
ship = " The Yankee Clipper "
ship
```




{:.input_area}
```
ship.strip()
```




{:.input_area}
```
ship.rstrip()
```




{:.input_area}
```
ship.lstrip()
```


### Content Manipulation



{:.input_area}
```
port = "Boston"
port.center(12, '*')
```




{:.input_area}
```
port.ljust(12)
```




{:.input_area}
```
port.rjust(12)
```




{:.input_area}
```
for port_city in ['Liverpool', 'Boston', 'New York', 'Philadelphia']:
  print(port_city.rjust(12))
```




{:.input_area}
```
"FILADELFIA".replace("F", "PH")
```




{:.input_area}
```
'-5'.zfill(3)
```


#### Spitting and Joining



{:.input_area}
```
words_string = "Here,Are,Some,Words"
words_string
```




{:.input_area}
```
words = words_string.split(',')
words
```




{:.input_area}
```
' '.join(words)
```




{:.input_area}
```
multiline = "Sometimes we are given\na multiline document\nas a single string"
multiline
```




{:.input_area}
```
for line in multiline.splitlines():
  print(line)
```


#### Interrogation



{:.input_area}
```
river = 'Mississippi'
river.count('s')
```




{:.input_area}
```
river.index('pp')
```




{:.input_area}
```
river.index('r')
```




{:.input_area}
```
river.find('r')
```




{:.input_area}
```
river.startswith('M')
```




{:.input_area}
```
river.endswith('i')
```


#### Content Type



{:.input_area}
```
'abc123'.isalpha()
```




{:.input_area}
```
'abc123'.isalnum()
```




{:.input_area}
```
'lowercase'.islower()
```




{:.input_area}
```
'lowercase'.isupper()
```




{:.input_area}
```
'The Good Ship'.istitle()
```




{:.input_area}
```
'The bad seed'.istitle()
```


More information: [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## 4.2 Format strings

### F-Strings



{:.input_area}
```
strings_count = 5
frets_count = 24
f"Noam Pikelny's banjo has {strings_count} strings and {frets_count} frets"
```





{:.output .output_data_text}
```
"Noam Pikelny's banjo has 5 strings and 24 frets"
```






{:.output .output_data_text}
```
"Noam Pikelny's banjo has 5 strings and 24 frets"
```





{:.input_area}
```
a = 12
b = 32
f"{a} times {b} equals {a*b}"
```





{:.output .output_data_text}
```
'12 times 32 equals 384'
```





{:.input_area}
```
players = ["Tony Trischka", "Bill Evans", "Alan Munde"]
f"Performances will be held by {players[1]}, {players[0]}, and {players[2]}"
```





{:.output .output_data_text}
```
'Performances will be held by Bill Evans, Tony Trischka, and Alan Munde'
```





{:.input_area}
```
nut = 'pistacio'
f"Calling repr on the string {nut} results in {nut!r}"
```




{:.input_area}
```
check = "√"
f"The ascii version of {check} is {check!a}"
```




{:.input_area}
```
some_num = 34
padding = 5
f"To pad the number {some_num} to {padding} places:{some_num:{padding}d}"
```


More information: [Format String Syntax](https://docs.python.org/2/library/string.html#format-string-syntax)

Other String Formatting: 
  [String Format Method](https://docs.python.org/2/library/string.html#custom-string-formatting)
  
  [Old Style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)

### String Quoting

#### Triple Strings



{:.input_area}
```
a_very_large_phrase = """
Wikipedia is hosted by the Wikimedia Foundation, 
a non-profit organization that also hosts a range of other projects.
"""

```


#### Raw Strings



{:.input_area}
```
jon_jones = r'...wrote on twitter he is the greatest "heavyw8e! fighter of all time'
jon_jones
```





{:.output .output_data_text}
```
'...wrote on twitter he is the greatest "heavyw8e! fighter of all time'
```



### Replacing



{:.input_area}
```
a_very_large_phrase

```





{:.output .output_data_text}
```
'\nWikipedia is hosted by the Wikimedia Foundation, \na non-profit organization that also hosts a range of other projects.\n'
```





{:.input_area}
```
a_very_large_phrase.replace("\n", "")
```





{:.output .output_data_text}
```
'Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects.'
```



### Stripping



{:.input_area}
```
annoying_text = "A half-formed sent"
annoying_text.rstrip(" sent")
```





{:.output .output_data_text}
```
'A half-formed'
```



### Splitting



{:.input_area}
```
shopping_list = "Carrots, apples, oranges"
shopping_list.split(",")
```





{:.output .output_data_text}
```
['Carrots', ' apples', ' oranges']
```



## 4.3 Manipulate strings

### Membership



{:.input_area}
```
'Rob' in "Robert Henry Wonderson"
```




{:.input_area}
```
"Bob" not in "Robert Henry Wonderson"
```


### Concatenation



{:.input_area}
```
"Bob" + "beroo"
```




{:.input_area}
```
"AB" * 8
```


### Slicing



{:.input_area}
```
collector = "William Main Doerflinger"
collector[0]
```




{:.input_area}
```
collector[-1]
```




{:.input_area}
```
collector[13:18]
```




{:.input_area}
```
collector[-7:]
```




{:.input_area}
```
len(collector)
```


More information: [common sequence operations](https://docs.python.org/3/library/stdtypes.html#typesseq-common)


## 4.4 Learn to use unicode

### Encode



{:.input_area}
```
# encode, casefold
twice_pie = 'ππ'
twice_pie
```




{:.input_area}
```
twice_π = twice_pie
twice_π
```




{:.input_area}
```
pie = "\N{GREEK CAPITAL LETTER PI}"
pie
```




{:.input_area}
```
ord(pie)
```




{:.input_area}
```
chr(928)
```




{:.input_area}
```
u = chr(40960) + 'abcd' + chr(1972)
u.encode('utf-8')
u
```


### Saving File in Unicode



{:.input_area}
```
with open("new_file.txt", "w", encoding='utf-8') as opened_file:
  opened_file.write("Søme Unˆcode text")
  
!cat new_file.txt
  
```


{:.output .output_stream}
```
Søme Unˆcode text
```

[Unicode](https://docs.python.org/3/howto/unicode.html)

## Notes


