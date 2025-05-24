from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Pineapple Express",
        "year": 2008,
        "director": "David Gordon Green",
        "length": 111,
        "image": "/static/images/pineapple_express.jpg",
        "short_description": "A stoner duo is forced to flee after witnessing a murder.",
        "description": "Pineapple Express follows process server Dale Denton and his laid-back marijuana dealer, Saul Silver, after they witness a brutal murder. Their accidental involvement drags them into a wild chase as hitmen and corrupt cops close in. The duo embarks on a dangerous road trip filled with absurd situations and unexpected alliances. Blending action and comedy, the film explores themes of friendship and survival in the unlikeliest of circumstances.",
        "stars": ["Seth Rogen", "James Franco", "Danny McBride"],
        "reviews": []
    },
    {
        "id": 2,
        "title": "The Interview",
        "year": 2014,
        "director": "Seth Rogen, Evan Goldberg",
        "length": 112,
        "image": "/static/images/the_interview.jpg",
        "short_description": "A journalist and his producer are recruited for a covert assassination mission.",
        "description": "The Interview follows talk show host Dave Skylark and his producer Aaron Rapoport when they are unexpectedly recruited by the CIA. Tasked with assassinating North Korea’s leader, the pair embarks on a perilous and politically charged mission. Their journey turns chaotic as they confront bureaucratic hurdles and unforeseen dangers. Blending satire, action, and absurd humor, the film delivers a bold commentary on international politics.",
        "stars": ["Seth Rogen", "James Franco", "Lizzy Caplan"],
        "reviews": []
    },
    {
        "id": 3,
        "title": "The Hangover",
        "year": 2009,
        "director": "Todd Phillips",
        "length": 100,
        "image": "/static/images/the_hangover.jpg",
        "short_description": "Three friends try to piece together a wild night in Las Vegas after losing the groom.",
        "description": "The Hangover follows a group of friends who travel to Las Vegas for a bachelor party and wake up with no memory of the previous night. They soon realize that the groom is missing and that they must retrace their steps to piece together the chaos. Along the way, they encounter bizarre characters and outlandish situations that defy logic. The film masterfully combines mystery and humor, leading to one unforgettable and unpredictable adventure.",
        "stars": ["Bradley Cooper", "Zach Galifianakis", "Ed Helms"],
        "reviews": []
    },
    {
        "id": 4,
        "title": "Moana",
        "year": 2016,
        "director": "Ron Clements, John Musker",
        "length": 107,
        "image": "/static/images/moana.jpg",
        "short_description": "A spirited teenager embarks on a daring journey to save her island.",
        "description": "Moana tells the story of a courageous Polynesian teenager chosen by the ocean to save her people. Determined to find her true destiny, she sets sail on a perilous voyage beyond the reef. Along the way, Moana confronts dangerous seas, discovers ancient legends, and gains the unlikely companionship of the demigod Maui. With breathtaking animation and memorable songs, the film celebrates self-discovery, tradition, and the power of nature.",
        "stars": ["Auli'i Cravalho", "Dwayne Johnson", "Rachel House"],
        "reviews": []
    },
    {
        "id": 5,
        "title": "The Batman",
        "year": 2022,
        "director": "Matt Reeves",
        "length": 176,
        "image": "/static/images/the_batman.jpg",
        "short_description": "Batman investigates a series of cryptic crimes in Gotham.",
        "description": "The Batman follows a young Bruce Wayne in his early days of fighting crime as he uncovers a deep-rooted conspiracy in Gotham City. As a serial killer known as The Riddler begins leaving cryptic clues, Batman is forced to confront the dark underbelly of his city. His investigation reveals corruption that ties back to his own family and the legacy of Gotham’s past. With a brooding atmosphere and intense action sequences, the film redefines the iconic superhero’s origins with a gritty, noir-inspired narrative.",
        "stars": ["Robert Pattinson", "Zoë Kravitz", "Paul Dano"],
        "reviews": []
    },
    {
        "id": 6,
        "title": "Spider-Man: Into the Spider-Verse",
        "year": 2018,
        "director": "Bob Persichetti, Peter Ramsey, Rodney Rothman",
        "length": 117,
        "image": "/static/images/spiderman_itsv.jpg",
        "short_description": "Teenager Miles Morales becomes Spider-Man and meets other Spider-People from alternate dimensions.",
        "description": "Spider-Man: Into the Spider-Verse introduces Miles Morales, a teenager who gains extraordinary powers and is thrust into the role of Spider-Man. His journey unveils a multiverse populated by different versions of Spider-People, each with their own story. Together, they unite to face a dangerous threat that endangers all realities. Celebrated for its groundbreaking animation and inventive storytelling, the film reinvents the superhero genre with fresh energy and heart.",
        "stars": ["Shameik Moore", "Jake Johnson", "Hailee Steinfeld"],
        "reviews": []
    },
    {
        "id": 7,
        "title": "Mr. Bean's Holiday",
        "year": 2007,
        "director": "Steve Bendelack",
        "length": 90,
        "image": "/static/images/mrbean_holiday.jpg",
        "short_description": "Mr. Bean’s vacation turns into a hilarious adventure in France.",
        "description": "Mr. Bean's Holiday follows the beloved, bumbling Mr. Bean as he wins a vacation to the south of France. His journey quickly derails into a series of unintended misadventures and comedic mishaps. Along the way, he unintentionally disrupts the lives of those around him while creating chaos at every turn. The film captures the timeless charm and visual humor of Mr. Bean in a lighthearted and entertaining escapade.",
        "stars": ["Rowan Atkinson", "Willem Dafoe", "Emma de Caunes"],
        "reviews": []
    },
    {
        "id": 8,
        "title": "Surf's Up",
        "year": 2007,
        "director": "Ash Brannon, Chris Buck",
        "length": 85,
        "image": "/static/images/surfs_up.jpg",
        "short_description": "A penguin dreams of becoming a surfing champion.",
        "description": "Surf's Up is a unique animated mockumentary that follows Cody Maverick, a young penguin with an unstoppable passion for surfing. Determined to prove his talent, Cody leaves his familiar Antarctic home to enter a prestigious surfing competition. Along his journey, he overcomes natural challenges and learns valuable lessons about perseverance and self-confidence. Blending humor with stunning visuals, the film celebrates the underdog spirit in a refreshing and entertaining way.",
        "stars": ["Shia LaBeouf", "Jon Heder", "Jeff Bridges"],
        "reviews": []
    },
    {
        "id": 9,
        "title": "Shrek",
        "year": 2001,
        "director": "Andrew Adamson, Vicky Jenson",
        "length": 90,
        "image": "/static/images/shrek.jpg",
        "short_description": "A grumpy ogre embarks on a quest to reclaim his swamp.",
        "description": "Shrek tells the story of a reclusive ogre whose quiet life in a swamp is shattered when an array of fairy tale creatures invade his home. Reluctantly, he embarks on a quest to confront the source of the invasion and reclaim his peace. Along the way, Shrek forms an unlikely bond with a talkative donkey, which adds humor and heart to his journey. With its clever twist on traditional fairy tales, the film has become a beloved classic that champions the importance of inner beauty and acceptance.",
        "stars": ["Mike Myers", "Eddie Murphy", "Cameron Diaz"],
        "reviews": []
    },
    {
        "id": 10,
        "title": "Ready Player One",
        "year": 2018,
        "director": "Steven Spielberg",
        "length": 140,
        "image": "/static/images/ready_player_one.jpg",
        "short_description": "A young gamer embarks on a quest in a virtual reality universe.",
        "description": "Ready Player One is set in a dystopian future where people escape their bleak reality by entering the vast virtual world known as the OASIS. When the eccentric creator of the OASIS dies, a contest is announced to find his hidden fortune, launching a high-stakes race through a digital universe. A young gamer rises to the challenge, forming alliances and facing fierce competitors along the way. The film combines thrilling action, pop culture nostalgia, and visionary storytelling to explore themes of identity, freedom, and the power of imagination.",
        "stars": ["Tye Sheridan", "Olivia Cooke", "Ben Mendelsohn"],
        "reviews": []
    },
    {
        "id": 11,
        "title": "The Adventures of Tintin",
        "year": 2011,
        "director": "Steven Spielberg",
        "length": 107,
        "image": "/static/images/tintin.jpg",
        "short_description": "Young reporter Tintin embarks on a thrilling treasure hunt.",
        "description": "The Adventures of Tintin follows the intrepid young reporter Tintin and his loyal friend Captain Haddock as they embark on a daring treasure hunt. Their journey takes them through mysterious, exotic locales filled with danger and intrigue. Clues and puzzles guide them as they confront adversaries determined to keep the treasure hidden. Combining dynamic animation with classic adventure, the film brings a beloved comic series to life with energy and heart.",
        "stars": ["Jamie Bell", "Andy Serkis", "Daniel Craig"],
        "reviews": []
    },
    {
        "id": 12,
        "title": "Wreck-It Ralph",
        "year": 2012,
        "director": "Rich Moore",
        "length": 101,
        "image": "/static/images/wreck_it_ralph.jpg",
        "short_description": "A video game villain dreams of becoming a hero.",
        "description": "Wreck-It Ralph follows the story of a misunderstood video game villain who is tired of being cast as the bad guy. Longing for respect and recognition, Ralph embarks on a quest to prove that he can be a hero. Along the way, he forges unlikely friendships with characters from other games and discovers his own potential. The film is a colorful, heartfelt celebration of self-acceptance and the power of change, all wrapped in a nostalgic arcade adventure.",
        "stars": ["John C. Reilly", "Sarah Silverman", "Jack McBrayer"],
        "reviews": []
    },
    {
        "id": 13,
        "title": "Teenage Mutant Ninja Turtles: Mutant Mayhem",
        "year": 2023,
        "director": "Jeff Rowe",
        "length": 99,
        "image": "/static/images/tmnt.jpg",
        "short_description": "The Ninja Turtles strive for acceptance while battling an army of mutants.",
        "description": "Teenage Mutant Ninja Turtles: Mutant Mayhem follows the iconic Turtle brothers as they struggle to fit into a world that misunderstands them. When a horde of mutants threatens their city, they must band together to defend their home and prove their worth. Their journey is filled with high-energy action, humorous banter, and heartfelt moments of brotherhood. This animated adventure reinvents the classic franchise with fresh visuals, dynamic storytelling, and a focus on identity and teamwork.",
        "stars": ["Micah Abbey", "Shamon Brown Jr.", "Nicholas Cantu"],
        "reviews": []
    },
    {
        "id": 14,
        "title": "Zoolander",
        "year": 2001,
        "director": "Ben Stiller",
        "length": 89,
        "image": "/static/images/zoolander.jpg",
        "short_description": "A clueless fashion model is unwittingly involved in an assassination plot.",
        "description": "Zoolander centers on Derek Zoolander, a dim-witted yet endearing fashion model whose life takes an unexpected turn. When he is manipulated into an assassination plot, his journey through the absurd world of high fashion becomes both hilarious and surreal. Along the way, he encounters a host of eccentric characters and bizarre scenarios that satirize the fashion industry. With its sharp wit and memorable one-liners, the film has become a cult classic that continues to entertain audiences.",
        "stars": ["Ben Stiller", "Owen Wilson", "Will Ferrell"],
        "reviews": []
    },
    {
        "id": 15,
        "title": "Tropic Thunder",
        "year": 2008,
        "director": "Ben Stiller",
        "length": 107,
        "image": "/static/images/tropic_thunder.jpg",
        "short_description": "Actors filming a war movie find themselves in real combat.",
        "description": "Tropic Thunder is a biting satire that follows a group of self-absorbed actors filming a war movie in a remote location. When their scripted environment turns into a genuine combat zone, reality and fiction become dangerously blurred. The actors must navigate real-life conflict while contending with their own egos and miscommunications. With over-the-top humor and sharp industry commentary, the film delivers a wild, unpredictable ride that lampoons Hollywood excess.",
        "stars": ["Ben Stiller", "Robert Downey Jr.", "Jack Black"],
        "reviews": []
    },
    {
        "id": 16,
        "title": "Rush Hour",
        "year": 1998,
        "director": "Brett Ratner",
        "length": 98,
        "image": "/static/images/rush_hour.jpg",
        "short_description": "A Hong Kong detective and an LAPD cop team up for a high-stakes rescue.",
        "description": "Rush Hour pairs Hong Kong detective Lee with fast-talking LAPD officer Carter as they join forces to rescue a kidnapped diplomat’s daughter. Their investigation leads them into a maze of cultural clashes, witty banter, and explosive action. As the duo tackles corrupt officials and dangerous criminals, a genuine bond forms amid the chaos. The film masterfully blends humor, suspense, and dynamic fight scenes to create a memorable buddy-cop adventure.",
        "stars": ["Jackie Chan", "Chris Tucker", "Tom Wilkinson"],
        "reviews": []
    },
    {
        "id": 17,
        "title": "The Lego Movie",
        "year": 2014,
        "director": "Phil Lord, Christopher Miller",
        "length": 100,
        "image": "/static/images/the_lego_movie.jpg",
        "short_description": "An ordinary Lego figure discovers he holds the key to saving his world.",
        "description": "The Lego Movie follows Emmet, an ordinary construction worker in a vast Lego universe who is mistaken for a prophesied hero. Thrust into an epic adventure, he must thwart the evil plans of a tyrant bent on destroying creativity. Along his journey, Emmet teams up with an eclectic group of heroes, each contributing to the quest in their unique way. Bursting with humor, inventive visuals, and a heartfelt message about creativity, the film redefines what it means to be extraordinary.",
        "stars": ["Chris Pratt", "Will Ferrell", "Elizabeth Banks"],
        "reviews": []
    },
    {
        "id": 18,
        "title": "The Unbearable Weight of Massive Talent",
        "year": 2022,
        "director": "Tom Gormican",
        "length": 107,
        "image": "static/images/the_unbearable_weight_of_a_massive_talent.jpg",
        "short_description": "Nicolas Cage plays a fictionalized version of himself in a high-stakes action comedy.",
        "description": "The Unbearable Weight of Massive Talent stars Nicolas Cage as a heightened version of himself, thrust into a bizarre and dangerous scenario. Invited by an overzealous fan, he finds himself embroiled in a wild scheme that blurs the lines between reality and performance. As he navigates a maze of action-packed encounters and self-referential humor, Cage is forced to confront his own celebrity persona. The film offers a clever, meta-commentary on fame while delivering thrilling sequences and unexpected laughs.",
        "stars": ["Nicolas Cage", "Pedro Pascal", "Tiffany Haddish"],
        "reviews": []
    },
    {
        "id": 19,
        "title": "This Is the End",
        "year": 2013,
        "director": "Seth Rogen, Evan Goldberg",
        "length": 107,
        "image": "/static/images/this_is_the_end.jpg",
        "short_description": "A group of celebrities must survive a catastrophic apocalypse.",
        "description": "This Is the End assembles a star-studded cast who find themselves trapped together as the world descends into chaos. While grappling with a series of bizarre and catastrophic events, the celebrities confront both physical dangers and personal vulnerabilities. The film uses over-the-top humor and self-aware satire to lampoon the nature of celebrity and the absurdity of the apocalypse. With its irreverent tone and unpredictable plot twists, it offers a wild, comedic exploration of survival at the end of the world.",
        "stars": ["Seth Rogen", "James Franco", "Jay Baruchel"],
        "reviews": []
    },
    {
        "id": 20,
        "title": "The Matrix",
        "year": 1999,
        "director": "The Wachowskis",
        "length": 136,
        "image": "/static/images/the_matrix.jpg",
        "short_description": "A hacker discovers that reality is a simulated illusion.",
        "description": "The Matrix follows computer hacker Neo as he discovers that the world he knows is a sophisticated simulation controlled by sentient machines. Drawn into a rebellion against these oppressors, he learns to harness extraordinary abilities that defy the limits of reality. As Neo embraces his destiny, the film explores deep philosophical questions about freedom, identity, and the nature of existence. With its groundbreaking visual effects and intense action sequences, The Matrix revolutionized the science fiction genre and left an indelible mark on popular culture.",
        "stars": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "reviews": []
    }
]

