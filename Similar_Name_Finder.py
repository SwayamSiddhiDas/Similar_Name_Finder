from rapidfuzz import process, fuzz

# Data Preparation: A list of names
names = [
    "Geetha", "Gita", "Gitu", "Geeta", "Geethu",
    "Sita", "Seetha", "Sitha",
    "Ram", "Rama", "Raam",
    "Krishna", "Krisna", "Krish",
    "Sathish", "Satish", "Satis",
    "Priya", "Pria", "Priyah",
    "Kavitha", "Kavita", "Kavitha",
    "Suresh", "Sures", "Sureshh",
    "Anitha", "Anita", "Anitah",
    "Rajesh", "Raj", "Rajes"
]

def find_similar_names(input_name):
    """
    Finds similar names from the list and returns them with similarity scores.
    """
    # Using RapidFuzz to find the best matches
    matches = process.extract(input_name, names, scorer=fuzz.WRatio, limit=5)
    
    if not matches:
        return None, []

    best_match = matches[0]
    other_matches = matches[1:]
    
    return best_match, other_matches

if __name__ == "__main__":
    user_input = input("Enter a name: ")
    
    best_match, other_matches = find_similar_names(user_input)
    
    if best_match:
        print(f"\nBest Match: '{best_match[0]}' with a similarity score of {best_match[1]:.2f}")
        
        if other_matches:
            print("\nOther similar names:")
            for match in other_matches:
                print(f"- '{match[0]}' with a similarity score of {match[1]:.2f}")
    else:
        print("No similar names found.")
