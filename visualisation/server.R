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
        for (i in 1:48){
            if (input$actor == df[i,2])
            {match = df[i,3]}
        }
        
        filename <- normalizePath(file.path('./www',
                                            paste(match, '.jpeg', sep='')))
        
        list(src = filename,
             alt = match)
        
    }, deleteFile = FALSE)
    
    output$textmatch <- renderText({
        for (i in 1:48){
            if (input$actor == df[i,2])
            {match = df[i,3]}
        }
        text = toString(match)
    })
    
    output$Score <- renderValueBox({
        for (i in 1:48){
            if (input$actor == df[i,2])
            {score = toString(round(df[i,4]*100, 2))}
        }
        
        valueBox(
            score, "Chemistry Score", icon = icon("percentage"),
            color = "purple"
        )
    })
    
    output$count <- renderValueBox({
        for (i in 1:48){
            if (input$actor == df[i,2])
            {count = toString(df[i,5])}
        }
        
        valueBox(
            count, "Number of reviews analysed", icon = icon("list"),
            color = "blue"
        )
    })
    
    output$highlow <- renderValueBox({
        for (i in 1:48){
            if (input$actor == df[i,2])
            {score = round(df[i,4]*100, 2)}
        }
        
        
        if (score>=42.2)
        {valueBox(
            value = "High Chemistry", subtitle = "High/Average/Low", icon = icon("check"),
            color = "green"
        )}
        
        else if (score<=24.6)
        {valueBox(
            value = "Low Chemistry", subtitle = "High/Average/Low", icon = icon("times"),
            color = "red"
        )}
        
        else
        {valueBox(
            value = "Average Chemistry", subtitle = "High/Average/Low", icon = icon("minus"),
            color = "yellow"
        )} 
        
    })
    
    output$text1 <- renderText({
        text <- input$newcomer
    })
    
    
    output$newimage <- renderImage({
        filename <- normalizePath(file.path('./www',
                                            paste(input$newcomer, '.jpeg', sep='')))
        
        list(src = filename,
             alt = input$newcomer)
        
    }, deleteFile = FALSE)
    
    output$newsimilarface <- renderImage({
        for (i in 1:54){
            if (input$newcomer == final[i,2])
            {match = final[i,4]}
        }
        
        filename <- normalizePath(file.path('./www',
                                            paste(match, '.jpeg', sep='')))
        
        list(src = filename,
             alt = match)
        
    }, deleteFile = FALSE)
    
    output$text2 <- renderText({
        for (i in 1:54){
            if (input$newcomer == final[i,2])
            {match = final[i,4]}
        }
        text = toString(match)
    })
    
    
    output$facialscore <- renderValueBox({
        for (i in 1:54){
            if (input$newcomer== final[i,2])
            {score = toString(round(final[i,5], 2))}
        }
        
        valueBox(
            score, "Facial Similarity Score", icon = icon("percentage"),
            color = "purple"
        )
    })
    
    output$highlowmid <- renderValueBox({
        for (i in 1:54){
            if (input$newcomer == final[i,2])
            {score = round(final[i,5], 2)}
        }
        
        
        if (score>=73.8)
        {valueBox(
            value = "High Facial Similarity", subtitle = "High/Average/Low", icon = icon("check"),
            color = "green"
        )}
        
        else if (score<=64.6)
        {valueBox(
            value = "Low Facial Similarity", subtitle = "High/Average/Low", icon = icon("times"),
            color = "red"
        )}
        
        else
        {valueBox(
            value = "Avg Facial Similarity", subtitle = "High/Average/Low", icon = icon("minus"),
            color = "yellow"
        )} 
        
    })
    
    output$static <- renderValueBox({
        valueBox(
            value = "Cosine Similarity", subtitle = "Metric used", icon = icon("sort-numeric-up"),
            color = "blue")})
        
    
    
    output$text3 <- renderText({
        text <- input$newcomer
    })
    
    
    output$newimage2 <- renderImage({
        filename <- normalizePath(file.path('./www',
                                            paste(input$newcomer, '.jpeg', sep='')))
        
        list(src = filename,
             alt = input$newcomer)
        
    }, deleteFile = FALSE)
    
    
    output$imagematch1<- renderImage({
        for (i in 1:54){
            if (input$newcomer == final[i,2])
            {match = final[i,4]}
        }
        
        for (j in 1:48)
        {if (match == df[j,2])
        {matchnew = df[j,3]}
            
        }
        
        filename <- normalizePath(file.path('./www',
                                            paste(matchnew, '.jpeg', sep='')))
        
        list(src = filename,
             alt = matchnew)
        
    }, deleteFile = FALSE)
    
    
    output$text4 <- renderText({
        for (i in 1:54){
            if (input$newcomer == final[i,2])
            {match = final[i,4]}
        }
        
        for (j in 1:48)
        {if (match == df[j,2])
        {matchnew = df[j,3]}
            
        }
        
        text = toString(matchnew)
    })
    
    output$matching <- renderInfoBox({
        
        for (i in 1:54){
            if (input$newcomer == final[i,2])
            {match = final[i,4]}
        }
        
        for (j in 1:48)
        {if (match == df[j,2])
        {matchnew = df[j,3]}
            
        }
        
        textA = toString(input$newcomer)
        textB = toString(matchnew)
        
        infoBox(
            "Potential Pairing", paste0(textA, " X ", textB), icon = icon("film"),
            color = "black"
        )
    })
    
    
    
    
    
}