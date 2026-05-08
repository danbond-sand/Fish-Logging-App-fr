from dataclasses import dataclass
from drafter import *

set_site_information(
    author="danbond@udel.edu",
    description="""A brief description of what your website does.
    Use a triple quoted string if you want to span multiple lines.""",
    sources=["Drafter 1.95 documentation", "ChatGPT Drafter Tutor"],
    planning=["your_planning_document.pdf"],
    links=["https://github.com/danbond-sand/Fish-Logging-App-fr"]
)
hide_debug_information()
set_website_title("Fish Log for Hog Slayers")
set_website_framed(False)

set_website_style("none")
add_website_css("""
body{
    background-color: azure;
    font-size: 24px;
}

.page-header {
    color: peru;
    text-align: center;
}

.catch-card {
    background-color: #fffacd;
    padding: 20px;
    margin: 20px;
    border-radius:15px;
    border: solid 2px peru;
    box-shadow: 2px 2px 10px lightgray
}
""")

start_server(
    State(
        catches = dannys_catches,
        next_id = 10,
        filtering_species = "",
        filtering_bait = "",
        filtering_location = "",
        min_weight = 0.0,
        min_length = 0.0,
        username = "Danny Ballz"
    )
)

@dataclass
class Catch:
    species: str
    weight: float
    length: float
    bait: str
    location: str
    date: str
    time: str
    image: bytes
    catch_id: int

@dataclass
class State:
    catches: list[Catch]
    next_id: int
    filtering_species: str
    filtering_bait: str
    filtering_location: str
    min_weight: float
    min_length: float
    username: str

def count_catches(catches: list[Catch], species: str) -> int:
    """
    """
    fish_caught = 0
    for catch in catches:
        if catch.species == species:
            fish_caught +=1
    return fish_caught
 
dannys_catches = [
    Catch("Snakehead", 5.0, 23.0, "Crankbait", 
          "Noxontown Pond, Middletown, DE",
          "June 8, 2024", "10:56 AM", "", 1),
    Catch("Largemouth Bass", 5.3, 20.5, "Crankbait", 
          "Noxontown Pond, Middletown, DE", 
          "June 26, 2024", "7:36 PM", "", 2),
    Catch("Snakehead", 8.0, 29.0, "Chatterbait", 
          "Noxontown Pond, Middletown, DE",  
          "May 17, 2025", "1:36 PM", "", 3),
    Catch("Pickerel", 4.0, 24.0, "Chatterbait", 
          "Betts Pond, Millsboro, DE",  
          "May 28, 2025", "4:20 PM", "", 4),
    Catch("Largemouth Bass", 5.0, 21.5, "Senko", 
          "Noxontown Pond, Middletown, DE", 
          "June 16, 2025",  "6:30 PM", "", 5),
    Catch("Largemouth Bass", 7.2, 23.5, "Senko", 
          "Noxontown Pond, Middletown, DE", 
          "June 16, 2025",  "8:16 PM", "", 6),
    Catch("Largemouth Bass", 4.0, 19.5, "Jig", 
          "Silver Lake, Middletown, DE", 
          "July 16, 2025", "7:23 AM", "", 7),
    Catch("Largemouth Bass", 4.5, 20.5, "Jig", 
          "Wiggins Mill Pond, Townsend, DE",
          "July 22, 2025", "8:36 AM", "", 8),
    Catch("Mahi", 14.5, 32.0, "Jig", 
          "North Atlantic Ocean, DE",  
          "August 6, 2025", "11:45 AM", "", 9)
] 

gracies_catches = [
    Catch("Largemouth Bass", 3.5, 20.8, "Senko", 
          "Back Creek Golf Course, Middletown, DE", 
          "October 26, 2023", "7:36 PM", "", 2),
    Catch("Crappie", 2.4, 14.5, "Chatterbait", 
          "Silver Lake, Middletown, DE",  
          "March 17, 2025", "1:36 PM", "", 3),
    Catch("Largemouth Bass", 3.0, 19.0, "Senko", 
          "Silver Lake, Middletown, DE",  
          "March 17, 2025", "4:20 PM", "", 4),
    Catch("Largemouth Bass", 2.5, 18.0, "Senko", 
          "Silver Lake, Middletown, DE", 
          "March 17, 2025",  "6:30 PM", "", 5),
]

