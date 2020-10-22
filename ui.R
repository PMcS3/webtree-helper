library(shiny)
library(sortable)
library(DiagrammeR)

ui <- fluidPage(
  
  # Application title
  titlePanel("Old Faithful Geyser Data"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 1,
                  max = 50,
                  value = 30)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      # plotOutput("distPlot")
      grViz("
                digraph boxes_and_circles {
                    node [shape = circle]
                    A; B; C; D; E; F
                    
                    node [shape = box]
                    1; 2; 3; 4; 5; 6; 7; 8
                    
                    A->1; B->2; B->3; B->4; C->A;
                }
            ")
    )
  )
)