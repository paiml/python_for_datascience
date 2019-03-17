---
redirect_from:
  - "/lessons/lesson7-python-for-datascience-execution-control"
interact_link: content/lessons/Lesson7_Python_For_Datascience_Execution_Control.ipynb
kernel_name: python3
title: 'Lesson 7 - Execution Control'
prev_page:
  url: /lessons/Lesson6_Python_For_Data_Science_Data_Conversion_Recipes
  title: 'Lesson 6 - Data Conversion Recipes'
next_page:
  url: /lessons/Lesson8_Python_For_Data_Science_Functions
  title: 'Lesson 8 - Functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson7_Python_For_Datascience_Execution_Control.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 7 Execution Control

## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 7.1 Learn to loop with for loops

### Using Loops

The for loop is one of the most fundamental control structures in Python.
One common pattern is to use the range function to generate a range of values, then to iterate on them.

#### Using a Simple For Loop

built in range() function creates an iterable



{:.input_area}
```
res = range(3)
res
```





{:.output .output_data_text}
```
range(0, 3)
```





{:.input_area}
```
for i in range(1,6):
    print(i)
```


{:.output .output_stream}
```
1
2
3
4
5

```

#### For loop over an iterable (list)

Another common pattern is to iterate on a list (or any iterable)



{:.input_area}
```
friends = ["Moby", "Ahab", "Stubb"]
for friend in friends:
  print(f"With friends like {friend} who needs a Yelp review?")
```


{:.output .output_stream}
```
With friends like Moby who needs a Yelp review?
With friends like Ahab who needs a Yelp review?
With friends like Stubb who needs a Yelp review?

```

## 7.2 Repeat with while loops

### While Loops




{:.input_area}
```
def sea_life():
    animals = ["whale", "orca","porpoise", "moby_dick"]
    print(f"There are many creatures in the sea: {len(animals)}")
    for animal in animals:
        yield animal

animals = sea_life()
count = 0

while next(animals) != "moby_dick":
    count +=1
    print(f"hold your fire #{count}, it is just a common sea creature")
else:
    count +=1
    print(f"Fire the harpoon, we spotted Moby Dick #{count}")
```


{:.output .output_stream}
```
There are many creatures in the sea: 4
hold your fire #1, it is just a common sea creature
hold your fire #2, it is just a common sea creature
hold your fire #3, it is just a common sea creature
Fire the harpoon, we spotted Moby Dick #4

```

## 7.3 Learn to handle exceptions

### Try/Except

There is an expression in sports, "Always be prepared to do your best on your worst day". Try/Except statements are similar. It is always a good idea to think about what happens when something goes wrong in code that is written. Try/Except blocks allow for this.

#### Using try/except

Catching a specific exception



{:.input_area}
```
whales = ["Keiko", "Shamu", "Moby Dick"]
while True:
    try:
        whale = whales.pop()
        print(f"I want this whale {whale}!")
    except IndexError:
        print("There are no more whales to be had")
        break
```


{:.output .output_stream}
```
I want this whale Moby Dick!
I want this whale Shamu!
I want this whale Keiko!
There are no more whales to be had

```

#### Logging exceptions

It is a best practice to log exception blocks



{:.input_area}
```
import logging

whales = ["Keiko", "Shamu", "Moby Dick"]
while True:
    try:
        whale = whales.pop()
        print(f"I want this whale {whale}!")
    except IndexError:
        logging.exception(f"Exception Logged:  There are no more tournaments")
        print("There are no more whales to be had")
        break
```


{:.output .output_stream}
```
I want this whale Moby Dick!
I want this whale Shamu!
I want this whale Keiko!
There are no more whales to be had

```

## 7.4 Use conditionals

### Using if/else/break/continue/pass statements


#### Using if/elif/else blocks
If/Else statements are a common way to branch between decisions. In the example below if/elif are used to match a branch. If there are no matches, the last "else" statement is run.



{:.input_area}
```
def recommended_whale(emotion):
    """Recommends a whale based on emotion"""
    
    if emotion == "angry":
        print(f"You seem very {emotion}, I have just the whale for you:  Moby Dick!")
    elif emotion == "happy":
        print(f"You seem very {emotion}, I have just the whale for you:  Shamu!")
    else:
        print(f"You seem very {emotion}, I have no whale to recommend: How about a Crocodile instead?")
```




{:.input_area}
```
recommended_whale("sad")
```


{:.output .output_stream}
```
You seem very sad, I have no whale to recommend: How about a Crocodile instead?

```

#### Single line conditional asssigment



{:.input_area}
```
happy = False
cloudy = False

happy = False if cloudy else True
  
happy
```





{:.output .output_data_text}
```
True
```



#### Using break



{:.input_area}
```
crew_members = 0
while True:
  crew_members +=1
  print(f"Moby Dick is attempting to eat crew member {crew_members}")
  if crew_members > 3:
    print(f"Moby Dick is very full, he ate {crew_members} and couldn't possibly eat any more")
    break
  
```


{:.output .output_stream}
```
Moby Dick is attempting to eat crew member 1
Moby Dick is attempting to eat crew member 2
Moby Dick is attempting to eat crew member 3
Moby Dick is attempting to eat crew member 4
Moby Dick is very full, he ate 4 and couldn't possibly eat any more

```

#### Using continue



{:.input_area}
```
whales = ["Keiko", "Shamu", "Moby Dick"]
for whale in whales:
  if not whale == "Moby Dick":
    continue
  print(f"My favorite whale is {whale}")
```


{:.output .output_stream}
```
My favorite whale is Moby Dick

```

#### Using pass

The pass keyword is often a placeholder to define a class or function



{:.input_area}
```
def my_func(): pass


my_func()
```


{:.output .output_traceback_line}
```

      File "<ipython-input-10-e2f9698e90a7>", line 4
        my_func()
              ^
    IndentationError: expected an indented block



```



{:.input_area}
```
class SomeClass: pass

some_class = SomeClass()

some_class
```





{:.output .output_data_text}
```
<__main__.SomeClass at 0x7fbdeb4e2a90>
```


