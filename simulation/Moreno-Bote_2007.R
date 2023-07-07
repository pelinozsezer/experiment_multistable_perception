
library(deSolve)
library(rootSolve)
library(FME)
library(Grind)

modelA1 <- function(t, state, parms) {
  with(as.list(c(state,parms)), {
    dn <- -n/ts
    return(list(c(dn)))
  })
}
ts=100
p <- c(ts=ts) # parameter r
s <- c(n=.1) # initial value
data=run(odes=modelA1,tmax=200,method="euler",tstep=.1,after="state=state+ .7 * sqrt(2/ts)*rnorm(1,0,1)",timeplot=F,table=T)
plot(data[,2],type='l')
print(sd(data[,2]))

model2 <- function(t, state, parms) {
  with(as.list(c(state,parms)), {
    dn <- -n/100
    dX <- (-4*X*(X^2-1) - 2*ga*(X-1)-2*gb*(X+1))/ts + n
    return(list(c(dn,dX)))
  })
}
p <- c(ts=10,ga=.1,gb=.1) # parameter r
s <- c(n=0,X=.1) # initial value
data=run(odes=model2,tmax=5000,method="euler",tstep=.1,after="state[1]=state[1]+ .7 * sqrt(2/100)*rnorm(1,0,1)",timeplot=F,table=T)
plot(data[,1],data[,3],type='l')
plot(data[,1],sign(data[,3]),type='l')
mean(rle(sign(data[,3]))$lengths/100) # in 10ms
  

