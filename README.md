# Movie recommender



## Content
I have downloaded a csv with films from [here](https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv) and created a users dataset using random numbers from numpy library. Using cosine similarity I have found the similarity among users and I have selected the movie that has not been rated by the user who has the highest rating for each similar user in order to make a 5 movies recommendation.


## Usage
It works by entering a number in the final function called 'top_5' and it will return 5 movies. Of course it only works if the user is already registered

## Examples
top_5(100)  # It asks 5 movies to recommend for user 100
'Gnomeo and Juliet.1',
 "It's Complicated",
 'The Twilight Saga: New Moon',
 'Remember Me',
 'Waiting For Forever'


## Project Structure

- `models/`: Stores the trained model (if applicable).
- `data/`: Directory to store the training and testing datasets.
    a) raw: Contains the original csv
    b) interim: Contains the movies csv after a little modification in the column genre
    c) processed: Contains the similarity matrix and the pivot table i have worked with
- `src/`: Contains the source code for the project.
- `docs/`: Documentation files for the project.
- `README.md`: Project documentation.

## Contribution

Contributions are welcome! If you find any issues or have improvements, please open an issue or submit a pull request.

