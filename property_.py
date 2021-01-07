class Player:

    def __init__(self, name):
        # '_'　隠蔽していることを示す
        # 完全の隠蔽ではない
        self._name = name

    # 'player.name()'の代わりに
    # 'player.name' が使えるように
    @property
    def name(self):
        return str(self._name)

    @name.setter
    def name(self, name):
        self._name = name


player = Player("Alice")

# pythonのオブジェクトは属性がなくても、値の付与はできる
player.family_name = "Bob"
# @property修飾される名前ですので、値の付与はできません
player.name = "Bob"

# 'name' という偽属性を利用できる
print(player.name)

# setもgetもできますが、
# [こうしないでください]を示すための'_'
player._name = "Chris"
print(player._name)
