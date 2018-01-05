library(likert)

survey <- read.csv(file="actual.csv", head=TRUE, sep=",")

# ---------------------- Q13 -- 14 ----------------------

items <- data.frame(survey$Q13, survey$Q14)

colnames(items) <- c("Your own research", "Research of others")
mylevels <- c("Very important", "Important", "Somewhat important", "Not important", "Not at all important")

for(i in seq_along(items)) {
  items[,i] <- factor(items[,i], levels=mylevels)
}

x <- likert(items)

postscript("q13-14-importance.eps", width=5.3,height=2,horizontal = FALSE, onefile = FALSE, paper = "special")

plot(x, group.order=x$results$Item) + guides(fill=guide_legend("", nrow = 2))

dev.off()


# ---------------------- Q15 ----------------------

items <- data.frame(survey$Q15.10y, survey$Q15.5y, survey$Q15.lastyear)

colnames(items) <- c("10 years ago", "5 years ago","Last year")
mylevels <- c("Much more time", "More time", "Same amount of time", "Less time", "Much less time")

for(i in seq_along(items)) {
  items[,i] <- factor(items[,i], levels=mylevels)
}

x <- likert(items)

postscript("q15-time-dev-sw.eps", width=5.3,height=2.2,horizontal = FALSE, onefile = FALSE, paper = "special")

plot(x, group.order=x$results$Item) + guides(fill=guide_legend("", nrow = 2))

dev.off()

# ---------------------- Q16 ----------------------

items <- data.frame(survey$Q16.self.study, survey$Q16.from.peers, survey$Q16.education.institution, survey$Q16.work)

colnames(items) <- c("Self study", "From peers", "Formal education", "At work")
mylevels <- c("Very important", "Important", "Somewhat important", "Not important", "Not at all important")

for(i in seq_along(items)) {
  items[,i] <- factor(items[,i], levels=mylevels)
}

x <- likert(items)

postscript("q16-learning.eps", width=5.3,height=3.2,horizontal = FALSE, onefile = FALSE, paper = "special")

plot(x, group.order=x$results$Item) + guides(fill=guide_legend("", nrow = 2))

dev.off()

# plot (530, 318)


# ---------------------- Q17 ----------------------

items <- data.frame(survey$Q17.high.school,survey$Q17.undergrad,survey$Q17.grad,survey$Q17.work15y,survey$Q17.work11y,survey$Q17.work6y,survey$Q17.work5y)

colnames(items) <- c("High School", "Undergrad studies", "Grad Studies", "At Work (>15 years)", "At Work (>10 years)", "At Work (>5 years)", "At Work (<5 years)")
mylevels <- c("Very important", "Important", "Somewhat important", "Not important", "Not at all important")

for(i in seq_along(items)) {
  items[,i] <- factor(items[,i], levels=mylevels)
}

x <- likert(items)

postscript("q17-learning-periods.eps", width=5.3,height=3.2,horizontal = FALSE, onefile = FALSE, paper = "special")

plot(x, group.order=x$results$Item) + guides(fill=guide_legend("", nrow = 2))

dev.off()

# plot (530, 318)

# ---------------------- Q18 ----------------------

items <- data.frame(survey$Q18.planning, survey$Q18.reading, survey$Q18.coding, survey$Q18.quality, survey$Q18.packaging, survey$Q18.documenting)


colnames(items) <- c("Planning", "Reading or Reviewing","Coding or Debugging","Quality Assurance" ,"Packaging" ,"Documenting")
mylevels <- c("Never", "Seldom", "Occasionally", "Almost every time", "Every time")

for(i in seq_along(items)) {
  items[,i] <- factor(items[,i], levels=mylevels)
}

x <- likert(items)

postscript("q18-rank.eps", width=5.3, height=3.2,horizontal = FALSE, onefile = FALSE, paper = "special")

plot(x, group.order=x$results$Item) + guides(fill=guide_legend("", nrow = 2))

dev.off()

# plot (530, 318)

# ---------------------- Q20 ----------------------


items <- data.frame(survey$Q20.swreq, survey$Q20.swdesign, survey$Q20.swconstruc, survey$Q20.swver, survey$Q20.swtesting, survey$Q20.swmaint, survey$Q20.swprodmngt, survey$Q20.swprojmngt)


colnames(items) <- c("SW Requirements", "SW Design","SW Construct","SW Verification","SW Testing","SW Maintanance","SW Product Mgmt","SW Project Mgmt")
mylevels <- c("Very important", "Important", "Somewhat important", "Not important", "Not at all important")

for(i in seq_along(items)) {
  items[,i] <- factor(items[,i], levels=mylevels)
}

x <- likert(items)

postscript("q20-how-important.eps", width=5.3, height=3.2,horizontal = FALSE, onefile = FALSE, paper = "special")

plot(x, group.order=x$results$Item) + guides(fill=guide_legend("", nrow = 2))

dev.off()

# plot (530, 318)

# ---------------------- Q21 ----------------------

items <- data.frame(survey$Q21.swreq, survey$Q21.swdesign, survey$Q21.swconstruc, survey$Q21.swver, survey$Q21.swtesting, survey$Q21.swmaint, survey$Q21.swprodmngt, survey$Q21.swprojmngt)

colnames(items) <- c("SW Requirements", "SW Design","SW Construct","SW Verification","SW Testing","SW Maintanance","SW Product Mgmt","SW Project Mgmt")
mylevels <- c("Expert-level understanding", "Understand for the most part", "Novice understanding", "Vague understanding", "No idea what it means")

for(i in seq_along(items)) {
  items[,i] <- factor(items[,i], levels=mylevels)
}

x <- likert(items)

postscript("q21-how-well.eps", width=6.4, height=3.2,horizontal = FALSE, onefile = FALSE, paper = "special")

plot(x, group.order=x$results$Item) + guides(fill=guide_legend("", nrow = 2))

dev.off()
