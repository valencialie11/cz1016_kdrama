library(shiny)
library(shinydashboard)

dashboardPage(skin = "purple",
    dashboardHeader(title = "Actor Matcher",
                    dropdownMenu(type = "messages",
                                 messageItem(
                                     from = "Database",
                                     message = "More actors and actresses are added!",
                                     icon = icon("database")
                                 ),
                                 messageItem(
                                     from = "New User",
                                     message = "Subscribe for daily K-drama news!"
                                 ),
                                 messageItem(
                                     from = "Support",
                                     message = "Email us at actormatcher@abc.com",
                                     icon = icon("life-ring")
                                 )
                    ),
                    dropdownMenu(type = "notifications",
                                 notificationItem(
                                     text = "5 new subscribers this week!",
                                     icon("users")
                                 ),
                                 notificationItem(
                                     text = "20 matchings made today!",
                                     icon("chart-line"),
                                     status = "success"
                                 )
                    )),
    dashboardSidebar(sidebarMenu(
        menuItem("Matching", tabName = "predict", icon = icon("question")),
        menuItem("New actors?", tabName = "new", icon = icon("question")),
        menuItem("Subscription", icon = icon("users"), tabName = "subscribe",
                                  badgeLabel = "new", badgeColor = "green"))),
    dashboardBody(tabItems(
        tabItem(tabName = 'predict',
                h3("Are you a very confused K-drama director who doesn't know which actor-actress pairing is best for your upcoming blockbuster? Or are you just an avid K-drama watcher who is curious which actress suits your favourite actor?
                   You have come to the right place!"
                ,style = "font-family: 'times'; font-si16pt", align = 'center'),
                h3("We employed the best machine learning algorithms out there to best pair actors and actresses by their on-screen chemistry, by analysing thousands and thousands of reviews.",style = "font-family: 'times'; font-si16pt", align = 'center'),
                br(),
                h3("What are you waiting for? Go on and try!",style = "font-family: 'times'; font-si16pt", align = 'center'),
                br(),
                br(),
                br(),
                fluidRow(
                    box(width = 3, title = "Choose an actor/actress:", background = "black", height = "120px", selectInput(inputId = "actor",
                                                                                                          label = "", choices = actor$actor, selected = "AhnHyoSeop")),
                    box(width = 4, title = textOutput(outputId = "text"), height = "500px", imageOutput(outputId = "preImage"), align = 'center'),
                    box(width = 4, title = textOutput(outputId = "textmatch"), height = "500px", imageOutput(outputId = "imageB"), align = 'center')
                    ),
                box(width = 12, valueBoxOutput("Score"), valueBoxOutput("count"), valueBoxOutput("highlow")),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br()),
        tabItem(tabName = 'new',
                h3("What about new actors? Can we still match them to a potential actor/actress?"
                   ,style = "font-family: 'times'; font-si16pt", align = 'center'),
                h3("Of course! We analysed hundreds of photos of these actors and actresses and compare their similarity in features. 
                   It is true that similarity in facial features does not equal to chemistry, but it is the only thing that we are able to quantify and compare as a cold start. 
                   Perhaps with this analysis, we can allow more unexpected pairings to happen and unexpectedness is not always a bad thing! ",style = "font-family: 'times'; font-si16pt", align = 'center'),
                br(),
                br(),
                br(),
                br(),
                fluidRow(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                br()),
        tabItem(tabName = "subscribe",
                h2("Subscribe to our email for the latest K-drama news!", align = "center", style = "font-family: 'times'; font-si16pt"),
                br(),
                br(),
                br(),
                br(),
                br(),
                br(),
                textInput(inputId = "email", label = "Email address:"),
                passwordInput(inputId = "password", label = "Password:"), align = "center",
                actionButton(inputId = "done", label = "Done")
        )
    ))
    
    
    
    
    
    )


