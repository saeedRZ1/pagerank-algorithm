import random

DAMPING = 0.85
SAMPLES = 10000

def transition_model(corpus, page, damping_factor):
    n = len(corpus)
    model = {}
    links = corpus[page]
    if links:
        for p in corpus:
            model[p] = (1 - damping_factor) / n
        for link in links:
            model[link] += damping_factor / len(links)
    else:
        for p in corpus:
            model[p] = 1 / n
    return model

def sample_pagerank(corpus, damping_factor, n):
    page = random.choice(list(corpus.keys()))
    counts = {p: 0 for p in corpus}
    for _ in range(n):
        counts[page] += 1
        model = transition_model(corpus, page, damping_factor)
        page = random.choices(list(model.keys()), weights=model.values())[0]
    return {p: counts[p] / n for p in counts}

if __name__ == "__main__":
    # Example corpus
    corpus = {
        "1.html": {"2.html", "3.html"},
        "2.html": {"3.html"},
        "3.html": {"1.html"},
    }
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print("PageRank Results:")
    for page, rank in ranks.items():
        print(f"{page}: {rank:.4f}")
