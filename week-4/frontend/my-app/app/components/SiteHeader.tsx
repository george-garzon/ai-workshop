"use client";

import { useEffect, useState } from "react";
import { Logo } from "./icons";

export const OPEN_MESSENGER_EVENT = "open-support-messenger";
const GITHUB_URL = "https://github.com/george-garzon/ai-workshop";

export function SiteHeader() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const updateHeader = () => setScrolled(window.scrollY > 0);
    updateHeader();
    window.addEventListener("scroll", updateHeader, { passive: true });
    return () => window.removeEventListener("scroll", updateHeader);
  }, []);

  return (
    <nav className={`site-nav fixed inset-x-0 top-0 z-50 flex h-[65px] items-center justify-between border-b border-black/10 px-[18px] transition-colors duration-200 min-[601px]:h-[78px] min-[601px]:px-[2.3vw] min-[901px]:relative ${scrolled ? "bg-white/80 backdrop-blur-md" : "bg-white"}`}>
      <a className="wordmark" href="#">
        <Logo full />
      </a>
      <div className="nav-actions">
        <button
          className="outline-button"
          onClick={() => window.dispatchEvent(new Event(OPEN_MESSENGER_EVENT))}
        >
          Chat
        </button>
        <a className="dark" href={GITHUB_URL} target="_blank" rel="noreferrer">GitHub</a>
      </div>
    </nav>
  );
}
