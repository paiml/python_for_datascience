---
redirect_from:
  - "/lessons/lesson13-python-for-data-science-sorting"
interact_link: content/lessons/Lesson13_Python_For_Data_Science_Sorting.ipynb
kernel_name: python3
title: 'Lesson 13 - Sorting'
prev_page:
  url: /lessons/Lesson12_Python_For_Data_Science_Pattern_Matching
  title: 'Lesson 12 - Pattern Matching'
next_page:
  url: /lessons/Lesson14_Python_For_Data_Science_I_O
  title: 'Lesson 14 - I/O'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<a href="https://colab.research.google.com/github/paiml/python_for_datascience/blob/master/Lesson13_Python_For_Data_Science_Sorting.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 13 Sorting


## Pragmatic AI Labs



![alt text](https://paiml.com/images/logo_with_slogan_white_background.png)

This notebook was produced by [Pragmatic AI Labs](https://paiml.com/).  You can continue learning about these topics by:

*   Buying a copy of [Pragmatic AI: An Introduction to Cloud-Based Machine Learning](http://www.informit.com/store/pragmatic-ai-an-introduction-to-cloud-based-machine-9780134863917)
*   Reading an online copy of [Pragmatic AI:Pragmatic AI: An Introduction to Cloud-Based Machine Learning](https://www.safaribooksonline.com/library/view/pragmatic-ai-an/9780134863924/)
*  Watching video [Essential Machine Learning and AI with Python and Jupyter Notebook-Video-SafariOnline](https://www.safaribooksonline.com/videos/essential-machine-learning/9780135261118) on Safari Books Online.
* Watching video [AWS Certified Machine Learning-Speciality](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
* Purchasing video [Essential Machine Learning and AI with Python and Jupyter Notebook- Purchase Video](http://www.informit.com/store/essential-machine-learning-and-ai-with-python-and-jupyter-9780135261095)
*   Viewing more content at [noahgift.com](https://noahgift.com/)


## 13.1 Sort in python

### Understanding Sorting

Python has powerful built-in sorting


#### World Food Facts DataSet

* Original Data Source:  https://www.kaggle.com/openfoodfacts/world-food-facts
* Modified Source:  https://www.kaggle.com/lwodarzek/nutrition-table-clustering/output

##### Ingest



{:.input_area}
```
import pandas as pd
```




{:.input_area}
```
df = pd.read_csv(
    "https://raw.githubusercontent.com/noahgift/food/master/data/features.en.openfoodfacts.org.products.csv")
df.drop(["Unnamed: 0", "exceeded", "g_sum", "energy_100g"], axis=1, inplace=True) #drop two rows we don't need
df = df.drop(df.index[[1,11877]]) #drop outlier
df.rename(index=str, columns={"reconstructed_energy": "energy_100g"}, inplace=True)
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
      <th>energy_100g</th>
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
    <tr>
      <th>5</th>
      <td>18.18</td>
      <td>60.00</td>
      <td>21.82</td>
      <td>14.55</td>
      <td>0.02286</td>
      <td>1976.37</td>
      <td>Cinnamon Nut Granola</td>
    </tr>
  </tbody>
</table>
</div>
</div>



#### Using built-in sorting

Convert Pandas DataFrame Columns into a list



{:.input_area}
```
food_facts = list(df.columns.values)
food_facts
```





{:.output .output_data_text}
```
['fat_100g',
 'carbohydrates_100g',
 'sugars_100g',
 'proteins_100g',
 'salt_100g',
 'energy_100g',
 'product']
```



##### Alphabetical Sort



{:.input_area}
```
sorted(food_facts)
```





{:.output .output_data_text}
```
['carbohydrates_100g',
 'energy_100g',
 'fat_100g',
 'product',
 'proteins_100g',
 'salt_100g',
 'sugars_100g']
```



##### Reverse Alphabetical Sort



{:.input_area}
```
sorted(food_facts, reverse=True)
```





{:.output .output_data_text}
```
['sugars_100g',
 'salt_100g',
 'proteins_100g',
 'product',
 'fat_100g',
 'energy_100g',
 'carbohydrates_100g']
```



##### Using built in list sort

Only works on a list



{:.input_area}
```
food_facts = list(df.columns.values)
print(f"Before sort: {food_facts}")
food_facts.sort()
print(f"After sort: {food_facts}")

```


{:.output .output_stream}
```
Before sort: ['fat_100g', 'carbohydrates_100g', 'sugars_100g', 'proteins_100g', 'salt_100g', 'energy_100g', 'product']
After sort: ['carbohydrates_100g', 'energy_100g', 'fat_100g', 'product', 'proteins_100g', 'salt_100g', 'sugars_100g']

```

##### Timing built-in sort function vs list sort method

list method



{:.input_area}
```
food_facts = list(df.columns.values)
```




{:.input_area}
```
%%timeit -n 3 -r 3
food_facts.sort()


```


{:.output .output_stream}
```
3 loops, best of 3: 489 ns per loop

```

built in function



{:.input_area}
```
food_facts = list(df.columns.values)
```




{:.input_area}
```
%%timeit -n 3 -r 3
sorted(food_facts)
```


{:.output .output_stream}
```
3 loops, best of 3: 656 ns per loop

```

#### Sorting Dictionary

sorting a dictionary



{:.input_area}
```
food_facts_row = df.head(1).to_dict()
food_facts_row
```





{:.output .output_data_text}
```
{'carbohydrates_100g': {'0': 64.29},
 'energy_100g': {'0': 2267.85},
 'fat_100g': {'0': 28.57},
 'product': {'0': 'Banana Chips Sweetened (Whole)'},
 'proteins_100g': {'0': 3.57},
 'salt_100g': {'0': 0.0},
 'sugars_100g': {'0': 14.29}}
```



reverse sort dictionary



{:.input_area}
```
sorted(food_facts_row, reverse=True)
```





{:.output .output_data_text}
```
['sugars_100g',
 'salt_100g',
 'proteins_100g',
 'product',
 'fat_100g',
 'energy_100g',
 'carbohydrates_100g']
```





{:.input_area}
```
df["product"].head().values
```





{:.output .output_data_text}
```
array(['Banana Chips Sweetened (Whole)', 'Organic Salted Nut Mix',
       'Organic Muesli', 'Zen Party Mix', 'Cinnamon Nut Granola'],
      dtype=object)
```



#### Sorting A Generator Pipeline



{:.input_area}
```
def dataframe_rows(df=df, column="product", chunks=10):
  
    count_row = df.shape[0]
    rows = list(df[column].values)
    for i in range(0, count_row, chunks):
      yield rows[i:i + chunks]
    
    
```




{:.input_area}
```
rows = dataframe_rows()
next(rows)

```





{:.output .output_data_text}
```
['Banana Chips Sweetened (Whole)',
 'Organic Salted Nut Mix',
 'Organic Muesli',
 'Zen Party Mix',
 'Cinnamon Nut Granola',
 'Organic Hazelnuts',
 'Organic Oat Groats',
 'Energy Power Mix',
 'Antioxidant Mix - Berries & Chocolate',
 'Organic Quinoa Coconut Granola With Mango']
```





{:.input_area}
```
next(rows)
```





{:.output .output_data_text}
```
['Fire Roasted Hatch Green Chile Almonds',
 'Peanut Butter Power Chews',
 'Organic Unswt Berry Coconut Granola',
 'Roasted Salted Black Pepper Cashews',
 'Thai Curry Roasted Cashews',
 'Wasabi Tamari Almonds',
 'Organic Red Quinoa',
 'Dark Chocolate Coconut Chews',
 'Organic Unsweetened Granola, Cinnamon Almond',
 'Organic Blueberry Almond Granola']
```





{:.input_area}
```
sorted_row = (sorted(row) for row in rows )
print(next(sorted_row))
```


## 13.2 Create custom sorting functions

### Building a Shuffle Function



{:.input_area}
```
food_items = ['Chocolate Nut Crunch', 'Cranberries', 'Curry Lentil Soup Mix', 
                'Milk Chocolate Peanut Butter Malt Balls', 'Organic Harvest Pilaf', 
                'Organic Tamari Pumpkin Seed', 'Split Pea Soup Mix', 
                'Swiss-Style Muesli', "Whole Wheat 'N Honey Fig Bars", 
                'Yogurt Pretzels']

```




{:.input_area}
```
from random import sample

def shuffle_list(items):
  """Randomly Shuffles List"""
  
  shuffled = sample(items, len(items))
  return shuffled
  
```




{:.input_area}
```
shuffled_food_items = shuffle_list(food_items)
shuffled_food_items
```





{:.output .output_data_text}
```
['Milk Chocolate Peanut Butter Malt Balls',
 'Organic Harvest Pilaf',
 'Curry Lentil Soup Mix',
 'Yogurt Pretzels',
 'Organic Tamari Pumpkin Seed',
 'Chocolate Nut Crunch',
 "Whole Wheat 'N Honey Fig Bars",
 'Split Pea Soup Mix',
 'Cranberries',
 'Swiss-Style Muesli']
```



### Custom Sort Functions

#### Highly Customized Sort



{:.input_area}
```
def best_snack(item):
  if item == "Chocolate Nut Crunch":
    return 1
  return len(item) 

sorted(shuffled_food_items, key=best_snack)
```





{:.output .output_data_text}
```
['Chocolate Nut Crunch',
 'Cranberries',
 'Yogurt Pretzels',
 'Split Pea Soup Mix',
 'Swiss-Style Muesli',
 'Organic Harvest Pilaf',
 'Curry Lentil Soup Mix',
 'Organic Tamari Pumpkin Seed',
 "Whole Wheat 'N Honey Fig Bars",
 'Milk Chocolate Peanut Butter Malt Balls']
```



#### Sorting Objects



{:.input_area}
```
class Food:
  def __init__(self, product, protein):
    self.product = product
    self.protein = protein
  def __repr__(self):
    return f"Food: {self.product}, Protein: {self.protein}"
```




{:.input_area}
```
pairs = df[["product", "proteins_100g"]].head().values.tolist()
pairs
```





{:.output .output_data_text}
```
[['Banana Chips Sweetened (Whole)', 3.57],
 ['Organic Salted Nut Mix', 17.86],
 ['Organic Muesli', 14.06],
 ['Zen Party Mix', 16.67],
 ['Cinnamon Nut Granola', 14.55]]
```





{:.input_area}
```
pairs = df[["product", "proteins_100g"]].head().values.tolist()
foods = [Food(item[0], item[1]) for item in pairs]
foods
```





{:.output .output_data_text}
```
[Food: Banana Chips Sweetened (Whole), Protein: 3.57,
 Food: Organic Salted Nut Mix, Protein: 17.86,
 Food: Organic Muesli, Protein: 14.06,
 Food: Zen Party Mix, Protein: 16.67,
 Food: Cinnamon Nut Granola, Protein: 14.55]
```





{:.input_area}
```
sorted(foods, key=lambda food: food.protein)

```





{:.output .output_data_text}
```
[Food: Banana Chips Sweetened (Whole), Protein: 3.57,
 Food: Organic Muesli, Protein: 14.06,
 Food: Cinnamon Nut Granola, Protein: 14.55,
 Food: Zen Party Mix, Protein: 16.67,
 Food: Organic Salted Nut Mix, Protein: 17.86]
```





{:.input_area}
```
foods[0].__dict__
type(foods[0])
```





{:.output .output_data_text}
```
__main__.Food
```



## 13.3 Sort in pandas

### Sort by One Column:  Protein



{:.input_area}
```
df.sort_values(by=["carbohydrates_100g"], ascending=False).head(5)
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
      <th>energy_100g</th>
      <th>product</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>42012</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>85.71</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>1700.0</td>
      <td>Spongebob Squarepants Valentine Candy Card Kit</td>
    </tr>
    <tr>
      <th>31827</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>80.00</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>1700.0</td>
      <td>Marvel Avengers Assemble, Classroom Candy Mail...</td>
    </tr>
    <tr>
      <th>31661</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.00</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>1700.0</td>
      <td>White Crystal Sugar</td>
    </tr>
    <tr>
      <th>31665</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.254</td>
      <td>1700.0</td>
      <td>Dried Habanero Chiles</td>
    </tr>
    <tr>
      <th>42366</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>88.89</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>1700.0</td>
      <td>Iced Tea Mix, Lemon</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Sort by Two Columns:  Sugar, Salt



{:.input_area}
```
df.sort_values(by=["fat_100g", "salt_100g"], ascending=[False, False]).head(10)
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
      <th>energy_100g</th>
      <th>product</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8390</th>
      <td>100.0</td>
      <td>20.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>1.524</td>
      <td>4240.00</td>
      <td>Horseradish Sauce</td>
    </tr>
    <tr>
      <th>44709</th>
      <td>100.0</td>
      <td>17.86</td>
      <td>3.57</td>
      <td>10.71</td>
      <td>0.381</td>
      <td>4385.69</td>
      <td>Roasted Pecans</td>
    </tr>
    <tr>
      <th>295</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Ventura, Soybean - Peanut Frying Oil Blend</td>
    </tr>
    <tr>
      <th>5122</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Corn Oil</td>
    </tr>
    <tr>
      <th>5123</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Canola Oil</td>
    </tr>
    <tr>
      <th>5124</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Vegetable Oil</td>
    </tr>
    <tr>
      <th>5125</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Vegetable Shortening</td>
    </tr>
    <tr>
      <th>5671</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Organic Coconut Oil</td>
    </tr>
    <tr>
      <th>5797</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Premium Sesame Oil (100% Pure)</td>
    </tr>
    <tr>
      <th>5798</th>
      <td>100.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.000</td>
      <td>3900.00</td>
      <td>Sesame Oil</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Groupby



{:.input_area}
```
def high_protein(row):
  """Creates a high or low protein category"""
  
  if row > 80:
    return "high_protein"
  return "low_protein"

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
      <th>energy_100g</th>
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
    <tr>
      <th>5</th>
      <td>18.18</td>
      <td>60.00</td>
      <td>21.82</td>
      <td>14.55</td>
      <td>0.02286</td>
      <td>1976.37</td>
      <td>Cinnamon Nut Granola</td>
      <td>low_protein</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```
df.groupby("high_protein").median()
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
      <th>energy_100g</th>
    </tr>
    <tr>
      <th>high_protein</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>high_protein</th>
      <td>1.665</td>
      <td>3.335</td>
      <td>1.665</td>
      <td>93.18</td>
      <td>0.5207</td>
      <td>1700.00</td>
    </tr>
    <tr>
      <th>low_protein</th>
      <td>3.170</td>
      <td>22.390</td>
      <td>5.880</td>
      <td>4.00</td>
      <td>0.6350</td>
      <td>1121.54</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```
df.groupby("high_protein").describe()
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

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">carbohydrates_100g</th>
      <th colspan="2" halign="left">energy_100g</th>
      <th>...</th>
      <th colspan="2" halign="left">salt_100g</th>
      <th colspan="8" halign="left">sugars_100g</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>...</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>high_protein</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>high_protein</th>
      <td>4.0</td>
      <td>7.350000</td>
      <td>10.724610</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>3.335</td>
      <td>10.685</td>
      <td>22.73</td>
      <td>4.0</td>
      <td>1795.09500</td>
      <td>...</td>
      <td>4.203065</td>
      <td>14.77772</td>
      <td>4.0</td>
      <td>4.242500</td>
      <td>6.458671</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1.665</td>
      <td>5.9075</td>
      <td>13.64</td>
    </tr>
    <tr>
      <th>low_protein</th>
      <td>45022.0</td>
      <td>34.056436</td>
      <td>29.557504</td>
      <td>0.0</td>
      <td>7.44</td>
      <td>22.390</td>
      <td>61.540</td>
      <td>100.00</td>
      <td>45022.0</td>
      <td>1111.22544</td>
      <td>...</td>
      <td>1.440180</td>
      <td>2032.00000</td>
      <td>45022.0</td>
      <td>16.006122</td>
      <td>21.496335</td>
      <td>-1.2</td>
      <td>1.57</td>
      <td>5.880</td>
      <td>23.0800</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 48 columns</p>
</div>
</div>


