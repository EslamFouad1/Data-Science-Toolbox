df['lightduty'] = df['lightduty'].apply(lambda x: 0 if x=='No' else 1)
