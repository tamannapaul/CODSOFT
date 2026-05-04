movies = [
    {"name": "Inception", "genre": "sci-fi"},
    {"name": "Interstellar", "genre": "sci-fi"},
    {"name": "The Matrix", "genre": "sci-fi"},
    {"name": "The Dark Knight", "genre": "action"},
    {"name": "Avengers", "genre": "action"},
    {"name": "John Wick", "genre": "action"},
    {"name": "Titanic", "genre": "romance"},
    {"name": "The Notebook", "genre": "romance"},
    {"name": "La La Land", "genre": "romance"},
    {"name": "Conjuring", "genre": "horror"},
    {"name": "Insidious", "genre": "horror"},
    {"name": "It", "genre": "horror"}
]
def recommend(genre):
    return [movie["name"] for movie in movies if movie["genre"] == genre]
def display_menu():
    print("\nSelect a genre:")
    print("1. Sci-Fi")
    print("2. Action")
    print("3. Romance")
    print("4. Horror")
    print("5. Exit")
def main():
    print("========================================")
    print("     MOVIE RECOMMENDATION SYSTEM")
    print("========================================")
    genre_map = {
        "1": "sci-fi",
        "2": "action",
        "3": "romance",
        "4": "horror"
    }
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "5":
            print("\nThank you for using the system.")
            break
        if choice in genre_map:
            selected_genre = genre_map[choice]
            results = recommend(selected_genre)
            print("\n----------------------------------------")
            print(f" Top Recommendations ({selected_genre.upper()})")
            print("----------------------------------------")
            for i, movie in enumerate(results, 1):
                print(f"{i}. {movie}")
        else:
            print("\nInvalid choice. Please try again.")
if __name__ == "__main__":
    main()