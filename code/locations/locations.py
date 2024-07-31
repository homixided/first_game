import random
from utils.utils import print_text_by_char, name, items, hp
import sys


def first_location():
    global hp
    print_text_by_char(f'{name} проснулась от пронзительного сквозняка, который пронизывал её до костей. Протерев глаза и оглядевшись, она осознала, что оказалась в незнакомом месте. Комната была погружена в зловещую тишину, наполненную пылью и паутиной, а старая мебель, покрытая слоем грязи, говорила о том, что здесь давно не убирались. Встав с кровати, {name} решила исследовать окружающее пространство. Перед ней открывались несколько вариантов действий:\n1. Заглянуть в тумбочку у кровати.\n2. Осмотреть стол.\n3. Открыть шкаф для одежды.\n4. Попробовать выйти из комнаты.')
    while True:
        print_text_by_char('Выберите действие (1-4):')
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print_text_by_char('Пожалуйста, введите число от 1 до 4.')
            continue

        if choice == 1:
            if not items['bandage']:
                print_text_by_char(f'Вы осмотрели тумбочку и нашли бинт. Теперь вы сможете подлатать себя во время дуэли. (+3 HP). Новое количество HP: {hp + 3}')
                items['bandage'] = True
                hp += 3
            else:
                print_text_by_char('Вы уже осмотрели тумбочку.')
        
        elif choice == 2:
            if not items['key']:
                print_text_by_char('Вы осмотрели стол и нашли ключ от двери.')
                items['key'] = True
            else:
                print_text_by_char('Вы уже осмотрели стол.')
        
        elif choice == 3:
            if not items['armor']:
                print_text_by_char(f'Вы осмотрели шкаф и нашли старинный костюм. Надев его, вы чувствуете себя защищеннее. (+2 HP). Новое количество HP: {hp + 2}')
                items['armor'] = True
                hp += 2
            else:
                print_text_by_char('Вы уже осмотрели шкаф.')
        
        elif choice == 4:
            if items['key']:
                print_text_by_char('Вы используете ключ и выходите из комнаты.')
                break
            else:
                print_text_by_char('Дверь заперта. Найдите ключ, чтобы выйти.')
        else:
            print_text_by_char('Пожалуйста, выберите число от 1 до 4.')

    print_text_by_char('Вы успешно покинули комнату.')
    second_location()

def second_location():
    global hp, dialog_played

    if not dialog_played:
        print_text_by_char(f'На диване сидел таинственный мужчина в тёмном плаще, его лицо было скрыто под капюшоном, из-под которого сверкающие глаза пристально следили за вами. Хотя его внешний вид внушал страх, его голос звучал спокойно и дружелюбно:\n"Меня зовут Антон. Ты понимаешь, почему ты здесь?"\nВы отрицательно качаете головой.\n"Это место - лишь сон, но замок этот проклят. В его стены попадают те, кто не в силах преодолеть свои страхи. Я помогу тебе, но все испытания ты должна пройти сама, {name}."\nОн продолжил: "Помни, это всего лишь сон. Если ты не справишься, больше никогда не проснешься. Если же преодолеешь свои страхи, тебя ждет счастливая жизнь. Действуй разумно, и когда будешь готова, возвращайся ко мне."')
        dialog_played = True
    else:
        print_text_by_char('Вы вернулись обратно в главную комнату.')

    while True:
        print_text_by_char('Выберите действие (1-4):\n1. Вернуться в свою комнату.\n2. Поговорить с Антоном.\n3. Зайти на кухню.\n4. Зайти в гостевой зал.')
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print_text_by_char('Пожалуйста, введите число от 1 до 4.')
            continue

        if choice == 1:
            print_text_by_char('Вы вернулись в свою комнату.')
            first_location()
            break
            

        elif choice == 2:
            print_text_by_char('Вы решили поговорить с Антоном дальше.')
            if items['kitchen_knife'] and items['wall_sword']:
                print_text_by_char('Ты готова к битве.')
                pre_boss_battle()
            else:
                print_text_by_char('Отправляйтесь на кухню или в гостевой зал и найдите оружие, прежде чем начинать битву.')
            continue

        elif choice == 3:
            print_text_by_char('Вы зашли на кухню.\nВыберите действие (1-3):\n1. Заглянуть в холодильник.\n2. Заглянуть в шкафчик.\n3. Вернуться в главную комнату.')
            try:
                choice2 = int(input())
            except ValueError:
                print_text_by_char('Пожалуйста, введите число от 1 до 3.')
                continue

            if choice2 == 1:
                if not items['apple_juice']:
                    print_text_by_char(f'Вы нашли яблочный сок и выпили его. (+2 HP). Новое количество HP: {hp + 2}')
                    hp += 2
                    items['apple_juice'] = True
                else:
                    print_text_by_char('Вы уже осмотрели холодильник.')
            elif choice2 == 2:
                if not items['kitchen_knife']:
                    print_text_by_char('Вы нашли кухонный нож. Он даст вам +2 HP к наносимому урону.')
                    items['kitchen_knife'] = True
                else: 
                    print_text_by_char('Вы уже осмотрели шкаф.')
            elif choice2 == 3:
                print_text_by_char('Вы вернулись обратно в главную комнату.')
                continue

        elif choice == 4:
            print_text_by_char('Вы зашли в гостевой зал.\nВыберите действие (1-3):\n1. Сыграть на пианино.\n2. Осмотреть камин.\n3. Вернуться в главную комнату.')
            try:
                choice3 = int(input())
            except ValueError:
                print_text_by_char('Пожалуйста, введите число от 1 до 3.')
                continue

            if choice3 == 1:
                print_text_by_char('Вы сыграли на пианино. Антон оценил ваши старания.')
            
            elif choice3 == 2:
                if not items['wall_sword']:
                    print_text_by_char('Вы осмотрели камин и нашли над ним старый настенный меч.')
                    items['wall_sword'] = True
                else: 
                    print_text_by_char('Вы уже осмотрели камин.')
        
            elif choice3 == 3:
                print_text_by_char('Вы вернулись обратно в главную комнату.')
                continue
            
        else:
            print_text_by_char('Пожалуйста, выберите число от 1 до 4.')

        if items['kitchen_knife'] and items['wall_sword']:
            print_text_by_char('Вы нашли все необходимые предметы для битвы. Теперь Вы готовы встретиться со своими страхами.')
            continue

