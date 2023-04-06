#Sweety

# main need module for basic create Animal_app
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

#there some extra modules are need for this animal app
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.utils.fitimage import FitImage
from kivy.uix.label import Label

#extr from out of kivy modules
import random

# this is a design file
Builder.load_file('desing.kv')

# minimum size of window
Window.size = (534,550)

# some out of def function 
like = []
liber = []
fav = []
history = []
alubm_cloumn = [
    # id of heart,hand,book

    # 'heart_','hand_','book_'
    [['cat','heart_cat_o','hand_cat_o','book_cat_o'],['dog','heart_dog_o','hand_dog_o','book_dog_o'],
    ['cow','heart_cow_o','hand_cow_o','book_cow_o'],['horse','heart_horse_o','hand_horse_o','book_horse_o'],
    ['monkey','heart_monkey_o','hand_monkey_o','book_monkey_o'],['wolf','heart_wolf_o','hand_wolf_o','book_wolf_o']],

    [['cat','heart_cat_t','hand_cat_t','book_cat_t'],['dog','heart_dog_t','hand_dog_t','book_dog_t'],
    ['rabbit','heart_rabbit_o','hand_rabbit_o','book_rabbit_o'],['parrot','heart_parrot_o','hand_parrot_o','book_parrot_o'],
    ['hamster','heart_parrot_o','hand_parrot_o','book_parrot_o'],['turtle','heart_turtle_o','hand_turtle_o','book_turtle_o']],
    
    [['whale','heart_whale_o','hand_whale_o','book_whale_o'],['turtle','heart_turtle_t','hand_turtle_t','book_turtle_t'],
    ['dolphin','heart_dolphin_o','hand_dolphin_o','book_dolphin_o'],['alligator','heart_alligator_o','hand_alligator_o','book_alligator_o'],
    ['crab','heart_crab_o','hand_crab_o','book_crab_o'],['seal','heart_seal_o','hand_seal_o','book_seal_o']],
    
    [['penguin','heart_penguin_o','hand_penguin_o','book_penguin_o'],['peacock','heart_peacock_o','hand_peacock_o','book_peacock_o'],
    ['chicken','heart_chicken_o','hand_chicken_o','book_chicken_o'],['parrot','heart_parrot_t','hand_parrot_t','book_parrot_t'],
    ['owl','heart_owl_o','hand_owl_o','book_owl_o'],['crow','heart_crow_o','hand_crow_o','book_crow_o']],
    
    [['monkey','heart_monkey_t','hand_monkey_t','book_monkey_t'],['donkey','heart_donkey_o','hand_donkey_o','book_donkey_o'],
    ['elephant','heart_elephant_o','hand_elephant_o','book_elephant_o'],['bull','heart_bull_o','hand_bull_o','book_bull_o'],
    ['zebra','heart_zebra_o','hand_zebra_o','book_zebra_o'],['deer','heart_deer_o','hand_deer_o','book_deer_o']],
    
    [['cow','heart_cow_t','hand_cow_t','book_cow_t'],['dog','heart_dog_th','hand_dog_th','book_dog_th'],
    ['wolf','heart_wolf_t','hand_wolf_t','book_wolf_t'],['monkey','heart_monkey_th','hand_monkey_th','book_monkey_th'],
    ['lion','heart_lion_o','hand_lion_o','book_lion_o'],['horse','heart_horse_t','hand_horse_t','book_horse_t']],
    
    [['turtle','heart_turtle_th','hand_turtle_th','book_turtle_th'],['crab','heart_crab_t','hand_crab_t','book_crab_t'],
    ['snake','heart_snake_o','hand_snake_o','book_snake_o'],['frog','heart_frog_o','hand_frog_o','book_frog_o'],
    ['alligator','heart_alligator_t','hand_alligator_t','book_alligator_t'],['seal','heart_seal_t','hand_seal_t','book_seal_t']],
    
    [['giraffe','heart_giraffe_o','hand_giraffe_o','book_giraffe_o'],['elephant','heart_elephant_t','hand_elephant_t','book_elephant_t'],
    ['whale','heart_whale_t','hand_whale_t','book_whale_t'],['gorilla','heart_gorilla_o','hand_gorilla_o','book_gorilla_o'],
    ['bull','heart_bull_t','hand_bull_t','book_bull_t'],['cow','heart_cow_th','hand_cow_th','book_cow_th']],
    
    [['frog','heart_frog_t','hand_frog_t','book_frog_t'],['mouse','heart_mouse_o','hand_mouse_o','book_mouse_o'],
    ['owl','heart_owl_t','hand_owl_t','book_owl_t'],['monkey','heart_monkey_f','hand_monkey_f','book_monkey_f'],
    ['rabbit','heart_rabbit_t','hand_rabbit_t','book_rabbit_t'],['parrot','heart_parrot_th','hand_parrot_th','book_parrot_th']],
]


