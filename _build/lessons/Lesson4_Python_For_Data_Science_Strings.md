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

## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 4.1 Use string methods



### String Quoting

#### Single quotes



{:.input_area}
```
'Here is a string'
```





{:.output .output_data_text}
```
'Here is a string'
```



#### Double quotes



{:.input_area}
```
"Here is a string" == 'Here is a string'
```





{:.output .output_data_text}
```
True
```



#### Triple Strings



{:.input_area}
```
a_very_large_phrase = """
Wikipedia is hosted by the Wikimedia Foundation, 
a non-profit organization that also hosts a range of other projects.
"""

print(a_very_large_phrase)
```


{:.output .output_stream}
```

Wikipedia is hosted by the Wikimedia Foundation, 
a non-profit organization that also hosts a range of other projects.


```

#### Raw Strings



{:.input_area}
```
jon_jones = '...wrote on twitter he is the greatest "heavyw8e! \nfighter of all time'
print(jon_jones)
```


{:.output .output_stream}
```
...wrote on twitter he is the greatest "heavyw8e! 
fighter of all time

```



{:.input_area}
```
jon_jones = r'...wrote on twitter he is the greatest "heavyw8e! \nfighter of all time'
print(jon_jones)
```


{:.output .output_stream}
```
...wrote on twitter he is the greatest "heavyw8e! \nfighter of all time

```

### Case Manipulation



{:.input_area}
```
captain = "Patrick Tayluer"

captain
```





{:.output .output_data_text}
```
'Patrick Tayluer'
```





{:.input_area}
```
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
captain.upper()
```





{:.output .output_data_text}
```
'PATRICK TAYLUER'
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
captain = 'patrick tayluer'
captain.title()
```





{:.output .output_data_text}
```
'Patrick Tayluer'
```



### Interrogation



{:.input_area}
```
river = 'Mississippi'

```




{:.input_area}
```
len(river)
```





{:.output .output_data_text}
```
11
```





{:.input_area}
```
river.count('s')
```





{:.output .output_data_text}
```
4
```





{:.input_area}
```
river.index('pp')
```





{:.output .output_data_text}
```
8
```





{:.input_area}
```
river.index('r')
```


