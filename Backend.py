from flask import Flask, render_template, jsonify

import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')


global bodylable,bodybutton,Clanbutton,Mindbutton,clanlable,mindlable,talentlable,Talentbutton,chakralable,Chakrabutton,jutsulable,Jutsubutton,DojutsuButton,Dojutsulable,JinButton,Jinlable,Tai,Tailable
global Guy,Lee,Naruto,Itachi,Shikimaru,Tenten,Senju,Hyuga,Boruto,Daemon,Sasuke,Sharingan,Tenseigan,Minato,Kyubi,Madara,None1

statusch = 1
statusbo = 1
statustai = 1
statuscl = 1
statusdoj = 1
statusjin = 1
statusmin = 1
statusta = 1
statusjut = 1
Guy="https://i.imgur.com/TLZSeT8.png"
Lee="https://i.imgur.com/A17eywL.png"
Naruto="https://i.imgur.com/qqmReh1.png"
Itachi="https://i.imgur.com/Ul6bF07.png"
Shikimaru="https://i.imgur.com/urHrojg.png"
Tenten="https://i.imgur.com/pr8QAIx.png"
Senju="https://i.imgur.com/XQ3eses.png"
Hyuga="https://i.imgur.com/d0zWjVX.png"
Daemon="https://i.imgur.com/HI9cr2F.png"
Sasuke="https://i.imgur.com/Zk6S3DR.png"
Sharingan="https://i.imgur.com/8JFZf28.png"
Tenseigan="https://i.imgur.com/eRtDw0D.png"
Minato="https://i.imgur.com/dndXQWb.png"
Kyubi="https://i.imgur.com/6OCPt24.png"
Otsutski="https://i.imgur.com/091rxkN.png"
Madara="https://i.imgur.com/F5X0Snk.png"
None1="https://i.imgur.com/l4BiRxS.png"
Boruto="https://i.imgur.com/IxuOJ63.png"
@app.route('/body', methods=['GET'])
def body():
    global characters,number_values,selected_character, selected_number,selected_image
    characters = ['Guy', 'Lee', 'Naruto', 'Itachi','Shikimaru','Tenten']
    number_values = {'Guy': 10, 'Lee': 7, 'Naruto': 7, 'Itachi': 6,'Shikimaru': 3, 'Tenten': -2}
    image_values ={'Guy': Guy, 'Lee': Lee, 'Naruto': Naruto, 'Itachi': Itachi,'Shikimaru': Shikimaru, 'Tenten': Tenten}
    selected_character = random.choice(characters)
    selected_number = number_values[selected_character]
    selected_image= image_values[selected_character]
    print("body ",selected_character,selected_number)
    global statusbo
    statusbo=0
    Setup()
    return jsonify(values=selected_character,image=selected_image)
@app.route('/clan', methods=['GET'])
def clan():
    global charactersclan,number_valuesclan,selected_characterclan, selected_numberclan,selected_imageclan,image_valuesclan
    charactersclan = ['Senju', 'Hyuga', 'Uzumaki', 'Uchiha','Otsutski','Nara']
    number_valuesclan = {'Senju': 9, 'Hyuga': 7, 'Uzumaki': 8, 'Uchiha': 9,'Otsutski': 11, 'Nara': 5}
    image_valuesclan = {'Senju': Senju, 'Hyuga': Hyuga, 'Uzumaki': Naruto, 'Uchiha': Itachi,'Otsutski': Otsutski, 'Nara': Shikimaru}
    selected_characterclan = random.choice(charactersclan)
    selected_numberclan = number_valuesclan[selected_characterclan]
    selected_imageclan= image_valuesclan[selected_characterclan]
    print("clan ",selected_characterclan,selected_numberclan)
    global statuscl
    statuscl=0
    Setup()
    return jsonify(values=selected_characterclan,image=selected_imageclan)

@app.route('/mind', methods=['GET'])
def mind():
    global charactersmind,number_valuesmind,selected_charactermind, selected_numbermind,image_valuesmind,selected_imagemind
    charactersmind = ['Guy', 'Lee', 'Naruto', 'Itachi','Shikimaru','Tenten']
    number_valuesmind = {'Guy': 4, 'Lee': 1, 'Naruto': 5, 'Itachi': 9,'Shikimaru': 11, 'Tenten': 6}
    image_valuesmind = {'Guy': Guy, 'Lee': Lee, 'Naruto': Naruto, 'Itachi': Itachi,'Shikimaru': Shikimaru, 'Tenten': Tenten}
    selected_charactermind = random.choice(charactersmind)
    selected_numbermind = number_valuesmind[selected_charactermind]
    selected_imagemind= image_valuesmind[selected_charactermind]
    print("mind ",selected_charactermind,selected_numbermind)
    global statusmin
    statusmin=0
    Setup()
    return jsonify(values=selected_charactermind,image=selected_imagemind)