jasons_catches = [
    Catch("Largemouth Bass", 0.4, 6.0, "Senko", 
          "Noxontown Pond, Middletown, DE",
          "June 8, 2025", "10:56 AM", "", 1),
    Catch("Largemouth Bass", 2.3, 17.5, "Senko", 
          "Noxontown Pond, Middletown, DE", 
          "June 26, 2025", "7:36 PM", "", 2),
    Catch("Snakehead", 2.0, 17.0, "Chatterbait", 
          "Noxontown Pond, Middletown, DE",  
          "July 2, 2025", "1:36 PM", "", 3),
    Catch("Crappie", 1.0, 9.0, "jig", 
          "Noxontown Pond, Middletown, DE",  
          "July 8, 2025", "4:20 PM", "", 4),
    Catch("Largemouth Bass", 4.0, 21.5, "Rooster Tail", 
          "Noxontown Pond, Middletown, DE", 
          "July 16, 2025",  "6:30 PM", "", 5)
]

assert_equal(count_catches(dannys_catches, "Largemouth Bass"), 5)
assert_equal(count_catches(dannys_catches, "Snakehead"), 2)
assert_equal(count_catches(dannys_catches, "Mahi"), 1)
    
def find_catch(catches: list[Catch], search_id: int) -> Catch | None:
    """
    """
    for catch in catches:
        if catch.catch_id == search_id:
            return catch
    return None
    
assert_equal(
    find_catch(dannys_catches, 4),
    Catch("Pickerel", 4.0, 24.0, "Chatterbait", 
          "Betts Pond, Millsboro, DE",  
          "May 28, 2025", "4:20 PM", "", 4)
)
assert_equal(
    find_catch(dannys_catches, 2),    
    Catch("Largemouth Bass", 5.3, 20.5, "Crankbait", 
          "Noxontown Pond, Middletown, DE", 
          "June 26, 2024", "7:36 PM", "", 2)
)
assert_equal(
    find_catch(dannys_catches, 3),
    Catch("Snakehead", 8.0, 29.0, "Chatterbait", 
          "Noxontown Pond, Middletown, DE",  
          "May 17, 2025", "1:36 PM", "", 3)
)
                                                    
def calculate_pb(catches: list[Catch], species: str) -> Catch:
    """
    """
    personal_best = catches[0]
    for catch in catches:
        if catch.species == species:
            if catch.weight > personal_best.weight:
                personal_best = catch
    return personal_best

assert_equal(
    calculate_pb(dannys_catches, "Largemouth Bass"),
    Catch("Largemouth Bass", 7.2, 23.5, "Senko", 
          "Noxontown Pond, Middletown, DE", 
          "June 16, 2025",  "8:16 PM", "", 6)
)
assert_equal(
    calculate_pb(dannys_catches, "Mahi"),
    Catch("Mahi", 14.5, 32.0, "Jig", 
          "North Atlantic Ocean, DE",  
          "August 6, 2025", "11:45 AM", "", 9)
)
assert_equal(
    calculate_pb(dannys_catches, "Snakehead"),
    Catch("Snakehead", 8.0, 29.0, "Chatterbait", 
          "Noxontown Pond, Middletown, DE",  
          "May 17, 2025", "1:36 PM", "", 3)
)
 
def most_caught(catches: list[Catch]) -> str:
    """
    """
    counts = {}
    for catch in catches:
        if catch.species not in counts:
            counts[catch.species] = 0
        counts[catch.species] += 1    
    best_species = ""
    best_count = 0
    for species in counts:
        if counts[species] > best_count:
            best_count = counts[species]
            best_species = species
    return best_species

assert_equal(most_caught(dannys_catches), "Largemouth Bass")
assert_equal(most_caught(gracies_catches), "Largemouth Bass")
assert_equal(most_caught(jasons_catches), "Largemouth Bass")
  
def most_successful_bait(catches: list[Catch]) -> str:
    """
    """
    counts = {}
    for catch in catches:
        if catch.bait not in counts:
            counts[catch.bait] = 0
        counts[catch.bait] += 1    
    best_bait = ""
    best_count = 0
    for bait in counts:
        if counts[bait] > best_count:
            best_count = counts[bait]
            best_bait = bait
    return best_bait

