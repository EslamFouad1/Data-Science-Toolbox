#Encoding: Three features (Cut, Clarity and Color) are going to be encoded.
cut_class_dict = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5, }
clarity_dict   = {'SI2': 2, 'SI1': 3, 'VS1': 5, 'VS2': 4, 'VVS2': 6, 'VVS1': 7, 'I1': 1, 'IF': 8 }
color_dict     = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6,'D': 7,} 

data['cut'] = data['cut'].map(cut_class_dict)
data['clarity'] = data['clarity'].map(clarity_dict)
data['color'] = data['color'].map(color_dict)
