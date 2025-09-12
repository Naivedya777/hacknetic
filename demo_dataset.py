# -------------------------
# Demo Dataset of Apps
# -------------------------

# Instagram comments (toxic)
comments_instagram = [
    "You are so stupid and disgusting",
    "This influencer is fake and a fraud",
    "Ugly content, I hate this",
    "Stop posting trash, loser",
    "Idiot, nobody likes you"
]

# Discord comments (mixed safe + toxic)
comments_discord = [
    "Great game tonight, loved the team!",
    "You noob, shut up idiot",
    "Thanks for helping me with the quest",
    "That boss fight was awesome",
    "Dumb move bro, but still fun"
]

# Reddit comments (toxic debate style)
comments_reddit = [
    "This is the dumbest opinion I’ve ever seen",
    "Stop being such a jerk",
    "I disagree but thanks for sharing",
    "You’re a disgusting troll",
    "Interesting perspective, I learned something"
]

# Women-only forum comments (positive / safe)
comments_forum = [
    "This community is so supportive and kind",
    "Thank you all for helping me feel safe",
    "I found amazing resources here",
    "You are all inspiring women",
    "Love the positivity in this space"
]

# WhatsApp group comments (family/friends, mostly safe)
comments_whatsapp = [
    "Happy birthday sis, we love you!",
    "Stop being so annoying",
    "Thanks for the recipe, it was delicious",
    "You’re acting dumb again",
    "Best family ever ❤"
]

# Combine into dataset
apps_dataset = {
    "Instagram": comments_instagram,
    "Discord": comments_discord,
    "Reddit": comments_reddit,
    "Women Forum": comments_forum,
    "WhatsApp": comments_whatsapp
}