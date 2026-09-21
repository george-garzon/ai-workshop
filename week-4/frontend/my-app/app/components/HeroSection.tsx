"use client";

import Image from "next/image";
import { OPEN_MESSENGER_EVENT } from "./SiteHeader";

const GITHUB_URL = "https://github.com/george-garzon/ai-workshop";

function ProductPreview() {
  return (
    <div className="hero-visual" aria-label="Capn AI document conversation preview">
      <video autoPlay loop muted playsInline preload="metadata" aria-hidden="true">
        <source src="/hero.mp4" type="video/mp4" />
      </video>
      <div className="hero-video-shade" />
      <Image
        className="conversation-manager-art"
        src="/pdf-landing.png"
        alt="Documents flowing into a Capn AI conversation and a generated report"
        width={1122}
        height={1402}
        priority
      />
      {/*<div className="hero-visual-label"><span>✦</span><b>Talk to every document</b><small>PDF · DOCX · XLSX · CSV</small></div>*/}
    </div>
  );
}

export function HeroSection() {
  return (
    <>
      <section className="main-hero">
        <div className="hero-copy">
          <div className="eyebrow"><i /> AI-POWERED KNOWLEDGE</div>
          <h1>One place for every answer your team needs.</h1>
          <p>Capn turns scattered documents into clear, cited answers—so your team can move with confidence.</p>
          <div className="hero-actions">
            <a className="dark large" href={GITHUB_URL} target="_blank" rel="noreferrer">GitHub</a>
            <button className="outline-button large" onClick={() => window.dispatchEvent(new Event(OPEN_MESSENGER_EVENT))}>Chat</button>
          </div>
        </div>
        <ProductPreview />
      </section>
    </>
  );
}
