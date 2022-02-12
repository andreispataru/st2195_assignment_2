# Scrape Wikipedia

library(rvest)
wiki_url <- "https://en.wikipedia.org/wiki/Comma-separated_values"

html <- read_html(wiki_url)

html_node(html, ".wikitable") %>% 
  html_children() %>% 
  html_text(trim=TRUE)