assert_equal(most_successful_bait(dannys_catches), "Jig")
assert_equal(most_successful_bait(gracies_catches), "Senko")
assert_equal(most_successful_bait(jasons_catches), "Senko")

def most_successful_spot(catches: list[Catch]) -> str:
    """
    """
    counts = {}
    for catch in catches:
        if catch.location not in counts:
            counts[catch.location] = 0
        counts[catch.location] += 1    
    best_spot = ""
    best_count = 0
    for location in counts:
        if counts[location] > best_count:
            best_count = counts[location]
            best_spot = location
    return best_spot

assert_equal(most_successful_spot(dannys_catches), "Noxontown Pond, Middletown, DE")
assert_equal(most_successful_spot(gracies_catches), "Silver Lake, Middletown, DE")
assert_equal(most_successful_spot(jasons_catches), "Noxontown Pond, Middletown, DE")
   
def species_found(catches: list[Catch]) -> int:
    """
    """
    unique_species = []
    for catch in catches:
        if catch.species not in unique_species:
            unique_species.append(catch.species)
    return len(unique_species)

assert_equal(species_found(dannys_catches), 4)
assert_equal(species_found(gracies_catches), 2)
assert_equal(species_found(jasons_catches), 3)
 
def filter_by_species(catches: list[Catch], species: str) -> list[Catch]:
    """
    """
    filtered_catches = []
    for catch in catches:
        if catch.species == species:
            filtered_catches.append(catch)
    return filtered_catches

assert_equal(
    filter_by_species(dannys_catches, "Largemouth Bass"),
    [
        Catch("Largemouth Bass", 5.3, 20.5, "Crankbait", 
              "Noxontown Pond, Middletown, DE", 
              "June 26, 2024", "7:36 PM", "", 2),
        Catch("Largemouth Bass", 5.0, 21.5, "Senko", 
              "Noxontown Pond, Middletown, DE", 
              "June 16, 2025",  "6:30 PM", "", 5),
        Catch("Largemouth Bass", 7.2, 23.5, "Senko", 
              "Noxontown Pond, Middletown, DE", 
              "June 16, 2025",  "8:16 PM", "", 6),
        Catch("Largemouth Bass", 4.0, 19.5, "Jig", 
              "Silver Lake, Middletown, DE", 
              "July 16, 2025", "7:23 AM", "", 7),
        Catch("Largemouth Bass", 4.5, 20.5, "Jig", 
              "Wiggins Mill Pond, Townsend, DE",
              "July 22, 2025", "8:36 AM", "", 8),
    ]
)
assert_equal(
    filter_by_species(dannys_catches, "Pickerel"),
    [
        Catch("Pickerel", 4.0, 24.0, "Chatterbait", 
              "Betts Pond, Millsboro, DE",  
              "May 28, 2025", "4:20 PM", "", 4)
    ]
)
assert_equal(
    filter_by_species(dannys_catches, "Snakehead"),
    [
        Catch("Snakehead", 5.0, 23.0, "Crankbait", 
              "Noxontown Pond, Middletown, DE",
              "June 8, 2024", "10:56 AM", "", 1),
        Catch("Snakehead", 8.0, 29.0, "Chatterbait", 
              "Noxontown Pond, Middletown, DE",  
              "May 17, 2025", "1:36 PM", "", 3)
    ]      
)
 
def filter_by_bait(catches: list[Catch], bait: str) -> list[Catch]:
    """
    """
    filtered_catches = []
    for catch in catches:
        if catch.bait == bait:
            filtered_catches.append(catch)
    return filtered_catches

