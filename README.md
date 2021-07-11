## Inspiration
We were inspired by the [Who's That Pokemon](https://cdn.vox-cdn.com/thumbor/KtqpDNPD586DmxLw1HzH6PVlUDg=/0x0:1920x1080/1400x1050/filters:focal(807x387:1113x693):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/53254027/who_pokemon.0.jpg) bit that appears right before and after commercial breaks from Pokemon. Our first conversation was a shared interest in the show and the impact it had on us during our childhood. However, we wanted to modify the idea in a way that was unique to us. After talking about it a little more, we came up with the idea of AniMatch.

## What it does
AniMatch is a guessing game that incorporates a variety of popular anime characters. The user is given a very blurred image of a random anime character. Furthermore, they are given four options. Over time, the image will become less and less blurred. The objective of the game is to correctly identify the anime character as quickly as they can. The faster the user pinpoints a character, the more points they get. However, the user needs to be careful. One incorrect answer and the game is over. 

## How we built it
AniMatch is a full-stack web application. The backend is a RESTful API that was built in Flask using the Flask-RESTful and Flask-CORS extensions. Images were processed using a combination of OpenCV and Pillow, applying changes to image saturation and pixelation. The front end was built using REACT.js. Additionally, Axios was used in the frontend to make cleaner calls to the API. The back-end is hosted on PythonAnywhere, and the front-end is hosted on Netlify. 

## What's next for AniMatch
There are several features that we didn't have enough time to implement, leaving us a lots of things we can add! We're planning on adding even more characters to our system, a stored online leaderboard with the highest scores, and a system to prevent cheating through the use of bots. After that, we'd like to generate revenue from AniMatch, potentially including custom "guess packs" from subscriptions or advertisements.  
