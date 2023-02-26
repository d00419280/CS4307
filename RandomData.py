import random
import string


posts = [
    'Hey Guys!',
    "Yall, I just failed my class.",
    'I got a new internship with a company!',
    'I have a test in two minutes and have not studied. Wish me luck, please.',
    'Traveling became almost extinct during the pandemic.',
    'I know many children ask for a pony, but I wanted a bicycle with rockets strapped to it.',
    "For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.",
    "I don’t respect anybody who can’t tell the difference between Pepsi and Coke.",
    "Iguanas were falling out of the trees.",
    "It had been sixteen days since the zombies first attacked.",
    "Chocolate covered crickets are my favorite snack.",
    "Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.",
    "My ultimate dream fantasy consists of being content and sleeping eight hours in a row.",
    "A quiet house is nice until you are ordered to stay in it for months.",
    "25 years later, I still regret that specific moment.",
    "Written warnings in instruction manuals are worthless since rabbits can't read.",
    "When I was little I had a car door slammed shut on my hand and I still remember it quite vividly.",
    "Smoky the Bear secretly started the fires.",
    "It didn't make sense unless you had the power to eat colors.",
    "She hadn't had her cup of coffee, and that made things all the worse.",
    "You've been eyeing me all day and waiting for your move like a lion stalking a gazelle in a savannah.",
    "The best key lime pie is still up for debate.",
    "Separation anxiety is what happens when you can't find your phone.",
    "The skeleton had skeletons of his own in the closet.",
    "It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.",
    "Wisdom is easily acquired when hiding under the bed with a saucepan on your head.",
    "I covered my friend in baby oil.",
    "If you're reading this message, It's too late. I got a perm...",
    "Each person who knows you has a different perception of who you are.",
    "Everyone was curious about the large white blimp that appeared overnight.",
    "Plans for this weekend include turning wine into water.",
    "I am counting my calories, yet I really want dessert.",
    "I just wanted to tell you I could see the love you have for your child by the way you look at her.",
]

names = [
    "Liam","Noah","Oliver","William","Elijah",
              "James","Benjamin","Lucas","Mason","Ethan",
              "Alexander","Henry","Jacob","Michael","Daniel",
              "Logan","Jackson","Sebastion","Jack","Aiden","Owen",
              "Samuel","Matthew","Joseph","Mateo","David","John",
              "Wyatt","Carter","Julian","Luke","Grayson","Isaac",
              "Jayden","Theodore","Gabriel","Anthony","Dylan","Leo",
              "Lincoln","Jaxon","Asher","Christopher","Josiah",
              "Andrew","Thomas","Joshua","Ezra","Hudson","Charles",
              "Olivia","Emma","Ava","Sophia","Isabella","Charlotte",
                "Amelia","Mia","Harper","Evelyn","Abigail","Emily",
                "Ella","Elizabeth","Camila","Luna","Sofia","Avery",
                "Mila","Aria","Scarlett","Penelope","Layla","Chloe",
                "Victoria","Madison","Eleanor","Grace","Nora","Riley",
                "Zoey","Hannah","Hazel","Lily","Ellie","Violet","Lillian",
                "Zoe","Stella","Aurora","Natalie","Emilia","Everly",
                "Leah","Aubrey","Willow","Addison","Lucy","Audrey",
                "Bella"
]

passwords = [
    "nursery",
    "software",
    "hell",
    "view",
    "farewell",
    "reporter",
    "inflation",
    "peasant",
    "impound",
    "sheet",
    "quiet",
    "look",
    "false",
    "dry",
    "dawn",
    "dentist",
    "past",
    "estimate",
    "conclusion",
    "awful",
]

def RandomPassword():
      return random.choice(passwords)

def RandomContent():
      return random.choice(posts)

def RandomChars(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def RandomEmail():
    numChar = random.randint(1,10)
    return RandomChars(numChar)+"@gmail.com"
