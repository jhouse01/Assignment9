class Person:
    '''
    A class representing a person in a social network.
    '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """Adds a Person object to the friends list."""
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network using an adjacency list.
    '''
    def __init__(self):
        # Key: name (str), Value: Person instance
        self.people = {}

    def add_person(self, name):
        """Creates a new Person and adds them to the network."""
        if name in self.people:
            print(f"User '{name}' already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        """Establishes a bidirectional friendship between two people."""
        p1 = self.people.get(person1_name)
        p2 = self.people.get(person2_name)

        if not p1 or not p2:
            missing = person1_name if not p1 else person2_name
            print(f"Friendship not created. {missing} doesn't exist!")
            return

        # Add each other to their respective friends lists
        p1.add_friend(p2)
        p2.add_friend(p1)

    def print_network(self):
        """Prints all users and their list of friends."""
        for name, person_obj in self.people.items():
            friend_names = [friend.name for friend in person_obj.friends]
            friends_str = ", ".join(friend_names)
            print(f"{name} is friends with: {friends_str}")

network = SocialNetwork()

users = ["Madison", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]
for user in users:
    network.add_person(user)

network.add_person("Jordan") 

network.add_friendship("Madison", "Jordan")
network.add_friendship("Madison", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Madison", "Taylor")
network.add_friendship("Casey", "Madison")

network.add_friendship("Alex", "Taylor")

print("\n--- Current Social Network ---")
network.print_network()

''' 
A graph is the best way to represent a social network because it closely represents how humans interact with each other in a non-linear fashion. In a graph, "nodes" (the people) are connected through "edges" (the friendships). Graphs are unique in that they allow complex relationships, where a person could have one friend, fifty friends, or no friends at all, and they could be friends with anyone else in the social network, regardless of when they were initially connected. In comparison, a list is slow and would require searching every friendship ever established, which quickly expands the computational time.

A tree data structure is also not suitable because trees are naturally hierarchical and restrictive in nature. For example, in a tree data structure, there exists a "parent" and "child" relationship with a single root node at the highest level of the tree. It also does not allow "cycles," meaning it is not possible to have a group of friends where a friend of a friend is also a friend (for example, Alex is friends with Jordan, Jordan is friends with Taylor, and Taylor is friends with Alex). As a social network is a collection of these "cycles" and doesn't have a "boss" or a starting point, a tree data structure would immediately break if two people in different "trees" tried to become friends. Using an adjacency list is a good trade-off because it is almost instantaneously efficient when we want to add a new friend. However, the trade-off occurs when we want to print the social network or look for a specific connection.

In order to print the entire network, we must traverse through each person and then traverse through their list of friends. However, a "celebrity" friend with millions of friends could create a lengthy list to traverse through. Furthermore, although it is easy to locate a friend by their name using a dictionary, it is not as easy to determine if two people are friends by having to traverse through a list, a process that becomes more time-consuming as this list becomes larger. Despite these small challenges, the graph remains the most scalable and logical solution in determining human connections.
'''
