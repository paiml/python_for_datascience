---
redirect_from:
  - "/lessons/lesson12-python-for-data-science-pattern-matching"
interact_link: content/lessons/Lesson12_Python_For_Data_Science_Pattern_Matching.ipynb
kernel_name: python3
title: 'Lesson 12 - Pattern Matching'
prev_page:
  url: /lessons/Lesson11_Python_For_Data_Science_Lazy_Evaluation
  title: 'Lesson 11 - Lazy Evaluation'
next_page:
  url: /lessons/Lesson13_Python_For_Data_Science_Sorting
  title: 'Lesson 13 - Sorting'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson12_Python_For_Data_Science_Pattern_Matching.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 12: Pattern Matching


## 12.1 Perform simple pattern matching




{:.input_area}
```
"sol" in "absolute"
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
'absolute'.startswith('ab')
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
'absolute'.endswith('lute')
```





{:.output .output_data_text}
```
True
```





{:.input_area}
```
'absolute'.find('sol')
```





{:.output .output_data_text}
```
2
```



## 12.2 Use regular expressions




{:.input_area}
```
# TDL SDL LN
text = '''
Ahab: ahab@pequod.com
Peleg: peleg@pequod.com
Ishmael: ishmael@pequod.com
Herman: herman@acushnet.io
Pollard: pollard@essex.me
'''
```


### Simple matching



{:.input_area}
```
import re


re.match("Ahab:", text )

```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(0, 5), match='Ahab:'>
```





{:.input_area}
```
if re.match("Ahab:", text ):
  print("We found Ahab")
```


{:.output .output_stream}
```
We found Ahab

```



{:.input_area}
```
if re.match("Peleg", text):
  print("We found Peleg")
else:
  print("No Peleg found!")
```


{:.output .output_stream}
```
No Peleg found!

```

### Search



{:.input_area}
```
if re.search("Peleg", text):
  print("We found Peleg")
else:
  print("No Peleg found!")
```


{:.output .output_stream}
```
We found Peleg

```

### Character sets



{:.input_area}
```
re.search("[A-Z][a-z]", text)
```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(0, 2), match='Ah'>
```





{:.input_area}
```
re.search("[A-Za-z]+", text)
```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(0, 4), match='Ahab'>
```





{:.input_area}
```
re.search("[A-Za-z]{7}", text)
```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(66, 73), match='Ishmael'>
```





{:.input_area}
```
re.search("[a-z]+\@[a-z]+\.[a-z]+", text)
```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(6, 21), match='ahab@pequod.com'>
```



### Character classes



{:.input_area}
```
re.search("\w\d\w", "His panic over Y2K was overwhelming.")
```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(15, 18), match='Y2K'>
```





{:.input_area}
```
re.search("\w+\@\w+\.\w+", text)
```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(6, 21), match='ahab@pequod.com'>
```



### Groups



{:.input_area}
```
m = re.search("(\w+)\@(\w+)\.(\w+)", text)
print(f'''
Group 0 is {m.group(0)}
Group 1 is {m.group(1)}
Group 2 is {m.group(2)}
Group 3 is {m.group(3)}
''')
```


{:.output .output_stream}
```

Group 0 is ahab@pequod.com
Group 1 is ahab
Group 2 is pequod
Group 3 is com


```

### Named groups



{:.input_area}
```
m = re.search("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", text)

print(f'''
Email address: {m.group()}
Name:  {m.group("name")}
Secondary level domain: {m.group("SLD")}
Top level Domain: {m.group("TLD")}
''')
```


{:.output .output_stream}
```

Email address: ahab@pequod.com
Name:  ahab
Secondary level domain: pequod
Top level Domain: com


```

### Find all



{:.input_area}
```
m = re.findall("\w+\@\w+\.\w+", text)
m
```





{:.output .output_data_text}
```
['ahab@pequod.com',
 'peleg@pequod.com',
 'ishmael@pequod.com',
 'herman@Acushnet.io',
 'pollard@essex.me']
```





{:.input_area}
```
re.findall("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", text)

```





{:.output .output_data_text}
```
[('ahab', 'pequod', 'com'),
 ('peleg', 'pequod', 'com'),
 ('ishmael', 'pequod', 'com'),
 ('herman', 'Acushnet', 'io'),
 ('pollard', 'essex', 'me')]
```



### Find iterator



{:.input_area}
```
iterator = re.finditer("\w+\@\w+\.\w+", text)

print(f"An {type(iterator)} object is returned by finditer" )
```


{:.output .output_stream}
```
An <class 'callable_iterator'> object is returned by finditer

```



{:.input_area}
```
m = next(iterator)
f"The first match, {m.group()} is processed without processing the rest of the text"
```





{:.output .output_data_text}
```
"The first match, <_sre.SRE_Match object; span=(39, 55), match='peleg@pequod.com'> is processed without processing the rest of the text"
```



### Iterators with named groups



{:.input_area}
```
iterator = re.finditer("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", text)
for m in iterator:
  print(m.groupdict())
```


{:.output .output_stream}
```
{'name': 'ahab', 'SLD': 'pequod', 'TLD': 'com'}
{'name': 'peleg', 'SLD': 'pequod', 'TLD': 'com'}
{'name': 'ishmael', 'SLD': 'pequod', 'TLD': 'com'}
{'name': 'herman', 'SLD': 'Acushnet', 'TLD': 'io'}
{'name': 'pollard', 'SLD': 'essex', 'TLD': 'me'}

```



{:.input_area}
```
iterator = re.finditer("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", text)
for m in iterator:
  data = m.groupdict()
  print(f"{data['name'].title()} sailed on the {data['SLD'].title()}")
```


{:.output .output_stream}
```
Ahab sailed on the Pequod
Peleg sailed on the Pequod
Ishmael sailed on the Pequod
Herman sailed on the Acushnet
Pollard sailed on the Essex

```

### Substitution



{:.input_area}
```
re.sub("\d", "#", "Your secrect pin is 12345")
```





{:.output .output_data_text}
```
'Your secrect pin is #####'
```



### Substitution using named groups



{:.input_area}
```
new_text = re.sub("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", "\g<TLD>.\g<SLD>.\g<name>", text)

print(new_text)
```


{:.output .output_stream}
```

Ahab: com.pequod.ahab
Peleg: com.pequod.peleg
Ishmael: com.pequod.ishmael
Herman: io.acushnet.herman
Pollard: me.essex.pollard


```

### Compiling regexes



{:.input_area}
```
regex = re.compile("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)")
regex
```





{:.output .output_data_text}
```
re.compile(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', re.UNICODE)
```





{:.input_area}
```
regex.search(text)
```





{:.output .output_data_text}
```
<_sre.SRE_Match object; span=(7, 22), match='ahab@pequod.com'>
```



## 12.3 Learn text processing techniques: Beautiful Soup


# Notes

[python regular expresssions](https://docs.python.org/3/library/re.html#re-syntax)

[python regex howto](https://docs.python.org/3/howto/regex.html)

[regular_expressions](https://en.wikipedia.org/wiki/Regular_expression)
