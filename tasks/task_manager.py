#1. create_student_tuple fonksiyonu name, age ve house değişkenlerini bir tuple olarak dönmelidir.
def create_student_tuple(name, age, house):
    return (name, age, house)

#2. add_spell_to_set fonksiyonu 2 parametre alır (spell_set bir set veri yapısıdır) ve new_spell. Görevin new_spell değerini spell_set kümesine eklemektir.
# spell_set değerini geri döndürmeyi unutma.
def add_spell_to_set(spell_set, new_spell):
    spell_set.add(new_spell)
    return spell_set 

#3. remove_forbidden_item fonksiyonu 2 parametre alır (forbidden_items bir set veri yapısıdır) ve item. Görevin item değerini forbidden_items kümesinden çıkarmaktır.
# forbidden_items değerini geri döndürmeyi unutma.
def remove_forbidden_item(forbidden_items, item):
    forbidden_items.remove(item)
    return forbidden_items

#4. count_students_per_house student_list isminde ve list tipinde bir parametre alır. 
# students = [("Harry", "Gryffindor"), ("Draco", "Slytherin"), ("Ron", "Gryffindor"), ("Myrtle Warren", "Ravenclaw")]
# Amacımız her house için toplamda kaç öğrenci olduğunu bulmak.
# İşlemi yaptıktan sonra fonksiyonda döndüğün değer şu şekilde olmalı. {"Gryffindor": 2, "Slytherin": 1, "Ravenclaw": 1}
def count_students_per_house(students_list):
    house_counts = {}
    for name, house in students_list:
        if house in house_counts:
            house_counts[house] += 1
        else:
            house_counts[house] = 1
    return house_counts

#5. house_with_most_students house_dict isminde bir parametre alır.(veri tipi olarak bu bir dictionary tipidir)
# Değeri şu şekildedir. house_dict = {"Gryffindor": 8, "Slytherin": 10, "Ravenclaw": 9}
# Görevin en çok öğrencisi olan grubun ismini dönmektir.  Yukardaki örnek için fonksiyon 'Slytherin' değerini dönmelidir.
def house_with_most_students(house_dict):
    max_students = -1
    max_house = ""

    for house, count in house_dict.items():
        if count > max_students:
            max_students = count
            max_house = house

    return max_house


#6. student_summary fonksiyonu student_tuple isminide tuple tipindedir. içeriği (name, age, house) şeklindedir.
#Örnek Değeri student_tuple = ('Harry', 15, 'Gryffindor') şeklindedir.
#Fonskiyon bu tuple değerinden şu şekilde bir string değerini dönmelidir. 'Harry, age 15, is in Gryffindor.'
def student_summary(student_tuple):
    name, age, house = student_tuple
    return f"{name}, age {age}, is in {house}."


#7. merge_spell_sets fonksiyonu 2 tane set tipinde input almaktadırlar. 
# Görevimiz bu iki kümenin verilerini birleştirip yine bir set olacak şekilde geri dönmektir.
# örnek:  set1 = {"Lumos", "Alohomora"} set2 = {"Accio", "Alohomora"} => fonksiyonun dönüşü: {"Lumos", "Accio", "Alohomora"}
def merge_spell_sets(set1, set2):
    union_set = set1.union(set2)
    return union_set


#8. create_student_dict fonksiyonu 3 tane input almaktadır. name değeri 'string', age değeri 'number', spells değeride bir set olacak şekilde.
# Görevin bütün bu değerleri içerisinde toplayan bir dictionary olarak bu veriyi geri dönmektir.
# Örek Output:  {"name": "Harry", "age": 16, "spells": {"Lumos", "Alohomora"}}
def create_student_dict(name, age, spells):
    student = {
        "name": name,
        "age": age,
        "spells": spells
    }
    return student 

#9. Hogwarts'da bir öğrencinin derse girerken bulundurabileceği eşyalar bellidir. 
# Görevin bu eşyaların kontrolünü sağlamak. is_student_allowed fonskiyonu öğrencinin üzerindeki eşyaları içeren bir set veri yapsıdır.
# forbidden_items ise öğrencinin içeri sokması yasaklı olan eşyaları içeren bir set veri yapısıdır.
# Eğer öğrencinin eşyaları bu yasaklı listeden birini dahi içeriyorsa öğrenci derse sokulmamalıdır.
# is_student_allowed fonksiyonunda bu işlemi gerçekleştirmeye çalış. Fonksiyon boolean bir değer dönmelidir.
def is_student_allowed(item_set, forbidden_items):
    if item_set.intersection(forbidden_items):
        return False
    else:
        return True


#10 Hogwarts'da verilen öğrenci listesinden sadece belli bir eve ait olanları almak istiyoruz.
# bunun için fonksiyon 2 tane parametre almaktadır. Bunlardan ilki students listesi ve ikincisi öğrencilerin hangi evden alınacağı.
# Örnek input:
# # students = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Hermione", "house": "Gryffindor"}
# ]
# Output:
#  [
#   {"name": "Harry", "house": "Gryffindor"},
#   {"name": "Hermione", "house": "Gryffindor"}
# ]
def filter_students_by_house(students, house_name):
    return [student for student in students if student.get("house") == house_name]
