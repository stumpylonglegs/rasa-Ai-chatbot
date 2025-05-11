Steps to use rasa 


1. when using visule studio code have 2 terminals open
2. in 1 terminal run the command "rasa run actions"
3. in the other terminal if you have made changes delete the old model and retrain the model with "rasa train"

Next, if you want to run chatbot through console, follow the console steps, otherwise, follow the GUI steps

For console:
4. after training and to run rasa use "rasa shell" in a separate terminal

For GUI:
4. run command < rasa run -m models --enable-api --cors "*" > in a separate terminal
5. Open Index.html (located inside Frontend folder) in a browser (on vscode you can do this by right-clicking on the file and choosing 'run live server')
