# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Anya = Character("Ayako", color="#ffffff")
define Amamura = Character("Amamura", color="#0066ff")
define Yoru = Character("Yoru")
define Sora = Character("Sora")
define Yuka = Character("Yuka")
define Touya = Character("Touya")
define Ayame = Character("Ayame")


label start:


    scene bg room

    "At Kaito High School."

    "Male Student A" "I thought she was just pretty but seeing her face up close.\nI thought she is a fashion model."

    "Male Student B" "No! She's an angel witl silver hair."

    "A girl who was being watched by the surrounding students her name is Ayako Ame."

    "She is Half Japanese, half Russian her beauty is unbelievable she has silver hair and blue eyes and even girls together can resist her beauty."

    "She is new student in Kaito High School who entered in the middle of the semester."

    "At Kaito High School. Those who take an entrance exam and pass are
    already impressed, Ayako is one of them."

    "Girl Student A" "Even I'm a girl though, but I feel like I fell in love with her!"

    "Girl Student B" "I heard the rumor that she rejected every guy who confesses to her even handsome senpai!"

    "Girl Student C" "She doesn't care about love, doesn't she ?"

    "Girl Student C" "I wonder what kind of guy that she likes looks like."

    "At Classroom."

    "Girl Classmate A" "Good Morning, Ame-san."

    Anya "Good Morning."

    "Ayako walks to her desk near a window and then looks at a guy who sit next and he is sleeping."

    "???" "......"

    "Male Classmate A" "Amamura! Wake Up!"

    "Girl Classmate B" "Ame-san is waiting for you, Amamura."

    Anya "*Sigh*"

    "Ayako walks behind Amamura's chair and kicks a chair."

    Amamura "Wha-!"

    "Classmates who see what's happening let out a sigh like a looped video."

    Anya "Morning, Amamura-kun."

    Anya "Watched anime at late night again ?"

    Amamura "*Yawn* Morning, Anya and yeah, you know me but that anime is very banger."

    Amamura "You should watch it sometimes, Anya."

    Anya "I warned you everyday, didn't-"

    Amamura "Yeah Yeah I know but everyone has a hobby."

    Amamura "So my hobby is watching anime all night because why not."

    Anya "Are you pretend to be an idiot ?"

    Amamura "If you think this guy who addicted to anime is idiot. Well *Chuckle* I don't mind."

    Anya "*Sigh* So you are actually are idiot, sorry for asking."

    Amamura "The way you speaking is in top form as usual."

    "The alarm ringing then everyone gets back to a seat while everyone is sitting and waiting
    calmly Amamura stretched his arm and yawns like he just waits up."

    "Anya sees his face and turns her face to the window and smiles while she says."

label choice1:
    Anya "what a milashka"
menu:
    "What did you say ?":
        jump choice1_1
    "Did you secretly speak bad words about me in Russian ?":
        jump choice1_2
    "Did you say something ?":
        jump choice1_3
    "(Stare at her.)":
        jump choice1_4
label choice1_1:
    Anya "I just say “disgusting”."
    jump choice1_finish

label choice1_2:
    Anya "Yes I am and I just say “disgusting”."
    jump choice1_finish

label choice1_3:
    Anya "DISGUSTING!"
    jump choice1_finish

label choice1_4:
    Anya "Why did you stare at me ?"
    Amamura "I thought you say something."
    Anya "I said disgusting."
    jump choice1_finish

label choice1_finish:
    Amamura "ah... Sorry"
    "He uses his hand to cover his mouth while he yawns."
    "Then Ayako turns her face to the window and suppresses her smile while speaking in her mind."
    Anya "(What a dummy, He doesn't even know what I said hehe~~~)"
    Amamura "She didn't know that I knew what 'milashka' means, didn't she?"
    "Ayako didn't know that Amamura knows Russia and she didn't know that Russia's words
    sometimes she slipped out Amamura know the meaning."
    "This sweet conversation nobody in the classroom knew."
    
    "Chapter 2"

    Amamura "Damn, I forget my chemistry book"
    
    "He looks at the clock in the classroom it is only 2 minutes and it is not enough time for him to
    borrow a chemistry book from his friend in another classroom so he calls Ayako."
    
    Amamura "I am sorry but can I look chemistry book with you ?"

    "Ayako turns her face toward Amamura with an annoyed expression."

    Anya "You forget your book again ?!"

    Amamura "Yeah, I think I forget it at my house."

    Anya "*Sigh* Fine, Take a look with me."

    "After Ayako permitted him to look at a book with her, he moves a desk closer to her."

    Amamura "Thanks."

label choice2:
    Anya "Amamura-kun aren't you forget things too often? you are a high school student
    already but you often forget things like a kid."
menu:
    "Well there are too many books besides sometimes people forget something.":
        jump choice2_1
    "I'm sorry I won't forget it next time.":
        jump choice2_2
    "I'M NOT A KID, ANYA!!":
        jump choice2_3
    "Stop complaining about me all the time, please.":
        jump choice2_4
label choice2_1:
    Anya "Yes, sometimes people forget things but not often as you."
    Amamura "Well, it's true that I always forget things."
    jump choice2_finish

label choice2_2:
    Anya "But you still forget when you said that."
    Amamura "Yeah, you're right."
    jump choice2_finish

label choice2_3:
    Anya "Even you say you are not a kid but you acting like a kid."
    Amamura "Dammit, you're not wrong."
    jump choice2_finish

label choice2_4:
    Anya "Try acting more seriously then I will stop complaining."
    Amamura "On the second thought. you can complain about me how much you want."
    jump choice2_finish