# Global variable to store reviews in memory (keyed by movie id)
movie_reviews = {}

@app.route('/')
def homepage():
   return render_template('index.html')   

@app.route('/search', methods=['GET'])
def search_results():
    query = request.args.get('query', '').strip()  # Trim whitespace from the query
    
    # Filter the movies based on the query (case insensitive search)
    results = [
        movie for movie in movies 
        if query.lower() in movie["title"].lower() or
           query.lower() in movie["director"].lower() or
           any(query.lower() in star.lower() for star in movie["stars"])
    ]
    
    return render_template('search_page.html', query=query, results=results)


@app.route('/view/<id>')
def movie_page(id):

    try:
        id = int(id)  # convert id to integer
    except ValueError:
        return "Invalid ID format", 400
    
    movie = next((m for m in movies if m["id"] == id), None)
    if not movie:
        return "Movie not found", 404
    
    reviews = movie.get("reviews", [])
    return render_template('movie_page.html', movie=movie, reviews=reviews)

@app.route('/api/movies')
def api_movies():
    return jsonify(movies)  # Assuming `movies` is a list of movie dictionaries

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('add_movie.html')
    elif request.method == 'POST':
        data = request.get_json()
        required_fields = ['title', 'year', 'director', 'length', 'image', 'short_description', 'description', 'stars']
        errors = {}
        # Validate required fields
        for field in required_fields:
            if field not in data or not str(data[field]).strip():
                errors[field] = f"{field.capitalize()} is required."
        if errors:
            return jsonify({'error': errors}), 400

        # Validate that 'year' and 'length' are integers
        try:
            year = int(data['year'])
        except ValueError:
            errors['year'] = "Year must be an integer."
        try:
            length = int(data['length'])
        except ValueError:
            errors['length'] = "Length must be an integer."
        if errors:
            return jsonify({'error': errors}), 400

        # Process stars (assume comma separated input)
        stars = [star.strip() for star in data['stars'].split(',') if star.strip()]

        # Generate new unique ID (assuming movies is non-empty)
        new_id = max(movie['id'] for movie in movies) + 1 if movies else 1

        new_movie = {
            "id": new_id,
            "title": data['title'].strip(),
            "year": year,
            "director": data['director'].strip(),
            "length": length,
            "image": data['image'].strip(),
            "short_description": data['short_description'].strip(),
            "description": data['description'].strip(),
            "stars": stars,
            "reviews": []
        }

        movies.append(new_movie)

        return jsonify({
            'message': 'New item successfully created.',
            'movie_url': f'/view/{new_id}'
        }), 200

