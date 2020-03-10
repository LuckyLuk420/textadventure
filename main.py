rooms_dict = {
    "bedroom": {
        "flavor": "You wake up in your apartment. You feel hung over and hungry.\n"
                  "Let's get ready and grab some food at the store.\n"
                  "Your phone lies on your desk next to  you're laptop. You left it there to charge over night.\n"
                  "You gaze over your small bedroom. There's not much in it.\n"
                  "Your most priced possession: A closet filled with comics.\n"
                  "Next to it is your desk, between them the door.\n"
                  "On the floor are your skateboard, some clothing and of course there is the bed your'e sitting on.",
        "items": {
            "bed": {
                "inspect": "It's untidy. You just slept in it",
                "interact": "You just woke up, of course you're tired. "
                            "But that wouldn't take the story forward, lazy-ass."
            },
            "skateboard": {
                "inspect": "I could take the skateboard to go to the city.",
                "interact": "You take the Skateboard and make your way to the city."
            },
            "comic collection": {
                "inspect": "It's filled to the brim with comics.",
                "interact": "I don't have the time."
            },
            "door": {
                "inspect": "A plain wooden door. It's like a Portal.",
                "interact": "You open the Portal and warp to the bus station."
            },
            "desk": {
                "inspect": "It's just an ordinary desk. What did you expect?",
                "interact": "You go to your desk.\n"
                            "On top of it are some office supplies, your laptop and your phone and a comic book",
                "items": {
                    "laptop": {
                        "inspect": "I don't need it right now.",
                        "interact": "You're right, it's very tempting to watch some porn!"
                    },
                    "phone": {
                        "inspect": "A few new messages, but nothing of interest. Should i call a cab?",
                        "interact": "You call a cab that arrives shortly after at your door."
                    },
                    "comic": {
                        "inspect": "'Captain Lorem Ipsum'",
                        "interact": "Not right now. I'm hungry"
                    }
                }
            }
        }
    },
    "bus stop": {
        "flavor": "There's a lady with her dog, also waiting.\n"
                  "The dog smiles at you and slightly waves it's tail\n"
                  "as you approach the bus station.",
        "items": {
            "lady": {
                "inspect": "",
                "interact": ""
            },
            "dog": {
                "inspect": "",
                "interact": "",
            },
            "ticket machine": {
                "inspect": "I have to buy a ticket for the bus. It will stop her in a few minutes",
                "interact": "You go ahead and buy a ticket.\n"
                            "Just in the moment the machine spits out your ticket,\n"
                            "you here a load roar as the bus stops at the station.\n"
                            "The Lady with her dog, followed by you step inside the bus.\n"
                            "The doors close behind you and the bus starts moving."
            }
        }
    },
    "city": {
        "flavor": "The city is filled with people. There are almost just as many stores.\n"
                  "On your way to the supermarket you come by a coffee truck and a food truck with fries and burgers.\n"
                  "Hungry as you are the fumes of the freshly brewed coffee and the food tempt you to stop\n"
                  "and eat a snack.",
        "items": {
            "coffee truck": {
                "inspect": "",
                "interact": "",
                "items": {
                    "coffee": {
                        "inspect": "",
                        "interact": ""
                    },
                    "espresso": {
                        "inspect": "",
                        "interact": ""
                    },
                    "cake": {
                        "inspect": "",
                        "interact": ""
                    }
                }
            },
            "burger truck": {
                "inspect": "",
                "interact": "",
                "items": {
                    "burger": {
                        "inspect": "",
                        "interact": ""
                    },
                    "fries": {
                        "inspect": "",
                        "interact": ""
                    },
                    "soda": {
                        "inspect": "",
                        "interact": ""
                    }
                }
            },
            "supermarket": {
                "inspect": "",
                "interact": "Finally in the supermarket you grab your favorite lasagna ingredients.\n"
                            "The line at the register is long. You patiently wait. After paying you call a cab.\n"
                            "It arrives a few minutes later."
            }
        }
    }
}


class Room:
    def __init__(self, name, flavor, items):
        self.commands = ["inspect", "interact", "quit"]
        self.name = name
        self.flavor = flavor
        self.items = items
        self.first = True

    def flavortext(self):
        if self.first:
            print(self.flavor)
            self.first = False
        self.event_handler()

    # ___Handle Input____
    # Extract the command and item from input
    def check_input(self, user_input):
        for command in self.commands:
            if user_input.startswith(command):
                for item in self.items:
                    if user_input.endswith(item):
                        return command, item
                print("Item not found")
                return None
        print("Command not found")
        return None

    def event_handler(self):
        global running
        while True:
            user_input = input("{0}\n{1}\n> ".format(self.items, self.commands)).lower()
            if user_input == self.commands[-1]:
                running = False
                break
            elif self.check_input(user_input) is not None:
                command, item = self.check_input(user_input)
                break
            else:
                continue
        try:
            if command == self.commands[0]:
                items_list[room[-1]][item].inspect()
            elif command == self.commands[1]:
                items_list[room[-1]][item].interact()
        except UnboundLocalError:
            pass

    def move(self):
        room.append(self.name)


class Item:
    def __init__(self, inspect, interact):
        self.flavor = inspect
        self.response = interact

    def inspect(self):
        print(self.flavor)

    def interact(self):
        print(self.response)