{:.output .output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-67-fcd85454de2b> in <module>()
    ----> 1 river.index('r')
    

    ValueError: substring not found


```



{:.input_area}
```
river.find('r')
```





{:.output .output_data_text}
```
-1
```





{:.input_area}
```
river.startswith('M')
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
river.endswith('i')
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
'sip' in river
```





{:.output .output_data_text}
```
True
```



### Content Type



{:.input_area}
```
'abc123'.isalpha()
```





{:.output .output_data_text}
```
False
```





{:.input_area}
```
'abc123'.isalnum()
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
'lowercase'.islower()
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
'lowercase'.isupper()
```





{:.output .output_data_text}
```
False
```





{:.input_area}
```
'The Good Ship'.istitle()
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
'The bad seed'.istitle()
```





{:.output .output_data_text}
```
False
```



More information: [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## 4.2 Format strings
F-strings where introduced in Python 3.6. They prefixed by either a 'F' or 'f' before the beginning quotation mark. Values can be inserted into F-strings at runtime using replacement fields which are deliminated by curly braces.

### Insert variable into replacement field



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



### Insert expression into replacement field



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



### Index list in string replacement fields



{:.input_area}
```
players = ["Tony Trischka", "Bill Evans", "Alan Munde"]
f"Performances will be held by {players[1]}, {players[0]}, and {players[2]}"
```





{:.output .output_data_text}
```
'Performances will be held by Bill Evans, Tony Trischka, and Alan Munde'
```



### Conversion flags
A conversion flag can be specified to convert the type of the value before formatting. The three available flags are 's', 'r' and 'a'.

#### Using str conversion



{:.input_area}
```
nuts = [1,2,3,4,5]
f"Calling str() on a the list {nuts} produces {nuts!s}"
```





{:.output .output_data_text}
```
'Calling str() on a the list [1, 2, 3, 4, 5] produces [1, 2, 3, 4, 5]'
```



#### Using repr conversiont



{:.input_area}
```
nut = 'pistacio'
f"Calling repr on the string {nut} results in {nut!r}"
```





{:.output .output_data_text}
```
"Calling repr on the string pistacio results in 'pistacio'"
```



#### Using ascii conversion



{:.input_area}
```
check = "√"
f"The ascii version of {check} is {check!a}"
```





{:.output .output_data_text}
```
"The ascii version of √ is '\\u221a'"
```



### Padding a number



{:.input_area}
```
lucky_num = 13
f"To pad the number {lucky_num} to 5 places:{lucky_num:5d}"
```





{:.output .output_data_text}
```
'To pad the number 13 to 5 places:   13'
```



### Setting padding value at runtime



{:.input_area}
```
luckey_num = 13
padding = 5
f"To pad the number {lucky_num} to {padding} places:{lucky_num:{padding}d}"
```





{:.output .output_data_text}
```
'To pad the number 13 to 5 places:   13'
```



More information: [Format String Syntax](https://docs.python.org/2/library/string.html#format-string-syntax)

Other String Formatting: 
  [String Format Method](https://docs.python.org/2/library/string.html#custom-string-formatting)
  
  [Old Style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)

## 4.3 Manipulate strings

### Concatenation



{:.input_area}
```
"Bob" + "beroo"
```





{:.output .output_data_text}
```
'Bobberoo'
```





{:.input_area}
```
"AB" * 8
```





{:.output .output_data_text}
```
'ABABABABABABABAB'
```



### Remove Whitespace



{:.input_area}
```
ship = " The Yankee Clipper "
ship
```





{:.output .output_data_text}
```
' The Yankee Clipper '
```





{:.input_area}
```
ship.strip()
```





{:.output .output_data_text}
```
'The Yankee Clipper'
```





{:.input_area}
```
ship.lstrip()
```





{:.output .output_data_text}
```
'The Yankee Clipper '
```





{:.input_area}
```
ship.rstrip()
```





{:.output .output_data_text}
```
' The Yankee Clipper'
```





{:.input_area}
```
ship.rstrip("per ")
```





{:.output .output_data_text}
```
' The Yankee Cli'
```



### Add padding



{:.input_area}
```
port = "Boston"
```




{:.input_area}
```
port.center(12, '*')
```





{:.output .output_data_text}
```
'***Boston***'
```





{:.input_area}
```
port.ljust(12, '*')
```





{:.output .output_data_text}
```
'Boston******'
```





{:.input_area}
```
port.rjust(12, '*')
```





{:.output .output_data_text}
```
'******Boston'
```





{:.input_area}
```
for port_city in ['Liverpool', 'Boston', 'New York', 'Philadelphia']:
  print(port_city.rjust(12))
```


{:.output .output_stream}
```
   Liverpool
      Boston
    New York
Philadelphia

```



{:.input_area}
```
'-5'.zfill(4)
```





{:.output .output_data_text}
```
'-005'
```



### Replace



{:.input_area}
```
"FILADELFIA".replace("F", "PH")
```





{:.output .output_data_text}
```
'PHILADELPHIA'
```



### Spitting and Joining



{:.input_area}
```
words_string = "Here,Are,Some,Words"
words_string
```





{:.output .output_data_text}
```
'Here,Are,Some,Words'
```



#### Split on comma



{:.input_area}
```
words = words_string.split(',')
words
```





{:.output .output_data_text}
```
['Here', 'Are', 'Some', 'Words']
```



#### Joining



{:.input_area}
```
':'.join(words)
```





{:.output .output_data_text}
```
'Here:Are:Some:Words'
```



#### Split on newline



{:.input_area}
```
multiline = "Sometimes we are given\na multiline document\nas a single string"
multiline
```





{:.output .output_data_text}
```
'Sometimes we are given\na multiline document\nas a single string'
```





{:.input_area}
```
for line in multiline.splitlines():
  print(line)
```


{:.output .output_stream}
```
Sometimes we are given
a multiline document
as a single string

```

### Slicing



{:.input_area}
```
collector = "William Main Doerflinger"
collector[0]
```





{:.output .output_data_text}
```
'W'
```





{:.input_area}
```
collector[-1]
```





{:.output .output_data_text}
```
'r'
```





{:.input_area}
```
collector[13:18]
```





{:.output .output_data_text}
```
'Doerf'
```





{:.input_area}
```
collector[-7:]
```





{:.output .output_data_text}
```
'flinger'
```



More information: [common sequence operations](https://docs.python.org/3/library/stdtypes.html#typesseq-common)


## 4.4 Learn to use unicode
There are multiple encoding possible for mapping characters to bytes. Python strings default to UTF-8. Earlier versions of Python used a more limited encoding.

### Encode



{:.input_area}
```
twice_pie = 'ππ'
twice_pie
```





{:.output .output_data_text}
```
'ππ'
```





{:.input_area}
```
twice_π = twice_pie
twice_π
```





{:.output .output_data_text}
```
'ππ'
```





{:.input_area}
```
pie = "\N{GREEK CAPITAL LETTER PI}"
pie
```





{:.output .output_data_text}
```
'Π'
```





{:.input_area}
```
ord(pie)
```





{:.output .output_data_text}
```
928
```





{:.input_area}
```
chr(928)
```





{:.output .output_data_text}
```
'Π'
```





{:.input_area}
```
u = chr(40960) + 'abcd' + chr(1972)
u.encode('utf-8')
u
```





{:.output .output_data_text}
```
'ꀀabcd\u07b4'
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


