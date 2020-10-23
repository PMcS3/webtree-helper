processData <- function(dataFile) {
  rawData <- read_csv(dataFile)
  return(rawData)
}

classTable <- read_csv("Open Classes.csv")
