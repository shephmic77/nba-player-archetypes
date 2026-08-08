# NBA Player Archetypes

A personal data science project exploring whether NBA players can be grouped into meaningful statistical archetypes using K-Means clustering.

Rather than relying only on traditional positions such as point guard, shooting guard, forward, and center, I wanted to see what types of player roles would emerge directly from player statistics.

This repository also preserves the development of the project. The original scripts, experiments, and datasets are included alongside a cleaned final implementation.

## Project Origin

The project did not originally start as a clustering project.

My first idea was based around the changing role of the power forward in the NBA. I was interested in how traditional basketball positions have become less clearly defined as players have become more versatile and styles of play have changed.

That early work became what I called **"Death of PF."**

As I experimented with NBA data, the question became broader:

> Instead of assigning players to traditional positions first, could their statistics reveal different types of players on their own?

That led me toward unsupervised machine learning and K-Means clustering.

## Project Development

The repository preserves the original development files because the progression of the project is an important part of the work.

### V0 — Death of PF

The earliest version explored the original positional idea.

These files represent the starting point of the project before it developed into a more general player-archetype problem.

### V1 — Player Clustering

I then began experimenting with clustering NBA players based on their statistical profiles.

This stage included:

- experimenting with NBA data sources
- testing the `nba_api`
- working with 2024–25 player data
- testing different clustering scripts
- moving to a Kaggle 2023–24 dataset
- experimenting with different numbers of clusters
- trying to understand what each statistical cluster represented

These files are intentionally preserved in `development/` rather than rewritten to look like finished code.

## Final Approach

The cleaned final version uses **2023–24 NBA regular-season player statistics** and K-Means clustering to create data-driven player archetypes.

The general pipeline is:

1. Load the player dataset.
2. Clean and prepare player records.
3. Handle players who appeared for multiple teams.
4. Remove extremely small samples.
5. Select statistical features representing different parts of a player's game.
6. Standardize the features so statistics on different scales can be compared.
7. Apply K-Means clustering.
8. Examine the statistical profile of each cluster.
9. Assign descriptive archetype names based on those profiles.

The final model uses **10 clusters**.

## Features

The final analysis uses 10 statistical features describing scoring, shooting, playmaking, rebounding, defense, and playing time.

Using multiple features allows the clustering algorithm to compare overall statistical profiles instead of grouping players using a single statistic such as points per game.

Because K-Means is distance-based, the features are standardized before clustering. This prevents statistics with naturally larger numerical scales from dominating the clustering process.

## Why K-Means?

K-Means was useful for this project because I did not want to tell the model beforehand what each player's role should be.

There is no target variable such as:

`Point Guard`, `Wing`, `Center`, or `Star`.

Instead, the algorithm groups players whose statistical profiles are similar.

I can then examine the cluster centers and players within each group to determine what type of basketball role the cluster appears to represent.

This made the project more exploratory than simply predicting an existing position label.

## Interpreting the Clusters

One important part of the project was realizing that the algorithm does not automatically produce meaningful basketball names.

K-Means only produces cluster numbers.

For example:

```text
Cluster 0
Cluster 1
Cluster 2
...
```

The basketball interpretation comes afterward.

I examined the statistical characteristics of each cluster and the players assigned to it, then used those patterns to create more understandable archetype names.

The goal is not to claim that every player perfectly fits one label. The archetypes are a way of summarizing similarities found in the available statistics.

## What I Learned

This project was also part of learning Python and machine learning through experimentation.

The early files show a much less structured approach than the final version. I tested APIs, datasets, clustering methods, feature combinations, and different ways of interpreting the results.

One of the biggest lessons was that **the data available determines what kinds of player roles a model can recognize.**

Box-score statistics can represent things such as:

- scoring
- assists
- rebounds
- steals
- blocks
- shooting
- minutes played

But many important parts of basketball are much harder to represent with basic player statistics.

Examples include defensive positioning, off-ball movement, spacing, screening, decision-making, matchup versatility, and basketball IQ.

A clustering model therefore does not discover every type of basketball value. It discovers patterns in the information that it is given.

## Limitations

The archetypes should be treated as exploratory statistical groups rather than definitive player classifications.

Some major limitations include:

**Feature selection**

Changing the statistics used by the model can change the resulting clusters.

**Number of clusters**

K-Means requires the number of clusters to be selected beforehand. Ten clusters provide useful separation, but they are not the only possible solution.

**Box-score limitations**

Traditional statistics do not capture every contribution a player makes.

**Era effects**

The statistical profile of an NBA role changes over time. A player considered a certain archetype today might look very different statistically from a player filling a similar role in an earlier era.

**Interpretation**

The algorithm generates clusters, but the archetype names are my interpretation of the statistical patterns.

## Future Ideas

If I continued the project, I would expand beyond basic numerical box-score statistics.

Possible additions include:

- multiple NBA seasons
- era-specific clustering
- tracking data
- shot-location data
- defensive matchup information
- play-type data
- lineup data
- spatial or heat-map features

One idea I find especially interesting is comparing eras.

Instead of asking only:

> "What type of player is this?"

the question could become:

> "What type of player would this statistical profile represent in a different NBA era?"

That could help explore how the meaning of positions and player roles changes with the league itself.

## Repository Structure

```text
nba-player-archetypes/
│
├── README.md
│
├── data/
│   └── Project datasets
│
├── development/
│   ├── v0_death_of_pf/
│   │   └── Original "Death of PF" work
│   │
│   └── v1_player_clustering/
│       ├── early_tests/
│       ├── nba_api_tests/
│       └── kaggle_23_24/
│
├── final/
│   ├── nba_player_archetypes_final.py
│   ├── nba_2023_24_player_archetypes.csv
│   └── cluster_centroids_standardized.csv
│
└── portfolio/
    └── Project case study / presentation material
```

## Development vs. Final

There are two intentionally different parts of this repository.

### `development/`

Contains the original project files and experiments.

These files are preserved to show how the project actually developed, including early approaches, abandoned ideas, tests, and changes in direction.

### `final/`

Contains a cleaned reconstruction of the final clustering approach based on the direction reached during development.

It is intended to make the completed project easier to understand and reproduce without rewriting or deleting the original development history.

## Tools

- Python
- pandas
- NumPy
- scikit-learn
- K-Means clustering
- StandardScaler
- Jupyter Notebook
- NBA datasets / API experimentation

## Project Status

The original project is complete.

The repository was later organized to preserve the development history and provide a cleaner final implementation for documentation and portfolio use.
