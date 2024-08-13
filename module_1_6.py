# Словарь
dict_ = {"Gregor": 89003312301, "Sergo": 89003322402}
print("Dict: ", dict_)
print("Existing value: ", dict_["Gregor"])
print("Not existing value: ", dict_.get("Lusi"))
dict_.update({"Dima": 89003352707,
             "Ivan": 89003362808})
d = dict_.pop("Dima")
print("Deleted value: ", d)
print("Modified dictionary: ", dict_)

# Множества
set_ = {1, 2, 3, 2, 3, "Honda", "Honda", "Toyota", 14.98}
print("Set:", set_)
set_.update(("Nissan", 1941))
set_.discard(14.98)
print("Modified set:", set_)