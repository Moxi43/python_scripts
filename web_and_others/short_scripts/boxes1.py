def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_throught()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('FOUND THE KEY!')


print (look_for_key(main_box))           
