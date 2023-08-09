def extract_numeric_value(value: str) -> float:
    try:
        strRep = str(value)
        floatRep = ""
        for char in strRep:
            if not char.isalpha() and not char.isspace() and char != '/':
                floatRep += char

        return float(floatRep)
    except:
        return None

 print(X['Mileage'] = X['Mileage'].apply(extract_numeric_value))
