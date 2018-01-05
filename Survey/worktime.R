survey <- read.csv(file="actual.csv", head=TRUE, sep=",")

x <- sub("%", "", survey$Q10.work.time)
x <- x[x != ""]
x <- as.numeric(x)

h <- hist(x, col="red", main="working hours", ylab="# of respondents", xlab="% of working hours", breaks=10, xlim=c(0,100), ylim=c(0,500))
rug(jitter(x))

xfit<-seq(min(x),max(x),length=40)
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x))
yfit <- yfit*diff(h$mids[1:2])*length(x)
lines(xfit, yfit, col="black", lwd=2)

# 380 x 340