label choice2_finish:
    "Ayako opened her chemistry book and Amamura thanks her again for letting him see her
    book while teacher is teaching Amamura tries to listen and tries not to sleep."

    Amamura "*Yawn* This is boring."
    
    "Amamura tries his best to not sleep when the teacher starts to call the student to answer the
    question he is even more sleepy than before. while he dozed…"

    Amamura "OUCH!!!"

    "Ayako stabs Amamura with her pen to wake him up."

    "Amamura turns his face toward Ayako with a protesting expression like he said “Why did you
    stab me!” when Amamura sees her face he saw she looking at him with disdainful blue eyes
    Amamura turns away because he knows that look on her face means “you ask me to let you
    see my book but you dare to sleep ?!"

    Amamura "Sorry, my bad."
    
    Anya "Hmph!"

    "Chemistry Teacher" "What answer should we put in the blank."
    "Chemistry Teacher" "Amamura, can you answer this ?"

    Amamura "Umm…ah….”"

    "It's obviously that Amamura doesn't know the answer. he thinks that should he tell “I don't know
    the answer” or just random answer in the choice."

    "Cheristry Teacher" "What's wrong ?, Amamura."

    Amamura "Uhhhhh.."

    "While he thinking about which choice he should answer Ayako moved her finger to the
    answer."

    "Amamura thank her in his mind."

    Amamura "Cholic Acid!"

    "Cheristry Teacher" "Wrong answer, Amamura."

    Amamura "What?!"

    "Amamura shout in his mind “That is the wrong answer” and turn his face to Ayako but she
    still did the unknown face. he looks at her mouth it looks like her try to not smile."

    "Cheristry Teacher" "Then Ame who sits next to Amamura can you answer the question ?"

    Anya "Yes, it's Hydron Chloride."

    "Cheristry Teacher" "That's correct. Amamura, please concentrate on your study."

    Amamura "Yes, sir."

    "Amamura turns his face to Ayako again and speaks quietly."

    Amamura "Why did you tell me the wrong answer ?"

    Anya "I didn’t tell you the answer I point out what question is."

    Amamura "YOU LIE!! it's obviously point at number 2!"

    Anya "Why do you so mean ?"

    Amamura "It's beacuse your mouth is smiling."

    "Ayako sees Amamura acting like a child she chuckles and said “CUTE” in a soft tone while
    smiling."

    "A sweet word that comes out suddenly makes Amamura cheek is twitching."

    Amamura "What did you just say?!"

    Anya "I just say you are an Idiot"

    "In his mind, he screams “LIARRRRR”."

    "Amamura understood Russian because of her paternal grandfather, who was
    a great lover of Russia."

    "It all started around the elementary school when he was under the care of his
    grandfather’s house for a time and his grandfather made him watch a lot of
    Russian films."

    "Amamura himself had never been to Russia, nor did he have any relatives
    who were Russian."

    "He never mentioned it at school, so the only person at this school who knew
    that Amamura understood Russian was his little sister in the neighboring
    class."

    "And he forbade his little sister to talk about it too, so there’s no one else who
    knew."

    "At this point in time, he thought he should’ve come out to her earlier, but it was
    too late to regret it."

    "This mysterious shameful play in which a beautiful girl in the neighboring
    seat who was sweet only in Russian, too; everything was a seed that he had
    sown, so he had to accept it."

    "He could feel the indescribable embarrassment welling up in his chest, his
    face reddening. He was trying his best to hold his breath while pursing his lips tightly.\nThereupon, Ayako who mistakenly believed that he was holding in
    his anger, muttered in amusement from the bottom of her heart."

    Anya "“I LIKE WHEN YOU ACT LIKE A CHILD, CUTE”"

    "Amamura’s mind conjured up images of himself transforming into a young
    child, poked at the cheeks by Ayako with a smirk on her face."

    Amamura "I see, you want war. huh!!"

    "Amamura understood he was completely being looked upon and played
    with, and his face became serious at once."

    Amamura "Fourteen minutes left. Ten minutes left."
    
    "During that time, I’ll try to fight back. Then he realizes he forget some things."

    Amamura "Damn it! I didn’t roll the free gacha in the morning!!"

    "Normally, he would have rolled it before he left home or
    before homeroom, but he was so sleepy this morning that he wasn’t thinking
    to that extent."

    "Because his thought has completely shifted to the otaku side, he no longer
    cared about the fact that Ayako treated him like a baby. It couldn’t be helped to
    have the feeling that his simple mind was called as on the same level like that
    of a child’s, too."
    "Though, the person in question wasn’t self-aware of it.
    The teacher properly performed his duty for the remainder of the lesson and
    left the classroom. As soon as he saw the teacher leave, bringing his desk back
    to its original position he quickly took out his phone and launched the game
    app as fast as he could."

    "Ayako who found fault at that knitted her brows and gave him a warning."

    Anya "It’s against school regulations to use your phone within school except in
    emergencies and when used for study. You have the nerve to use your phone
    in front of me, a student council member."

    Amamura "Then, it’s not a violation of school regulations, right? It’s an emergency after
    all."

    Anya "I’ll listen just in case, what’s the emergency ?"

    "Under Ayako’s scornful eyes, which like it’s saying, probably for the wrong
    reasons, anyway, Amamura said with an unnecessarily crisp face."

    Amamura "“Free gacha. Ten minutes left until it ends."

    Anya "Do you want me to confiscate your phone ?"

    Amamura "I believe you wouldn’t do something like that EHE☆."

    Anya "“Maybe I really should confiscate your phone for once."

    Amamura "Now I’ve noticed, I haven’t
    done a wink or anything like that in a long time. It surprisingly has a high
    degree of difficulty, huh ? *Wink*."

    Anya "What are you saying all of sudden..."

    Amamura "“I mean, idols, like, do it sometimes, but there are not many celebrities who
    can wink beautifully, isn’t there."

    Anya "“Do you think so ?"

    Amamura "Eh? Isn’t it difficult? Doesn’t it make your cheeks and the edges of your
    mouth twitch in a weird way no matter what, making it feel more like ‘mmm’ than a ‘snap’ ?"

    Anya "It doesn’t, you know."

    Amamura "Ooh? Then how about you show it, a really beautiful wink."

    "Amamura raised his head and smiled challengingly. With a sour look,
    Ayako’s eyebrows twitched and the classmates in the surrounding who were
    listening to the conversation lightly buzzed."

    "In a moment all of the attention from the surrounding were on her; she faced
    Amamura with a disappointed look on her face and let out a big sigh once."

    Anya "Haah... Look, like this, right?"

    "And then, while tilting her head she did an extremely brilliant wink.
    Without applying any extra force to the rest of the face, her eye closed
    naturally with a snap."

    "In the precious scene of the aloof princess winking, “Ooohh!!”, the
    surrounding raised the sounds of commotion and cheers, and there was even
    sparse applause."

    "But, as for, Amamura the one who made the request...."

    Amamura "Yeaaah! SSR Tsukuyomi came!! ....huh, aah sorry. I wasn’t looking for a second."

    Anya "Confiscated."

    Amamura "No!"

    "Amamura screamed as his phone was mercilessly taken away.\n
    At that, Ayako looked down on him with a daunting pose."

    "Whether out of anger or even shame, her face reddened slightly,
    And there, Aykao’s ears picked up the voices of three male students facing each
    other conversing in a whisper."

    "Male Classmate A" "He-hey, did you get that?"
    "Male Classmate B" "No, the angle is a little...."
    "Male Classmate C" "Fuuh, leave it to me. I got that wink moment down perfectly."
    "Male Classmate B" "Give me that picture! I’ll even give you up a thousand yen!"

    Anya "Confiscated."

    "Male Classmate A-C" "Geh!? Ame-san!?"
    "Male Classmate A" "Ame-san! We’re not doing any-"

    "They tried to play dumb but they instantly shrunk back at the gaze that was
    directed at them."
    "However, it’s understandable. In fact, The figure of Ayako raising her chin and
    looking down at them in the argument was so powerful that even a big man
    would have flinched."
    "Her cold, hard gaze was exactly tundra-class."
    "As if a blizzard was blowing powerfully behind them, the other classmates
    who had been excited by Ayako’s wink all looked away quickly and held their
    breath so the aftermath wouldn’t reach them."
    "The classmates waited for the blizzard to pass, face down. However, there
    was about one boy who wasn’t at all afraid of her imposing appearance."

    Amamura "Please forgive mee~ Have mercy~"

    "Furthermore, he even defended himself. While words such as, “Is this guy for
    real”, came from the surroundings and their gazes gathered at Amamura."
    "Ayako kept her tundra-like expression and looked down at the phone she had
    taken away from Amamura."

    Anya "Tsukiyomi? Tsukiyomi is the goddess of the moon in Japanese
    mythology, right? Why is her hair not black but silver ?"

    Amamura "Eh... who knows? Isn’t it because of the image of the moon? Well, she’s cute
    so don’t bother with tiny details."

    Anya "...Hmph!"

    "As Amamura took the phone in both hands and worshipped her, Ayako snorted, not even
    trying to hide her displeasure. The other three phones were
    also returned to their owners."
    "After she made sure that the photographs taken sneakily were deleted, she sat
    down at her seat roughly."
    
    Amamura "Uwaah~ It’s seriously Tsukiyomi-sama. I thought I will never get her."

    "Wrapping her own hair around her finger and playing with it, Ayako glanced
    at Amamura who was looking at the screen of his phone with sparkling eyes,
    and pouted her lips."

    Anya "(I also have silver hair aswell you know ?)"

    "Amamura froze at the surprise jealousy attack that came flying suddenly."

    Amamura "....What did you say ?"

    "He naturally didn’t fail to hear it and Amamura raised his head with his face
    twitching. She glanced at him with a cold gaze, stopped playing with her hair
    and said as if to spit out."

    Anya "I just said ‘GAME ADDICT'."
    Amamura " “Hey! it’s rude to talk like that."

    "Ayako flinched a little when Amamura raised his voice with a rugged voice
    donning an unusually serious expression. But immediately she said, “I’m not
    saying anything wrong”, and strongly glared back at him."
    "Amamura cautioned her with a deadly serious expression, and the overflowing tension
    around them, once again, the eyes of the surrounding gathered at them."

    Amamura "Don’t you think it’s rude to the true addicts who play 20 hours a day, to call
    me, who play 8 hours a day, a game addict ?"

    "As if she was looking at trash, Ayako’s gaze pierced Amamura, who said
    something stupid with a uselessly crisp face. As if it physically pierced him."
    "Amamura let out a “Guhaa” and held down his chest."
    "Ayako just couldn’t deal with Amamura’s theatrical demeanor that had no
    bounds anymore and sighed grandly."
    
    Anya "Good grief.... You look unusually serious, so I thought you going to speak something
    seriously."
    Amamura "Hey, that’s absurd. I’m always serious at any time, you know? It’s no
    exaggeration to say that seriousness is my good point."
    Anya "It’s the biggest exaggeration of the century."
    Amamura "There’s still 80 percent left in this century though?!"
    Anya "Haah... Enough already and put your phone away."

    "As he was about to put his phone away and decided to leave it at that.... Immediately, he
    stopped moving at the Russian words that reached his ears."

    Anya "If you were serious you’d look cool, and I will fall for you for sure."

    "He spontaneously turned around at the murmur that really made his spine
    tingle."

    Amamura "What did you say ?"
    Anya "I said, ‘I lost hope'"
    Amamura "...Aah that so."
    Anya "Yes, that’s right"
    
    "Not leaving his mouth, Amamura screamed his inner thoughts loudly,
    “Liiiiaaaaaaarr!!”, and He read Ayako face expression: “I~diot. Humph”. Accurately
    understanding."
    "what she really thought, Amamura ’s face was twitching."

    Amamura "(I. Totally. Understand. What are you saying you know ?!!!)"
    
    "How refreshing it would be if he could shout it out as loud as he could. But,
    the only one who would lose out by revealing it would be him."

    Amamura "AHHH!!!"

    "Amamura knew he couldn’t reveal it but, he just felt pent-up. One way or another he
    wanted to reveal the nose of this hidden tsundere-girl."
    "He was grinding his teeth, but at that moment, suddenly the door in front of the classroom was
    opened."

    "Teacher" "‘Allo~, it’s a little early but the lesson will start okay~ .... Huh, Amamura. Why are
    you taking out your phone."
    Amamura "AH!!"

    "Being pointed out by the teacher who came in, Amamura realized after all
    this time that he was still holding his phone."

    Amamura "Well, just a little research for an assignment."
    "Teacher" "Is that true, Ame?"
    Anya "No, Amamura-Kun was playing a game on his phone."
    Amamura "Hey?!"
    "Teacher" "I knew it. Come here, Amamura! It’s confiscated!"
    Amamura "No, what do you mean you knew it!"
    
    "Amamura protested to the teacher as he reluctantly went to the teacher’s
    platform. As she watched his back, Ayako shrugged her shoulders."

    Anya "Haah... He’s really an idiot."

    "She muttered in a completely dumbfounded tone but, contrary to her tone, her
    lips slightly smiling. However, her classmates, except Amamura, didn’t notice this."

    Amamura "ANYA! you little-"

    "Amamura return to his seat and talk to Ayako quietly."

    Amamura "You seem to be happy, huh."
    Anya "Well isn’t it true that you use your phone to play game not searching something
    useful."
    Amamura "I can’t argue with that…"

    "Amamura want to tease Ayako back but he has no idea how to tease her back."

    Amamura "AHHH!! forget it."
    Amamura "But I didn’t see her smile for a while."

label choice3:
    "Amamura turn his face to speak to Ayako again."
menu:
    "It very rare to see you smile, huh.":
        jump choice3_1
    "I didn’t know you can smile like that.":
        jump choice3_2
    "You know, your smile remind me when we dance in the school festival.":
        jump choice3_3
    "I think it’s worth to my phone being confiscated.":
        jump choice3_4
label choice3_1:
    Anya "You talk like I am a type of a girl who doesn’t have a feeling."
    Amamura "Isn’t it true when you talk to other people ?"
    Anya "Hmph."
    "Amamura didn’t say anything back and There was no further conversation after
    that, only the sound of the teacher teaching."
    jump chapter3_1

label choice3_2:
    Anya "You didn’t see me smile before ?"
    Amamura "Huh, When ?"
    Anya "I Won’t tell."
    "Amamura still tries to remember when she smiles and Ayako turns her face to the side
    window with a red face."
    jump chapter3_1

label choice3_3:
    Anya "*Frustrated*...What are you talking about ?!"
    Amamura "The last time I saw you smile was at the school festival when we dance right ?"
    Anya "Yes…*embarass*...(BECAUSE OF YOU, AMAMURA!!!)."
    "Both of them have embarrassed at the same time and there is just only a sweet
    atmosphere."
    jump chapter3_1

