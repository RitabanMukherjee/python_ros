monthConversion = {
    "Jan": "January",
    "Feb": "February", # all keys must be unique
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July"
}

print(monthConversion)
print(monthConversion["Mar"])
print(monthConversion.get("Jul")) #similar way of accessing specific key/value pairs in dictionary
print(monthConversion.get("Luv", "Not a valid key"))    # a deafult value can also be provided to .get() method when trying to access invalid keys