import { useMemo, useState, type ReactNode } from "react";
import { Arrow } from "./icons";
import { caretLeft as CaretLeftIcon, search as SearchIcon } from "./svg";
import { workshopArticles, type WorkshopArticle } from "./workshopArticles";

type WorkshopHelpProps = { onBack: () => void; onArticleOpen: () => void; onArticleBack: () => void; windowControls: ReactNode };

export function WorkshopHelp({ onBack, onArticleOpen, onArticleBack, windowControls }: WorkshopHelpProps) {
  const [query, setQuery] = useState("");
  const [collectionOpen, setCollectionOpen] = useState(false);
  const [selected, setSelected] = useState<WorkshopArticle | null>(null);
  const articles = useMemo(() => {
    const search = query.trim().toLowerCase();
    if (!search) return workshopArticles;
    return workshopArticles.filter((article) => [article.title, article.summary, article.accomplishment, ...article.concepts, ...article.steps].join(" ").toLowerCase().includes(search));
  }, [query]);

  function openArticle(article: WorkshopArticle) {
    setSelected(article);
    onArticleOpen();
  }

  function goBack() {
    if (selected) {
      setSelected(null);
      onArticleBack();
    }
    else if (collectionOpen) setCollectionOpen(false);
    else onBack();
  }

  return (
    <div className="messenger-page help-view">
      <header className="help-header border-b border-[#e9e9e7] bg-white px-3 pb-2">
        <div className="relative flex h-11 w-full items-center justify-center">
          {(selected || collectionOpen) && <button className="back absolute left-0 grid size-8 place-items-center text-[#62656a]" onClick={goBack} aria-label="Back"><CaretLeftIcon /></button>}
          <h2 className="m-0 text-[17px] font-semibold tracking-[-0.2px]">Help</h2>
          {windowControls}
        </div>
        {!selected && <label className="flex h-10 w-full items-center gap-2.5 rounded-[10px] bg-[#f2f2f1] px-3 text-[#111]">
          <input className="min-w-0 flex-1 border-0 bg-transparent text-[13px] outline-none placeholder:text-[#303236]" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Search for help" />
          <SearchIcon />
        </label>}
      </header>
      {selected ? (
        <article className="article-detail">
          <span className="week-label">WEEK {selected.week}</span>
          <h3>{selected.title}</h3>
          <p className="article-summary">{selected.summary}</p>
          <div className="article-byline">AI Workshop team · Updated for Week {selected.week}</div>
          <h4>Concepts we learned</h4>
          <ul>{selected.concepts.map((concept) => <li key={concept}>{concept}</li>)}</ul>
          <h4>What we built</h4>
          <p>{selected.accomplishment}</p>
          <ol>{selected.steps.map((step) => <li key={step}>{step}</li>)}</ol>
        </article>
      ) : (
        <div className="help-body">
          {collectionOpen || query ? <>
            {!query && <section className="collection-summary"><h3>AI Workshop</h3><p>Everything you need to review the concepts and projects from each week.</p><small>{workshopArticles.length} articles</small></section>}
            <div className="article-list">
              {articles.map((article) => <button key={article.week} onClick={() => openArticle(article)}><span><b>{article.title}</b><small>Week {article.week} · {article.summary}</small></span><Arrow /></button>)}
              {articles.length === 0 && <p className="empty-results">No articles match “{query}”.</p>}
            </div>
          </> : <>
            <h3>1 collection</h3>
            <button className="collection-card" onClick={() => setCollectionOpen(true)}><span><b>AI Workshop</b><small>Everything you need to review the concepts and projects from each week.</small><em>{workshopArticles.length} articles</em></span><Arrow /></button>
          </>}
        </div>
      )}
    </div>
  );
}