label choice3_4:
    Anya "Why ? you speak like you got something."
    Amamura "It’s worth seeing you smile, you always act like you don’t have feelings when
    you talk to people."
    Anya "What are you talking about ?!… Jeez…(AMAMURA YOU STUPID!)."
    "Amamura confuse about what did he say wrong and Ayako turns her face to the
    side window to cover her embarrassment."
    jump chapter3_1

label chapter3_1:
    "Chapter 3" 

    Amamura "“Have you guy decide want do you want to eat ?"
    Yoru "Yup."
    Sora "Me as well."
    Amamura "See you guys at the table."

    "Yoru he had slightly pigmented light brown hair and was a slender androgynous
    handsome young man."
    "He was one of the top five most handsome guys at school and the girls
    entering the cafeteria kept sending passionate glances at him."
    "Sora He was a guy, a little shorter than Amamura, and had close-cropped hair.
    From Amamura’s view, he was his friend since middle school."
    "Each of them secured their dish and returned to their seats to start eating.
    Naturally, the one that gathered attention was the mapo ramen brought by Amamura."

    Yoru "Whoah...Looking at the real thing it’s redder than I thought."
    Sora "It’s not spicy? That ramen."
    Amamura "Hmm, not at all? Rather, it’s not spicy enough. It tastes good, though."

    "Yoru and Sora were sitting opposite of Amamura, and their expression
    looked like in awe when they saw Masachika slurping down the mapo ramen.
    The person concerned, Amamura, had a cool look."

    Yoru "Fun, let me have a little sip for tasting"
    Sora "Uuuh, this one is the one that comes later."

    "Intrigued, both of them reached out their chopsticks and took a bite of the
    noodles but, they instantly frowned and reached their hands to their cup. To
    such two people, Amamura said as if to admonish them."

    Amamura "Hey, you can’t call something spicy if the steam doesn’t sting your eyes,
    right ?"
    Yoru "In the first place, I can’t even slurp up really spicy ramen because it hurts
    my lips."
    Sora "It hurts your stomach too right?"

    "The entrance of the cafeteria became noisy."
    "Amamura and the others reflexively turned their eyes in that direction and
    three girls were just entering the cafeteria."
    "It’s a little like an idol appearance but, in fact, those three girls were all far
    better looking than most idols out there."

    Yoru "Really, they’re truly beautiful sisters, aren’t they? Ame sisters”
    That’s right, the girl in front of Ayako was a second-year and student
    council secretary, and her name was Ayame Ame. Her
    nickname was Masha and her a-year-older biological elder sister."

    "Her shoulder-length, wavy hair was light brown. Her gentle-looking slightly
    drooping eyes were also light brown. Her face too In contrast to Ayako, was a
    childlike face that was far more Japanese looking."
    "Her voluptuous body, the combination of her gentle-looking appearance and
    soft atmosphere; she radiated a motherly quality that was hard to believe for a
    second-year high school student."

    Sora "Hmmm!! I almost forget that I need to go to my club room."
    Yoru "I have business with my music band too."
    Amamura "So you guys gonna leave from me, I am sad you know."

    "Amamura speaks like a princess who feels lonely."
    
    Sora "Please don’t speak with princess tone of voice."
    Yoru "I am sorry Amamura it is an important one."
    Amamura "Just kidding just go, I can eat alone."
    Sora "Yoru, let's go."
    Yoru "See you at the classroom Amamura."
    Amamura "Guess I should finish eating this quickly."

    "Amamura met his eye with his friend in another classroom who is a student council member.
    she looks around the surrounding."
    "She sees Amamura table have an available seat."

    Amamura "Ah… Don’t come here."

    'Her call out to Ayako and walked straight towards Amamura direction.'

    "???" "Hachi-kun,  May I have a seat ?"

    "She was a first-year who served as the student council public relation, and her
    name was Suou Yuka."
    "She had long, lustrous waist-length black hair and in spite of her small build,her body was
    well-proportioned, asserting femininity properly."
    "her appearance was very well-groomed, with a hint of elegance in her cuteness. Even from
    a distance, you could see the girl’s good upbringing from her straight posture and her
    graceful conduct."
    "The moment Yuka said that Ayako, who was following behind her, had a
    wrinkle between her eyebrows."

    Amamura "Yes, you can have a seat."

    "She thanked Amamura with a beautiful smile on her face. Yuka then
    walked around the table and sat down next to Amamura. Ayako also sat down diagonally
    right ahead of Amamura."

    Yuka "Aah, as expected, Amamura-Kun ordered the same thing too, didn’t he ?"

    "Exactly as she said, on Yuka’s tray was a bowl of mapo ramen, the same as
    Amamura."

    Yuka "It’s delicious, isn’t it. I think it could be a little spicier, though."
    Amamura "I know, right. I need to add more chili oil."
    Yuka "Although we have salt and soy sauce here, there is no chili oil, isn’t it.
    Maybe we could consider it for the next student council agenda."
    Amamura "Hey, you’re mixing public and private affairs."

    "Yuka let out a giggle at Amamura’s retort while saying, “It’s just a joke”.At the two people’s
    friendly conversation, Ayako who was eating set meal A had a second wrinkle appear
    between her eyes. As before, Amamura and Yuka didn’t notice it."
    "While the area between her eyebrows wrinkled more and more at this, Ayako’s
    closed her eyes and corrected her expression, and asked in a casual tone."

    Anya "I wonder if you two are close ?"
    
    "To Ayako’s question, Yuka faced forward and answered while smiling pleasantly."

    Yuka "We are childhood friends."
    Anya "Childhood friends ?"
    Yuka "Yes, We have been at the same school since kindergarten, you know?
    Unfortunately, we have never been in the same class before, though."
    Anya "I see."

    "Ayako nodded really half-heartedly as if she was convinced and not
    convinced at the same time. This time, Amamura asked a question."

    Amamura "Do you two get along like that ?"
    Yuka "We are in the middle of trying to get along, I think? At least, I would like to
    be friends with Ayako-san, however."

    "At Yuka’s direct words, Ayako’s eyes opened wide and her eyes wandered
    about as if in a little bit of trouble."

    Anya "....I don’t think it’d be enjoyable being friends with me."
    Yuka "In other words, Ayako-san doesn’t mind being friends with me, do you ?"
    Anya "Eh.... I guess, so ?"
    Yuka "Then, let’s be friends! We are in the same student council and in the same
    first year after all. Aah, that’s right! If you don’t mind, is it fine for me to call
    you Anya-san ?"
    Yuka "I heard Masha-senpai and Hachi-kun are you calling you
    that, and I was thinking it was a lovely way of calling you."
    Anya "Ye-yes.... That’s fine, I think."
    Yuka "Fufuu, I am glad. Once again, I am looking forward to getting along with
    you, okay? Anya-san. And me too, please call me Yuka."
    Anya "Yes.... likewise, Yuka-san."

label choice4:
    Anya "Amamura-kun, what do you usually say about me to.... Yuka-san ?"
menu:
    "You always angry with me.":
        jump choice4_1
    "You always scold me in Russian language.":
        jump choice4_2
    "I am telling her that I respect you.":
        jump choice4_3
    "You don't have many friends to talk with.":
        jump choice4_4

label choice4_1:
    Anya "Don’t talk about a person like they’re hot-tempered. It’s all you reaping
    what you sowed, isn’t it."
    Amamura "Ahhhh, you're right."
    jump chapter3_2

label choice4_2:
    Anya "Don’t talk like I gossip about you in Russian language."
    Amamura "I did not say you gossip about me."
    jump chapter3_2

label choice4_3:
    Anya "-Wha….What…respect ?"
    Amamura "Respect in your very hard-working."
    jump chapter3_2

label choice4_4:
    Anya "I am not a loner!"
    Amamura "I didn’t say you are a loner I say it because I think you can have many good
    friends if you try to communicate and it is better for you to talk to someone else more than
    me who just a lazy students."
    Amamura "I am sorry that I raise my voice I just want you to make a friend that all…"
    Anya "THANK YOU FOR YOUR CONCERN BUT ONLY PERSON I WANNA MAKE FRIEND WITH IS YOU!!!"
    jump chapter3_2

