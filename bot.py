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
    "I knew you were a killer.",
    "Sure, sure. As long as I get paid, it makes no difference to me",
    "You lack the experience to be goin' up against me.",
]

triggerPhrase = "!cadbane"
subreddit = reddit.subreddit('PrequelMemes') 
for comment in subreddit.stream.comments():
    if triggerPhrase in comment.body.lower():
        randomIndex = random.randint(0, len(cadBaneQuotes) - 1)
        comment.reply(cadBaneQuotes[randomIndex])
        time.sleep(5)