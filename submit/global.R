library(shiny)
library(shinydashboard)
library(plotly)
library(tidyverse)
library(ggrepel)
library(lubridate)
library(DT)
library(leaflet)
library(readxl)
library(readr)

df <- read_csv("dfR.csv")
actor <- df[,2]
match <- df[,3]
score <- df[,4]

final <- read_csv("final.csv")