label chapter3_2:
    Yuka "Let's change the topic of conversation, shall we?.... oh I forgot."

    "Before Yuka changed the topic of conversation she smirked and say to Ayako."

    Yuka "Anya-san, Hachi-Kun always says that he respects you Anya-san for your very hard
    work, you know."
    Anya "Eh?"

    "Ayako look toward Amamura but he avoids her to look face to face to cover his
    embarrassment."

    Yuka "You don’t have to be shy, Hachi-Kun."

    "When he turned his head, Ayako was pouting. Despite that, she had a somewhat happy,
    indescribable expression on her face. She glanced at Amamura, who looked back at her,
    then quickly shifted her gaze down to her hands and continued to eat in silence."

    Anya "(DON’T LOOK AT ME, IDIOT!!)"
    Amamura "I see you got embarrassed when I said I’m respecting you don’t you huh, I see."
    Yuka "Hachi-Kun, would you please consider the talk about joining the student
    council ?"
    Amamura "How many times have I told you? I have no intention of joining. Besides,
    didn’t you say you brought in a new member the other day ?"
    Yuka "I did but.... As expected, it didn’t last long."
    Amamura "Didn’t you say guys are too obsessed with love affairs and the like they
    won’t get anything done, so now you’re bringing girls? You said around three
    people joined but, don’t tell me, they all quit?"
    Yuka "Everyone, did.... We are lacking in abilities, they said."
    Amamura "Well see the same age girl having more talented that must make them feel like
    they are lacking abilities to do so."
    Yuka "In that aspect, Amamura-Kun should not have a problem in practical skills, and you
    can get along well with me and Alya-san, is what I think. In any case, you are a former
    student council vice president after all."
    Anya "Eeh?"
    "Ayako’s eyes widened in surprise at Yuka’s words. Receiving her gaze,Amamura’s face
    grimaced in displeasure."
    Anya "You were in the student council, Amamura-Kun ?"
    Yuka "He was, you know? Two years ago, In the middle school’s student council I
    was the president and Amamura-kun was the vice president."
    Anya "Is that, so.."
    Amamura "That was a long time ago. I don’t want to do it again."
    Yuka "Ayako-san may find it surprising but, even though Amamura-kun may
    appear this way, he is the kind of man who does things when he has to, you
    know? He usually gives this kind of feel, though."
    Amamura "What do you mean, ’this kind of feel’ ? Hey, what do you mean?"
    Yuka "Fufu, who knows? What kind of feel is it, I wonder ?"
    
    "Receiving Yuka’s words, Alisa showed a sullen look. And then she,
    somewhat dissatisfied, looked at them having a truly friendly exchange face-to-face."

    Anya "(I know it too, that much.)"

    "The Russian words she murmured didn’t reach the two of them."

    Yuka "Well then, I will go to the student council room for a bit."
    Anya "Uh okay, see you later."
    Amamura "See ya."
    Yuka "Yes. Please think about joining the student council, okay ?"
    Amamura "I did tell you I’m not joining."
    Yuka "Fufu."
    Amamura "Hey, what’s with that ‘I know I know’ face."
    Anya "You two are really close, aren't you ?"
    
    "Ayako’s cold voice pierced him. sounds colder than usual."

    Amamura "Are you surprise ?"
    Anya "Yes, I'm surprise. To think that you have a female friend."

    "Then he pointed at Ayako’s face with a look that seemed to say, “what are you talking
    about ?"

    Amamura "Female Friend ?"
    Anya "..."

    "Ayako blinked slowly with a straight face and tilted her head slightly."

    Anya "Are we.... Friends ?"
    Amamura "Yes ? Am I wrong ?"
    Anya "..."

    "Ayako fell silent for a moment and she suddenly turned around. Turning her back on
    Amamura, she replied with a flat voice, as if she was holding something back."

    Anya "That’s right, we’re friends."
    
    "After saying that, she started walking in the direction Yuka had went."
    
    Amamura "Hee~y, where are you going~ ?"
    Anya "I just remembered I have some business to do in the student council room.....Don’t
    follow me."

    "The very same day in the afternoon. There was a rumor among some students
    that Princess Ayako was walking down the corridor while humming, but for
    better or worse, the rumor never reached the ears of Amamura"

    "Chapter 4"
    # PAGE 15
    Anya "I'm home"
    Ayame "Welcome baack~, Anya-chan"
    Anya "I'm back Masha"
    Ayame "Geez, I did tell you to call me 'one-chan' when in Japan didn't I"
    Anya "Don't want to. Too late for that"
    Ayame "Uuu.... Alya-chan so cold...."
    Ayame "Hmmmm...."
    Ayame "Anya-chan, are you in bad mood?"
    Anya "....Not really?"
    "Ayako immediately showed a dubious look to hide her inner turmoil.However, it seemed that such deceptions didn't work on this older sister"
    Ayame "That reaction... as expected, was it that guy? Did something happen with Amamura-kun?"
    Anya "There's nothing happening"
    Ayame "That's a lie, you can't deceive onee-chan. Hey hey, what happened?"
    "Ayako gave up when they finally got into her room. Still, in her uniform, she satdown on a chair, and Ayame pestering Ayako to talk flopped down on top of acushion spread out on the floor. As if it's troublesome, Ayako opened her mouth."
    Anya "Really, it's no big deal.... We just got into a little fight\" \"Hee~~~ a fight!\""
    "Thinking normally, it's not a word to speak highly of but, Ayame's eyes sparkled for some reason, seeming joyful"
    Anya"....What?"
    Ayame"I mean... fufuu, to think Arya-chan got into a fight, it's really unusual isn't it. And it's with that guy even"
    Ayame "I, guess"
    Anya "I see~, a guy who can move Alya-chan's heart finally appeared, huh"
    Ayame "What are you talking about"
    "Ayako frowned towards Mariya's somewhat meaningful way of saying. Then Ayame said with a know-it-all air."
    Ayame "You like him, don't you? That Amamura-kun"
    Anya "....Haa?"
    "When Ayako thrusted her unreserved gaze to Mariya's face as if to say \"What's this flower garden for brains talking about\", Ayame shook her head saying, \"Good grief\"."
    "Classmate" "Hey hey, did you really easily pass that super difficult transfer exam test?"
    "Her classmates flocked to her with open curiosity. Ayako was a little fed up inside but, she
    tried not to be too rude and just dealt with them accordingly."
    "As a person who looked down on those around her, being close to someone was not good
    for either of them. It would offend the other party, and even she herself would feel the same if
    she found herself in that situation."
    "That's why she was not going to get close to anyone here either."
    # PAGE 16
    "Classmate" "Huh, already? Can't be helped. Then see you later, Ame-san"
    "Classmate" "I'd like to hear your story in the next break too, okay"
    Anya "Yes"
    "After seeing off her classmates regrettably returning to their seats, Alisa looked to the seat in the neighboring seat."
    Amamura "....., ......."
    "There, despite all the fuss happening, she saw the figure of a male student,
    plopped down on his desk, not bothered by it in the slightest."
    "Ayako's curiosity was more than
    a little piqued by this overly free spirit.Before she noticed, she found herself shaking his
    shoulder lightly, and talked to that classmate for the first time."
    Anya "Ermm... the bell already rang, you know?"
    Amamura "Mmm... huh?"
    "He raised his head at the sound of Ayako's voice. He was a male student with an ordinary appearance and a slovenly face."
    Amamura "Aaah~~ Are you the transfer student who gave a greeting at the opening ceremony?"
    Anya "Yes, Ayako Mikhailovna Ame. Nice to meet you"
    Amamura "Yeah... I'm Amamura Hachi Likewise"
    "After saying that much, Amamura turned to the front and stretched out one
    go. And then, with a look of realization on his face, he poked the back of the
    guy in the seat in front of him."
    Amamura "Heey~Yoru, you're here too, huh"
    Yoru "Yeah.... By the way Sora also here too, "
    Amamura "Oh, you're right. I was sleeping so I didn't notice"
    "After that, Ayako was caught off guard seeing Amamura start chatting
    pleasantly without minding her.Ayako was self-aware that she had a better appearance than
    most people."
    "Ayako understood that beauty was one of the weapons in interpersonal
    relationships and of course, she was also trying to improve herself in that
    regard. She didn't use make-up because it was against school regulations but
    still, she was proud of her beauty, which wasn't at all inferior to any celebrity
    out there."
    "She wasn't interested in attracting the attention of the opposite sex in
    particular but, she knew that her appearance, especially her silver, would
    attract people's attention."
    "For this reason,Amamura, who was almost the only one who showed no
    interest in her, made a lasting impression on her.
    However, when it reached the point where she started to pay attention to Amamura, Ayako
    noticed immediately."
    "It's not that Amamura was not interested in girls, nor was he not interested in other people.
    He's just a guy with no motivation for everything."
    "Forgetting his textbooks. Falling asleep in class. Hurrying to get his
    homework done at the last minute during break time. Not standing out and performing in PE class with the least minimum amount of effort. An ounce of
    motivation couldn't be felt from his feckless attitude."
    # PAGE 17
    Anya "Even in the most prestigious schools, there are students like this everywhere, isn't it"
    "With that said, Ayako lost interest in this neighbor. That all changed during the school
    festival in September.
    The last school festival of junior high school. It was a time period where
    many junior high school students were busy with exams."
    "They had decided to do something big for the last time and at Sora suggestion who
    became a member of the school festival executive committee, the class was to carry out a
    haunted house for their event."
    "But, it was overflowing with motivation only at the beginning. Despite everyone being in high
    spirits at the planning meeting stage, once the actual preparation work actually started, its
    plainness and difficulty made the motivation of the class go down and down."
    "Sensing the mood, Ayako quickly prepared herself to take on the bulk of the work.
    After school, Ayako remained alone in class to make costumes. She accidentally stuck
    her own finger with the needle, then reflexively she pulled her hand away."
    "She sucked and sterilized the appearing ball of blood with her mouth,This wasn't the first
    time she injured her fingers doing unfamiliar needlework. The band-aids around Ayako's
    fingers had already reached the fifth one."
    "However, she continued her work despite the throbbing pain coming from her fingers.
    She couldn't afford to be discouraged by something just this much. As long as she was
    participating, there was no way she was going to have a half-hearted event. With that in
    mind, she once again faced the costume."
    Amamura "Ah, as expected you're still here, huh"
    "The door of the classroom was opened with a clatter, and Amamura, who had disappeared
    somewhere as soon as the homeroom was over, came in."
    Anya "Amamura-kun.... What's wrong?"
    Amamura "Thanks for your hard work. Well, got a little something to do, see"
    "Amamura looked down at the several documents fluttering in his hands. Alisa was drawn by
    it and looked at it too but she didn't know what kind of documents it was."
    Amamura "Well, you should also go home today too, Ame-san. We can also work on that
    part again with everyone tomorrow, too"
    "Ayako became a little irritated at Amamura who said that while shrugging his shoulders."
    Anya "You'll never make it if you take your time... In the first place, isn't it that I'm doing it because no one was doing it"
    "She turned her irritation into clear rejection. Strengthening her tone, she pushed him away."
    Anya "You don't have to worry about me. After just a little bit more I'll go home too. So please don't bother me"
    Amamura ".... Aaa~ well, okay"
    "Amamura's gaze wandered about as he sat on his seat. He scratched his head and said in an as-matter-of-fact tone."
    # PAGE 18
    Amamura "For making the costumes, I've already talked to the handicraft club aboutgetting
    them to cooperate, so you can just leave it to them"
    Anya "Eh....?"
    Amamura "Also, here"
    "Ayako was stunned by his unexpected words, and Amamura held out thedocuments he had
    been holding."
    Amamura "It's permission to use the boarding house. If it's a staying over event, I tshould
    also motivate those guys who are losing motivation"
    Anya "Wah... such a, how..."
    Amamura "Nnn~ well, it's the student council. The former vice-president was.... No, I asked
    the former student council president, you see. Got a little connection with that person"
    "Ayako looked suspiciously at Amamura who suddenly said that hesitatingly but Amamura
    continued talking as if he was avoiding her questioning."
    Amamura "Yeah.... Well, so that is why. The handicraft club agreed to lend a male-helping
    hand. If you tell them it's a chance to show the girls in the handicraftclub your reliability,
    some of the guys will be happy to take it, right.Regarding the preparation for the activities...
    well, I guess it's Sora's jobfrom here"
    Amamura "Anyway, you can go home now. It's no use if Ame-san is doing your best
    alone,right"
    "At Amamura's casual remark, Alisa's pent-up emotions were unleashed."
    Anya "What do you mean... it's no use?"
    "She was struggling with the unfamiliar needlework and was stressed out, and the usually
    unmotivated person she looked down upon in her heart offered her a solution, and then
    denied her efforts."
    "That fact pushed down the bulwark in her heart.
    Before she realized it, Ayako slammed the costume she was working onto the desk with a
    bang."
    "She stood up with the same vigor and severely glared at Amamura."
    Anya "I....! As long as I'm participating, I will make sure this event is good! For itto be
    presented in half-hearted shape on the actual day, I absolutely don'twant that! I absolutely
    don't want to make compromises!!"
    "Ayako herself was aware that more than halfway through she was venting outher anger at
    him, but the words wouldn't stop."
    Anya "But.... I know, I know that I'm being selfish! Everyone is not as serious as me, I know
    that! That's why I'm trying to make up for that! Do you know what am I doing wrong!?"
    "She let emotions get the better of her, and lashed it out on someone. It was the first time for
    Ayako since elementary school."
    "Ayako who usually didn't show her feelings, good or bad, showed her bare andintense
    emotions."
    "In response, Amamura opened his eyes wide and said clearly."
    Amamura "You're putting effort in the wrong direction"
    Anya "Eh-?"
    # RAGE 19
    Amamura "A school festival's event is not something you create alone. We all have to
    work together to make it happen, right? If you want to have a good event,instead of giving up
    that everyone isn't going to do it anyway, shouldn't we think about how to motivate everyone
    to do it instead?"
    Anya "...."
    "Ayako wanted to turn her head away.However, Ayako's pride would not allow her to do that.
    She glared back at Amamura as hard as she could, determined to not be defeated insilence.
    But before Ayako could say anything else, Amamura looked away."
    Amamura "....But you know, I would also be annoyed if I were talked to like that. It's my bad."
    "I know that Kujou-san was doing you best, and I'm not going to deny that
    He bowed his head slightly, and Ayako was not sure what to do."
    "Her anger that was lashed out on him was returned with an apology. Her raised fist had
    nowhere to go."
    "Above all, \" I know that Ame-san was doing you best\". Those words were so strangely close
    to her heart that she couldn't breath."
    Anya "....I'm going home"
    Anya "What's with him...? What's with him really, geez!"
    "The next day"
    Sora "You guys! We have a stay oveeeeeerr!!!!"
    "The schedule for that day had been set up. When the meeting was over, everyone was
    happily discussing the upcoming stay-over.
    They were even more excited than when they were planning the school festival's
    program."
    "Then the day for the preparation of the stay over came.
    In addition to the activities at night, the guys who were lured by the bait of the girls'
    home-cooked meals, worked unusually hard and the work progressed at a rapid pace."
    "The high morale continued even after the stay over, and on the day of the
    school festival, Alisa's target was achieved.... No, the haunted was even of a higher quality.
    In the end, the sales amount was the highest among all programs and they even received
    an award for that."
    "The closing party after everything was done. While the students were folk-dancing in a
    circle in the schoolyard, Ayako was walking towards the school building when she came
    across Amamura sitting on the stairs in front of the entrance."
    "Amamura was sitting with his knee up resting his chin there while he was looking at the
    schoolyard with a wry smile."
    Amamura "Aah, Thanks for your hardwood. Kujou-san"
    Anya "Ah...."
    "Ayako followed his gaze. There she found Sora, who seemed to be calling out to every girl
    he could find, and Yoruwho seemed to be invited to dance by girls one after another."
    Amamura "Haha, those guys really got it tough"
    Anya "....You're not going to join them?"
    "Amamura raised one of his eyebrows and shrugged his shoulders."
    # PAGE 20
    Amamura "Hmm? I don't even have a partner to dance with... But then, this school is
    very old fashioned-like in this way. Holding folk dances at the closing party these days...
    Well, there's no campfire, though"
    Anya ".... Can I... sit next to you?"
    Amamura "Hmm? Aah, it's fine but, are you not going to dance? If it's Ame-san I'm
    sure you'd be in great demand, right? Ah, by chance, do you not know how
    to folk dance?"
    "Aykao" "That's rude. I used to do ballet when I was little, you know? I can dance like
    that in no time. But well, it's troublesome so I pretended I can't dance and declined the
    invitations"
    "Ayako sat down next to Masachika while snorting her nose and brushing her
    hair to her back."
    Amamura "Thanks for your hard work again.... for that one"
    Anya "I'm not really bothered though? I'm used to it so it's not a big deal"
    Amamura "Is that so. That's the Aloof Princess for you"
    Anya "What's with that name?"
    "Towards Ayako knitting her eyebrows in suspicion, Amamura a said in surprise."
    Amamura "Huh? You don't know? It's what the other students recently call Ame-san,
    though"
    Anya "....Ummmm"
    Amamura "You don't seem... to be happy with it huh?"
    Anya "What I'm not happy about is the \"Princess\" part"
    Amamura "Why? Isn't that just a normal complement"
    Anya "You think so? To me, it sounds like someone who lives in a dream, notknowing any
    hardship"
    Amamura "Aaah~ I see, there's also a way of seeing it like that?"
    Anya "It's true that I was born with looks and talents more than what most people have. But,
    I've never once sat on my hands. I don't like it when people talk about my past efforts as if I
    was just born lucky"
    Amamura "I see"
    "Amamura showed his understanding that she was not happy with the idea."
    Anya "....Thank you, Amamura-kun"
    "Ayako said quietly while still looking to the front."
    Amamura "Hmm? What for?"
    Anya "I think... this is the first time I've ever finished a school festival with such joyful
    feelings"
    "She always had to cover for the other members, and when it was all done, she
    felt more exhausted than accomplished."
    "The sense of accomplishment that came from working together was greater
    than the sense of accomplishment that came from working alone. Now, there
    was a certain exhilaration in the midst of the fatigue."
    # PAGE 21
    Anya "Like you said, I was wrong. If I tried to do it alone, I don't think I would be able to
    spend the school festival feeling this way.... And, I'm sorry. I vented my anger on you"
    "When Ayako apologized clearly while looking away, Amamura waved hishand in an
    uncomfortable manner."
    Amamura "Don't worry about it. Besides, I just did some light formalities, and I didn't
    work as hard as Sora and Ame-san"
    "Indeed. It was actually Sora who led and motivated their classmates. But, the one who
    moved Sora, and set up all of the groundwork was Amamura."
    "The person himself might have said that he hasn't done anything big, but Ayako knew it
    was Amamura who had done the most."
    Anya "But I do mind it. I want to do something to apologize for taking out myanger on you
    and to show my thanks to you for... this time. Is there anything in mind?"
    Amamura "Thanks.... thanks, huh?"
    Anya "Don't answer with there's none, okay"
    Amamura "Hmmm~..."
    Amamura "By the way you have a nickname in Russia?"
    Anya "What? It's so sudden"
    Amamura "Alisha? No, is it Alishika, Alichika? Something like that was the nicknamein
    Russia, wasn't it?"
    Anya"....It's Anya. My family calls me Anya"
    Amamura "I see... Then, in return for the apology and thanks, I'll have you give me theright
    to call you Anya"
    Anya "What's that? How's that me thanking you?"
    "When Ayako frowned in confusion, Amamura showed a wry smile."
    Amamura "I will be the only person and the only guy who calls the idol of the class
    everyone admires by her nickname."
    Anya "Are you an idiot?"
    Amamura "Thank you very much!!"
    Anya "Gross"
    "Ayako spit that out with a put-off face to Amamura, who suddenly started saying something
    stupid. And there, one of the boys who had been hanging around in the surrounding all the
    time called out to her."
    "Male student" "Err, um, Ame-san. Would you like to dance with me?"
    "Male Student" "Aah, you can't just steal the march! Ayako-san, to tell you the truth,you've
    been on my mind all the time. Please dance with me!"
    "Male student" "Didn't you just confess in the heat of the moment! Then I will too-"
    "Starting from one guy calling out to her, all at once five, six guys swarmed Ayako."
    Anya "I'm sorry. I can't dance"
    "Even though Alisa apologized and clearly rejected them, all the guys were so
    determined to dance with her and showed no sign of backing down.Slowly, the guys came
    closer. Alisa suddenly narrowed her eyes and stood up."
    Anya "You people-"
    # PAGE 22
    "Suddenly Ayako's right hand was being pulled to the right in one go."
    Amamura "A-My bad, we have prior promise. Let's go, Anya B-Sorry Guy!! she mine now
    hehe C-I ask her first I get first HEHE Let's Go Anya! D-She said she want to dance with me
    so goodbye"
    "Amamura said this so the guys would hear it and he walked to the schoolyard while still
    holding Alyako's hand."
    Anya "Wa-wait...!"
    "Ayako hurriedly followed him while raising a voice of protest against the forcefulness.
    Normally, she would have forced him to let go of her hand and given him a slap but at that
    moment, Ayako followed Amamura in a surprisingly obedient manner."
    "Her heart was racing. She couldn't take her eyes off of the big back of Amamura ahead of
    her."
    "When she thought about it, it was the first time for Alisa that an opposite sex forcibly held her
    hand and pulled her."
    Anya "That's right, it's my first time experiencing this so I'm just a little confused.
    There's nothing more, that's all!"
    "As Ayako said this to herself, Amamura stopped in the middle of the circle of students.
    Simultaneously, the last song began to play."
    Amamura "Aah right, you said it earlier right? That you used to do ballet so you can do folk
    dance just from watching"
    Anya "Ye-yes, what about it?"
    Amamura "Then, how about you show me what you've got? Oh . PRINCESS?"
    "A teasing way of speaking. Based on what was said earlier, his intention was clear."
    Anya "....You have some nerve. Do your best to keep up with me so you don't
    look like a fool, okay."
    Amamura "Don't step on my foot out of being too eager, yeah? Anya-chan?"
    Anya "Bring it on!!"
    "In the last dance, where normally was a time in which two people who loved each other
    danced, the two of them challenged each other with an atmosphere totally devoid of any kind
    of sweetness."
    "With her long arms and legs spread gracefully, Ayako danced in a non-serious manner
    through the schoolyard at night. Although her dance fit the song, it was no longer something
    that could be called a folk dance."
    "However, Amamura properly moved in line with his out-of-control partner His movements
    were not equal to hers. But he wasn't being pushed around either."
    "He was trying to say out of his partner's way. Despite all that, he's also doing a good job
    of not letting her get out of control. Their match was miraculously formed as a dance with a
    clear distinction between the main and supporting roles."
    Anya "Ah, that's right. that's.. all you're about, isn't it 'Keeping yourself from the limelight
    and supporting others. Staying in the shadows and making others shine. That was the kind
    of person Amamura was'."
    Anya "Fufu.... Ahaha!"
    "Before she realized, Ayako was laughing."
    # PAGE 23
    "However, that time didn't last long. Not long after that, the song ended and the dance was
    over. Feeling reluctant, she let go of Amamura 's hands and bowed."
    Amamura "....Then, I'll be returning first"
    Anya "Oh my? You're not going to escort me?"
    Amamura "Give me a break. If I do that all those jealous guys will come and kill me"
    Anya "HEHE. I see, that's nice to hear"
    "Ayako smiled at Amamura lowering his head and smoothly wrapped Amamura's arm around
    hers."
    Amamura "Wai-, what are-"
    Anya "So, could you escort me, please?"
    Amamura "....In other words, you want me dead?"
    Anya "It's a punishment for calling me a princess"
    Amamura "Uugh...."
    "As Amamura, with a dejected look, began to walk without shaking off her arm, Ayako
    smiled good-humoredly as she finally managed to score a hit on him."
    "After all this time, she felt embarrassed by her own actions but even more than that, she
    felt good. She was walking shoulder-to-shoulder with someone. She was incredibly happy
    about that."
    "On the short distance heading to the school building. Ayako felt that the vague sense of
    loneliness and alienation she had felt ever since her elementary school days started to melt
    away and disappear, little by little...."
    "The Next Day"
    Amamura "Morning. Anya, my bad. Can you show me the textbook for modern Japanese?"
    "Amamura was... returning back to the unmotivated Amamura ."
    Anya "...."
    Amamura  "He-hey, what's wrong? Anya. You're looking at me like I'm trash, you know?"
    Anya "This piece of trash"
    Amamura "Isn't that blow too strong!?"
    Anya "....Hmpphh"
    "As Amamura screamed with a stiff smile, Alisa let out an ostentatious sigh and turned her
    face away as if in a bad mood."
    "Then while still looking the other way she thrusted out the textbook for modern Japanese
    straight forwardly and let out a brief comment in Russian."
    Anya "【Even though you looked so cool yesterday】"
    "she muttered that softly.
    Even after that Amamura remained the same. He was always so unmotivated and always
    made her exasperated. And yet, when the time came he was more reliable than anyone
    else."
    "He casually supported others as if it's something trivial.For Ayako who always saw everyone
    around her as her rival, Amamura 's behaviour came out as strange but.... At the same time,
    she felt relieved."
    # PAGE 24
    "She didn't have to compete with this person. Knowing that she didn't have to compete for
    superiority with him lightened Ayako's heart. Since then, Ayako was able to get in touch with
    Amamura without worry."
    "Frustrated by his usual lack of motivation, she would give him a scolding.
    Annoyed by his usual air of composure, she would tease him. Aggravated by his stance as
    if he was watching over her from above, she would show him a gap in Russian and laugh at
    his silly obliviousness."
    "As she spent her days like that, before she noticed it she...."
    Ayame "So you've fallen in love with him right~ How wonderful!"
    Anya "Like I said.... That's not it. Did you hear what I said?"
    Ayame "Eee~h? No matter how I heard it, it sounded like two people's beginning of love
    though?"
    Anya "Don't put it strangely like that. Earlier didn't I tell you we are friends?"
    Anya"But well... let's see. Regarding his ability.... I've recognized it. And I also... trust him"
    Ayame "Mm-hmm, a boy who does what he has to do is cool right. Anya-chan so cute when
    you acting like this."
    Anya "If you not going to listen to me could you leave!?"
    Ayame "Eh! Anya so cold"
    Anya "Besides, I prefer someone who is usually hardworking"
    Ayame "You don't get it, Anya-chan. He is usually a downer, but at a moment's notice, he
    shows his manly side! I think that's ni~ce"
    Anya "It's a difference in opinion. I'm usually.. Rather seriously annoyed at the
    usually unmotivated Amamura-kun after all"
    "Perhaps because she remembered a lot of things while she was talking, Ayako continued
    with a stronger tone."
    Anya "Really, forgetting things all the time, sleeping in class, moreover! No matter how
    many times I warned him, he doesn't even feel sorry! Always evading frivolously and
    elusively... well, that's why I can say whatever I want to him without worry though...."
    Ayame "I see I see. In other words, there's a trusting relationship between you two, right?"
    Anya "How it became like that"
    Ayame "No matter what was said, Amamura-kun will never leave you. Precisely because
    you know it, Anya-chan is able to talk to Amamura-kun without hesitation, right? And
    Amamura-kun tolerates it. Isn't that a splendid trusting relationship"
    "Ayame start to teash Ayako"
    Ayame "Anya-chan is in love!~~ Anya-chan is in love!~~,Anya chan is in love!~~"
    Anya "Stop! I gonna go change so get out!"
    "After chasing Ayame out of the room with a miserable look on her face and drooping
    shoulders, Ayako looked down at her right again and gently ran her fingers down her own
    thigh."
    "Feeling somewhat embarrassed, she looked up and there was a large mirror. What reflected
    was Ayako with cheeks slightly dyed in red."
    Anya "Muu...As if to deny herself such a thing, Alisa made a sullen face. She then muttered with a grim
    expression"
    Anya "【Am I being honest...】"
    "The Russian words she leaked out in a whisper melted into the air in the room, and
    disappeared without reaching anyone."
    # PAGE 25
    "Chapter 5"
    "School is over Amamura is going to leave school Then the phone in his pocket vibrated
    Just to be safe, he looked around to make sure there were no teachers nearby, and
    Amamura took out his phone and looked down at the message displayed on the screen."
    Amamura " seriously..."
    "He then let out a small sigh and turned on his heel.
    Going down the hallway, he knocked on the door of the room indicated by the message
    and opened it. Right there, the perpetrator who called out Amamura to come here, Suou
    Yuka, turned her head to look at Amamura."
    Yuka "Ah, Hachi-kuu~un. Come come~"
    "who had been crouching down in front of a shelf organizing equipment, smiled like a
    blooming flower. She held her skirt down while standing up.... And immediately afterwards,
    she rushed over to Amamure in pitter-patter while raising a sweet voice."
    Yuka "Thank you for coming Hachi-Kun"
    Amamura "Why you called out for me when you have other friend to help you huh Yuka???"
    Yuka "Yes I can but I choose you because you used to do a student council work so It will
    be faster if the person who comes to help is you…andddd because you are my friend so you
    are the first one who I will…"
    Anya "EHEMMM"
    "Before Yuka can finish her sentence Ayako interrupts the conversation"
    Amamura "....So you're here, Anya"
    Anya "Yes, I'm here. I'm sorry, okay? That I'm being a bother"
    Amamura "No way, haha...."
    Amamura "Err... so? You want me to help you organize the equipment?"
    Yuka "Yes. It seems just the two of us were not enough to do it... May I ask for your help?"
    Amamura "Well, I guess I could help.... I got the feeling that I need to start with other
    problems first though and it doesn't feel great"
    Yuka "For now, could you please start from around here?"
    Amamura "Desks and folding chairs. Checking for the quantity and damages, huh.
    Ro~ger..... Wait, I've been wondering since middle school but, is this a job for student
    council....?"
    Yuka "Who knows... but, it is really convenient at a time of an event to know whatequipment
    is available, where they are, and how much you have, you know?"
    Amamura "Uhuh, that's true but... this, I think it's unreasonable for two girls...."
    Yuka "Just in case, the president intends to lend us a hand later but anyhow, the president is
    also very busy too"
    # PAGE 26
    Amamura "I see"
    "Once again realizing the lack of human resources in the current student council, Amamura
    began his work."
    "For a short while, it was silent inside the room. What was audible was just the sound of
    equipment being moved around and something being written on the list. In the silence,
    Ayako's Russian slipped out."
    Anya"【Give me your attention, too】"
    "A critical hit on Masachika's heart! It was a surprise attack and it was very effective!"
    Amamura "Ngguuuh~~! seriously Anya…in this time"
    "Biting his lips, Amamura desperately struggled to endure the coming onslaught of mushy
    feelings."
    Anya "【Give~ me~ , give~ me~ , give me~ your attention】"
    "The pressure is.. incredible....!"
    "Amamura was vomiting blood in his heart at Ayako calling out in a whisper as if singing. It
    was not a situation where one could say she didn't mean it anymore."
    Amamura "Rather, how do you feel about this!? Are you not embarrassed!?"
    "Amamura was screaming his thoughts inside but, even Ayako too was embarrassed."
    Anya "Hnnnnggg—–!!"
    "Ayako writhed in agony, soundlessly. As she crouched down in front of a shelf to do her
    work, deep down Alisa was excited in various ways.She glanced behind her to check, even
    though she knew her thoughts didn'tget through."
    "She was relieved to see Masachika's back as he continued his work"
    Anya "Fu, fuu~n. He didn't get it~. It's an easy to understand appeal too.... Tru-truly, he's
    really not sensible"
    "They were working with their backs to each other, but in reality, those two's bodies were
    trembling in shame. It was very funny to watch from the side."
    Anya "【Give~ me~ it~, give~ me~ it~】"
    "Yuka called out to Alisa from the entrance, though she probably hadn't noticed the state of
    the two of them."
    Yuka "Anya-san, is something the matter?"
    "Ayako was startled, but quickly glossed over her appearance and tone."
    Anya "\"Aah, I'm sorry. I was singing a little\"【Not you】"
    Amamura "–Not her, all right! I knew it!"
    Yuka "He- hee~h, a Russian song? What song?"
    Anya "\"The title is...\"it\'s Unreachable Feelings\'?"
    Amamura "UNREACHABLE!.... UNREACHABLE FEELING!!?? YOU THINK IT DIDN'T
    REACH? IT REACH ANYA!!'"
    "Amamura screaming in his head while he cover his face"
    # PAGE 27
    "Moment later"
    Yuka "With this, we are more or less done. Thanks for your hard work. Thank you very
    much,Hachi-Kun"
    Anya "Thank you, you really did help us"
    Amamura "Yeah"
    "About an hour later, with the remarkable work of Masachika, who had put his heart and soul
    into it, the three of them left the equipment room having finished the work much earlier than
    planned. Then, a large male student approached them."
    "MaleStudent" "What, are you done?"
    Yuka "Aah, president. Thanks for your hard work. And yes, thanks to Amamura-kun's
    cooperation, we finished much earlier than scheduled"
    Touya "Ah, so you're Kuze, huh. I'm Kenzaki, the student council president. I've heard
    about you, you know? I heard you're considerably outstanding"
    Amamura "Uhuh, thanks"
    "While giving a light bow, Amamura looked up at the man in front of him. Self-introduction
    was unnecessary, Masachika already knew who he was."
    "Second year, Kenzaki Touya. He was the charismatic student council president leading
    the current student council of the high school section."
    "He was a big man. In addition to being tall, he had broad shoulders and thick chest,
    which made him look bigger than he actually was if you looked at him up close. At a glance,
    he wasn't a particularly handsome man."
    "Rather, he had a quite old-looking face. Together with his physique, he didn't
    look like a second-year high school student."
    Amamura "Then, I will leave now"
    Touya "Hold on. It'd be a shame to send you home without giving anything back after
    receiving your help. Time is of the essence. If you like, let me treat you to a meal at least"
    Amamura "Err, just your feelings are enough...."
    Yuka "Isn't it fine to accept it. Either way, when you get home you won't have any food,
    right?"
    Amamura "Yuka...."
    Touya "Hmm? Why does Suou know about Kuze's home situation?"
    "Yuka replied with a clear smile towards Touya and Alisa's very reasonable questioning look."
    Yuka "We are childhood friends after all"
    Amamura "That not an answer"
    Touya "Is that so.... Well, that being the case then it's just right. Suou and Ame little sister
    also come too. It's my apology for pushing the odd jobs to you.It'll be my treat today"
    Yuka "It's my pleasure to accept it, president"
    Anya "....I understand. Thank you very much"
    "Anamura" "Eee~h seriously"
    "The next thing he knew, he was supposed to go. To be honest, he wasn't too keen on the
    idea, but he couldn't bring himself to obstinately refuse. Thus,Amamura reservedly followed
    after them."
    Amamura "So this is the strength of the student council president, huh...."
    # PAGE 28
    "As he was thinking about that with resignation, Yuka looked back and gave him a
    complacent smile. Apparently, this was really her true aim."
    Amamura "So this is the ploy of the student council public relation, huh...."
    "Amamura sighed inwardly. Going by the flow, Amamura turned his attention to Amamura
    walking next to him."
    Anya "....What?"
    Amamura "Well, no reason"
    Anya "What's that. It's usually rude to stare at a woman's face for no reason"
    Amamura "Sorry"
    "It was a valid point, so Amamura honestly reflected on it and looked forward."
    Amamura "So this is the cold treatment of the student council accountant, huh...."
    "Amamura was thinking stupid things while having a distant look inside."
    Anya "【Now I'm nervous, aren't I】"
    "Still having a faraway look, Amamura vomited blood. He could feel Ayako with a smirk on
    her lips glancing at him, but he had no room to spare to react. Amamura Mental Point was
    already zero."
    "Four of them entered a family restaurant about ten minute walk away from school
    Ayako sat down next to Amamura and Yuka sat down next to Kenzaki"
    Touya "Don't mind it. It's not uncommon for me to be late for a student council meeting, go
    out to eat and then go home. It's a school regulation that has long since become an empty
    word. Never mind that and order anything you want. Anything less than a thousand yen,
    of course"
    Yuka "President, you did lose half of your coolness with those last words, you know?"
    Touya "Fuu, Manliness won't fill your wallet, Suou"
    "As soon as they finished their orders, and precisely within a thousand per person, the topic
    of conversation immediately turned to Amamura."
    Touya "Even so, you managed to go through all that in so little time, huh. I was prepared
    it'd take until tomorrow, though"
    Yuka "It was thanks to Hachi-Kun doing his best after all. As expected, having
    a male help really makes a difference. Especially if you are used to it"
    Touya "I suppose you're right"
    Yuka "Hachi-kun is amazing, you know? He can do physical and office work without
    complaining, and he is also very good at negotiation and making connections"
    Amamura "Hey, Yuka. You're praising me too much. Overestimating someone even has
    limits"
    Touya "Hoh, it's unusual for Suou to say that much. What do you think, Amamura Are you
    interested in joining the student council? It's just right when we don't have anyone for the
    general affairs"
    "It came to this after all. Amamura glared at Yuka glancing at him from his side, and then
    formally informed Kenzaki."
    Amamura "I'm sorry but, I'm not going to be in the student council anymore. I already
    learned my lesson in the middle school"
    # PAGE 29
    Touya "I see.... It's true that the work of the student council in the high school section is
    more exhausting than in the middle school, but it's worth the effort, alright? Compared to
    other school, our school gives the student council a lot more discretionary power, and to be
    honest, it's going to have a big impact on your personal evaluation"
    Amamura "Unfortunately, I don't have that much ambition or aspiration. Currently I don't plan
    to go to another university and the idea of having connections with big-shots isn't particularly
    appealing to me"
    "For Amamura , who was just spending his daily lives casually without any future goal, such
    things were of no particular benefit, however."
    Yuka "Don't say that, and let's work together in the student council. And then, let's run for the
    election again, shall we?"
    Amamura "Don't increase your requests so casually. I mean, even without me you're almost
    certain to be the next president, right? You're the former middle school student council
    president after all"
    Yuka "I want to work in the student council together with you, Amamura-kun"
    Amamura "Don't want to. It's troublesome"
    "More than 90% of the male students at school would most likely involuntarily nod their heads
    to Yuka's begging, but Amamura just cut it down. Looking at them amusingly, Touya stroked
    his chin."
    Touya "Amamura, to say Suou is surely to win the election is a big mistake, alright? There
    are other candidates too, and there's this Ame little sister"
    "Saying that, he glanced down at Ayako who sitting next to Amamura. Lured by it, Amamura
    also looked at her and his eyes met with Ayako 's staring at him silently."
    Amamura "Anya, are you planning to run for the next student council president election?"
    Anya "Yes, Yuka-san and I are going to fight for it next year"
    "Ayako looked at Yuka in front of her. Yuka met her gaze with a calm smile."
    "Amamura conjured up a vision of flames rising behind the two of them.As if to break the ice,
    Kenzaki now brought up a subject to Ayako"
    Touya "Come to think of it, Ame little sister is sitting next to Kuze in class, huh. So how's
    Kuze? From your point of view"
    "But as it turned out, it was an act of adding fuel to the fire."
    Anya "Even if you asked me how's him... If I were to put in one word, it's ‘frivolous'"
    Touya "Hoh?"
    "Ayako trashed him with a cold-hearted face, while Kenzaki looked very interested.
    Immediately after she glanced at Amamura,
    But Amamura was aware of it and could only shrug his shoulders."
    "Rather, \"Way to go, keep at it and bring down Yuka's exaggerated praises\", what a way he
    was thinking about."
    Anya "Always forgetting things, and his attitude in class can't be said to be good either. It
    seems quicker to look for his grades from the bottom, too"
    Yuka "Masachika-kun is.. Only doing the bare minimum when his motivation is
    low after all. But  he always managed to just precisely not get a failing mark, though"
    # PAGE 30
    "Yuka immediately made a follow-up after Ayako's relentless evaluation of him. Ayako's
    eyebrows twitched, and flames once again appeared behind her."
    Anya "....I guess so, I'm sitting next to him so I know his scores. Even on quizzes,he's
    always avoided retests. That impressed me a little. If only he really puts his mind into it,
    couldn't he get high scores, is what I think, too"
    Yuka "Hachi-kun is originally really smart after all. He was also able to make it into Seirei
    without much trouble. Ah, I know all this because we are childhood friends, though"
    Anya "Amamura-kun is not only smart but he is athletic too and yet.. he's not very good
    at ball games. Sometime ago too, in basketball lesson he jammed his fingers"
    Yuka "Hachi-kun.. hasn't been good at ball games since he was little.Although I said that, I
    can't speak for others. Aah,Hachi-kun, your favorite in PE class is endurance run, right?"
    "Blazing Blazing Blazing"
    "Phantom flames blazed up behind Ayako. Wondering if it hit him, sweat started to ooze out
    from his forehead. However, he didn't feel hot at all in reality."
    "It was strange that Yuka, who was facing her directly from the front, had a cool face."
    "Waitress" "Tha-thank you for waiting~"
    "Then, the employee called out shyly, bringing their food."
    Touya "Oh, the food came. For now, how about we start eating"
    "After they had finished eating in the family restaurant, they went outside and as one would
    expect, the surrounding was already dark"
    "Thank you for the meal"
    "After Touya was done paying the bill, he left the family restaurant. The three juniors each
    thanked him and Touya nodded humbly. Then he made a thinking face as he moved to the
    parking lot."
    Touya "Ame little sister is a walker, aren't you. Suou takes the train like me, how's
    Amamura getting home?"
    Amamura "Ah, I'll also be on foot"
    Touya "Is that so. Then Amamura, send Ame little sister home. I'll send Suou home"
    Amamura "Yes"
    Yuka "Umm, President. I really appreciate your consideration but, I will call for a car so it's
    fine"
    Touya "Mu, is that so?"
    Yuka "Yes. I will wait here until the car arrives, so please don't worry about me"
    Touya ".... I see. Then, see you next week"
    "Amamura saw Kenzaki off, who told them so and walked towards the station.
    Then Amamura made eye contact with Ayako."
    Amamura "Well then, let's go?"
    Anya "It's not like, you have to go out of your way to send me home. It's fine"
    Amamura "That reason won't work. C'mon, let's go. See ya, Yuka"
    Yuka "Yes, see you"
    Anya "See you in a few days, Yuka-san"
    Yuka "Yes, Anya-san too"
    # PAGE 31
    "Yuka bowed beautifully while sending them off. Amamura and Ayako started walking in the
    opposite direction Kenzaki was headed."
    Amamura "How far is Anya's home on foot?"
    Anya "Roughly about twenty minutes"
    Amamura "I see, you sure do walk a lot"
    Anya "How about Amamura-kun?"
    Amamura "Me? About 15 minutes I guess. Considering our walking speed, maybe the
    distance is not that different"
    Anya "Oh"
    "While escorting Ayako to her apartment he thinks about the Students Council and about the
    election about the Student council next year he ask Ayako."
    Amamura  "Anya"
    Anya "What is it?"
    Amamura "I think I am going to…. join a Student Council"
    "Ayako feels surprise and ask Amamura"
    Anya "Really that unexpected"
    Amamura "I thought so"
    Anya "Can I ask why ? you say you are not motivated but why are you suddenly tell me that
    you are going to join the student council
    Amamura: Because…."
    "Moment Earlier In Restaurant"
    "While Kenzaki check his bill and Yuka going to the toilet she ask Ayako"
    Amamura "Anya can I ask something?"
    Anya "Yes sure What is it?, I hope is it important one"
    "Anamura"  "You said earlier that you going to Join Student Council President election so who
    going to be your vice-president with you?"
    "Ayako surprise about what he ask and start thinking for a while"
    Anya "There's none. But, it's not particularly a problem. Things like vice-president, it's
    unnecessary"
    Amamura "No, saying it's unnecessary is.... As long as there's a rule to run the
    candidacy in pair, it's not unnecessary"
    Anya "It's fine as long as the vice-president's name is on the paper, right? I'll find
    someone to bear that role for me at random"
    "Those words made Amamura feel terribly lonely. This was it. This was why Ayako looked
    helplessly fragile."
    "Not relying on others. Not expecting anything from others. Not seeking
    recognition nor praises from others, only trying her best to pursue the results she envisioned."
    "No, perhaps it was precisely because she was thinking everything was for her own
    self-satisfaction that she believed she shouldn't be relying on others.
    Amamura just couldn't leave Ayako alone."
    "It was because he knew the limit of what one person could do. And because he knew the
    sadness, the pain, and emptiness one felt when their efforts were not rewarded."
    # PAGE 32
    Amamura "Efforts.... Should be rewarded. Human beings who truly exert efforts
    with their all should seize the results they want"
    "Precisely because of this belief that Amamura had been able to considerably help Alisa
    until now."
    "He even tried to ease up Ayako's unapproachability by involving the people around her,
    getting her to cooperate with the people around her, and taking the initiative to call her by her
    nickname."
    Amamura "I see"
    "While he was about turn to face Anya to ask more questions she suddenly speak in Russian"
    Anya "【IF IT POSSIBLE….I WANT YOU TO BE THE ONE】"
    "That sentence make Amamura stand still like rock"
    Amamura "But I…"
    "He didn't have the radiance of soul that Ayako, Yuka and Touya had.
    Neither the initiative to set his own goals, nor the passion to continue exerting efforts, facing
    forward."
    "Always leaving his goals to others . Always relying on the passions of others."
    Amamura "I …. am not worthy"
    "Amamura was.. grateful that Ayako's words had been leaked out in Russian.If even if it had
    been said in Japanese Amamura still would have had no choice but to choose cowardly
    remaining in silence."
    Amamura "I am not worthy..But!!! I will ma…"
    "This is why he going to joined a student council one only cause to make Amamura join
    Student Council"
    "Back to the present"
    Anya "So that you can run for the student council president election together with Yuka-san?
    Ayako interrupt Amamura before he start to talk"
    Amamura  "… And if so?"
    "Amamura returned Ayako's question with another question."
    Amamura "If so, what would you do? Are you gonna give up becoming one?"
    Anya "NO"
    "Ayako closed her eyes for a moment as if to cast away her complacency, and replied with
    eyes harboring strong radiance."
    Anya "I will.. definitely be the student council president.... Even if.. the opponent is you. I'm
    never going to give up"
    "Amamura's expression loosened at those powerful eyes."
    "I wanted to see this radiance.
    I wanted to protect this radiance."
    "Longing for this radiance of her fragile, yet noble soul, I've quietly supported
    so it won't ever get clouded."
    "So far, only from the shadows."
    "But, from now on...."
    Amamura "I see"
    Anya "....."
    # PAGE 33
    "When Amamura nodded with his eye closed, Ayako tightly pursed her lips. As Ayako slightly
    casted her eye down, Amamura suddenly opened his eyes wide and declared clearly."
    Amamura "Then, I'll make you the student council president"
    Anya "Eh....?"
    "Ayako looked up in shock. Staring fixedly at those wavering eyes, Amamura held out his
    hand towards Ayako."
    Amamura "If you wish for it, I'll make you the student council president with all my power. I
    won't leave you alone anymore. From now on, I'll be by your side supporting you. That's
    why.... Just take this hand!\" Anya!"
    "At Amamura's words, all kinds of words came and went inside Ayako's mind."
    "\"Why?\" \"Why me?\" \"Not Yuka-san?\", many doubts arose. However, before Amamura 's
    unyielding gaze, it's all dissolved and disappeared"
    Anya "(Aah, I see....)"
    "Suddenly, Ayako realized. Amamura has seen through it. Ayako's.... hopeless, stubborn
    nature."
    "That's why he was telling her. No need for \"Help\" nor \"Let's fight together\".He just said, take
    this hand."
    Anya "Aah...."
    "I have.. always been alone. I thought I would never have anyone to call an ally as I always
    regarded everyone as rivals, and only looked down on others."
    "But.... what if, there's someone who would accept all of this hopelessness of
    mine, and become an ally unconditionally. If such a being exists, then....I wonder what the
    emotion that welled up in my heart really is."
    "Ayako didn't understand didn't understand this feeling Deeply moved? Hope? Joy?
    It seemed to be all of those things and none of those things."
    "That's why, she puffed her chest up in pride and looked forward.
    She wasn't asking for help."
    "No flattery, nor dependence. She just... held this hand as an equal partner."
    Amamura "Yeah, I look forward to working with you from now on. Anya"
    "At his nonchalant kindness, Alisa's mouth naturally broke out into a smile as beautiful as a
    blooming flower."
    "From her slightly opened lips, a voice coming from the bottom of her heart spilled out."
    Anya "Thank you and….."
    Anya "[I LOVE YOU]"
    "There are only sweet and grateful atmosphere in near the park there are only two of them
    under the moon light"
    "Amamura 's heart leapt at the confession which she had not intended to make, and at the
    heartfelt smile he had never seen before until now."
    "Amamura thinking that should he accept that he know russian and accept her or ignore it
    maybe it is her instant feeling"
    menu:
        "-I Love you too Anya":
            jump choices_a
        "- (ignore it and don’t confess)":
            jump choices_b
