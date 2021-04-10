function(input, output) { 
    output$preImage <- renderImage({
        filename <- normalizePath(file.path('./www',
                                            paste(input$actor, '.jpeg', sep='')))
        
        list(src = filename,
             alt = input$actor)
        
    }, deleteFile = FALSE)
    
    output$text <- renderText({
        text <- input$actor
    })
    
    
    output$imageB <- renderImage({
        for (i in 1:128){
            if (input$actor == df[i,2])
            {match = df[i,3]}
        }
        
        filename <- normalizePath(file.path('./www',
                                            paste(match, '.jpeg', sep='')))
        
        list(src = filename,
             alt = match)
        
    }, deleteFile = FALSE)
    
    output$textmatch <- renderText({
        for (i in 1:128){
            if (input$actor == df[i,2])
            {match = df[i,3]}
        }
        text = toString(match)
    })
    
    output$Score <- renderValueBox({
        for (i in 1:128){
            if (input$actor == df[i,2])
            {score = toString(round(df[i,4]*100, 2))}
        }
        
        valueBox(
            score, "Chemistry Score", icon = icon("percentage"),
            color = "purple"
        )
    })
    
    output$count <- renderValueBox({
        for (i in 1:128){
            if (input$actor == df[i,2])
            {count = toString(df[i,5])}
        }
        
        valueBox(
            count, "Number of reviews analysed", icon = icon("list"),
            color = "blue"
        )
    })
    
    output$highlow <- renderValueBox({
        for (i in 1:128){
            if (input$actor == df[i,2])
            {score = round(df[i,4]*100, 2)}
        }
        
        
        if (score>=30)
        {valueBox(
            value = "High Chemistry", subtitle = "High/Low", icon = icon("check"),
            color = "green"
        )}
        
        else
        {valueBox(
            value = "Low Chemistry", subtitle = "High/Low", icon = icon("times"),
            color = "red"
        )}   
        
    })
}