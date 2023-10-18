library(deSolve)
library(rootSolve)
library(coda)
library(FME)
library(Grind)

# model A1
modelA1 <- function(t, state, parms) {
  with(as.list(c(state,parms)), {
    dn <- -n/ts
    return(list(c(dn)))
  })
}
ts=100
p <- c(ts=ts) 
s <- c(n=.1) 
data=run(odes=modelA1,tmax=200,method="euler",tstep=.1,after="state=state+ .7 * sqrt(2/ts)*rnorm(1,0,1)",timeplot=F,table=T)
plot(data[,2],type='l')
print(sd(data[,2]))

# model 2 
model2 <- function(t, state, parms) {
  with(as.list(c(state,parms)), {
    dn <- -n/taus
    dX <- (-4*X*(X^2-1) -2*ga*(X-1) -2*gb*(X+1))/ts + n # X is delta r
    return(list(c(dn,dX)))
  })
}
p <- c(ts=10,ga=.1,gb=.1, taus=100) 
s <- c(n=0,X=.1) 
data=run(odes=model2,tmax=5000,method="euler",tstep=.1,after="state[1]=state[1]+ .7 * sqrt(2/100)*rnorm(100,0,1)",timeplot=F,table=T)
plot(data[,1],data[,3],type='l')
plot(data[,1],sign(data[,3]),type='l')
mean(rle(sign(data[,3]))$lengths/100) # in 10ms

##########
## Appendix B: Rate-Based Models
# Model with direct cross-inhibition - model B1
modelB1 <- function(t, state, parms) {
  with(as.list(c(state,parms)), {
    dn <- -n/100
    dX <- (-4*X*(X^2-1) -2*ga*(X-1) -2*gb*(X+1))/ts + n # X is delta r
    return(list(c(dn,dX)))
  })
}

# Model with inhibition driven indirectly by an excitatotry pool and weak adaptation - model ?
# linear thresholding
data=run(odes=model?,method="euler",tstep=.1,after="state=state+ .7 * sqrt(2/ts)*rnorm(1,0,1);state[1]=max(0,state[1])",timeplot=F,table=T))




  