label choices_a:
    Anya "Wai..Wait you know I said…"
    Amamura "Sorry I didn’t tell you that I know russian"
    Anya "A-You…!!!!"
    jump page_34
label choices_b:
    Anya "ahhh..you….!!"
    Amamura "What the matter?"
    Anya "B-You Idiots!!"
    jump page_34
    # PAGE 34
label page_34:
    "Ayako feel embarrassed and suddenly slap Amamura left cheek with her full power"
    Amamura "HEHE.. Nice slap"
    Anya "Stupid"
    "Amamura gave Anya a thumbs up as he pathetically fell to the ground. She made an
    astonished face at such Amamura while offering her hand, putting her anger to rest as she
    had declared."
    "Amamura accepted her hand, stood up, and slapped his pants to remove the
    dusts."
    Anya "....Time to go home"
    Amamura "I suppose so"
    "They then headed home side by side. Not too close and not too far apart, it’s a distance
    where they could naturally hold hands if they reached out to each other."
    Amamura "Boy, that was my first time getting slapped by a girl. My experience as a
    guy has increased again, huh"
    Anya "Did you hit your head when you fell earlier?"
    Amamura "There’s nothing wrong with my head, okay!?"
    Anya "\"I guess so, you have a disappointing head from the start after all\" They walked a little
    closer than usual, while both of them feeling relieved they’re able to carry on their usual
    interactions with each other. And by the time they reached the front of Ayako’s apartment
    building, Ayako looked a little concerned."
    Anya "....is your cheek, okay? Do you want something to cool it down?"
    Amamura "Yeah, it’s fine. I couldn’t feel my right cheek somewhat, but it’s nothing compared
    to the anesthesia I got from the dentist!"
    Anya "That’s not what you call ‘it’s fine’.... "
    "Having her worry replied with a joke, Alisa shrugged her shoulders with a dumbfounded
    expression. And, with a face having realized something, she raised her head and reached
    out her index finger and gently stroked Amamura’s right cheek."
    Anya "Can you really, not feel anything?"
    Amamura "Ah, well.... I was just joking. The sense a bit numbed is true, though"
    Anya "....I see"
    "Ayakosuddenly smiled at Amamura answering while slightly flustered. In the next moment,
    Ayako placed her hands on Amamura ’s shoulders, and got closer with a soft smile."
    Amamura "Eh?"
    "A soft sensation was pressed against Amamura ’s right cheek as he froze at the sudden
    situation, and a kissing sound sounded in his ear."
    Amamura "Eh?!!"
    "Amamura opened his eyes wide in surprise and Ayako quickly stepped back, giving him a
    ridiculing look."
    Anya "What are you so shocked about. It’s just a kiss cheek"
    Amamura "What do you mean ‘just’.... Isn’t cheek kisses usually just cheek to cheek...."
    # PAGE 35
    Anya "That’s right? Actually it’s not a kiss, but just a sound I made with my mouth"
    Amamura "No, but.... Hmm?"
    Amamura "The sensation just now.... wait, which is it!?"
    Anya "Well then, see you tomorrow"
    "Ayako going to walk inside the apartment but Amamura call her"
    Amamura "Ayako!!"
    Anya "what is it?"
    "she turn to face Amamura again"
    Amamura "I will do my best to make you become a president of Student
    Council for sure"
    Anya "I will do my best too!!"
    "THE END"

    return
