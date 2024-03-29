library(ggplot2)

calculateAndPlotLaplaceTrend <- function(dataFrame, dataSetName) {
    # Initialize the results matrix
    resultsMatrix <- matrix(nrow = nrow(dataFrame), ncol = 2)
    
    # Calculation loop
    for (index in 2:nrow(dataFrame)) {
        # Calculate the trend value
        cumulativeSum <- sum(dataFrame[1:index, 2])
        # Calculate the partial cumulative sum
        partialCumulativeSum <- sum(sapply(2:(index-1), function(m) sum(dataFrame[1:m, 2])))
        # Store the trend value in the results matrix
        resultsMatrix[index, 2] <- ((1/(index-1))*partialCumulativeSum - cumulativeSum/2)/(cumulativeSum*sqrt(1/(12*(index - 1))))
    }
    
    # Define filename for plots
    generatePlotFilename <- function(extension) paste0(dataSetName, "_LaplaceTrend.", extension)
    
    # Save plot as EPS to be used in LaTeX
    postscript(generatePlotFilename("eps"), horizontal = FALSE, onefile = FALSE, paper = "special", height = 6, width = 6)
    generatePlot(resultsMatrix, dataSetName)
    dev.off()
    
    # Save plot as PNG for human viewing
    png(generatePlotFilename("png"), width = 480, height = 480)
    generatePlot(resultsMatrix, dataSetName)
    dev.off()
}

generatePlot <- function(trendResults, titleName) {
    plot(1:nrow(trendResults), trendResults[, 2], type = "o", col = "blue", xlab = "Index", ylab = "Trend Value",
        main = paste("Laplace Trend Test for", titleName))
    abline(h = c(1.96, -1.96), col = "gray60")
}

data1 <- read.csv("../data1.csv")
data2 <- read.csv("../data2.csv")

# Perform the calculation and plotting for each dataset
calculateAndPlotLaplaceTrend(data1, "Data1")
calculateAndPlotLaplaceTrend(data2, "Data2")
