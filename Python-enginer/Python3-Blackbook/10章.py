#1
class Duck:
    #クラス変数familyの定義
    family="Anatidae"

    #特殊メソッド__init__の定義
    def __init__(self):
        #インスタンス変数birdsongの定義
        self.birdsong="quack"

    #show_familyメソッドの定義
    def show_family(self):
        return f"Ducks belong to the family {self.family}."

#3
class Duck:
    def __init__(self):
        self.birdsong="quack"

    def sing(self):
        birdsong="ga-ga-"
        print(birdsong)
        print(self.birdsong)
        self.birdsong="coin"
        print(self.birdsong)
        print(birdsong)
duck=Duck()
duck.sing()
#4
#A 実行できない 
# class Duck:
#     def __init__(self):
#         self.birdsong="quack"
    
#     def change_birdsong(birdsong):
#         birdsong=birdsong
    
#     def show_birdsong():
#         print(birdsong)
#         change_birdsong("ga-ga")
#         print(birdspng)
#B
# class Duck:
#     def __init__(self):
#         self.birdsong="quack"

#     def change_birdsong(self,birdsong):
#         self.birdsong=birdsong
    
#     def shhow_birdsong(self):
#         print(birdsong)
#         change_birdsong("ga-ga")
#         print(birdsong)
#C
# class Duck:
#     def __init__(self):
#         self.birthsong="quack"

#     def change_birthsong(birthsong):
#         birthsong=birthsong
    
#     def show_birthsong():
#         print(self.birthsong)
#         self.change_birthsong("ga-ga")
#         print(self.birthsong)
#D
class Duck:
    def __init__(self):
        self.birdsong="quack"
    def change_birdsong(self,birdsong):
        self.birdsong=birdsong
    def show_birdsong(self):
        print(self.birdsong)
        self.change_birdsong("ga-ga-")
        print(self.birdsong)
