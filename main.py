import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

conn1 = sqlite3.connect('planets.db')

pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1 — all columns for planets with 0 moons
# NOTE: replace 'num_moons' below if the column name differs in your DB
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
""", conn1)

# STEP 2 — name and mass for planets with a 7-letter name
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3 — name and mass for planets with mass <= 1.00
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
""", conn1)

# STEP 4 — all columns for planets with at least 1 moon and mass < 1.00
# NOTE: replace 'num_moons' below if the column name differs in your DB
df_mass_moon = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1
      AND mass < 1.00;
""", conn1)

# STEP 5 — name and color for planets whose color contains "blue"
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
""", conn1)

##### Part 3: Ordering and Limiting #####

conn2 = sqlite3.connect('dogs.db')

pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6 — name, age, breed of hungry dogs (hungry=1), youngest to oldest
df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
""", conn2)

# STEP 7 — name, age, hungry for hungry dogs aged 2–7, alphabetical by name
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
""", conn2)


# STEP 8 — name, age, breed for the 4 oldest dogs, sorted alphabetically by breed
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed FROM (
        SELECT name, age, breed
        FROM dogs
        ORDER BY age DESC
        LIMIT 4
    )
    ORDER BY breed ASC;
""", conn2)

##### Part 4: Aggregation #####

conn3 = sqlite3.connect('babe_ruth.db')

pd.read_sql("""SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9 — total number of seasons
df_ruth_years = pd.read_sql("""
    SELECT COUNT(*) FROM babe_ruth_stats;
""", conn3)

# STEP 10 — total career home runs
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) FROM babe_ruth_stats;
""", conn3)

##### Part 5: Grouping and Aggregation #####

# STEP 11 — number of seasons per team, ordered alphabetically by team
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(*) AS number_years
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY team;
""", conn3)

# STEP 12 — average at-bats per team, highest average first
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY average_at_bats DESC;
""", conn3)


conn1.close()
conn2.close()
conn3.close()