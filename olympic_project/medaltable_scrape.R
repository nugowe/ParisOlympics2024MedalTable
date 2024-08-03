# Load necessary libraries
library(rvest)
library(dplyr)

# URL of the Wikipedia page containing the medal table
url <- "https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table"

# Read the HTML content from the URL
page <- read_html(url)

# Print the title of the page to confirm we are on the right page
page_title <- page %>% html_node("title") %>% html_text()
cat("Page title:", page_title, "\n")

# Find the table with the specified class
medal_table <- page %>%
  html_node("table.wikitable.sortable.notheme.plainrowheaders.jquery-tablesorter")

# Check if the table was found
if (!is.null(medal_table)) {
  cat("Medal table found.\n")

  # Extract the data from the table
  medal_data <- medal_table %>%
    html_table(fill = TRUE) %>%
    # Clean the data by removing extra spaces and unnecessary rows
    filter(Rank != "") %>%
    mutate(across(everything(), ~gsub("\\[.*\\]", "", .))) %>%
    # Rename columns for clarity
    rename(
      Rank = 1,
      Country = 2,
      Gold = 3,
      Silver = 4,
      Bronze = 5,
      Total = 6
    )
    medal_data$Flag <- ""
  # Display the medal table
  #print(medal_data[c(1),])
  medal_data <- medal_data[c(1,2,7,3,4,5,6)]
  medal_data <- head(medal_data, -1)
  medal_data <- medal_data[-1,]
  print(medal_data)
} else {
  cat("Could not find the medal table on the Wikipedia page.\n")
}

write.csv(medal_data, "/home/nosa2k/MYPROJECTS/DJANGO/ParisOlympics2024MedalTable/olympic_project/olympic_project/medaltable_2024.csv", row.names = FALSE)