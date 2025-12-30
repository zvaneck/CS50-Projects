import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    N = len(corpus)
    probabilities = {}

    if len(corpus[page]) == 0:
        for p in corpus:
            probabilities[p] = 1 / N
    else:
        for p in corpus:
            if p in corpus[page]:
                probabilities[p] = (damping_factor / len(corpus[page])) + ((1 - damping_factor) / N)
            else:
                probabilities[p] = (1 - damping_factor) / N

    return probabilities

    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    count = {page: 0 for page in corpus}

    sample = random.choice(list(corpus.keys()))
    count[sample] += 1

    for _ in range(n - 1):
        probabilities = transition_model(corpus, sample, damping_factor)

        r = random.random()
        cumulative = 0
        for page, prob in probabilities.items():
            cumulative += prob
            if r <= cumulative:
                sample = page
                break

        count[sample] += 1

    pagerank = {page: count[page] / n for page in count}

    return pagerank

    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    N = len(corpus)
    pagerank = {page: 1 / N for page in corpus}
    change = 1

    while change >= 0.001:
        new_ranks = {}
        change = 0

        for page in corpus:
            rank_sum = (1 - damping_factor) / N
            linking_pages = set()
            for possible_linker in corpus:
                if page in corpus[possible_linker]:
                    linking_pages.add(possible_linker)
                if len(corpus[possible_linker]) == 0:
                    linking_pages.add(possible_linker)


            for linker in linking_pages:
                if len(corpus[linker]) == 0:
                    rank_sum += damping_factor * (pagerank[linker] / N)
                else:
                    rank_sum += damping_factor * (pagerank[linker] / len(corpus[linker]))

            new_ranks[page] = rank_sum


            change = max(change, abs(new_ranks[page] - pagerank[page]))

        pagerank = new_ranks  

    return pagerank

    raise NotImplementedError


if __name__ == "__main__":
    main()
