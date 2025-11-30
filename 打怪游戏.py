import random
monsters = [
    ["哥布林杂兵", 120],
    ["骷髅弓箭手", 280],
    ["石巨人守卫", 550],
    ["深渊恶魔", 920],
    ["BOSS·熔岩龙", 1500]
]
your_hp = 500
your_exp = 0
total_exp = 0
print(f"你的初始血量是{your_hp}")
for monster in monsters:
    name = monster[0]
    hp = monster[1]
    print(f"第{monsters.index(monster)+1}战开始，{name}出现，血量{hp}")
    while your_hp > 0 and hp > 0:
        damage = random.randint(100,1000)
        hp -= damage
        if hp<0:
            hp = 0
        print(f"你对{name}做出攻击造成了{damage}伤害，剩余{hp}血量")
        if hp>0:
            monster_damage = random.randint(30,80)
            your_hp -= monster_damage
            if your_hp<0:
                your_hp=0
            print(f"{name}反击，对你造成了{monster_damage}伤害，你还剩余{your_hp}")
    if your_hp <= 0:
        print("你死了")
        break
    else:
         your_exp = monster[1]//10
         total_exp += your_exp
         print(f"你击败了{name}，获得{your_exp}经验")
else:
    print(f"恭喜通关，总共获得{total_exp}经验值")
    print(f"最终剩余{your_hp}，你已升级至LV.{total_exp//100}.")
print(f"游戏结束")