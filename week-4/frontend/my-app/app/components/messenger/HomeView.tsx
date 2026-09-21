import { motion } from "framer-motion";
import Image from "next/image";
import { Arrow, Logo } from "../icons";
import { useMessenger } from "./MessengerContext";
import { WindowControls } from "./WindowControls";

const chatAgents = [
  { name: "Chat agent 1", image: "/person1.jpg" },
  { name: "Chat agent 2", image: "/person2.jpeg" },
  { name: "Chat agent 3", image: "/person3.png" },
];

export function HomeView() {
  const { reduceMotion, setTab, startConversation } = useMessenger();
  return <motion.div className="messenger-page home-view" initial={reduceMotion ? { opacity: 0 } : { opacity: 0, x: -18 }} animate={{ opacity: 1, x: 0 }} exit={reduceMotion ? { opacity: 0 } : { opacity: 0, x: -14 }} transition={{ duration: reduceMotion ? 0.01 : 0.2, ease: "easeOut" }}>
    <div className="home-gradient" aria-hidden="true"><video src="/hero.mp4" autoPlay loop muted playsInline /><div className="home-video-overlay" /><div className="home-gradient-fade" /></div>
    <header className="messenger-hero">
      <div className="messenger-top"><Logo light /><div className="avatars" aria-label="Chat agents">{chatAgents.map((agent) => <Image key={agent.image} src={agent.image} alt={agent.name} width={29} height={29} />)}</div><WindowControls /></div>
      <p>Hello there.</p><h2>How can we help?</h2>
    </header>
    <div className="messenger-content">
      <button className="ask-card" onClick={() => startConversation()}>
        <span><b>Ask a question</b><small>Our AI agent can help</small></span>
        <span className="cta-agents" aria-label="Capn and our chat agents"><Image src={chatAgents[0].image} alt={chatAgents[0].name} width={30} height={30} /><span className="cta-logo"><Logo /></span><Image src={chatAgents[1].image} alt={chatAgents[1].name} width={30} height={30} /></span>
      </button>
      <article className="resource-card">
        <div className="resource-art"><small>NEW GUIDE</small><b>BUILD A KNOWLEDGE<br />BASE PEOPLE TRUST</b></div>
        <div className="resource-copy"><b>Your team’s answers, all in one place.</b><p>Learn how searchable, cited knowledge keeps everyone moving.</p><button onClick={() => startConversation("How does the knowledge base work?")}>Read the guide <Arrow /></button></div>
      </article>
      <div className="quick-links">
        <button onClick={() => startConversation("How do I upload a document?")}><span>Upload and index documents</span><Arrow /></button>
        <button onClick={() => setTab("help")}><span>Browse the help center</span><Arrow /></button>
      </div>
      <footer className="messenger-socials" aria-label="Capn social links"><a href="https://github.com/capn" target="_blank" rel="noreferrer">GitHub</a><a href="https://twitter.com/capn" target="_blank" rel="noreferrer">Twitter</a><a href="https://www.linkedin.com/company/capn" target="_blank" rel="noreferrer">LinkedIn</a></footer>
    </div>
  </motion.div>;
}