# there are this three Screen 
#frist main screen
class Main(Screen):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

        animal_fav = ObjectProperty()
        animal_history = ObjectProperty()
        animal_liber = ObjectProperty()
        animal_like = ObjectProperty()

        none_id_o = ObjectProperty()
        none_id_t = ObjectProperty()
        none_id_th = ObjectProperty()
        none_id_f = ObjectProperty()

        self.listss = []


        # lists of animal include in  this project
        self.Animal_name = [['bull',["anima/bull/food.txt","anima/bull/image.txt","anima/bull/note.txt","anima/bull/.elk.jpg", "anima/bull/sound.txt"]],
        ['cat',["anima/cat/food.txt","anima/cat/image.txt","anima/cat/note.txt","anima/cat/.cute cats.jpg", "anima/cat/sound.txt"]],
        ['cow',["anima/cow/food.txt","anima/cow/image.txt","anima/cow/note.txt","anima/cow/.sahiwal cattle.jpg", "anima/cow/sound.txt"]],
        ['dog',["anima/dog/food.txt","anima/dog/image.txt","anima/dog/note.txt","anima/dog/.german shepherd.jpg", "anima/dog/sound.txt"]],
        ['horse',["anima/horse/food.txt","anima/horse/image.txt","anima/horse/note.txt","anima/horse/.andalusian horse.jpg", "anima/horse/sound.txt"]],
        ['crab',["anima/crab/food.txt","anima/crab/image.txt","anima/crab/note.txt","anima/crab/.cancer pagurus.jpg", "anima/crab/sound.txt"]],
        ['wolf',["anima/wolf/food.txt","anima/wolf/image.txt","anima/wolf/note.txt","anima/wolf/.eurasian wolf.jpg", "anima/wolf/sound.txt"]], 
        ['monkey',["anima/monkey/food.txt","anima/monkey/image.txt","anima/monkey/note.txt","anima/monkey/.vervet monkey.jpg", "anima/monkey/sound.txt"]], 
        ['parrot',["anima/parrot/food.txt","anima/parrot/image.txt","anima/parrot/note.txt","anima/parrot/.lovebirds.jpg", "anima/parrot/sound.txt"]], 
        ['rabbit',["anima/rabbit/food.txt","anima/rabbit/image.txt","anima/rabbit/note.txt","anima/rabbit/.flemish giant rabbit.jpg", "anima/rabbit/sound.txt"]], 
        ['seal',["anima/seal/food.txt","anima/seal/image.txt","anima/seal/note.txt","anima/seal/.harbor seal.jpg", "anima/seal/sound.txt"]], 
        ['turtle',["anima/turtle/food.txt","anima/turtle/image.txt","anima/turtle/note.txt","anima/turtle/.green sea turtle.jpg", "anima/turtle/sound.txt"]],
        ['whale',["anima/whale/food.txt","anima/whale/image.txt","anima/whale/note.txt","anima/whale/.gray whale.jpg", "anima/whale/sound.txt"]], 
        ['hamster',["anima/hamster/food.txt","anima/hamster/image.txt","anima/hamster/note.txt","anima/hamster/.syrian hamster.jpg", "anima/hamster/sound.txt"]],
        ['chicken',["anima/chicken/food.txt","anima/chicken/image.txt","anima/chicken/note.txt","anima/chicken/.brahma.jpg", "anima/chicken/sound.txt"]],
        ['crow',["anima/crow/food.txt","anima/crow/image.txt","anima/crow/note.txt","anima/crow/.torresian crow.jpg", "anima/crow/sound.txt"]],
        ['elephant',["anima/elephant/food.txt","anima/elephant/image.txt","anima/elephant/note.txt","anima/elephant/.loxodonta atlantica.jpg", "anima/elephant/sound.txt"]], 
        ['dolphin',["anima/dolphin/food.txt","anima/dolphin/image.txt","anima/dolphin/note.txt","anima/dolphin/.dolphin.jpg", "anima/dolphin/sound.txt"]], 
        ['penguin',["anima/penguin/food.txt","anima/penguin/image.txt","anima/penguin/note.txt","anima/penguin/.adélie penguin.jpg", "anima/penguin/sound.txt"]], 
        ['deer',["anima/deer/food.txt","anima/deer/image.txt","anima/deer/note.txt","anima/deer/.roe deer.jpg", "anima/deer/sound.txt"]],
        ['snake',["anima/snake/food.txt","anima/snake/image.txt","anima/snake/note.txt","anima/snake/.black mamba.jpg", "anima/snake/sound.txt"]],
        ['lion',["anima/lion/food.txt","anima/lion/image.txt","anima/lion/note.txt","anima/lion/.transvaal lion.jpg", "anima/lion/sound.txt"]], 
        ['frog',["anima/frog/food.txt","anima/frog/image.txt","anima/frog/note.txt","anima/frog/.hylidae.jpg", "anima/frog/sound.txt"]], 
        ['giraffe',["anima/giraffe/food.txt","anima/giraffe/image.txt","anima/giraffe/note.txt","anima/giraffe/.northern giraffe.jpg", "anima/giraffe/sound.txt"]], 
        ['owl',["anima/owl/food.txt","anima/owl/image.txt","anima/owl/note.txt","anima/owl/.eastern screech owl.jpg", "anima/owl/sound.txt"]],
        ['zebra',["anima/zebra/food.txt","anima/zebra/image.txt","anima/zebra/note.txt","anima/zebra/.chapman's zebra.jpg", "anima/zebra/sound.txt"]], 
        ['donkey',["anima/donkey/food.txt","anima/donkey/image.txt","anima/donkey/note.txt","anima/donkey/.mule donkey.jpg", "anima/donkey/sound.txt"]], 
        ['gorilla',["anima/gorilla/food.txt","anima/gorilla/image.txt","anima/gorilla/note.txt","anima/gorilla/.western gorilla.jpg", "anima/gorilla/sound.txt"]],
        ['peacock',["anima/peacock/food.txt","anima/peacock/image.txt","anima/peacock/note.txt","anima/peacock/.indian peafowl.jpg", "anima/peacock/sound.txt"]],
        ['mouse',["anima/mouse/food.txt","anima/mouse/image.txt","anima/mouse/note.txt","anima/mouse/.house mouse.jpg", "anima/mouse/sound.txt"]], 
        ['alligator',["anima/alligator/food.txt","anima/alligator/image.txt","anima/alligator/note.txt","anima/alligator/.alligator.jpg", "anima/alligator/sound.txt"]]]
        self.num = 0                  #for sidler image

        Clock.schedule_interval(self.side_image, 8)
    
    # In like list to remove albumn with help delete button
    def like_remove(self, instance):

        # to remove with help of delete icon
        name = instance.text

        for li in like:
            if li[0]==name:
                like.pop(like.index([name,li[1]]))
        
        n = [name+"ani_like"]
        m = self.ids[n[0]]
        self.ids.animal_like.remove_widget(m)
        anin_like = self.ids.animal_like
        anin_like.height-=30

        #butto  icon change
        for line in alubm_cloumn:
            for word in line:
                if name==word[0]:
                    self.ids[word[1]].icon="heart-circle"
    
    def like_remove_bot(self,name):
        
        id_name = name+"ani_like"
        m = self.ids[id_name]

        for li in like:
            if li[0]==name:
                like.pop(like.index([name,li[1]]))

        self.ids.animal_like.remove_widget(m)
        anin_like = self.ids.animal_like
        anin_like.height-=30

    # out like list to remove and add album with help of like
    def like_list(self,name):
        for animal in self.Animal_name:
            if name==animal[0]:
                if [name,animal[1][3]] in like:
                    like.pop(like.index([name,animal[1][3]]))

                    n = [animal[0]+"ani_like"]
                    m = self.ids[n[0]]
                    self.ids.animal_like.remove_widget(m)
                    anin_like = self.ids.animal_like
                    anin_like.height-=30


                    # change icon of all the same animal in every album 
                
                    for line in alubm_cloumn:
                        for word in line:
                            if name==word[0]:
                                self.ids[word[1]].icon="heart-circle"

                            else:pass
                     
                else:
                    n_list = [name,animal[1][3]]
                    like.append(n_list)

                    # change icon of all the same animal in every album 

                    for line in alubm_cloumn:
                        for word in line:
                            if name==word[0]:
                                self.ids[word[1]].icon="heart-circle-outline"
                            else:pass


                    # this is for create alubum and add like list

                    self.ids.None_id_o.text = "[size=50][b]+[/b][/size]"
                    anin_like = self.ids.animal_like
                    anin_like.height+=30

                    like_Card = MDCard(orientation='vertical', size_hint=(None,None), size=(150,170), radius=[20])
                    like_Card.text = animal[0]
                    like_Card.bind(on_release=lambda btn: self.cardmd(like_Card))
                    ani_img = FitImage(source=animal[1][3], radius=[20])
                    icon_b  = MDIconButton(icon="delete")
                    icon_b.pos_hint = {"center_x":0.5}
                    icon_b.bind(on_release=lambda btn: self.like_remove(like_Card))

                    like_Card.add_widget(ani_img)
                    like_Card.add_widget(icon_b)
                    self.ids[str(animal[0]+"ani_like")] = like_Card
        
                    self.ids.animal_like.add_widget(like_Card)

    # In favorite list to remove albumn with help delete button
    def fav_remove(self, instance):

        # to remove with help of delete icon
        name = instance.text

        for li in fav:
            if li[0]==name:
                fav.pop(fav.index([name,li[1]]))

        n = [name+"ani_fav"]
        m = self.ids[n[0]]
        self.ids.animal_fav.remove_widget(m)

        anin_like = self.ids.animal_fav
        anin_like.height-=30

        #button icon change
        for line in alubm_cloumn:
            for word in line:
                if name==word[0]:
                    self.ids[word[2]].icon="hand-heart"

    def fav_remove_bot(self,name):

        id_name = name+"ani_fav"
        m = self.ids[id_name]

        for li in fav:
            if li[0]==name:
                fav.pop(fav.index([name,li[1]]))

        self.ids.animal_fav.remove_widget(m)
        anin_like = self.ids.animal_fav
        anin_like.height-=30

    # out favorite list to remove and add album with help of favorite
    def fav_list(self,name):
        for animal in self.Animal_name:
            if name==animal[0]:
                if [name,animal[1][3]] in fav:
                    fav.pop(fav.index([name,animal[1][3]]))

                    n = [animal[0]+"ani_fav"]
                    m = self.ids[n[0]]
                    self.ids.animal_fav.remove_widget(m)

                    anin_like = self.ids.animal_fav
                    anin_like.height-=30

                    # change icon of all the same animal in every album 
                    for line in alubm_cloumn:
                        for word in line:
                            if name==word[0]:
                                self.ids[word[2]].icon="hand-heart"
                            else:pass

                else:
                    n_list = [name,animal[1][3]]
                    fav.append(n_list)

                    # change icon of all the same animal in every album 
                    for line in alubm_cloumn:
                        for word in line:
                            if name==word[0]:
                                self.ids[word[2]].icon="hand-heart-outline"
                            else:pass

                    # this is for create alubum and add in favourite list

                    self.ids.None_id_t.text = "[size=50][b]+[/b][/size]"
                    anin_like = self.ids.animal_fav
                    anin_like.height+=30

                    Fav_Card = MDCard(orientation='vertical', size_hint=(None,None), size=(150,180), radius=[20])
                    Fav_Card.text = animal[0]
                    Fav_Card.bind(on_release=lambda btn: self.cardmd(Fav_Card))
                    ani_img = FitImage(source=animal[1][3], radius=[20])
                    icon_b  = MDIconButton(icon="delete")
                    icon_b.pos_hint = {"center_x":0.5}
                    icon_b.bind(on_release=lambda btn: self.fav_remove(Fav_Card))

                    Fav_Card.add_widget(ani_img)
                    Fav_Card.add_widget(icon_b)
                    self.ids[str(animal[0]+"ani_fav")] = Fav_Card

                    self.ids.animal_fav.add_widget(Fav_Card)

    # In libery list to remove albumn with help delete button
    def liber_remove(self, instance):

        # to remove with help of delete icon
        name = instance.text

        for li in liber:
            if li[0]==name:
                liber.pop(liber.index([name,li[1]]))

        n = [name+"ani_liber"]
        m = self.ids[n[0]]
        self.ids.animal_liber.remove_widget(m)

        anin_like = self.ids.animal_liber
        anin_like.height-=30

        #button icon change
        for line in alubm_cloumn:
            for word in line:
                if name==word[0]:
                    self.ids[word[3]].icon="bookmark"
    
    def liber_remove_bot(self,name):

        id_name = name+"ani_liber"
        m = self.ids[id_name]

        for li in like:
            if li[0]==name:
                like.pop(like.index([name,li[1]]))

        self.ids.animal_liber.remove_widget(m)
        anin_like = self.ids.animal_liber
        anin_like.height-=30

    # out libery list to remove and add album with help of libery
    def liber_list(self,name):
        for animal in self.Animal_name:
            if name==animal[0]:
                if [name,animal[1][3]] in liber:
                    liber.pop(liber.index([name,animal[1][3]]))

                    n = [animal[0]+"ani_liber"]
                    m = self.ids[n[0]]
                    self.ids.animal_liber.remove_widget(m)
                    anin_like = self.ids.animal_liber
                    anin_like.height-=30

                    # change icon of all the same animal in every album 
                    for line in alubm_cloumn:
                        for word in line:
                            if name==word[0]:
                                self.ids[word[3]].icon="bookmark"
                            else:pass

                else:
                    n_list = [name,animal[1][3]]
                    liber.append(n_list)

                    # change icon of all the same animal in every album 
                    for line in alubm_cloumn:
                        for word in line:
                            if name==word[0]:
                                self.ids[word[3]].icon="bookmark-check"
                            else:pass

                    # this is for create alubum and add in libery list

                    self.ids.None_id_th.text = "[size=50][b]+[/b][/size]"
                    anin_like = self.ids.animal_liber
                    anin_like.height+=30

                    Liber_Card = MDCard(orientation='vertical', size_hint=(None,None), size=(150,180), radius=[20])
                    Liber_Card.text = animal[0]
                    Liber_Card.bind(on_release=lambda btn: self.cardmd(Liber_Card))
                    ani_img = FitImage(source=animal[1][3], radius=[20])
                    icon_b  = MDIconButton(icon="delete")
                    icon_b.pos_hint = {"center_x":0.5}
                    icon_b.bind(on_release=lambda btn: self.liber_remove(Liber_Card))
                    
                    Liber_Card.add_widget(ani_img)
                    Liber_Card.add_widget(icon_b)
                    self.ids[str(animal[0]+"ani_liber")] = Liber_Card

                    self.ids.animal_liber.add_widget(Liber_Card)

    #on the click of album of animal after go in history
    def history_list(self, instance):
        name = instance.text

        for animal in self.Animal_name:
            if name == animal[0]:

                history.append([name,animal[1][3]])

                self.ids.None_id_f.text = "[size=50][b]+[/b][/size]"
                anin_like = self.ids.animal_liber
                anin_like.height+=20

                His_Card = MDCard(orientation='vertical', size_hint=(None,None), size=(150,180), radius=[20])
                His_Card.text = animal[0]
                His_Card.bind(on_release=lambda btn: self.cardmd(His_Card))
                ani_img = FitImage(source=animal[1][3], radius=[20])
                label_img = Label(text="[b]Open[/b]",size_hint=(None,None), size=(150,40),halign="center",markup=True)
                    
                His_Card.add_widget(ani_img)
                His_Card.add_widget(label_img)
                self.ids[str(animal[0]+"ani_liber")] = His_Card
            
                self.ids.animal_history.add_widget(His_Card)

    #----------------music to play--------------------#     
    def muisc(self,obj):
        if self.sound.state == "play":
            self.sound.stop()
        else:
            self.sound.loop = True
            self.sound.play()

    def muisc1(self,obj):
        if self.sound0.state == "play":
            self.sound0.stop()
            print(self.sound0)
        else:
            self.sound0.loop = True
            self.sound0.play()
            print(self.sound0)

    def muisc2(self,obj):
        if self.sound1.state == "play":
            self.sound1.stop()
        else:
            self.sound1.loop = True
            self.sound1.play()
    
    def muisc3(self,obj):
        if self.sound2.state == "play":
            self.sound2.stop()
        else:
            self.sound2.loop = True
            self.sound2.play()
    
    def muisc4(self,obj):
        if self.sound3.state == "play":
            self.sound3.stop()
        else:
            self.sound3.loop = True
            self.sound3.play()

    def muisc5(self,obj):
        if self.sound4.state == "play":
            self.sound4.stop()
        else:
            self.sound4.loop = True
            self.sound4.play()

    def muisc6(self,obj):
        if self.sound5.state == "play":
            self.sound5.stop()
        else:
            self.sound5.loop = True
            self.sound5.play()

    def muisc7(self,obj):
        if self.sound6.state == "play":
            self.sound6.stop()
        else:
            self.sound6.loop = True
            self.sound6.play()
    
    def muisc8(self,obj):
        if self.sound7.state == "play":
            self.sound7.stop()
        else:
            self.sound7.loop = True
            self.sound7.play()
        
    def muisc9(self,obj):
        if self.sound8.state == "play":
            self.sound8.stop()
        else:
            self.sound8.loop = True
            self.sound8.play()

    #side of image in top of side
    def side_image(self, interval):
        side = self.ids.siler

        if self.num <= 5:
            side.index = self.num
            self.num+=1
        else:
            self.num = 0

    def cardmd(self, instance):
        
        self.manager.current = "animal"

        m = instance.text

        random.shuffle(self.Animal_name)

        new_anima_name = []
        
        for i in range(3):
            new_anima_name.append(self.Animal_name[i])
        
        self.RandomAnime(new_anima_name)

        for name in self.Animal_name:
            if m == name[0]:
                self.run_from(name[1][0],name[1][1],name[1][2],name[1][3],name[1][4])

            else:print("none")           
    
    # to change random animal
    def RandomAnime(self, lists):
        self.listss = lists
        anima = self.manager.get_screen("animal")

        cardsid = [anima.cards_o,anima.cards_t,anima.cards_th]
        cards_image_id = [anima.card_image_o,anima.card_image_t,anima.card_image_th]
        
        for i in range(3):
            cardsid[i].text = lists[i][0]
            cards_image_id[i].source = lists[i][1][3]
        
        for list in lists:
            ind = lists.index(list)

            if ind == 0: 
                for i in range(3):
                    if i==0: #liber
                        if list in liber:anima.booktbt_o.icon = "bookmark-check"
                        else:anima.booktbt_o.icon = "bookmark"

                    elif i==1:#fav
                        if list in fav:anima.handbt_o.icon = "hand-heart-outline"
                        else:anima.handbt_o.icon = "hand-heart"

                    elif i==2:#like
                        if list in like:anima.heartbt_o.icon = "heart-circle-outline"
                        else:anima.heartbt_o.icon = "heart-circle"
                    
            elif ind == 1:
                 for i in range(3):
                    if i==0: #liber
                        if list in liber:anima.booktbt_t.icon = "bookmark-check"
                        else:anima.booktbt_t.icon = "bookmark"

                    elif i==1:#fav
                        if list in fav:anima.handbt_t.icon = "hand-heart-outline"
                        else:anima.handbt_t.icon = "hand-heart"

                    elif i==2:#like
                        if list in like:anima.heartbt_t.icon = "heart-circle-outline"
                        else:anima.heartbt_t.icon = "heart-circle"

            elif ind == 2:
                 for i in range(3):
                    if i==0: #liber
                        if list in liber:anima.booktbt_th.icon = "bookmark-check"
                        else:anima.booktbt_th.icon = "bookmark"

                    elif i==1:#fav
                        if list in fav:anima.handbt_th.icon = "hand-heart-outline"
                        else:anima.handbt_th.icon = "hand-heart"

                    elif i==2:#like
                        if list in like:anima.heartbt_th.icon = "heart-circle-outline"
                        else:anima.heartbt_th.icon = "heart-circle"
        
    def fill_from(self, food_image, spcies_image, name_note, m_image, audio_name):

        anima = self.manager.get_screen("animal")

        #main image change
        anima.main_image.source = m_image

        # main text change 
        name_f = name_note
        with open(name_f,encoding ="utf8") as file:
            m = file.read().split("\n")
            # main text part 1 change 
            anima.infro_o.text = f"[b]Kingdom[/b] : {m[0]}\n[b]Class[/b] : {m[1]}\n[b]Lifespan[/b] : {m[2]}\n[b]Height[/b] : {m[3]}\n[b]Family[/b] : {m[4]}\n[b]Species[/b] : {m[5]}\n"

            # main text part 2 change 
            anima.infro_t.text = f"[b]Behavouir:[/b]\n \n{m[6]}"

            # main text part 3 change
            anima.infro_th.text = f"[b]Communication:[/b]\n \n{m[7]}"

            # main text part 4 change
            anima.infro_f.text = f"[b]Intellignce[/b]\n \n{m[8]}"

            #main text part 5 change
            anima.infro_fi.text = f"[b]Food[/b]\n \n{m[9]}"

        # change of spices animal image
        spicess = spcies_image
        with open(spicess,encoding ="utf8") as file:
            m = file.read().split("\n")
            num_img = len(m)
         
            box = anima.spices_image

            for i in range(num_img):
                image = Image(source=m[i])
                box.add_widget(image)
        
        # change of spices animal image
        foods = food_image
        with open(foods,encoding ="utf8") as file:
            m = file.read().split("\n")
            num_img = len(m)
             
            box = anima.food_image

            for i in range(num_img):
                image = Image(source=m[i])
                box.add_widget(image) 

        #add the music in alubm
        sounds = audio_name
        with open(sounds,encoding="utf8") as file:
            m = file.read().split("\n")
            num = len(m)
            audio_list = [anima.audio_o,anima.audio_t,anima.audio_th,anima.audio_f,anima.audio_fi,anima.audio_s,
            anima.audio_se,anima.audio_e,anima.audio_n]

            if num==1:

                audio_list[0].bind(on_release=self.muisc1)
                self.sound0 = SoundLoader.load(str(m[0]))

                audio_list[1].bind(on_release=self.muisc2)
                self.sound1 = SoundLoader.load(str(m[0]))

                audio_list[2].bind(on_release=self.muisc3)
                self.sound2 = SoundLoader.load(str(m[0]))

                audio_list[3].bind(on_release=self.muisc4)
                self.sound3 = SoundLoader.load(str(m[0]))

                audio_list[4].bind(on_release=self.muisc5)
                self.sound4 = SoundLoader.load(str(m[0]))

                audio_list[5].bind(on_release=self.muisc6)
                self.sound5 = SoundLoader.load(str(m[0]))

                audio_list[6].bind(on_release=self.muisc7)
                self.sound6 = SoundLoader.load(str(m[0]))

                audio_list[7].bind(on_release=self.muisc8)
                self.sound7 = SoundLoader.load(str(m[0]))

                audio_list[8].bind(on_release=self.muisc9)
                self.sound8 = SoundLoader.load(str(m[0]))
                

            else:

                audio_list[0].bind(on_release=self.muisc1)
                self.sound0 = SoundLoader.load(str(m[0]))

                audio_list[1].bind(on_release=self.muisc2)
                self.sound1 = SoundLoader.load(str(m[1]))

                audio_list[2].bind(on_release=self.muisc3)
                self.sound2 = SoundLoader.load(str(m[2]))

                audio_list[3].bind(on_release=self.muisc4)
                self.sound3 = SoundLoader.load(str(m[3]))

                audio_list[4].bind(on_release=self.muisc5)
                self.sound4 = SoundLoader.load(str(m[4]))

                audio_list[5].bind(on_release=self.muisc6)
                self.sound5 = SoundLoader.load(str(m[5]))

                audio_list[6].bind(on_release=self.muisc7)
                self.sound6 = SoundLoader.load(str(m[6]))

                audio_list[7].bind(on_release=self.muisc8)
                self.sound7 = SoundLoader.load(str(m[7]))

                audio_list[8].bind(on_release=self.muisc9)
                self.sound8 = SoundLoader.load(str(m[8]))
                      
    def run_from(self, food_image_file, spcies_image_file, name_note_file, main_image, audio_name_file):
        anima = self.manager.get_screen("animal")

        try:
            anima.food_image.clear_widgets()
            anima.spices_image.clear_widgets()
            print("try")

            self.fill_from(food_image_file,spcies_image_file,name_note_file,main_image,audio_name_file)
            
        except:
            print("except")
            self.fill_from(food_image_file,spcies_image_file,name_note_file,main_image,audio_name_file)
        
                
