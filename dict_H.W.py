keys = ["home_key", "2nd_home-key", "bike_key", "car_key", "shop_key", "safe-key"]

for key in keys:
  if key == "safe_key":
    print("open the safe")
  else:
    print("this is not safe key") 

key_bunch = {
  "home_key" : "key1",
  "2nd_home_key" : "key2",
  "bike_key" : "key3",
  "car_key" : "key4",
  "shop_key" : "key5",
  "safe_key" : "key5"
}

print(key_bunch["safe_key"]