assert_equal(
    filter_by_bait(dannys_catches, "Chatterbait"), 
    [
        Catch("Snakehead", 8.0, 29.0, "Chatterbait", 
              "Noxontown Pond, Middletown, DE",  
              "May 17, 2025", "1:36 PM", "", 3),
        Catch("Pickerel", 4.0, 24.0, "Chatterbait", 
              "Betts Pond, Millsboro, DE",  
              "May 28, 2025", "4:20 PM", "", 4)
    ]
)
assert_equal(
    filter_by_bait(dannys_catches, "Jig"), 
    [
        Catch("Largemouth Bass", 4.0, 19.5, "Jig", 
              "Silver Lake, Middletown, DE", 
              "July 16, 2025", "7:23 AM", "", 7),
        Catch("Largemouth Bass", 4.5, 20.5, "Jig", 
              "Wiggins Mill Pond, Townsend, DE",
              "July 22, 2025", "8:36 AM", "", 8),
        Catch("Mahi", 14.5, 32.0, "Jig", 
              "North Atlantic Ocean, DE",  
              "August 6, 2025", "11:45 AM", "", 9)
    ]
)
assert_equal(
    filter_by_bait(dannys_catches, "Senko"),
    [
        Catch("Largemouth Bass", 5.0, 21.5, "Senko", 
              "Noxontown Pond, Middletown, DE", 
              "June 16, 2025",  "6:30 PM", "", 5),
        Catch("Largemouth Bass", 7.2, 23.5, "Senko", 
              "Noxontown Pond, Middletown, DE", 
              "June 16, 2025",  "8:16 PM", "", 6)
    ]
)
     
def filter_by_location(catches: list[Catch], location: str) -> list[Catch]:
    """
    """
    filtered_catches = []
    for catch in catches:
        if catch.location == location:
            filtered_catches.append(catch)
    return filtered_catches 

assert_equal(
    filter_by_location(dannys_catches, "Wiggins Mill Pond, Townsend, DE"),
    [
        Catch("Largemouth Bass", 4.5, 20.5, "Jig", 
              "Wiggins Mill Pond, Townsend, DE",
              "July 22, 2025", "8:36 AM", "", 8)
    ]
)
assert_equal(
    filter_by_location(dannys_catches, "Noxontown Pond, Middletown, DE"),
    [
        Catch('Snakehead', 5.0, 23.0, 'Crankbait', 
              'Noxontown Pond, Middletown, DE', 
              'June 8, 2024', '10:56 AM', "", 1), 
        Catch('Largemouth Bass', 5.3, 20.5, 'Crankbait', 
              'Noxontown Pond, Middletown, DE', 
              'June 26, 2024', '7:36 PM', "", 2), 
        Catch('Snakehead', 8.0, 29.0, 'Chatterbait', 
              'Noxontown Pond, Middletown, DE', 
              'May 17, 2025', '1:36 PM', "", 3), 
        Catch('Largemouth Bass', 5.0, 21.5, 'Senko', 
              'Noxontown Pond, Middletown, DE', 
              'June 16, 2025', '6:30 PM', "", 5), 
        Catch('Largemouth Bass', 7.2, 23.5, 'Senko', 
              'Noxontown Pond, Middletown, DE', 
              'June 16, 2025', '8:16 PM', "", 6)
    ]
)
assert_equal(
    filter_by_location(dannys_catches, "North Atlantic Ocean, DE"), 
    [
        Catch("Mahi", 14.5, 32.0, "Jig", 
              "North Atlantic Ocean, DE",  
              "August 6, 2025", "11:45 AM", "", 9)
    ]
)


def apply_filters(state: State) -> list[Catch]:
    """
    """
    filtered_catches = []
    for catch in state.catches:
        display_catch = True
        if state.filtering_species != "":
            if catch.species != state.filtering_species:
                display_catch = False
                
        if state.filtering_bait != "":
            if catch.bait != state.filtering_bait:
                display_catch = False
                
        if state.filtering_location != "":
            if catch.location != state.filtering_location:
                display_catch = False
                
        if state.min_weight > 0:
            if catch.weight <= state.min_weight:
                display_catch = False
                
        if state.min_length > 0:
            if catch.length <= state.min_length:
                display_catch = False
        
        if display_catch:
            filtered_catches.append(catch)
            
    return filtered_catches



def filter_by_weight(catches: list[Catch], min_weight: float) -> list[Catch]:
    """
    """
    filtered_catches = []
    for catch in catches:
        if catch.weight >= min_weight:
            filtered_catches.append(catch)
    return filtered_catches 


