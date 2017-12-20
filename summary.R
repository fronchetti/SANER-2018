install.packages("ggplot2")
library(ggplot2)

setwd("/home/fronchetti/Documentos/SANER-2017")

data <- read.csv("summary.csv")

# Identifies other languages used in projects where the main language is C or C++
c_cpp_languages <- subset(data, main_language == "C" | main_language == "C++")
write.csv(c_cpp_languages, file = "c_cpp_languages.csv")

# Identifies projects without commits
zero_commits <- subset(data, commits == 0)
write.csv(zero_commits, file = "zero_commits.csv")

# Identifies projects without contributors
zero_contributors <- subset(data, newcomers == 0)
write.csv(zero_contributors, file = "zero_contributors.csv")