def pre_boss_battle():
    print_text_by_char(f'Вы отправились по темному коридору, вокруг начали мелькать неизвестные страшные силуэты. Но {name} продолжала идти, чувствуя в себе силу и решимость.')
    print_text_by_char('Вдруг перед вами предстала тень, которая изменила свой облик на нечто ужасающее и зловещее. Это был босс, главный враг в этом странном сне.')
    fight_boss()

def fight_boss():
    global hp, items
    boss_hp = 20
    knife_used = items['kitchen_knife']
    sword_used = items['wall_sword']
    player_choice = None

    count_knife = 0
    count_sword = 0

    print_text_by_char(f'Битва началась! У вас {hp} HP, у босса {boss_hp} HP.')
    while hp > 0 and boss_hp > 0:
        print_text_by_char(f'Выберите действие:\n1. Ударить ножом дважды.\n2. Ударить мечом один раз.\n3. Похилиться.\n4. Атаковать руками.')

        try:
            player_choice = int(input())
        except ValueError:
            print_text_by_char('Пожалуйста, введите число от 1 до 4.')
            continue

        if player_choice == 1 and knife_used:
            if count_knife >= 2:
                print_text_by_char('Вы больше не можете использовать нож.')
            else:
                first_hit = random.randint(3, 5) + random.randint(1, 2)
                second_hit = random.randint(3, 5) + random.randint(1, 2)
                total_damage = first_hit + second_hit
                print_text_by_char(f'Вы атаковали ножом дважды и нанесли {total_damage} урона.')
                boss_hp -= total_damage
                count_knife += 1

        elif player_choice == 2 and sword_used:
            if count_sword >= 1:
                print_text_by_char('Вы больше не можете использовать меч.')
            else:
                damage = random.randint(3, 4) + random.randint(2, 4)
                print_text_by_char(f'Вы атаковали мечом и нанесли {damage} урона.')
                boss_hp -= damage
                count_sword += 1

        elif player_choice == 3:
            heal_amount = 3
            hp += heal_amount
            print_text_by_char(f'Вы использовали бинт и восстановили {heal_amount} HP. Текущие HP: {hp}')

        elif player_choice == 4:
            damage = random.randint(2, 4)
            print_text_by_char(f'Вы атаковали руками и нанесли {damage} урона.')
            boss_hp -= damage

        else:
            print_text_by_char('Вы выбрали недопустимое действие.')
            continue

        boss_attack = random.randint(2, 6)
        hp -= boss_attack
        print_text_by_char(f'Босс атакует и наносит {boss_attack} урона.')

        if hp <= 0:
            print_text_by_char('Сражение было ожесточенным и безжалостным. Удары босса становились всё более сокрушительными, и, несмотря на все усилия, герой не смог устоять. Антон, со слезами на глазах, наблюдал, как герой исчезает в бездну, но в его сердце оставалась надежда, что однажды, в другой жизни, герою удастся победить.')
            print_text_by_char('Вы погибли. Игра окончена.')
            sys.exit()

        elif boss_hp <= 0:
            print_text_by_char(f'Последний удар был нанесен, и босс, издавая ужасающий рёв, пал перед героем. Антон, появившись из тени, подошёл к герою и, с улыбкой на лице, протянул руку.\n"Ты справилась, {name}. Ты преодолела свои страхи и победила проклятие этого места. Теперь ты свободна." ')
            print_text_by_char('Вы победили босса! Поздравляем!')
            sys.exit()