from django import forms


category = [
        ('movies' ,'Movies'),
        ('series' , 'Series'),
        ('anime' , 'Anime'),
        ('tvshows', 'TV_Show')
    ]

ent_genre = [
        ('thriller','thriller'),
        ('comedy','comedy'),
        ('drama','drama'),
        ('action','action'),
        ('horror','horror'),
        ('romance','romance'),
        ('sci-fi','sci-fi')
    ]

class ent_form(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()

    entertainment_choice = forms.ChoiceField(choices=category)
    genre = forms.MultipleChoiceField(choices=ent_genre)



