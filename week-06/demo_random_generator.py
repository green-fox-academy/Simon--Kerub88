import random

def demo_random(first, mid, last, rand):
    random.shuffle(first)
    random.shuffle(mid)
    random.shuffle(last)
    random.shuffle(rand)

    final_list = []
    new_first = []
    new_mid = []
    new_last = []

    while len(final_list) <= 15:
        random_number = random.randint(1, 100)
        for i in first:
            if len(new_last) <= 2 and len(new_mid) <= 3:
                if random_number >= 50 and len(new_first) < 5:
                    new_first.append(i)
                elif 50 > random_number >= 25 and len(new_last) < 5:
                    new_last.append(i)
                else:
                    new_mid.append(i)
                first.remove(i)
            else:
                if random_number >= 34 and len(new_first) < 5:
                    new_first.append(i)
                elif 34 > random_number >= 17 and len(new_last) < 5:
                    new_last.append(i)
                else:
                    new_mid.append(i)
                first.remove(i)

        for i in mid:
            if random_number >= 50:
                new_mid.append(i)
            elif 50 > random_number >= 25 and len(new_first) < 5:
                new_first.append(i)
            else:
                new_last.append(i)
            mid.remove(i)

        for i in last:
            if len(new_first) <=2  and len(new_mid) <= 2:
                if random_number >= 50 and len(new_last) < 5:
                    new_last.append(i)
                elif 50 > random_number >= 25 and len(new_first) < 5:
                    new_first.append(i)
                else:
                    new_mid.append(i)
                last.remove(i)
            else:
                if random_number >= 34 and len(new_last) < 5:
                    new_last.append(i)
                elif 34 > random_number >= 17 and len(new_first) < 5:
                    new_first.append(i)
                else:
                    new_mid.append(i)
                first.remove(i)

        for i in rand:
            if random_number >= 67 and len(new_first) < 4:
                new_first.append(i)
            elif 66 >= random_number >= 34 and len(new_last) < 4:
                new_last.append(i)
            else:
                new_mid.append(i)
            rand.remove(i)

        if len(first) + len(mid) + len(last) + len(rand) == 0:
            final_list.append(new_first + new_mid + new_last)

    place = 0
    for i in final_list:
        place += 1
        print(str(place) + ". " + str(i[place - 1]))


first = ["Simon", "Dori", "Zsolt"]
mid = ["Fanni", "gaborvrg", "Vera"]
last = []
rand = ["SepGab", "Pati", "Dani", "Pami", "Balint", "Szilard",
"Bence", "ilcsik.balazs", "Ylwoi Balazs", "hartmann"]

demo_random(first, mid, last, rand)
