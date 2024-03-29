data2 <- read.csv("../data2.csv")
dim(data2)

result2 <- matrix(0, nrow = 104, ncol = 2)
for (i in 2:104) {
    # calculate sum of sm
    sum_sm <- 0
    for (m in 1:(i - 1)) {
        for (j in 1:m) {
            sum_sm <- sum_sm + data2[j, 2]
        }
    }

    # Calculate si
    si <- 0
    for (j in 1:i) {
        si <- si + data2[j, 2]
    }

    print(i)

    # calculate final result
    result2[i, 2] <- (1 / (i - 1) * sum_sm - si / 2) / (si * sqrt(1 / (12 * (i - 1))))
}

plot(1:104, result2[, 2], type = "p", main = "Laplace Trend Test", ylab = "Calculated value of u(i)", xlab = "failure")
abline(h = 1.96)
abline(h = -1.96)
text(70, 1.96, pos = 3, labels = "upper bound")
text(70, -1.96, pos = 1, labels = "lower bound")
