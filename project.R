

a <- function(c_name , n_days , chart){
  
  #getting data from csv file 
  first = "C:/Users/raj rathod/Downloads/archive/v1/"
  c = c_name
  last = ".NS.csv"
  path = paste(first , c , last ,sep="")
  dat<- read.csv(path)
  
  #change the date format
  
  dat = head(dat , n_days)
  r = dat$Date
  dat$Date = substring(r ,first=6,last=10)
  
  
  if(chart == "bar"){
    ggplot(dat , aes( Date,High))+
      geom_bar(stat = "identity" , fill= "blue" , alpha = 0.5 )
    
  }
  if(chart == "line"){
    
    fig <- plot_ly(data = dat, x = ~Date, y = ~High, type = 'scatter', mode = 'lines')%>%
      layout(
        plot_bgcolor='#e5ecf6',
        title = "Apple Stock Price")
    fig
  }
  
  if (chart == "candle"){
    f <- dat %>%
      plot_ly(x = ~Date, type = "candlestick",
              open = ~Open, close = ~Close,
              high = ~High, low = ~Low)
    print(f)
  }
  
  if (chart == "ohlc"){
    f <- dat %>%
      plot_ly(x = ~Date, type = "ohlc",
              open = ~Open, close = ~Close,
              high = ~High, low = ~Low)
    print(f)
  }
  
}
a(c_name , n_data , chart)
{
  c_name = readline(prompt = "enter comapny name :- ")
  n_data = as.numeric(readline(prompt = "how many days of data you want :- "))
  chart = readline(prompt =  "enter type of chart (candle , ohlc , line , bar ) :- ")
  
}