@app.route('/talent', methods=['GET'])
def talent():
    global characterstal,number_valuestal,selected_charactertal, selected_numbertal,image_valuestal,selected_imagetal
    characterstal = ['Guy', 'Lee', 'Naruto', 'Itachi','Shikimaru','Tenten','Boruto','Minato','Hashirama']
    number_valuestal = {'Guy': 3, 'Lee': -2, 'Naruto': 9, 'Itachi': 7,'Shikimaru': 4, 'Tenten': 1,'Boruto':11,'Minato':8,'Hashirama':9}
    image_valuestal = {'Guy': Guy, 'Lee': Lee, 'Naruto': Naruto, 'Itachi': Itachi,'Shikimaru': Shikimaru, 'Tenten': Tenten,'Boruto':Boruto,'Minato':Minato,'Hashirama':Senju}
    selected_charactertal = random.choice(characterstal)
    selected_numbertal = number_valuestal[selected_charactertal]
    selected_imagetal = image_valuestal[selected_charactertal]
    print("talent ",selected_charactertal,selected_numbertal)
    global statusta
    statusta=0
    Setup()
    return jsonify(values=selected_charactertal,image=selected_imagetal)

@app.route('/chakra', methods=['GET'])
def chakra():
    global charactersch,number_valuesch,selected_characterch, selected_numberch,image_valuesch,selected_imagech
    charactersch = ['Guy', 'Lee', 'Naruto', 'Itachi','Shikimaru','Tenten','Boruto','Minato','Hashirama']
    number_valuesch = {'Guy': 0, 'Lee': 0, 'Naruto': 11, 'Itachi': 6,'Shikimaru': 4, 'Tenten': 3,'Boruto':8,'Minato':6,'Hashirama':10}
    image_valuesch = {'Guy': Guy, 'Lee': Lee, 'Naruto': Naruto, 'Itachi': Itachi,'Shikimaru': Shikimaru, 'Tenten': Tenten,'Boruto':Boruto,'Minato':Minato,'Hashirama':Senju}
    selected_characterch = random.choice(charactersch)
    selected_numberch = number_valuesch[selected_characterch]
    selected_imagech = image_valuesch[selected_characterch]
    print("chakra ",selected_characterch,selected_numberch)
    global statusch
    statusch=0
    Setup()
    return jsonify(values=selected_characterch,image=selected_imagech)
@app.route('/jutsu', methods=['GET'])
def Jutsu():
    global charactersj,number_valuesj,selected_characterj, selected_numberj,image_valuesj
    charactersj = ['Guy', 'Lee', 'Naruto', 'Sasuke','Shikimaru','Tenten','Boruto','Minato','Hashirama','Daemon']
    number_valuesj = {'Guy': 0, 'Lee': 0, 'Naruto': 10, 'Sasuke': 10,'Shikimaru': 2, 'Tenten': 1,'Boruto':11,'Minato':6,'Hashirama':9,'Daemon':12}
    image_valuesj = {'Guy': Guy, 'Lee': Lee, 'Naruto': Naruto, 'Sasuke': Sasuke,'Shikimaru': Shikimaru, 'Tenten': Tenten,'Boruto':Boruto,'Minato':Minato,'Hashirama':Senju,'Daemon':Daemon}
    selected_characterj = random.choice(charactersj)
    selected_numberj = number_valuesj[selected_characterj]
    selected_imagej = image_valuesj[selected_characterj]
    print("Jutsu ",selected_characterj,selected_numberj)
    global statusjut
    statusjut=0
    Setup()
    return jsonify(values=selected_characterj,image=selected_imagej)

@app.route('/doj', methods=['GET'])
def Dojutsu():
    global charactersd,number_valuesd,selected_characterd, selected_numberd,image_valuesd,selected_imaged
    charactersd = ['None', 'None', 'None', 'None','None','Sharingan','Mangekyo','Byakugan','Sasuke`s\nRinnegan','Tenseigan']
    number_valuesd = {'None': 0, 'None': 0, 'None': 0, 'None': 0,'None': 0, 'Sharingan': 2,'Mangekyo':5,'Byakugan':3,'Sasuke`s\nRinnegan':9,'Tenseigan':7}
    image_valuesd = {'None':None1,'Sharingan': Sharingan,'Mangekyo':Itachi,'Byakugan':Hyuga,'Sasuke`s\nRinnegan':Sasuke,'Tenseigan':Tenseigan}
    selected_characterd = random.choice(charactersd)
    selected_numberd = number_valuesd[selected_characterd]
    selected_imaged = image_valuesd[selected_characterd]
    print("Dojutsu ",selected_characterd,selected_numberd)
    global statusdoj
    statusdoj=0
    Setup()
    return jsonify(values=selected_characterd,image=selected_imaged)

