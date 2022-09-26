days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_dict1 = dict(zip(range(1, len(days)+1), days))
days_dict2 = dict(zip(days, range(1, len(days)+1)))
print(days_dict2)