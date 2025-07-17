# import re

# def detect_emotion(text):
#     text = text.lower()

#     emotion_keywords = {
#         "cheerful": [
#             "happy", "glad", "joy", "great", "good", "ecstatic", "peace", "abundance", "gratitude",
#             "wonderful", "excited", "love", "fun", "wish", "win", "won", "lovely", "1st", "over the moon",
#             "rank", "new", "happiness", "cute", "beauty", "kiss", "joyful", "best", "filled", "cloud nine",
#             "smiling", "satisfied", "cheerful", "pleased"
#         ],
#         "sad": [
#             "sad", "cry", "decline", "sadness", "ruin", "tears", "negative", "unhappy", "miserable",
#             "depressed", "alone", "bad", "mourn", "trying", "lonely", "ditch", "break up", "divorce",
#             "dead", "not well", "hospital", "sick", "lost", "lose"
#         ],
#         "angry": [
#             "angry", "furious", "annoyed", "outraged", "mess", "shout", "dare", "slap", "beat", "mad",
#             "rage", "hate", "frustrated", "fuck you", "fuck", "stop", "idiot", "stupid", "kill", "banned", "ban"
#         ],
#         "excited": [
#             "excited", "fab", "fling", "grin", "vacation", "delight", "delighted", "thrilled", "amazing",
#             "awesome", "fantastic", "can't wait", "wow", "wonderful", "beautiful", "pretty"
#         ],
#         "fearful": [
#             "scared", "help!", "sweat", "ice", "disbelief", "terror", "dread", "faint", "frighten",
#             "frightened", "crime", "horrified", "petrified", "terrify", "horrify", "anxiety", "anxious",
#             "terrific", "horrific", "afraid", "panicked", "fear", "nervous", "worried", "horror"
#         ],
#         "friendly": [
#             "hi", "hello", "thanks", "light", "please", "polite", "respectful", "could", "wondering",
#             "kind", "kindness", "helped", "sure", "okay", "hey", "smile", "positive", "sweet", "good",
#             "morning", "nice", "hug"
#         ]
#     }

#     scores = {emotion: 0 for emotion in emotion_keywords}
#     for emotion, keywords in emotion_keywords.items():
#         for kw in keywords:
#             matches = len(re.findall(rf"\b{re.escape(kw)}\b", text))
#             scores[emotion] += matches

#     if all(score == 0 for score in scores.values()):
#         return "neutral"

#     return max(scores, key=scores.get)









import re

def detect_emotion(text):
    text = text.lower()

    emotion_keywords = {
        "cheerful": [
            "happy", "glad", "joy", "great", "good", "ecstatic", "peace", "abundance", "gratitude",
            "wonderful", "excited", "love", "fun", "wish", "win", "won", "lovely", "1st", "over the moon",
            "rank", "new", "happiness", "cute", "beauty", "kiss", "joyful", "best", "filled", "cloud nine",
            "smiling", "satisfied", "cheerful", "pleased"
        ],
        "sad": [
            "sad", "cry", "decline", "sadness", "ruin", "tears", "negative", "unhappy", "miserable",
            "depressed", "alone", "bad", "mourn", "trying", "lonely", "ditch","broke","hunger","miss you","missed", "break up", "divorce",
            "dead", "not well", "hospital", "sick", "lost", "lose","hurt","deeply","depromote","depromoted","expired","demise","tears"
        ],
        "angry": [
            "angry", "furious", "annoyed", "outraged", "mess", "shout", "dare", "slap", "beat", "mad",
            "rage", "hate", "frustrated","be lazy", "fuck you", "fuck", "stop", "idiot", "stupid", "kill", "banned", "ban","war","fight","fought"
        ],
        "excited": [
            "excited", "fab", "fling", "grin", "vacation", "delight", "delighted", "thrilled", "amazing",
            "awesome", "fantastic", "can't wait", "wow", "wonderful","promoted","promotion","thrilling","thrill","head over heels","birthday" "beautiful", "pretty"
        ],
        "fearful": [
            "scared", "help!", "sweat", "ice", "disbelief", "terror", "dread", "faint", "frighten",
            "frightened", "crime", "horrified", "petrified", "terrify", "horrify", "anxiety", "anxious",
            "terrific", "horrific", "afraid", "panicked", "fear", "nervous", "worried", "horror", "run", "ran","ghost", "devil","evil"
        ],
        "friendly": [
            "hi", "hello", "thanks", "light", "please", "polite", "respectful", "could", "wondering","positive","healthy"
            "kind", "kindness", "helped", "sure", "okay", "hey", "smile", "positive", "sweet", "good","for you",
            "morning", "nice", "hug", "understand","understanding","listen","listening","man","woman","men","say","thank you","chuckle"
        ]
    }

    scores = {emotion: 0 for emotion in emotion_keywords}
    
    
    for emotion, keywords in emotion_keywords.items():
        for kw in keywords:
            matches = len(re.findall(rf"\b{re.escape(kw)}\b", text))
            scores[emotion] += matches

    
    if all(score == 0 for score in scores.values()):
        return "neutral"

    
    return max(scores, key=scores.get)



