import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='1BvuBw3OHLZfrA',
                     client_secret='n9NIg5jCaGaEOydxHMXOMf3_kqA',
                     user_agent='lebriones'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
   submission = reddit.submission(url=url)
   submission.comments.replace_more()

   return submission.comments

def process_comments(neg,pos,neu,comments):
   for comment in comments:
      positive = get_text_positive_proba(comment.body)
      neutral = get_text_neutral_proba(comment.body)
      negative = get_text_negative_proba(comment.body)
      #add to positive list if its more positive than anything else
      if (positive > neutral and positive > negative):
         pos.append(comment.body)
         #add to neutral list if its more neutral than anything else
      elif(neutral > positive and neutral > negative):
         neu.append(comment.body)
      #add to negative list if its more positive than anything else
      elif(negative > positive and negative > neutral):
         neg.append(comment.body)
      process_comments(neg, pos, neu, comment.replies)
   return neg, pos, neu

def main():
   comments = get_submission_comments('https://www.reddit.com/r/science/comments/e92tzy/psychopathic_individuals_have_the_ability_to/')
   #print(comments[0].body)
   #print(comments[0].replies[3].body)

   neg = []
   pos = []
   neu = []
   process_comments(neg, pos, neu, comments)
   print("Negative comment: ", neg[0], '\n')
   print("Positive comment: ", pos[0], '\n')
   print("Neutral comment: ", neu[0], '\n')
   print(len(neg))
   print(len(pos))
   print(len(neu))
main()
