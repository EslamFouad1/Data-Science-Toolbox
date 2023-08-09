#Encoding: Three features (Cut, Clarity and Color) are going to be encoded.
cut_class_dict = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5, }
clarity_dict   = {'SI2': 2, 'SI1': 3, 'VS1': 5, 'VS2': 4, 'VVS2': 6, 'VVS1': 7, 'I1': 1, 'IF': 8 }
color_dict     = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6,'D': 7,} 

data['cut'] = data['cut'].map(cut_class_dict)
data['clarity'] = data['clarity'].map(clarity_dict)
data['color'] = data['color'].map(color_dict)


# Another way
diamonds_num = diamonds.loc[:,["carat","depth","table","x","y","z"]]
diamonds_cat = diamonds.loc[:,["cut","color","clarity"]]

from sklearn.preprocessing import OrdinalEncoder

ordinal_categories = [
  ["Fair","Good","Very Good","Premium","Ideal"],
  ["J","I","H","G","F","E","D"],
  ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
]

ordinal_encoder = OrdinalEncoder(categories=ordinal_categories)
diamonds_cat_encoded = ordinal_encoder.fit_transform(diamonds_cat)
diamonds_cat_encoded[:3]

ordinal_encoder.categories_
