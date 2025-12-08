def greet_person(name):
    """個人化問候函數"""
    print(f"你好，{name}!很高興見到你!")
    
def greet_person():
    """個人化問候函數"""
    name_i = input(" please input a name :")
    print(f"你好，{name}!很高興見到你!")    
# 呼叫函數
greet_person("小明")
greet_person("小華")
greet_person(name = input(" please input a name _2:"))
