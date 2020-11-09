#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Your code here
    route = {}
    #put all tickets in a dictionary
    for ticket in range(length):
        #set source as key and destination as value
        route[tickets[ticket].source] = tickets[ticket].destination
    #array to hold results
    trip = []
    #set first destination
    current_destination = "NONE"

    # go through the route putting it in order
    while len(route) > 0:
        #get next destination
        new_destination = route[current_destination]
        #add current destination to array
        trip.append(route[current_destination])
        #delete current object entry
        del route[current_destination]
        #set current destination to new detination
        current_destination = new_destination

    return trip
