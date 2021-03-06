from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="abc", email="abc@qq.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/' +
             '18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# first category
category1 = Category(name="Comedy")

session.add(category1)
session.commit()

item1 = Item(title="The Hangover", description="Three buddies wake up \
        from a bachelor party in Las Vegas, with no memory of the previous \
        night and the bachelor missing. They make their way around the city \
        in order to find their friend before wedding.", category=category1,
             user=User1)

session.add(item1)
session.commit()

item2 = Item(title="Zootopia", description="The modern mammal metropolis of\
        Zootopia is a city like no other. Comprised of habitat neighborhoods \
        like ritzy Sahara Square and frigid Tundratown, it's a melting pot \
        where animals from every environment live together-a place where no \
        matter what you are, from the biggest elephant to the smallest shrew, \
        you can be anything.", category=category1, user=User1)

session.add(item2)
session.commit()

# second category
category2 = Category(name="Romance")

session.add(category2)
session.commit()

item1 = Item(title="Casablanca", description="One of the most beloved \
        American films, this captivating wartime adventure of romance and \
        intrigue from director Michael Curtiz defies standard categorization. \
        Simply put, it is the story of Rick Blaine (Humphrey Bogart), a \
        world-weary ex-freedom fighter who runs a nightclub in Casablanca \
        during the early part of WWII. ", category=category2, user=User1)

session.add(item1)
session.commit()

item2 = Item(title="The Philadelphia Story", description="Set among the \
        upper class in 1930s Philadelphia, this irreverent classic romantic \
        comedy features radiant performances by three legendary stars. On \
        the eve of her marriage to an uninteresting man, a headstrong \
        socialite jousts verbally with her charming ex-husband, drinks too \
        much champagne, and flirts outrageously with a handsome \
        reporter.", category=category2, user=User1)

session.add(item2)
session.commit()

# third category
category3 = Category(name="Action & Adventure")

session.add(category3)
session.commit()

item1 = Item(title="Mad Max: Fury Road", description="Filmmaker George \
        Miller gears up for another post-apocalyptic action adventure with \
        Fury Road, the fourth outing in the Mad Max film series. Charlize \
        Theron stars alongside Tom Hardy (Bronson), with Zoe Kravitz, \
        Adelaide Clemens, and Rosie Huntington Whiteley heading up the \
        supporting cast. ~ Jeremy Wheeler, Rovi", category=category3,
             user=User1)

session.add(item1)
session.commit()

item2 = Item(title="Wonder Woman", description="An Amazon princess \
        (Gal Gadot) finds her idyllic life on an island occupied only by \
        female warriors interrupted when a pilot (Chris Pine) crash-lands \
        nearby. After rescuing him, she learns that World War I is \
        engulfing the planet, and vows to use her superpowers to restore \
        peace. Directed by Patty Jenkins (Monster).", category=category3,
             user=User1)

session.add(item2)
session.commit()

# fourth category
category4 = Category(name="Horror")

session.add(category4)
session.commit()

item1 = Item(title="The Dark Tower", description="The Gunslinger, Roland \
        Deschain, roams an Old West-like landscape where \"the world has \
        moved on\" in pursuit of the man in black. Also searching for the \
        fabled Dark Tower, in the hopes that reaching it will preserve his \
        dying world.", category=category4, user=User1)

session.add(item1)
session.commit()

item2 = Item(title="Get Out", description="It's time for a young African \
        American to meet with his white girlfriend's parents for a weekend \
        in their secluded estate in the woods, but before long, the friendly \
        and polite ambience will give way to a nightmare.", category=category4,
             user=User1)

session.add(item2)
session.commit()

# fifth category
category5 = Category(name="Drama")

session.add(category5)
session.commit()

item1 = Item(title="War for the Planet of the Apes", description="After the \
        apes suffer unimaginable losses, Caesar wrestles with his darker \
        instincts and begins his own mythic quest to avenge his \
        kind.", category=category5, user=User1)

session.add(item1)
session.commit()

item2 = Item(title="Dunkirk", description="Allied soldiers from Belgium, \
        the British Empire and France are surrounded by the German army and \
        evacuated during a fierce battle in World War II.", category=category5,
             user=User1)

session.add(item2)
session.commit()

print "added category items!"