assert_equal(
    filter_by_weight(dannys_catches, 5.0),
    [
        Catch('Snakehead', 5.0, 23.0, 'Crankbait', 
              'Noxontown Pond, Middletown, DE', 
              'June 8, 2024', '10:56 AM', "", 1), 
        Catch('Largemouth Bass', 5.3, 20.5, 'Crankbait', 
              'Noxontown Pond, Middletown, DE', 
              'June 26, 2024', '7:36 PM', "", 2), 
        Catch('Snakehead', 8.0, 29.0, 'Chatterbait', 
              'Noxontown Pond, Middletown, DE', 
              'May 17, 2025', '1:36 PM', "", 3), 
        Catch('Largemouth Bass', 5.0, 21.5, 'Senko', 
              'Noxontown Pond, Middletown, DE', 
              'June 16, 2025', '6:30 PM', "", 5), 
        Catch('Largemouth Bass', 7.2, 23.5, 'Senko', 
              'Noxontown Pond, Middletown, DE', 
              'June 16, 2025', '8:16 PM', "", 6), 
        Catch('Mahi', 14.5, 32.0, 'Jig', 
              'North Atlantic Ocean, DE', 
              'August 6, 2025', '11:45 AM', "", 9)
    ]
)
assert_equal(
    filter_by_weight(dannys_catches, 7.0), 
    [ 
        Catch('Snakehead', 8.0, 29.0, 'Chatterbait', 
              'Noxontown Pond, Middletown, DE', 
              'May 17, 2025', '1:36 PM', "", 3), 
        Catch('Largemouth Bass', 7.2, 23.5, 'Senko', 
              'Noxontown Pond, Middletown, DE', 
              'June 16, 2025', '8:16 PM', "", 6), 
        Catch('Mahi', 14.5, 32.0, 'Jig', 
              'North Atlantic Ocean, DE', 
              'August 6, 2025', '11:45 AM', "", 9)
    ]
)
assert_equal(
    filter_by_weight(dannys_catches, 8.0), 
    [
        Catch('Snakehead', 8.0, 29.0, 'Chatterbait', 
              'Noxontown Pond, Middletown, DE', 
              'May 17, 2025', '1:36 PM', "", 3),  
        Catch('Mahi', 14.5, 32.0, 'Jig', 
              'North Atlantic Ocean, DE', 
              'August 6, 2025', '11:45 AM', "", 9)
    ]
)
 
def filter_by_length(catches: list[Catch], min_length: float) -> list[Catch]:
    """
    """
    filtered_catches = []
    for catch in catches:
        if catch.length >= min_length:
            filtered_catches.append(catch)
    return filtered_catches

assert_equal(
    filter_by_length(dannys_catches, 22.0 ),
    [
        Catch("Snakehead", 5.0, 23.0, "Crankbait", 
              "Noxontown Pond, Middletown, DE",
              "June 8, 2024", "10:56 AM", "", 1),
        Catch("Snakehead", 8.0, 29.0, "Chatterbait", 
              "Noxontown Pond, Middletown, DE",  
              "May 17, 2025", "1:36 PM", "", 3),
        Catch("Pickerel", 4.0, 24.0, "Chatterbait", 
              "Betts Pond, Millsboro, DE",  
              "May 28, 2025", "4:20 PM", "", 4),
        Catch("Largemouth Bass", 7.2, 23.5, "Senko", 
              "Noxontown Pond, Middletown, DE", 
              "June 16, 2025",  "8:16 PM", "", 6),
        Catch("Mahi", 14.5, 32.0, "Jig", 
              "North Atlantic Ocean, DE",  
              "August 6, 2025", "11:45 AM", "", 9)
    ]
)
assert_equal(
    filter_by_length(dannys_catches, 26.0 ), 
    [
        Catch("Snakehead", 8.0, 29.0, "Chatterbait", 
              "Noxontown Pond, Middletown, DE",  
              "May 17, 2025", "1:36 PM", "", 3),
        Catch("Mahi", 14.5, 32.0, "Jig", 
              "North Atlantic Ocean, DE",  
              "August 6, 2025", "11:45 AM", "", 9)
    ]
)
assert_equal(
    filter_by_length(dannys_catches, 30.0), 
    [
        Catch("Mahi", 14.5, 32.0, "Jig", 
              "North Atlantic Ocean, DE",  
              "August 6, 2025", "11:45 AM", "", 9)
    ]
)

def format_date(date: str) -> str:
    if "-" not in date:
        return date
    parts = date.split("-")
    
    year = parts[0]
    month = parts[1]
    day = parts[2]
    
    months = [
        "January","February","March",
        "April","May","June",
        "July","August","September",
        "October","November","December"
    ]
    
    month_name = months[int(month)-1]
    
    return month_name + " " + str(int(day)) + "," + year

