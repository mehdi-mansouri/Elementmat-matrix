# Elementmat-matrix
Bitte nutzen Sie Master-Braunch<br>
Bitte Installieren zuerst fogende <br><br><br>

    python3 -m venv env 
    source env/bin/activate
    pip install matrix-nio
oder können Sie unter Link finden :
https://matrix.org/docs/guides/usage-of-matrix-nio<br>
Sie sollten auch Ihre Account information (Username  and password) in Zeile 11,12,20,22 hinzufügen<br><br><br>

     client = AsyncClient("https://matrix.org", "YOUR_USER_NAME")
        await client.login("YOUR_PASSWORD")
Wenn Sie Hallo schicken mit Ihrem Account ,erhalten Sie Antwort "Hallo,was kann ich für Sie tun?"<br>
        