@app.route('/kyubi', methods=['GET'])
def Jin():
    global charactersji,number_valuesji,selected_characterji, selected_numberji,image_valuesji,selected_imageji
    charactersji = ['None', 'None', 'None', 'None','None','1 Tail','2 Tails','3 Tails','4 Tails','5 Tails', '6 Tails','7 Tails','8 Tails','9 Tails','10 Tails']
    number_valuesji = {'None': 0, 'None': 0, 'None': 0, 'None': 0,'None': 0, '1 Tail':1,'2 Tails':2,'3 Tails':3,'4 Tails':4,'5 Tails':5, '6 Tails':6,'7 Tails':7,'8 Tails':8,'9 Tails':10,'10 Tails':12}
    image_valuesji = {'None': None1, '1 Tail':Kyubi,'2 Tails':Kyubi,'3 Tails':Kyubi,'4 Tails':Kyubi,'5 Tails':Kyubi, '6 Tails':Kyubi,'7 Tails':Kyubi,'8 Tails':Kyubi,'9 Tails':Kyubi,'10 Tails':Kyubi}
    selected_characterji = random.choice(charactersji)
    selected_numberji = number_valuesji[selected_characterji]
    selected_imageji = image_valuesji[selected_characterji]
    print("Kyubi ",selected_characterji,selected_numberji)
    global statusjin
    statusjin=0
    Setup()
    return jsonify(values=selected_characterji,image=selected_imageji)

@app.route('/taijutsu', methods=['GET'])
def Taijutsu():
    global characterst,number_valuest,selected_charactert, selected_numbert,image_valuest,selected_imaget
    characterst = ['Guy', 'Lee', 'Naruto', 'Tenten','Shikimaru','Madara']
    number_valuest = {'Guy': 10, 'Lee': 8, 'Naruto': 9, 'Tenten': -2,'Shikimaru': 3, 'Madara': 12}
    image_valuest = {'Guy': Guy, 'Lee': Lee, 'Naruto': Naruto, 'Tenten': Tenten,'Shikimaru': Shikimaru, 'Madara': Madara}
    selected_charactert = random.choice(characterst)
    selected_numbert = number_valuest[selected_charactert]
    selected_imaget = image_valuest[selected_charactert]
    print("Taijutsu ",selected_charactert,selected_numbert)
    global statustai
    statustai=0
    Setup()
    return jsonify(values=selected_charactert,image=selected_imaget)
    



@app.route('/reset', methods=['GET'])
def reset():
    global statusbo,statusch,statuscl,statusdoj,statusjin,statusjut,statusmin,statusta,statustai
    resetvalue=" "
    print("reset")
    statusbo=1
    statusch=1
    statuscl=1
    statusdoj=1
    statusjin=1
    statusjut=1
    statusmin=1
    statusta=1
    statustai=1
    return jsonify(values=resetvalue)


    
@app.route('/answer', methods=['GET'])
def Setup():
    values=" "
    if (statusch<1 and statuscl<1 and statusta<1 and statusjut<1 and statusbo<1 and statusdoj<1 and statusjin<1 and statustai<1 and statusmin<1):
        ans=(selected_number,selected_numberch,selected_numberclan,selected_numberj,selected_numbermind,selected_numbertal,selected_numberji,selected_numbert,selected_numberd)
        finalans=sum(ans)
        print(finalans)
        if finalans==9:
            print("The worst ninja")
            values= "The worst ninja"
            return jsonify(values=values)
        elif finalans>=97:
            print("Perfect Shinobi")
            values= "Perfect Shinobi"
            return jsonify(values=values)
        elif finalans>=78:
            values= "#0"
            print("#0")
            return jsonify(values=values)
        elif finalans>=76:
            values= "#1"
            print("#1")
            return jsonify(values=values)
        elif finalans>=72:
            values= "God Slayer"
            print("God Slayer")
            return jsonify(values=values)
        elif finalans>=67:
            values= "Legendary Shinobi"
            print("Legendary Shinobi")
            return jsonify(values=values)
        elif finalans>=51:
            values= "High Kage"
            print("High Kage")
            return jsonify(values=values)
        elif finalans>=46:
            values= "Kage"
            print("Kage")
            return jsonify(values=values)
        elif finalans>=38:
            values= "High Tier Jonin"
            print("High Tier Jonin")
            return jsonify(values=values)
        elif finalans>=32:
            values= "Jonin"
            print("Jonin")
            return jsonify(values=values)
        elif finalans>=24:
            values= "High Tier Chunin"
            print("High Tier Chunin")
            return jsonify(values=values)
        elif finalans>=17:
            values= "Chunin"
            print("Chunin")
            return jsonify(values=values)
        elif finalans>=13:
            values= "Genin"
            print("Genin")
            return jsonify(values=values)
    else:
        return jsonify(values=values)
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
