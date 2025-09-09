import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
var1 = pd.read_csv("netflix_titles.csv")
csv2 = var1.dropna(subset=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
      'release_year', 'rating', 'duration', 'listed_in', 'description'])
csv2 = csv2.drop_duplicates()
csv2.to_csv("enhanced_netflix_dataset.csv", index=False)

# Count by release year
year_counts = csv2['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.plot(year_counts.index, year_counts.values, marker='o', linestyle='-', color='purple')
plt.title('Netflix Releases Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.grid(True)
plt.tight_layout()
plt.savefig("Netflix Releases Over the Years.png")
plt.show()

#comparision between movies  and tv show

type_counts = csv2["type"].value_counts()
plt.figure(figsize=(12, 6))
plt.bar(type_counts.index, type_counts.values,  color=["orange","green"],label="Movies vs T.V. shows")
plt.title('Number of movies vs T.V shows on Netflix')
plt.xlabel(' Show type')
plt.ylabel(' Show count')
plt.legend()
plt.tight_layout()
plt.savefig("Number of movies vs T.V shows on Netflix.png")
plt.show()

#percentage of content rating
rating_counts = csv2["rating"].value_counts()
plt.figure(figsize=(6,8))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct="%1.1f%%")  
plt.title("Percentage of contents rating")
plt.legend(rating_counts.index, title="Ratings", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("Percentage of contents rating.png")
plt.show()

#movie duration
movie_dur = csv2[csv2['type']== "Movie"].copy()
movie_dur['duration_int'] = movie_dur['duration'].str.replace('min', '', regex=False).astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_dur['duration_int'] ,bins=30,color="purple",edgecolor="black",label="Movie duration")
plt.title('Distribution of movie duration')
plt.xlabel('Duration(Minutes)')
plt.ylabel('Number of movies')
plt.legend()
plt.tight_layout()
plt.savefig("Distribution of movie duration.png")
plt.show()

#scatter plot
#release year vs number of shows
release_counts = csv2['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,6))

plt.scatter(release_counts.index,release_counts.values,color="green", marker="o")
plt.title('Release year vs Number of shows')
plt.xlabel('Release Year')
plt.ylabel('Number of shows')
plt.tight_layout()
plt.savefig("Release year vs Number of shows.png")
plt.show()


# Top 10 directors by number of shows/movies
top_directors = csv2['director'].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.barh(top_directors.index[::-1], top_directors.values[::-1], color='teal',label="Director")
plt.title('Top 10 Directors on Netflix')
plt.xlabel('Number of shows')
plt.ylabel('Director Name')
plt.tight_layout()
plt.legend()
plt.savefig("Top 10 Directors on Netflix.png")
plt.show()

#country most producer of shows

country_counts = csv2["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color="dark green",label="country")
plt.title('Top 10 country by Number of shows')
plt.xlabel('Number of shows')
plt.ylabel('Country')
plt.legend()
plt.tight_layout()
plt.savefig("Top 10 country by Number of shows.png")
plt.show()

#subplotting 
content_by_year = csv2.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,5))
#first movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color="orange",label="movies")
ax[0].set_title("Movies release per years")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")
ax[0].legend()


#tV shows
ax[1].plot(content_by_year.index, content_by_year["TV Show"], color="green",label="TV shows")
ax[1].set_title("TV show release per year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of TV shows")
ax[1].legend()

fig.suptitle("Comparison of movies and TV shows")
plt.tight_layout()
plt.savefig("Comparison of movies and TV shows.png")
plt.show()
print("Total Movies:", len(csv2[csv2['type'] == 'Movie']))
print("Total TV Shows:", len(csv2[csv2['type'] == 'TV Show']))
print("Time Span:", csv2['release_year'].min(), "to", csv2['release_year'].max())
