from entities.enemy import Enemy

def test_enemy_speed():
    obj = Enemy(0,0)
    assert obj.speed == 7