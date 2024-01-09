#Exercise 8: Rename key of a dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict.pop("city")
sample_dict["location"] = "New york"

print(sample_dict)