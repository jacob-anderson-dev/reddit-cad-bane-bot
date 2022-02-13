import praw, random, time

reddit = praw.Reddit(client_id = "47NVbbqqoOMlKvLCfv_4jQ", client_secret = "9iLl5BCaSw4pVieJVund7Cl6X9hvQg", username = "cad-bane-bot", password = "CadBaneB0t", user_agent = "cad-bane-bot") 

cadBaneQuotes = [
    "Tatooine belongs to the Syndicate. As long as the spice keeps running, everyone will be left alone.",
    "Sorry, little lady.",
    "Now all I need's a new hat.",
    "I don't like to hide under a helmet",
    "Nice hat. Where did you get it?",
    "What are you looking at? It's a nice hat.",
    "Hurry up, Jedi, or she dies.",
    "How touching",
    "The rest of you, stay here and defend the bridge.",
    "Young Skywalker. Not so impressive without your lightsaber are you, Jedi?",
    "Well, Hutt, it doesn't look like prison had too adverse an effect on you.",
    "Consider this my final lesson. Look out for yourself. Anything else is weakness.",
    "I'm listening.",
    "This holocron contains information I've been paid to collect. I can't unlock it, but you can. The last Jedi who had it wouldn't open it. I hope you don't make the same mistake.",
    "Kidnapping innocent children? Seems like a small-time crime for the likes of you.",
    "I'm in control. I make the rules now.",
    "I'm kind of tired of being paid for this job, too. But not that tired.",
    "It's not the first time I've broken out of this stinkhole.",
    "Relax. On this slime pool, everybody's an outlaw.",
    "If you're gonna kill him, do it like a man.",
    "Kenobi! I should have known. Something smelled wrong about you from the start.",
    "Reward?! I'll give you a reward when I plug you full of laser bolts!",
    "I've taken down so many clones over the years. Once you figure out one, the rest are easy.",
    "By hook or by crook…you're coming with me.",
    "I knew you were a killer. *gets shanked*",
    "Sure, sure. As long as I get paid, it makes no difference to me",
    "You lack the experience to be goin' up against me.",
    "Oh, I just hate it when somebody does my job.",
    "Cad Bane at your service.",
    "I'm your worst nightmare, pal.",
    "I'd be careful where I was sticking my nose if I were you.",
    "I paid Marshal Vanth a visit. You should've never left him wihtout his armor.",
    "You won't have to worry about Freetown.",
    "Does Fett know that?",
    "I didn't realize the Pyke syndicate was so ruthless.",
    "That all depends on how much your two stomachs can bear.",
    "I think I have an idea how to draw Boba Fett out.",
    "I've already got a job. I'm here to negotiate on behalf of the Pyke syndicate.",
    "I wouldn't be counting on the people of Freetown to be coming anytime soon.",
    "Let the spice move through Mos Espa and all this can be avoided.",
    "You mean the one that massacred your Tusken family and blamed it on a speed bike gang?",
    "Let's do this, right here, right now.",
    "You're going soft in your old age.",
    "I've known you a long time, Boba. One thing I can't figure: What's your angle?",
    "I'm still faster than you. Let's find out.",
    "This isn't the first time I beat you out on a job. There's no shame in it.",
    "Simply open this little box of yours so I can get the information from this crystal and your suffering will come to an end.",
    "Unfortunately, I don't have time to discuss this with you.",
    "Again! Full power!",
    "Good. Step back and shut up.",
    "Next time I will try a different method.",
    "Initiate the self-destruct sequence!",
    "Welcome, Jedi, we've been expecting you.",
    "Let's make this a bit more interesting!",
    "You're not much of a challenge, ugly. I got you right where I want you.",
    "I wouldn't do that, those binders have been specially designed for Jedi.",
    "the more you struggle, the tighter they get.",
    "Impressed now, youngling?",
    "We have time."
]

triggerPhrase = "!cadbane"
subreddit = reddit.subreddit('PrequelMemes') 
for comment in subreddit.stream.comments():
    if triggerPhrase in comment.body.lower():
        randomIndex = random.randint(0, len(cadBaneQuotes) - 1)
        comment.reply(cadBaneQuotes[randomIndex])
        time.sleep(5)