@app.route('/edit_movie/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = next((m for m in movies if m["id"] == id), None)
    if not movie:
        return "Movie not found", 404

    if request.method == 'GET':
        # Render the edit page with the current movie data
        return render_template("edit_movie.html", movie=movie)
    else:
        # Process POST submission from the edit form
        title = request.form.get("title", "").strip()
        year = request.form.get("year", "").strip()
        director = request.form.get("director", "").strip()
        length = request.form.get("length", "").strip()
        image = request.form.get("image", "").strip()
        short_description = request.form.get("short_description", "").strip()
        description = request.form.get("description", "").strip()
        stars = request.form.get("stars", "").strip()

        # Basic validation: ensure no field is blank
        if not (title and year and director and length and image and short_description and description and stars):
            error = "All fields are required."
            return render_template("edit_movie.html", movie=movie, error=error)
        
        try:
            year = int(year)
            length = int(length)
        except ValueError:
            error = "Year and Length must be valid numbers."
            return render_template("edit_movie.html", movie=movie, error=error)
        
        # Update the movie with new data
        movie["title"] = title
        movie["year"] = year
        movie["director"] = director
        movie["length"] = length
        movie["image"] = image
        movie["short_description"] = short_description
        movie["description"] = description
        movie["stars"] = [s.strip() for s in stars.split(",") if s.strip()]

        return render_template('movie_page.html', movie=movie)

@app.route('/add_review/<int:movie_id>', methods=['POST'])
def add_review(movie_id):
    data = request.get_json()
    reviewer = data.get('reviewer', '').strip()
    rating = data.get('rating')
    
    if not reviewer or not rating:
        return jsonify({'error': 'Missing reviewer name or rating'}), 400
    
    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
    except ValueError:
        return jsonify({'error': 'Invalid rating value'}), 400

    review = {'reviewer': reviewer, 'rating': rating}
    
    # Find the movie and append the review
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    movie.setdefault("reviews", [])
    movie["reviews"].append(review)
    
    return jsonify({
        'message': 'New item successfully created.',
        'movie_url': f'/view/{movie_id}'
    }), 200



if __name__ == '__main__':
   app.run(debug = True, port=5001)




