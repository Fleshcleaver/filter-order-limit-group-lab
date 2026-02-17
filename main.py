import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1 — planets with no moons
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE moons = 0;
""", conn1)

# STEP 2 — planets whose name is exactly 7 characters, return name + one other column
df_name_seven = pd.read_sql("""
    SELECT name, moons
    FROM planets
    WHERE LENGTH(name) = 7;
""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3 — low-mass planets (the 4 terrestrial ones), 2 columns
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass < 10;
""", conn1)

# STEP 4 — low-mass planet that also has moons (only Mars), all columns
df_mass_moon = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE mass < 1
      AND moons > 0;
""", conn1)

# STEP 5 — blue planets, 2 columns
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color = 'blue';
""", conn1)

##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6 — all dogs ordered by hunger descending (hungriest first)
df_hungry = pd.read_sql("""
    SELECT name
    FROM dogs
    ORDER BY hunger DESC;
""", conn2)

# STEP 7 — named dogs ordered by hunger ascending, return name + age
df_hungry_ages = pd.read_sql("""
    SELECT name, age
    FROM dogs
    WHERE name IS NOT NULL
    ORDER BY hunger ASC;
""", conn2)

# STEP 8 — the 4 oldest dogs
df_4_oldest = pd.read_sql("""
    SELECT name
    FROM dogs
    ORDER BY age DESC
    LIMIT 4;
""", conn2)


##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9 — total number of seasons (rows) in the table
df_ruth_years = pd.read_sql("""
    SELECT COUNT(*) FROM babe_ruth_stats;
""", conn3)

# STEP 10 — total career home runs
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) FROM babe_ruth_stats;
""", conn3)


##### Part 5: Grouping and Aggregation #####

# STEP 11 — seasons played per team, ordered alphabetically by team
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(*) AS number_years
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY team;
""", conn3)

# STEP 12 — average at-bats per team, highest average first
df_at_bats = pd.read_sql("""
    SELECT team, AVG(AB) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY average_at_bats DESC;
""", conn3)


conn1.close()
conn2.close()
conn3.close()