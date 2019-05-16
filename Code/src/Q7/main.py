from Q7 import learner, parser

FILENAME = 'data\\spam.data'

def main():

    spam_parser = parser.Parser(FILENAME)
    spam_parser.clean_df()
    spam_learner = learner.Learner(spam_parser.get_df())
    spam_learner.learn()