def format_time(time: str) -> str:
    if "AM" in time:
        return time
    elif "PM" in time:
        return time
    parts = time.split(":")
    
    hour = int(parts[0])
    minute = parts[1]
    
    suffix = "AM"
    
    if hour >= 12:
        suffix = "PM"
    if hour > 12:
        hour = hour - 12
    if hour == 0:
        hour = 12
    
    return str(hour) + ":" + minute + " " + suffix

set_website_style("none")

@route
def index(state: State) -> Page:
    """
    """
    total_catches = state.next_id - 1
    return Page(
        state, 
        [
            Header(
                "Welcome " + state.username,
                style_text_align = "center",
                style_color = "peru",
                style_font_size = "32px",
            ),
            HorizontalRule(),
            
            Row(Text("Total Catches : " + str(total_catches))),
            LineBreak(),
                
            Row(Text("Best Bait : " + most_successful_bait(state.catches))),
            LineBreak(),
                
            Row(Text("Best Location : " +  most_successful_spot(state.catches))),
            LineBreak(),
                
            Row(Text("Most Recorded Species : " + most_caught(state.catches))),
            LineBreak(),
                
            Row(Text("Species Caught : " + str(species_found(state.catches)))),
            HorizontalRule(),
            
            Button("View Your Catches", "view_catches"),
            Button("Log New Catch", "log_catch"),
            HorizontalRule()
        ],
    )



@route
def log_catch(state: State) -> Page:
    """
    """
    return Page(
        state,
        [
            Header("LOG CATCH"),
            HorizontalRule(),
        
            Row ("SPECIES : ", TextBox("species", "")),
            LineBreak(),
                
            Row ("WEIGHT : ", TextBox("weight", "")),
            LineBreak(),
                
            Row ("LENGTH : ", TextBox("length", "")),
            LineBreak(),
                
            Row ("BAIT : ", TextBox("bait", "")),
            LineBreak(),
                
            Row ("LOCATION : ", TextBox("location", kind="date")),
            LineBreak(),
                
            Row ("TIME : ", TextBox("time", kind="date")),
            LineBreak(),
                
            Row ("DATE : ", TextBox("date", "")),
            LineBreak(),
                
            Row ("PHOTO : ", FileUpload("image")),
            HorizontalRule(),
        
            "Confirm inputs and log your catch.",
            Button("Submit", "save_new_catch"),
            HorizontalRule(),
            
            Button("Cancel", "index"),
            HorizontalRule(),
        ],
    )
  
@route
def save_new_catch(
    state: State, 
    species: str,
    weight: float, 
    length: float, 
    bait: str, 
    location: str, 
    date: str, 
    time: str,
    image: str
) -> Page:
    """
    """
    new_id = state.next_id
    state.next_id += 1
    new_catch = Catch(
        species, 
        weight, 
        length, 
        bait, 
        location, 
        date, 
        time,
        image,
        new_id  
    )
    state.catches.append(new_catch)
    return index(state)

@route
def view_catches(state: State) -> Page:
    """
    """
    content = []
    
    
    filtered_catches = apply_filters(state)
    if not filtered_catches:
        return Page(
            state,
            [
                Header("No catches, return to homepage."),
                    
                Button("Home", "index",)
            ]
        )
    
    for catch in filtered_catches:
        content.append(
            
            
            Div(                
                Header(catch.species),
                
                Image(catch.image, width = 300) if catch.image != "" else "",
                LineBreak(),
                
                 
                Text(
                     "Size : " + str(catch.weight) +
                     " lbs.    |    " +
                     str(catch.length) +
                     " in."
                ), 
                LineBreak(),         
                 
                Text("Caught At : " + catch.location ),
                LineBreak(),
                
                Text(
                    "Date : " +
                    format_time(catch.time) +
                    "    |    " +
                    format_date(catch.date)
                ),
                LineBreak(),
                
                Text("Bait Used : " + catch.bait),
                LineBreak(),
                        
                Text("Catch # : " + str(catch.catch_id)),
                HorizontalRule(),
                        
                Button(
                    "Edit Catch",
                    "edit_catch",
                    [Argument("search_id",catch.catch_id)]
                ),
                Button(
                   "Delete Catch",
                    "delete_catch",
                    [Argument("search_id",catch.catch_id)]
                ),
                
                classes="catch-card"
            ), 
        )
        
    return Page(
        state, 
        [
            Header(state.username + "'s Catches"),
            HorizontalRule(),
            
            Button("Choose Filter", "filter_by"),
            Button("Return Home", "index",),
            
            HorizontalRule(),
            *content,
            HorizontalRule()
        ]
    )     