#second animal album screen
class Animal(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

        #MDtoolbar id for refresh
        arrow_left = ObjectProperty()

        # spices image installed
        spices_image = ObjectProperty()

        # food image installed
        food_image = ObjectProperty()

        #main image name change
        main_image = ObjectProperty()

        #infromation of animal change
        infro_o = ObjectProperty()
        infro_t = ObjectProperty()
        infro_th = ObjectProperty()
        infro_f = ObjectProperty()
        infro_fi = ObjectProperty()

        #to give sound box to audio
        audio_o = ObjectProperty()
        audio_t = ObjectProperty()
        audio_th = ObjectProperty()
        audio_f = ObjectProperty()
        audio_fi = ObjectProperty()
        audio_s = ObjectProperty()
        audio_se = ObjectProperty()
        audio_e = ObjectProperty()
        audio_n = ObjectProperty()
    
        # In animal screen bottom cards id to change text
        cards_o = ObjectProperty()
        cards_t = ObjectProperty()
        cards_th = ObjectProperty()
        
        # In animal screen bottom cards image id to change image
        card_image_o = ObjectProperty()
        card_image_t = ObjectProperty()
        card_image_th = ObjectProperty()

        #bottom btn id of heart
        heartbt_o = ObjectProperty()
        heartbt_t = ObjectProperty()
        heartbt_th = ObjectProperty()

        #bottom btn id of hand
        handbt_o = ObjectProperty() 
        handbt_t = ObjectProperty()
        handbt_th = ObjectProperty()

        #bottom btn id of book
        booktbt_o = ObjectProperty()
        booktbt_t = ObjectProperty()
        booktbt_th = ObjectProperty()

        self.Animal_name = [['bull',["anima/bull/food.txt","anima/bull/image.txt","anima/bull/note.txt","anima/bull/.elk.jpg", "anima/bull/sound.txt"]],
        ['cat',["anima/cat/food.txt","anima/cat/image.txt","anima/cat/note.txt","anima/cat/.cute cats.jpg", "anima/cat/sound.txt"]],
        ['cow',["anima/cow/food.txt","anima/cow/image.txt","anima/cow/note.txt","anima/cow/.sahiwal cattle.jpg", "anima/cow/sound.txt"]],
        ['dog',["anima/dog/food.txt","anima/dog/image.txt","anima/dog/note.txt","anima/dog/.german shepherd.jpg", "anima/dog/sound.txt"]],
        ['horse',["anima/horse/food.txt","anima/horse/image.txt","anima/horse/note.txt","anima/horse/.andalusian horse.jpg", "anima/horse/sound.txt"]],
        ['crab',["anima/crab/food.txt","anima/crab/image.txt","anima/crab/note.txt","anima/crab/.cancer pagurus.jpg", "anima/crab/sound.txt"]],
        ['wolf',["anima/wolf/food.txt","anima/wolf/image.txt","anima/wolf/note.txt","anima/wolf/.eurasian wolf.jpg", "anima/wolf/sound.txt"]], 
        ['monkey',["anima/monkey/food.txt","anima/monkey/image.txt","anima/monkey/note.txt","anima/monkey/.vervet monkey.jpg", "anima/monkey/sound.txt"]], 
        ['parrot',["anima/parrot/food.txt","anima/parrot/image.txt","anima/parrot/note.txt","anima/parrot/.lovebirds.jpg", "anima/parrot/sound.txt"]], 
        ['rabbit',["anima/rabbit/food.txt","anima/rabbit/image.txt","anima/rabbit/note.txt","anima/rabbit/.flemish giant rabbit.jpg", "anima/rabbit/sound.txt"]], 
        ['seal',["anima/seal/food.txt","anima/seal/image.txt","anima/seal/note.txt","anima/seal/.harbor seal.jpg", "anima/seal/sound.txt"]], 
        ['turtle',["anima/turtle/food.txt","anima/turtle/image.txt","anima/turtle/note.txt","anima/turtle/.green sea turtle.jpg", "anima/turtle/sound.txt"]],
        ['whale',["anima/whale/food.txt","anima/whale/image.txt","anima/whale/note.txt","anima/whale/.gray whale.jpg", "anima/whale/sound.txt"]], 
        ['hamster',["anima/hamster/food.txt","anima/hamster/image.txt","anima/hamster/note.txt","anima/hamster/.syrian hamster.jpg", "anima/hamster/sound.txt"]],
        ['chicken',["anima/chicken/food.txt","anima/chicken/image.txt","anima/chicken/note.txt","anima/chicken/.brahma.jpg", "anima/chicken/sound.txt"]],
        ['crow',["anima/crow/food.txt","anima/crow/image.txt","anima/crow/note.txt","anima/crow/.torresian crow.jpg", "anima/crow/sound.txt"]],
        ['elephant',["anima/elephant/food.txt","anima/elephant/image.txt","anima/elephant/note.txt","anima/elephant/.loxodonta atlantica.jpg", "anima/elephant/sound.txt"]], 
        ['dolphin',["anima/dolphin/food.txt","anima/dolphin/image.txt","anima/dolphin/note.txt","anima/dolphin/.dolphin.jpg", "anima/dolphin/sound.txt"]], 
        ['penguin',["anima/penguin/food.txt","anima/penguin/image.txt","anima/penguin/note.txt","anima/penguin/.adélie penguin.jpg", "anima/penguin/sound.txt"]], 
        ['deer',["anima/deer/food.txt","anima/deer/image.txt","anima/deer/note.txt","anima/deer/.roe deer.jpg", "anima/deer/sound.txt"]],
        ['snake',["anima/snake/food.txt","anima/snake/image.txt","anima/snake/note.txt","anima/snake/.black mamba.jpg", "anima/snake/sound.txt"]],
        ['lion',["anima/lion/food.txt","anima/lion/image.txt","anima/lion/note.txt","anima/lion/.transvaal lion.jpg", "anima/lion/sound.txt"]], 
        ['frog',["anima/frog/food.txt","anima/frog/image.txt","anima/frog/note.txt","anima/frog/.hylidae.jpg", "anima/frog/sound.txt"]], 
        ['giraffe',["anima/giraffe/food.txt","anima/giraffe/image.txt","anima/giraffe/note.txt","anima/giraffe/.northern giraffe.jpg", "anima/giraffe/sound.txt"]], 
        ['owl',["anima/owl/food.txt","anima/owl/image.txt","anima/owl/note.txt","anima/owl/.eastern screech owl.jpg", "anima/owl/sound.txt"]],
        ['zebra',["anima/zebra/food.txt","anima/zebra/image.txt","anima/zebra/note.txt","anima/zebra/.chapman's zebra.jpg", "anima/zebra/sound.txt"]], 
        ['donkey',["anima/donkey/food.txt","anima/donkey/image.txt","anima/donkey/note.txt","anima/donkey/.mule donkey.jpg", "anima/donkey/sound.txt"]], 
        ['gorilla',["anima/gorilla/food.txt","anima/gorilla/image.txt","anima/gorilla/note.txt","anima/gorilla/.western gorilla.jpg", "anima/gorilla/sound.txt"]],
        ['peacock',["anima/peacock/food.txt","anima/peacock/image.txt","anima/peacock/note.txt","anima/peacock/.indian peafowl.jpg", "anima/peacock/sound.txt"]],
        ['mouse',["anima/mouse/food.txt","anima/mouse/image.txt","anima/mouse/note.txt","anima/mouse/.house mouse.jpg", "anima/mouse/sound.txt"]], 
        ['alligator',["anima/alligator/food.txt","anima/alligator/image.txt","anima/alligator/note.txt","anima/alligator/.alligator.jpg", "anima/alligator/sound.txt"]]]

    #function
    def cardmd(self, instance):
        m = instance.text

        for name in self.Animal_name:
            if m == name[0]:
                self.run_from(name[1][0],name[1][1],name[1][2],name[1][3],name[1][4])

            else:print("none")  

    def fill_from(self, food_image, spcies_image, name_note, m_image, audio_name):

        anima = self

        #main image change
        anima.main_image.source = m_image

        # main text change 
        name_f = name_note
        with open(name_f,encoding ="utf8") as file:
            m = file.read().split("\n")
            # main text part 1 change 
            anima.infro_o.text = f"[b]Kingdom[/b] : {m[0]}\n[b]Class[/b] : {m[1]}\n[b]Lifespan[/b] : {m[2]}\n[b]Height[/b] : {m[3]}\n[b]Family[/b] : {m[4]}\n[b]Species[/b] : {m[5]}\n"

            # main text part 2 change 
            anima.infro_t.text = f"[b]Behavouir:[/b]\n \n{m[6]}"

            # main text part 3 change
            anima.infro_th.text = f"[b]Communication:[/b]\n \n{m[7]}"

            # main text part 4 change
            anima.infro_f.text = f"[b]Intellignce[/b]\n \n{m[8]}"

            #main text part 5 change
            anima.infro_fi.text = f"[b]Food[/b]\n \n{m[9]}"

        # change of spices animal image
        spicess = spcies_image
        with open(spicess,encoding ="utf8") as file:
            m = file.read().split("\n")
            num_img = len(m)
         
            box = anima.spices_image

            for i in range(num_img):
                image = Image(source=m[i])
                box.add_widget(image)
        
        # change of spices animal image
        foods = food_image
        with open(foods,encoding ="utf8") as file:
            m = file.read().split("\n")
            num_img = len(m)
             
            box = anima.food_image

            for i in range(num_img):
                image = Image(source=m[i])
                box.add_widget(image) 

        #add the music in alubm
        sounds = audio_name
        with open(sounds,encoding="utf8") as file:
            
            scren = self.manager.get_screen("front")

            m = file.read().split("\n")
            num = len(m)
            audio_list = [anima.audio_o,anima.audio_t,anima.audio_th,anima.audio_f,anima.audio_fi,anima.audio_s,
            anima.audio_se,anima.audio_e,anima.audio_n]

            if num==1:
                audio_list[0].bind(on_release=scren.muisc1)
                scren.sound0 = SoundLoader.load(str(m[0]))

                audio_list[1].bind(on_release=scren.muisc2)
                scren.sound1 = SoundLoader.load(str(m[0]))

                audio_list[2].bind(on_release=scren.muisc3)
                scren.sound2 = SoundLoader.load(str(m[0]))

                audio_list[3].bind(on_release=scren.muisc4)
                scren.sound3 = SoundLoader.load(str(m[0]))

                audio_list[4].bind(on_release=scren.muisc5)
                scren.sound4 = SoundLoader.load(str(m[0]))

                audio_list[5].bind(on_release=scren.muisc6)
                scren.sound5 = SoundLoader.load(str(m[0]))

                audio_list[6].bind(on_release=scren.muisc7)
                scren.sound6 = SoundLoader.load(str(m[0]))

                audio_list[7].bind(on_release=scren.muisc8)
                scren.sound7 = SoundLoader.load(str(m[0]))

                audio_list[8].bind(on_release=scren.muisc9)
                scren.sound8 = SoundLoader.load(str(m[0]))

            else:
                
                audio_list[0].bind(on_release = scren.muisc1)
                scren.sound0 = SoundLoader.load(str(m[0]))

                audio_list[1].bind(on_release = scren.muisc2)
                scren.sound1 = SoundLoader.load(str(m[1]))

                audio_list[2].bind(on_release = scren.muisc3)
                scren.sound2 = SoundLoader.load(str(m[2]))

                audio_list[3].bind(on_release = scren.muisc4)
                scren.sound3 = SoundLoader.load(str(m[3]))

                audio_list[4].bind(on_release = scren.muisc5)
                scren.sound4 = SoundLoader.load(str(m[4]))

                audio_list[5].bind(on_release = scren.muisc6)
                scren.sound5 = SoundLoader.load(str(m[5]))

                audio_list[6].bind(on_release = scren.muisc7)
                scren.sound6 = SoundLoader.load(str(m[6]))

                audio_list[7].bind(on_release = scren.muisc8)
                scren.sound7 = SoundLoader.load(str(m[7]))

                audio_list[8].bind(on_release = scren.muisc9)
                scren.sound8 = SoundLoader.load(str(m[8]))

    def run_from(self, food_image_file, spcies_image_file, name_note_file, main_image, audio_name_file):
        anima = self

        try:
            anima.food_image.clear_widgets()
            anima.spices_image.clear_widgets()
            print("try")

            self.fill_from(food_image_file,spcies_image_file,name_note_file,main_image,audio_name_file)
            
        except:
            print("except")
            self.fill_from(food_image_file,spcies_image_file,name_note_file,main_image,audio_name_file)
                   
    def icon_change(self):

        anima = self.manager.get_screen("front")
        self.manager.current = "front"

        for list in anima.listss:
            ind = anima.listss.index(list)
            if ind == 0:
                for i in range(3):

                    if i==0:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                   if list in like:anima.ids[word[1]].icon="heart-circle-outline"
                                   else:anima.ids[word[1]].icon="heart-circle"
                    elif i==1:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                    if list in fav:anima.ids[word[2]].icon="hand-heart-outline"
                                    else:anima.ids[word[2]].icon="hand-heart"
                    
                    elif i==2:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                    if list in fav:anima.ids[word[3]].icon="bookmark-check"
                                    else:anima.ids[word[3]].icon="bookmark"
            
            elif ind == 1:
                for i in range(3):

                    if i==0:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                   if list in like:anima.ids[word[1]].icon="heart-circle-outline"
                                   else:anima.ids[word[1]].icon="heart-circle"
                    elif i==1:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                    if list in fav:anima.ids[word[2]].icon="hand-heart-outline"
                                    else:anima.ids[word[2]].icon="hand-heart"
                    
                    elif i==2:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                    if list in fav:anima.ids[word[3]].icon="bookmark-check"
                                    else:anima.ids[word[3]].icon="bookmark"

            elif ind == 2:
                for i in range(3):

                    if i==0:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                   if list in like:anima.ids[word[1]].icon="heart-circle-outline"
                                   else:anima.ids[word[1]].icon="heart-circle"
                    elif i==1:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                    if list in fav:anima.ids[word[2]].icon="hand-heart-outline"
                                    else:anima.ids[word[2]].icon="hand-heart"
                    
                    elif i==2:
                        for line in alubm_cloumn:
                            for word in line:
                                if list[0]==word[0]:
                                    if list in fav:anima.ids[word[3]].icon="bookmark-check"
                                    else:anima.ids[word[3]].icon="bookmark"


    def bottom_but(self,instance, id_card,btn_name): 

        name = self.ids[id_card].text
        anima = self.manager.get_screen("front")
        
        if btn_name == "heart":
            for animal in self.Animal_name:
                if name==animal[0]:
                    if [name,animal[1][3]] in like:
                        like.pop(like.index([name,animal[1][3]]))

                        instance.icon = "heart-circle"
                        anima.like_remove_bot(animal[0])

                    else:

                        instance.icon = "heart-circle-outline"
                        anima.like_list(animal[0])

        elif btn_name == "book":
            for animal in self.Animal_name:
                if name==animal[0]:
                    if [name,animal[1][3]] in liber:
                        liber.pop(liber.index([name,animal[1][3]]))

                        instance.icon = "bookmark"
                        anima.liber_remove_bot(animal[0])

                    else:

                        instance.icon = "bookmark-check"
                        anima.liber_list(animal[0])

        elif btn_name == "hand":
            for animal in self.Animal_name:
                if name==animal[0]:
                    if [name,animal[1][3]] in fav:
                        fav.pop(fav.index([name,animal[1][3]]))

                        instance.icon = "hand-heart"
                        anima.fav_remove_bot(animal[0])

                    else:
                
                        instance.icon = "hand-heart-outline"
                        anima.fav_list(animal[0])

#thrid navbar screen
class Navbar(Screen):
    pass

# this is main app run class
class Animal_app(MDApp):

    # create app with this def function
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"

        self.sm = ScreenManager(transition=NoTransition())
        
        self.sm.add_widget(Main(name="front"))
        self.sm.add_widget(Animal(name="animal"))
        self.sm.add_widget(Navbar(name="navbar"))

        return self.sm

    # def function for chaning screen
    def creating(self, scre):
        if self.sm.current == scre:
            print('allredy')
        else:self.sm.current = scre


# inhereditry the app in sweety
sweet = Animal_app()
# run this app
sweet.run()

