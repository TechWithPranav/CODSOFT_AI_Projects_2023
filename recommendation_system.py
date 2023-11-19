import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample data for movies--------------------------------------
movies_data = {'movie_id': [1, 2, 3, 4],
               'title': ['Action Movie', 'Comedy Film', 'Adventure Flick', 'Drama Feature'],
               'genre': ['Action', 'Comedy', 'Adventure', 'Drama']}
movies_df = pd.DataFrame(movies_data)

# Sample data for books-------------------------------------
books_data = {'book_id': [1, 2, 3, 4],
              'title': ['Mystery Novel', 'Science Fiction Book', 'Romance Story', 'Thriller'],
              'genre': ['Mystery', 'Science Fiction', 'Romance', 'Thriller']}
books_df = pd.DataFrame(books_data)

# Sample data for products--------------------------------
products_data = {'product_id': [1, 2, 3],
                 'name': ['Laptop', 'Headphones', 'Smartwatch'],
                 'category': ['Electronics', 'Audio', 'Wearables']}
products_df = pd.DataFrame(products_data)

def get_recommendations(df, title_column, genre_column):
    # Create a TF-IDF Vectorizer-----------------------
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df[genre_column])

    # Compute the cosine similarity---------------------
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Function to get item recommendations-------------------
    def recommend_item(title):
        idx = df.index[df[title_column] == title].tolist()[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:4]  # Get the top 3 similar items
        item_indices = [i[0] for i in sim_scores]
        return df[title_column].iloc[item_indices]

    return recommend_item

# Menu-driven program-------------------------------
global item_type
global title_column
global genre_column
while True:
    print("1. Movies")
    print("2. Books")
    print("3. Products")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == '1':
        item_type = 'Movies'
        title_column = 'title'
        genre_column = 'genre'
        df = movies_df
    elif choice == '2':
        item_type = 'Books'
        title_column = 'title'
        genre_column = 'genre'
        df = books_df
    elif choice == '3':
        item_type = 'Products'
        title_column = 'name'
        genre_column = 'category'
        df = products_df
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue

    print(f"\n--- {item_type} Recommendation ---")
    
    
    recommend_item = get_recommendations(df, title_column, genre_column)
    title_to_recommend = input(f"Enter the {item_type[:-1]} title for recommendations: ")
    recommendations = recommend_item(title_to_recommend)

    print(f"\nTop 3 {item_type} Recommendations for '{title_to_recommend}':")
    for recommendation in recommendations.values:
        print(recommendation)
print("\n")
