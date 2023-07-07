library(colorRamps)
library(colorspace)
library(beepr)
library(magick)


n=8

m=matrix(0,n^2,2)
shift=matrix(0,n^2,2)
  for(i in 1:n)
    for(j in 1:n)
    {
      # shifti=ifelse(i%%2==1,-shiftii,shiftii)
      # shiftj=ifelse(j%%2==1,-shiftjj,shiftjj)
      # shift[n*(i-1)+j,]=c(shifti,shiftj)
      m[n*(i-1)+j,]=c(i,j)
    }

m=m/(n+1)

x=matrix(c(T,F),n+1,n)[-(n+1),]
x=as.vector(x)

y=!x

mask=matrix(F,n,n)
mask[c(.5*n,.5*n-1),]=T
mask=as.vector(mask)

# x=x&mask
# y=y&mask


p=seq(-1,1,length=.5*n)
posx=matrix(rep(p,each=2),n,n,byrow = T)*matrix(rep(c(-1,1),each=n),n,n)
posy=matrix(rep(p,each=2),n,n,byrow = T)*matrix(rep(c(1,-1)),n,n)

pos=cbind(as.vector(posx),as.vector(posy))
pos=pos/400



shiftii=.01
shiftjj=.01

shift=cbind(rep(c(shiftii,-shiftii),each=n,times=.5*n),rep(c(shiftjj,-shiftjj),each=1,times=n^2/2))

par(bg='black')
plot((m+shift+pos)[x,],col='grey',cex=.5,xlim=0:1,ylim=c(0,max(m)+min(m)),pch=19,axes=F,bty='n')

col=rep(1:(n),each=2)
col='white'
cex=2
iteration=0
ii=2
for(i in 1:ii)
  {
  iteration=iteration+1
   png(paste0("plots/pngplots_",1000+iteration,".png"),
      width=9,height=9,units="in",res=200)
  
  par(bg='black')
  plot(m[y,]+shift[y,]+pos[y,],col=col,cex=cex,xlim=0:1,ylim=0:1,pch=19,axes=F,bty='n',xlab='',ylab='')
#  Sys.sleep(.1)
   dev.off()
   iteration=iteration+1
   png(paste0("plots/pngplots_",1000+iteration,".png"),
       width=9,height=9,units="in",res=200)

 par(bg='black')
  plot(m[x,]+shift[x,]+pos[x,],col=col,cex=cex,xlim=0:1,ylim=0:1,pch=19,axes=F,bty='n',xlab='',ylab='')
  #Sys.sleep(.1)
   dev.off()
  }


list.files(path=paste0("plots/"), pattern = '*.png', full.names = TRUE) %>%
  image_read() %>% # reads each path file
  image_join() %>% # joins image
  image_animate(fps=4,loop=0) %>% # animates, can opt for number of loops
  image_write(paste0("plots/Anim.gif")) # write to current dir

beep(2)
