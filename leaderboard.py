import pickle

def save_scores(score_list):
    filename = "score_file"
    with open(filename, 'wb') as fh:
        pickle.dump(score_list, fh, pickle.HIGHEST_PROTOCOL)

def load_scores():
    filename = "score_file"
    with open(filename, 'rb') as fh:
        score_list = pickle.load(fh)
    return score_list

def clear_file():
    filename = "score_file"
    clear_list = []
    with open(filename, 'wb') as fh:
        pickle.dump(clear_list, fh, pickle.HIGHEST_PROTOCOL)
