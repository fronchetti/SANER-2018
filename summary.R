# install.packages("ggplot2")
# install.packages("reshape2")
# install.packages("scales")
library(ggplot2)
library(reshape2)
library(scales)

setwd("/home/fronchetti/Documentos/SANER-2017") # Working directory

####################
#   Time series    #
####################

monthly <- read.csv("monthly_contributions.csv", colClasses=c("Date",NA, NA, NA,NA)) # This file will be used in time series analysis

# CHART: Number of projects
ggplot(monthly, aes(x=Date, y=Projects)) +
  scale_x_date(breaks = date_breaks("years"), labels = date_format("%Y")) + 
  geom_line(size=1.2, color="#DC3912") +
  theme(axis.text=element_text(size=12, colour = "black"), axis.title=element_text(size=14, face="bold"), legend.title=element_blank(), legend.text=element_text(size=12)) + 
  labs(y = "# Projects", x = "Years")

# CHART: Project's mean and median
chart_data <- monthly[,-which(names(monthly)=="Amount" | names(monthly)=="Projects")] # We're not using some values in this chart
chart_data_melt <- melt(chart_data, id="Date") # Melting values

ggplot(chart_data_melt, aes(x=Date, y=value, colour=variable, group=variable)) +
  scale_x_date(breaks = date_breaks("years"), labels = date_format("%Y")) + 
  geom_line(size=1.2, aes(linetype = variable)) + scale_color_manual(values=c("#3366CC", "#109618")) +
  theme(axis.text=element_text(size=12, colour = "black"), axis.title=element_text(size=14, face="bold"), legend.title=element_blank(), legend.text=element_text(size=12)) + 
  labs(y = "# Commits", x = "Years")

####################
#     Boxplots     #
####################

data <- read.csv("summary.csv") # This file will be used in our box plot analysis
data_final <- subset(data, newcomers > 0 & commits > 0) # Final dataset (Without projects with zero contributors or contributions)

# Image size (Suggested): Width: 360 x Height: 280
boxplot(data_final$age, las = 1, xlab = "Age (Years)", outline = FALSE, cex.lab=1.2, horizontal = TRUE)
boxplot(data_final$commits, las = 1, xlab = "# Commits", outline = FALSE, cex.lab=1.2, horizontal = TRUE)
boxplot(data_final$newcomers, las = 1, xlab = "# Contributors", outline = FALSE, cex.lab=1.2, horizontal = TRUE)
boxplot(data_final$pulls_opened, las = 1, xlab = "# PRs Opened", outline = FALSE, cex.lab=1.2, horizontal = TRUE)
boxplot(data_final$pulls_closed, las = 1, xlab = "# PRs Closed", outline = FALSE, cex.lab=1.2, horizontal = TRUE)
boxplot(data_final$pulls_merged, las = 1, xlab = "# PRs Merged", outline = FALSE, cex.lab=1.2, horizontal = TRUE)
stars_forks_names <- c("Stars", "Forks") # Grouped boxplot
boxplot(data_final$stars, data_final$forks, names=stars_forks_names, las = 1, outline = FALSE, cex.lab=1.2, horizontal = TRUE) 
loc_names <- c("Total", "R") # Grouped boxplot
boxplot(data_final$loc_total, data_final$loc_r, names=loc_names, las = 1, outline = FALSE, cex.lab=1.2, horizontal = TRUE, margin = list(l = 10, r = 10, b = 0, t = 0))

####################
#     Others       #
####################

# Summaries
summary(data_final$loc_r)
summary(data_final$loc_total)

# Projects without commits
zero_commits <- subset(data, commits == 0)
write.csv(zero_commits, file = "zero_commits.csv")

# Projects without contributors
zero_contributors <- subset(data, newcomers == 0)
write.csv(zero_contributors, file = "zero_contributors.csv")