@route
def edit_catch(state: State, search_id: int) -> Page:
    """
    """
    selected_catch = find_catch(state.catches, search_id)
    return Page(
        state, 
        [
            Header("EDIT CATCH : "),
            HorizontalRule(),
            
            Row ("SPECIES : ", TextBox("new_species", selected_catch.species)),
            LineBreak(),
             
            Row ("WEIGHT : ", TextBox("new_weight", str(selected_catch.weight))),
            LineBreak(),
             
            Row ("LENGTH : ", TextBox("new_length", str(selected_catch.length))),
            LineBreak(),
             
             
            Row ("BAIT : ", TextBox("new_bait", selected_catch.bait)),
            LineBreak(),
             
            Row ("LOCATION : ", TextBox("new_location", selected_catch.location)),
            LineBreak(),
             
            Row ("DATE : ", TextBox("new_date", selected_catch.date, kind="date")),
            LineBreak(),
             
            Row ("TIME : ", TextBox("new_time", selected_catch.time, kind="time")),
            LineBreak(),
             
           "Confirm and update your catch.",
            Button(
                "Save to log", 
                "save_catch_edits",
                [Argument("search_id", search_id)],
            ),
            HorizontalRule(),
            
            Button("Cancel", "index"),
            HorizontalRule()
        ]
    )

@route
def save_catch_edits(
    state: State,
    new_species: str,
    new_weight: float,
    new_length: float,
    new_bait: str,
    new_location: str,
    new_date: str,
    new_time: str,
    search_id: int
) -> Page:
    """
    """
    selected_catch = find_catch(state.catches, search_id)
    if selected_catch:
        selected_catch.species = new_species
        selected_catch.weight = new_weight
        selected_catch.length = new_length
        selected_catch.bait = new_bait
        selected_catch.location = new_location
        selected_catch.date = new_date
        selected_catch.time = new_time        
        
    return view_catches(state)

@route
def delete_catch(state: State, search_id: int) -> Page:
    """
    """
    updated_catches = []
    for catch in state.catches:
        if catch.catch_id != search_id:
            updated_catches.append(catch) 
    state.catches = updated_catches
    return index(state)

@route
def filter_by(state: State) -> Page:
    """
    """
    return Page(
        state,
        [
            Header("Filter Catches"),
           
            HorizontalRule(),
            
            "Enter Filter Condition Below",
            LineBreak(),
             
            Row("Species : ", TextBox("species", "")),
            LineBreak(),
             
            Row("Bait : ", TextBox("bait", "")),
            LineBreak(),
             
            Row("Location : ", TextBox("location", "")),
            LineBreak(),
             
            Row("Minimum Weight : ", TextBox("min_weight", "")),
            LineBreak(),
             
            Row("Minimum Length : ", TextBox("min_length", "")),           
            HorizontalRule(),
            
            Button("Confirm Selections", "save_filter_to_state"),
            Button("Clear Selections", "clear_all_filters"),
            HorizontalRule(),
            
            Button("Cancel", "view_catches"),
            HorizontalRule(),
                
        ]
    )    
@route
def save_filter_to_state(state: State, species: str, bait: str, location: str, min_weight: str, min_length: str,) -> Page:
    """
    """
    state.filtering_species = species
    state.filtering_bait = bait
    state.filtering_location = location
    if min_weight == "":
        state.min_weight = 0.0
    else:
        state.min_weight = float(min_weight)
    if min_length == "":
        state.min_length = 0.0
    else:
        state.min_length = float(min_length)
    return view_catches(state)

@route
def clear_all_filters(state: State) -> Page:
    """
    """
    state.filtering_species = ""
    state.filtering_bait = ""
    state.filtering_location = ""
    state.min_weight = 0.0
    state.min_length = 0.0
    
    return view_catches(state)


    )
)


