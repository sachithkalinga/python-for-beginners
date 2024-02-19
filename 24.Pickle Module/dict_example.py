import pickle

#Serialize/ Pickling.....................................................................

data = {"Name": "John", "Age": 24, "City": "LBC"}

with open(f"24.Pickle Module\dict.pickle", "wb") as f:        # wb = write binary mode
    pickle.dump(data, f)

#De-serialize/ Unpickling................................................................

with open(f"24.Pickle Module\dict.pickle", "rb") as f:      # rb = read binary mode
    dict_data = pickle.load(f)
    
print(dict_data)                # {'Name': 'John', 'Age': 24, 'City': 'LBC'}
print(dict_data["Name"])        # John