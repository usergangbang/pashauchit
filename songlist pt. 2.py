violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
x = violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress']
second_x = violator_songs_dict['Halo'] + violator_songs_dict['Enjoy the Silence'] + violator_songs_dict['Clean']
print(
    f"'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress' звучат: {x} минут, остальные три песни звучат столько: {second_x}"
        )
