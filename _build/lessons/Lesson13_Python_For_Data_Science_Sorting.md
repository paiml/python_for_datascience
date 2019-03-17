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
3 loops, best of 3: 307 ns per loop

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
3 loops, best of 3: 513 ns per loop

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


{:.output .output_stream}
```
['35% Fruit And Fiber Muesli', "Aunt Ginger's Snappy Granola", 'Coconut Almond Granola', 'Dark Chocolate Sea Salt & Turbinado Almonds', 'Maple Almond Granola', 'Organic Coconut Chips', 'Organic Garbanzo Beans', 'Organic Yellow Split Peas', 'Super Nutty Granola', 'Tricolor Tortellini']

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
["Whole Wheat 'N Honey Fig Bars",
 'Organic Harvest Pilaf',
 'Chocolate Nut Crunch',
 'Organic Tamari Pumpkin Seed',
 'Milk Chocolate Peanut Butter Malt Balls',
 'Yogurt Pretzels',
 'Split Pea Soup Mix',
 'Swiss-Style Muesli',
 'Curry Lentil Soup Mix',
 'Cranberries']
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



## 13.3 Sort in pandas

### Sort by One Column:  Protein



{:.input_area}
```
df.sort_values(by=["proteins_100g"], ascending=False).head(10)
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
      <th>2377</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>100.00</td>
      <td>0.00000</td>
      <td>1700.00</td>
      <td>Unflavored Gelatin</td>
    </tr>
    <tr>
      <th>37027</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>100.00</td>
      <td>0.36322</td>
      <td>1700.00</td>
      <td>Unflavored Gelatin</td>
    </tr>
    <tr>
      <th>16674</th>
      <td>6.82</td>
      <td>22.73</td>
      <td>13.64</td>
      <td>86.36</td>
      <td>14.77772</td>
      <td>2120.51</td>
      <td>Fisherman's Wharf, Cocktail Shrimp</td>
    </tr>
    <tr>
      <th>37415</th>
      <td>3.33</td>
      <td>6.67</td>
      <td>3.33</td>
      <td>83.33</td>
      <td>0.67818</td>
      <td>1659.87</td>
      <td>Whey &amp; Soy Protein, Flavored Drink Mix, Vanilla</td>
    </tr>
    <tr>
      <th>133</th>
      <td>4.60</td>
      <td>8.80</td>
      <td>6.00</td>
      <td>78.05</td>
      <td>1.21158</td>
      <td>1655.85</td>
      <td>Whey Protein aus Molke 500 Gramm Vanilla</td>
    </tr>
    <tr>
      <th>131</th>
      <td>4.60</td>
      <td>8.80</td>
      <td>6.00</td>
      <td>78.05</td>
      <td>1.21158</td>
      <td>1655.85</td>
      <td>Whey Protein aus Molke 1000 Gramm Vanilla</td>
    </tr>
    <tr>
      <th>129</th>
      <td>4.60</td>
      <td>8.80</td>
      <td>6.00</td>
      <td>78.05</td>
      <td>1.21158</td>
      <td>1655.85</td>
      <td>Whey Protein aus Molke Vanilla</td>
    </tr>
    <tr>
      <th>33115</th>
      <td>1.67</td>
      <td>13.33</td>
      <td>0.00</td>
      <td>76.67</td>
      <td>0.00000</td>
      <td>1595.13</td>
      <td>Vital Wheat</td>
    </tr>
    <tr>
      <th>37392</th>
      <td>6.25</td>
      <td>8.33</td>
      <td>4.17</td>
      <td>75.00</td>
      <td>0.63500</td>
      <td>1660.36</td>
      <td>Whey Protein Powder, Chocolate</td>
    </tr>
    <tr>
      <th>16669</th>
      <td>5.36</td>
      <td>21.43</td>
      <td>14.29</td>
      <td>67.86</td>
      <td>12.79144</td>
      <td>1726.97</td>
      <td>Fisherman's Wharf, Cocktail Shrimp</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Sort by Two Columns:  Sugar, Salt



{:.input_area}
```
df.sort_values(by=["sugars_100g", "salt_100g"], ascending=[False, False]).head(10)
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
      <th>33151</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>71.1200</td>
      <td>0.0</td>
      <td>Turkey Brine Kit, Garlic &amp; Herb</td>
    </tr>
    <tr>
      <th>24783</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>24.1300</td>
      <td>1700.0</td>
      <td>Seasoning</td>
    </tr>
    <tr>
      <th>4073</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>7.6200</td>
      <td>1700.0</td>
      <td>Seasoning Rub, Sweet &amp; Spicy Seafood</td>
    </tr>
    <tr>
      <th>10282</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>2.5400</td>
      <td>1700.0</td>
      <td>Instant Pectin</td>
    </tr>
    <tr>
      <th>17880</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.6350</td>
      <td>1700.0</td>
      <td>Cranberry Cosmos Cocktail Rimming Sugar</td>
    </tr>
    <tr>
      <th>8822</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.5588</td>
      <td>1700.0</td>
      <td>Alaga, The Original Cane Flavor Syrup, Cane</td>
    </tr>
    <tr>
      <th>8823</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.5588</td>
      <td>1700.0</td>
      <td>The Original Cane Syrup</td>
    </tr>
    <tr>
      <th>41157</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.3175</td>
      <td>1700.0</td>
      <td>Panela Brown Sugar Cane</td>
    </tr>
    <tr>
      <th>41158</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.3175</td>
      <td>1700.0</td>
      <td>Panela Brown Sugar Cane</td>
    </tr>
    <tr>
      <th>41159</th>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.3175</td>
      <td>1700.0</td>
      <td>Panela</td>
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



## Notes

Similar to Notes section of Powerpoint (where we can exchange ideas)

* We may want Lesson 1 to be PowerPoint only