# import spacy
# import re

# # Load spaCy English model once globally
# nlp = spacy.load("en_core_web_sm")

# def lemmatize_text(text):
#     doc = nlp(text.lower())
#     # Keep lemmas of words that are not punctuation or spaces
#     lemmas = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
#     return lemmas  # return list of lemmas for easier matching

# def detect_emotion(text):
#     lemmas = lemmatize_text(text)

#     emotion_keywords = {
#         "cheerful": [
#             "happy", "glad", "joy", "great", "good", "ecstatic", "peace", "abundance", "gratitude",
#             "wonderful", "excited", "love", "fun", "wish", "win", "lovely", "1st", "over the moon",
#             "rank", "new", "happiness", "cute", "beauty", "kiss", "joyful", "best", "filled", "cloud nine",
#             "smiling", "satisfied", "cheerful", "pleased","proud","accomplished","celebrate","celebration","perfect","light up","good news", "looking forward","look forward","so full"
#         ],
#         "sad": [
#             "sad", "cry", "decline", "sadness", "ruin", "tears", "negative", "unhappy", "miserable","anymore",
#             "slip away","slipping away","walking away","walked away","gone","silence","alone","I smile","tried so hard","never enough",
#             "depressed", "alone", "bad", "mourn", "trying", "lonely", "ditch", "broke", "hunger", "miss you", "missed", "break up", "divorce",
#             "dead", "not well", "hospital", "sick", "lost", "lose", "hurt", "deeply", "depromote", "depromoted", "expired", "demise", "tears"
#         ],
#         "angry": [
#             "angry", "furious", "annoyed", "outraged", "mess", "shout", "dare", "slap", "beat", "mad","mess","stay away","stay out","never","ruined","cross the line","crossed the line","dont","behind my back","do you","I'm done",
#             "rage", "hate", "frustrated", "be lazy", "fuck you", "fuck", "stop", "idiot", "stupid", "kill", "banned", "ban", "war","not to", "fight", "fought","my patience","have patience"
#         ],
#         "excited": [
#             "excited", "fab", "fling", "grin", "vacation", "delight", "delighted", "thrilled", "amazing","trip","exactly","won","new","favorite","celebrity","let's go","ever","guess what",
#             "awesome", "fantastic", "can't wait", "wow", "wonderful", "promoted", "promotion", "thrilling", "thrill", "head over heels", "birthday", "beautiful", "pretty"
#         ],
#         "fearful": [
#             "scared", "help!", "sweat", "ice", "disbelief", "terror", "dread", "faint", "frighten","please help","dont think", "please save","help me","creepy","creeps","don't leave",
#             "frightened", "crime", "horrified", "petrified", "terrify", "horrify", "anxiety", "anxious","someone is following","what if","panicking","alive","bad feeling","you hear","can you hear","i can hear","heard some"
#             "terrific", "horrific", "afraid", "panicked", "fear", "nervous", "worried", "horror", "run", "ran", "ghost", "devil", "evil","can't breathe"
#         ],
#         "friendly": [
#             "hi", "hello","hey", "thanks", "light", "please", "polite","nice talking","nice meeting","to meet","let me know", "respectful", "could", "wondering", "positive", "healthy",
#             "kind", "kindness", "helped", "sure", "okay", "helping me","hey", "smile", "positive", "sweet", "good","hope",
#             "morning", "nice", "hug","hang out","be fun","coffee","believe you","believe in you","great friend","feel free","great job","good job","impressed", "understand", "understanding", "listen", "listening", "man", "woman", "men", "thank you", "chuckle"
#         ]
#     }

#     # Flatten lemmas into a single string for phrase matching
#     text_str = " ".join(lemmas)

#     scores = {emotion: 0 for emotion in emotion_keywords}

#     for emotion, keywords in emotion_keywords.items():
#         for kw in keywords:
#             # Lemmatize keyword phrase as well for consistent matching
#             kw_lemmas = lemmatize_text(kw)
#             kw_str = " ".join(kw_lemmas)
#             # Count how many times the keyword phrase appears in the text (word boundary aware)
#             pattern = re.compile(rf"\b{re.escape(kw_str)}\b")
#             matches = len(pattern.findall(text_str))
#             scores[emotion] += matches

#     if all(score == 0 for score in scores.values()):
#         return "neutral"

#     return max(scores, key=scores.get)

