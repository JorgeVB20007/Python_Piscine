ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

tuple2list = list(ft_tuple)
tuple2list[1] = "Spain!"
ft_tuple = tuple(tuple2list)

ft_set.remove("tutu!")
ft_set.add("Madrid!")

ft_dict["Hello"] = "42 Madrid!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
