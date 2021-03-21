library(tidyverse)
library(stringr)

factory <- read_csv("factory.csv")

# extract last word from string for 'city'
tail(strsplit('P4M6+FV San Kamphaeng, San Kamphaeng District, Chiang Mai', split = " ")[[1]],2)

tail(strsplit(factory$city, split = " ")[[1]],2)

factory %>%
    mutate(
        city2 = tail(strsplit(factory$city, split = " ")[[1]], 2)
    )


word('P4M6+FV San Kamphaeng, San Kamphaeng District, Chiang Mai', -2)

# Extract last two words from sentence ----
# https://rdrr.io/cran/stringr/man/word.html

word(unlist(factory$city),start = -2, end = -1)

# create new column for city2
factory1 <- factory %>%
    mutate(
        city2 = word(unlist(factory$city),start = -2, end = -1)
    )

# create new data.frame to join with THAI.map
city.map <- data.frame(Location = factory1$city2, lat = factory1$lat, long = factory1$lng)


# Maps Package ----
library(maps)

world.map <- map_data("world")

THAI.map <- world.map %>% filter(region == "Thailand")

# visualize THAI.map + city.map
THAI.map %>%
    ggplot() + 
    geom_map(map = THAI.map, aes(x = long, y = lat, map_id = region), fill = "white", color = "black") +
    geom_point(data = city.map, aes(x = long, y = lat, color = "red"), alpha = 0.9)
