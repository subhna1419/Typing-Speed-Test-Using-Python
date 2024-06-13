from time import *
import random as rnd

def Typing_Errors(paragraphs,usersparagraphs):
    errors = 0
    for i in range(len(paragraphs)):
        try:
            if paragraphs[i]!= usersparagraphs[i]:
                errors += 1
        except:
            errors += 1
    return errors

def Typing_Speed(start_time, end_time,user_input):
    total_time = end_time - start_time
    time_round = round(total_time, 2)
    speed = round(len(user_input) / time_round)
    return speed

test_list = [
            "The sun dipped below the horizon, casting a warm, golden glow across the tranquil landscape. Birds chirped their final melodies of the day, while the gentle rustle of leaves whispered secrets to the evening breeze. As the sky transitioned from vibrant hues of orange and pink to the deep blues of twilight, stars began to twinkle into existence, each one a tiny beacon of light in the vast expanse. The scent of blooming flowers wafted through the air, mingling with the earthy aroma of freshly cut grass. In this serene moment, time seemed to slow, inviting a sense of peace and reflection.",
            
            "In the heart of the bustling city, life moved at a frenetic pace. Skyscrapers towered above, their glass facades reflecting the vibrant energy below. The streets were alive with the sounds of honking horns, chattering pedestrians, and the distant wail of sirens. Sidewalk cafes spilled over with patrons enjoying their lattes, while street vendors hawked their wares to passersby. Amidst the chaos, there was a rhythm, a pulse that drove the city's relentless momentum, as people from all walks of life converged in this urban symphony.",
            
            "Nestled in the valley between two majestic mountains, the village remained untouched by time. Cobblestone streets wound their way through charming cottages with thatched roofs, each one adorned with colorful flower boxes. The scent of freshly baked bread wafted from the local bakery, inviting residents and visitors alike to indulge in its warm, crusty delights. Children played in the village square, their laughter echoing through the air, while elders sat on benches, sharing stories of days gone by. It was a place where community thrived, and traditions were cherished.",
            
            "The library was a sanctuary for those who sought knowledge and solace. Shelves upon shelves of books lined the walls, each one a portal to another world. The air was thick with the scent of aged paper and leather bindings, a comforting aroma for avid readers. Sunlight streamed through the large windows, casting a dappled glow on the wooden floors. In the quiet corners, individuals lost themselves in stories, their imaginations soaring with each turn of the page. It was a haven where time stood still, and the power of words reigned supreme.",
            
            "On the edge of the forest, a cabin stood in quiet solitude. Smoke curled lazily from the chimney, blending with the mist that hung in the air. Inside, a fire crackled warmly in the hearth, casting flickering shadows on the log walls. The cabin's interior was simple yet cozy, with handmade quilts draped over the furniture and a well-worn rug on the floor. Outside, the forest teemed with life, the sounds of birds and insects creating a symphony of nature. It was a retreat from the world, a place where one could find peace and reconnect with the earth.",
            
            "The beach was a stretch of golden sand that met the turquoise waters of the ocean. Waves crashed rhythmically against the shore, their salty spray refreshing to the touch. Seagulls called out as they soared overhead, their cries mingling with the laughter of children building sandcastles. The sun blazed high in the sky, its warmth enveloping everything it touched. Palm trees swayed gently in the breeze, their fronds casting dappled shadows on the sand. It was a place of joy and relaxation, where the worries of the world seemed to melt away with the tides.",
            
            "In the midst of a dense jungle, life thrived in a vibrant tapestry of green. The canopy above was a thick blanket of leaves, allowing only slivers of sunlight to penetrate. The air was humid, filled with the earthy scent of moss and rich soil. Exotic birds and insects created a cacophony of sounds, each one contributing to the jungle's symphony. Vines and creepers wound their way around ancient trees, while the underbrush teemed with hidden creatures. It was a world of mystery and wonder, where nature reigned supreme in all its untamed glory.",
            
            "The farm was a patchwork of fields, each one a testament to the toil and dedication of its workers. Rows of crops stretched out in neat lines, their vibrant greens and golds painting a picturesque scene. The farmhouse, with its whitewashed walls and red roof, stood as a beacon of hard work and perseverance. Animals roamed freely in the pastures, their contented sounds adding to the farm's rustic charm. The scent of fresh hay and tilled earth filled the air, mingling with the aroma of home-cooked meals wafting from the kitchen. It was a place of sustenance and simplicity, where the rhythms of nature dictated the pace of life.",
            
            "In the heart of the desert, the landscape was an expanse of endless dunes, each one a shifting sculpture of sand. The heat was intense, the sun a relentless presence in the cloudless sky. Despite the harsh conditions, life found a way to thrive. Cacti stood tall, their spines a testament to their resilience, while small creatures darted from shadow to shadow in search of sustenance. At night, the desert transformed, the cool air bringing relief and the sky unveiling a blanket of stars. It was a place of extremes, where beauty and danger coexisted in a delicate balance.",
            
            "The mountain trail wound its way through rocky terrain, each twist and turn revealing breathtaking vistas. Snow-capped peaks loomed in the distance, their majestic presence a reminder of nature's grandeur. The air was crisp and clean, filled with the scent of pine and the sound of rustling leaves. Hikers made their way along the path, their footsteps a steady rhythm against the rocky ground. Along the way, wildflowers bloomed in vibrant colors, adding a touch of beauty to the rugged landscape. It was a journey of challenge and reward, where the effort of the climb was matched by the splendor of the views.",
        ]

response = input("Do you want to start the test? (yes/no) ").strip().lower()
if response == "yes":
    while True:
        test1 = rnd.choice(test_list)
        print("***Typing Speed***")
        print(test1)
        print()
        print()
        time_1 = time()
        typing_input = input("Start typing: ")
        time_2 = time()
        print("Speed:  ", Typing_Speed(time_1, time_2, typing_input), "words per second")
        print("Error:  ", Typing_Errors(test1, typing_input))

        retake_response = input("Do you want to retake this test? (yes/no) ").strip().lower()
        if retake_response == "no":
            print("Thank You for using the typing speed test!")
            break
elif response == "no":
    print("Test cancelled")
else:
    print("Invalid input")








