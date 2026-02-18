# Exercises 1
# បង្កើត List មួយឈ្មោះ fruits ដែលមាន:
# apple
# banana
# mango
# orange
# 📌 កិច្ចការ:
# បង្ហាញ List ទាំងមូល
# បង្ហាញធាតុទី 2
# បង្ហាញធាតុចុងក្រោយ
# ==========code==============
# fruits=["apple","banana","mango","orange",]
# print(fruits)
# print("I like",fruits[1])

# Exercises 2
# មាន List ផ្ទុកឈ្មោះសិស្ស 4 នាក់
# 📌 កិច្ចការ:
# ប្តូរឈ្មោះសិស្សទី 3 ទៅជា Sokha
# ==========code==============
# student=["meng","nana","kaka","lyza"]
# student[2]=("Sokha")
# print(student)

# Exercises 3
#     មាន List: ការទិញក្នុងផ្សារ
#     📌 កិច្ចការ:
#     បន្ថែម “milk” ចុងក្រោយ
#     បន្ថែម “bread” ទៅទីតាំងដើម (index 0)
# ==========code==============
# item=["Drink","fruits"]
# item.append("milk")
# item.insert(0,"bread")
# print(item)

# Exercises 4
#    មាន List ផ្ទុកលេខ 1,2,3,4,5
#    📌 កិច្ចការ:
#    លុបលេខ 3
#    លុបធាតុចុងក្រោយ
#    លុបធាតុទី 1
# ==========code==============
# num=[1,2,3,4,5]
# num.remove(3)
# num.pop(1)
# num.pop(len(num)-1)
# print(num)

# Exercises 5
#     មាន List ផ្ទុកឈ្មោះមិត្តភក្តិ
#     📌 កិច្ចការ:
#     រកចំនួនមិត្តភក្តិទាំងអស់ក្នុង List
# ==========code==============
# friend=["kaka","lyza","nona"]
# print(len(friend))

# Exercises 6
#     មាន List ផ្ទុកពណ៌:
#     red, blue, green, yellow
#     📌 កិច្ចការ:
#     បង្ហាញពណ៌ម្តងមួយ (loop)
# ==========code==============
# colors = ["red", "blue","grenn","yellow"]
# for name in colors:
#     print("This Color",name)

# Exercises 7
#     មាន List ផ្ទុកសត្វ:
#     cat, dog, tiger, lion
#     📌 កិច្ចការ:
#     ពិនិត្យថា “dog” មានក្នុង List ឬអត់
#     បង្ហាញលទ្ធផល Yes / No
# ==========code==============
# list=["cat","dog","tiger","lion"]
# if "dog" in list:
#     print("Yes")
# else:
#     print("No")

# Exercise 8
#     មាន List លេខ:
#     5, 1, 9, 3, 7
#     📌 កិច្ចការ:
#     រៀបពីតូច → ធំ
#     រៀបពីធំ → តូច
# ==========code==============
# num=[ 5, 1, 9, 3, 7]
# num.sort(reverse=True) # Big to small
# print(num)
# num.sort()             # Small to Big
# print(num)

# Exercise 9
#     មាន List លេខ:
#     10, 20, 30, 40, 50
#     📌 កិច្ចការ:
#     គណនាផលបូកលេខទាំងអស់
# ==========code==============
# num=[10, 20, 30, 40, 50]
# li=0
# for i in num:
#     li+=i
# print("Sum list:",li)

# Exercise 10
#     បង្កើត List មួយឈ្មោះ shopping_cart
#     📌 កិច្ចការ:
#     បន្ថែមទំនិញ 3 មុខ
#     លុបទំនិញ 1 មុខ
#     បង្ហាញទំនិញដែលនៅសល់
# ==========code==============
# shop=["Drink","Bread","food","coffe"]
# newShop=["Toy","Game","DVD"]
# shop.extend(newShop)
# print(shop)
# shop.remove(shop[0])
# print(shop)