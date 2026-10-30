# Backlog checklist (practicals ~30 Nov 2026)

Rules: read instructor version → close it → rewrite from memory in my own notebook → compare. No copy-paste. Every session starts with the 15-min NumPy/Pandas drill at the bottom.

## Folder map
- `Numpy And Pandas/` — intro notebooks, the drill material
- `Feature Extraction/` — PCA.ipynb (done, understand), LDA.ipynb (scratch S_B done; S_W, eig, in-built LDA missing), SVM.ipynb (just started), `data/` has user_data.csv + movies.csv
- `Feature Selection/material/` — Outlier Analysis.ipynb + Handling Missing Value.ipynb (instructor), divyansh_reference_CHI2_IG.ipynb (classmate's 23 Oct lab, DELETE once my own version is done)
- `Regression/` — from 30 Oct class onward
- `Data_Collection/Web_scraping.ipynb` — MY old scraping attempt (incomplete get_data, no assignment done)
- `Data_Collection/WebScraping_material/` — Web_Scraping_Amazon.ipynb (instructor), BS4 notes PDF, Assignment-V (Amazon + IMDb)
- `Data_Collection/API_material/` — TMDB_API.ipynb (instructor), Assignment-4 (a–c movies), Assignment-3 (d–h TV series), title.ratings.tsv
- `NLP-labs/` — Preprocessor_lab3a.ipynb and lab3(b).ipynb are mine, "Lab Session 3(x)" are instructor's
- `Image_Processing/` — lab1–5 mine, Assignment 1–5 PDFs

## Priority 1: Feature Extraction
- [ ] PCA — walkthrough with Claude: why standardize, why cov, why eigh, why last 2 columns, what @ does, sign flips vs sklearn
- [ ] PCA — re-type from blank notebook, scratch + in-built, no notes
- [ ] LDA — S_W by hand (formula on paper first), eig of inv(S_W)@S_B, project, scatter
- [ ] LDA — in-built `LinearDiscriminantAnalysis`, compare with scratch
- [ ] LDA — answer: why S_B is weighted by N_c, what rank S_B has for 3 classes, why at most C−1 components
- [ ] SVM — figure out what sir wants with user_data.csv / movies.csv, in-built `SVC`, linear vs rbf kernel
- [ ] Regression — rewrite 30 Oct lab from memory: scratch (normal equation / gradient descent) + sklearn LinearRegression

## Priority 1: Feature Selection
- [ ] Outlier Analysis — boxplot, z-score, IQR, IsolationForest. `load_boston` is gone from sklearn, pick a replacement dataset. Apply all 4 on user_data.csv
- [ ] Handling missing values — dropna (axis/how/thresh/subset), fillna constant/mean/median, bfill/ffill with limit, fill from another df, SimpleImputer. `method=` arg is deprecated, find the replacement. MissForest needs `missingpy`, skip if it won't install
- [ ] Chi-square from scratch on `car` dataset (observed vs expected per attribute/target pair) → chi2_contingency → SelectKBest(chi2)
- [ ] Entropy, avg info entropy, information gain from scratch → SelectKBest(mutual_info_classif)
- [ ] Only then open divyansh's notebook to check. Delete it after
- [ ] t-test feature selection — implement from scratch MYSELF when sir covers it (two-sample t per feature between classes), verify with scipy.stats.ttest_ind

## Priority 2: Data Collection
- [ ] Web scraping revise — requests → BeautifulSoup → find/find_all → .text → DataFrame. Finish my broken `get_data` in Data_Collection/Web_scraping.ipynb WITHOUT looking at instructor's
- [ ] Assignment-V Q1 — Amazon bestsellers (2 pages), follow each book link: publisher, language, paperback, ISBN-10/13, weight, dimensions, first 3 reviews. Headers + sleep for blocking
- [ ] Assignment-V Q2 — IMDb 2020 movies, 1000 rows via pagination: name, rating, description, votes, directors, stars, metascore, genre, duration
- [ ] Assignment-V — Selenium version of at least one question
- [ ] API — get TMDb key, keep it in `tmdbapi.ipynb` (already gitignored). Rewrite TMDB_API.ipynb from memory: genre list → discover → paginate to 300 → similar → external_ids → merge with title.ratings.tsv
- [ ] Assignment-4 (a–c) — movie_ID_name.csv, movie_ID_sim_movie_ID.csv, exact format (no header, no space after comma), respect 40 req/10 s
- [ ] Assignment-3 (d–g) — TV series discover (drama, 2015+, 200 most popular), 5 recommendations each, IMDb merge, rating diff, scatter
- [ ] Assignment-3 (h) — recommender: user types a series name → search → id → 5 similar → IMDb ids → formatted table

## Priority 3: NLP revise
- [ ] Preprocessing from memory — regex normalize, tokenize, stopwords, stem/lemma
- [ ] Fix my lab3(b) bugs — missing `>` in HTML regex, dict assignment inside wrong loop
- [ ] TDM variants from scratch — binary, tf, length-norm, max-norm, log, tf-idf (+ sklearn smoothed idf and l2)
- [ ] Co-occurrence matrix homework

## Priority 3: Image Processing revise
- [ ] Labs 1–4 from memory — threshold, grayscale weights, padding, log/gamma/contrast stretch
- [ ] Lab 5 — avg/weighted/gaussian filters, fix exit() ordering bug, try median filter on salt_pepper_duck
- [ ] Answer: what `borderType` does in cv2.filter2D

## Final stretch: mock practicals
- [ ] Blank notebook, 45 min timer, no notes, one random topic. Log mistakes in `MISTAKES.md`
- [ ] Cycle: PCA, LDA, SVM, regression, outliers, missing values, chi2/IG/t-test, scraping, API, NLP TDM, image filters

## Daily NumPy/Pandas drill (15 min, no autocomplete)
array creation, reshape, axis=0 vs 1 on mean/sum, boolean mask, np.where, @ vs *, .T, np.linalg.eigh/inv, np.outer, np.percentile,
pd.read_csv, iloc/loc, df[mask], groupby, merge, value_counts, apply/lambda, to_csv(index=False), fillna, drop_duplicates.

## Open questions for Claude
- Regex non-greedy `?`, what `.T` does on a 1-D array
- Why eigh over eig, why eigenvectors can flip sign