class Container(Item):
    def __init__(self, inspect, interact, name, items):
        super().__init__(inspect, interact)
        self.name = name
        self.items = items
        self.commands = ["inspect", "interact", "back", "quit"]

    def interact(self):
        print(self.response)
        room.append(self.name)
        self.event_handler()

    # ___Handle Input____
    # Extract the command and item from input
    def check_input(self, user_input):
        for command in self.commands:
            if user_input.startswith(command):
                for obj in self.items:
                    if user_input.endswith(obj):
                        return command, obj
                print("Item not found!")
                return None
        print("Command not found!")
        return None

    def event_handler(self):
        if self.items is not None:
            global running
            while True:
                user_input = input("{0}\n{1}\n> ".format(self.items, self.commands)).lower()
                if user_input == self.commands[-1]:
                    running = False
                    break
                elif user_input == self.commands[-2]:
                    rooms_list[room[-2]].move()
                if self.check_input(user_input) is not None:
                    command, item = self.check_input(user_input)
                    break
            if command == self.commands[0]:
                items_list[room[-1]][item].inspect()
            elif command == self.commands[1]:
                items_list[room[-1]][item].interact()
        else:
            pass


class Portal(Item):
    def __init__(self, inspect, interact, destination):
        super().__init__(inspect, interact)
        self.destination = destination

    def interact(self):
        print(self.response)
        rooms_list[self.destination].move()


class Goal(Item):
    def __init__(self, inspect, interact):
        super().__init__(inspect, interact)

    def interact(self):
        global running
        print(self.response)
        running = False


# Initiating Items
# ___Bedroom___
path = rooms_dict["bedroom"]["items"]
# Desk
desk = path["desk"]
desk = Container(desk["inspect"], desk["interact"], "desk", list(desk["items"].keys()))
# Bed
bed = path["bed"]
bed = Item(bed["inspect"], bed["interact"])
# Skateboard
skateboard = path["skateboard"]
skateboard = Portal(skateboard["inspect"], skateboard["interact"], "city")
# Comic Collection
comic_collection = path["comic collection"]
comic_collection = Item(comic_collection["inspect"], comic_collection["interact"])
# Door
door = path["door"]
door = Portal(door["inspect"], door["interact"], "bus stop")

# ___Desk___
path = rooms_dict["bedroom"]["items"]["desk"]["items"]
# Laptop
laptop = path["laptop"]
laptop = Item(laptop["inspect"], laptop["interact"])
# Phone
phone = path["phone"]
phone = Portal(phone["inspect"], phone["interact"], "city")
# Comic
comic = path["comic"]
comic = Item(comic["inspect"], comic["interact"])

# ___Bus stop___
path = rooms_dict["bus stop"]["items"]
# Lady
lady = Item(path["lady"]["inspect"], path["lady"]["interact"])
# Dog
dog = Item(path["dog"]["inspect"], path["dog"]["interact"])
# Ticket Machine
ticket_machine = Portal(path["ticket machine"]["inspect"], path["ticket machine"]["interact"], "city")

# ___City___
path = rooms_dict["city"]["items"]
# Coffee Truck
c_truck = path["coffee truck"]
c_truck = Container(c_truck["inspect"], c_truck["interact"], "coffee truck", list(c_truck["items"].keys()))
# Burger Truck
b_truck = path["burger truck"]
b_truck = Container(b_truck["inspect"], b_truck["interact"], "burger truck", list(b_truck["items"].keys()))
# Supermarket
supermarket = Goal(path["supermarket"]["inspect"], path["supermarket"]["interact"])

# ___Coffee Truck___
path = rooms_dict["city"]["items"]["coffee truck"]["items"]
# Coffee
coffee = Item(path["coffee"]["inspect"], path["coffee"]["interact"])
# Espresso
espresso = Item(path["espresso"]["inspect"], path["espresso"]["interact"])
# Cake
cake = Item(path["cake"]["inspect"], path["cake"]["inspect"])

# ___Burger Truck___
path = rooms_dict["city"]["items"]["burger truck"]["items"]
# Burger
burger = Item(path["burger"]["inspect"], path["burger"]["interact"])
# Fries
fries = Item(path["fries"]["inspect"], path["fries"]["interact"])
# Soda
soda = Item(path["soda"]["inspect"], path["soda"]["interact"])

items_list = {
    "bedroom": {
        "desk": desk,
        "bed": bed,
        "skateboard": skateboard,
        "comic collection": comic_collection,
        "door": door
    },
    "desk": {
        "laptop": laptop,
        "phone": phone,
        "comic": comic
    },
    "bus stop": {
        "lady": lady,
        "dog": dog,
        "ticket machine": ticket_machine
    },
    "city": {
        "coffee truck": c_truck,
        "burger truck": b_truck,
        "supermarket": supermarket
    },
    "coffee truck": {
        "coffee": coffee,
        "espresso": espresso,
        "cake": cake
    },
    "burger truck": {
        "burger": burger,
        "fries": fries,
        "soda": soda
    }
}

# Initiating Rooms
# Bedroom
bedroom = Room("bedroom", rooms_dict["bedroom"]["flavor"], list(rooms_dict["bedroom"]["items"].keys()))
# Bus Stop
bus_stop = Room("bus stop", rooms_dict["bus stop"]["flavor"], list(rooms_dict["bus stop"]["items"].keys()))
# City
city = Room("city", rooms_dict["city"]["flavor"], list(rooms_dict["city"]["items"].keys()))

rooms_list = {
    "bedroom": bedroom,
    "desk": desk,
    "bus stop": bus_stop,
    "city": city,
    "coffee truck": c_truck,
    "burger truck": b_truck
}

cur_item = []
room = ["bedroom"]
running = True

while running:
    if type(rooms_list[room[-1]]) is Room:
        rooms_list[room[-1]].flavortext()
    else:
        rooms_list[room[-1]].interact()
