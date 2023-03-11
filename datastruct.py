#List
list_of_cloud = ["aws","azure","oracel","gcp"]
list_of_env = ["test","dev","prod"]
print(list_of_cloud)

#list literation
for cloud in list_of_cloud:
    print(cloud)
    print("Azure is best")

#Dictionary
dict_of_cloud = {
    "aws"   :"Amazon Web Services",
    "azure" : "Microsoft Services",
    "gcp"   :"Google Services"
}
print(dict_of_cloud["azure"])
print(dict_of_cloud["aws"])