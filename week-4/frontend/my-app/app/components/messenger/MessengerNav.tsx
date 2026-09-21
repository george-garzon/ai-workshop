import { helpSVG as HelpIcon, homeSVG as HomeIcon, messagesSVG as MessagesIcon } from "../svg";
import { useMessenger } from "./MessengerContext";

export function MessengerNav() {
  const { setTab, tab } = useMessenger();
  return <nav className="messenger-nav" aria-label="Messenger navigation">
    <button className={tab === "home" ? "active" : ""} onClick={() => setTab("home")}><span><HomeIcon /></span>Home</button>
    <button className={tab === "messages" ? "active" : ""} onClick={() => setTab("messages")}><span><MessagesIcon /></span>Messages</button>
    <button className={tab === "help" ? "active" : ""} onClick={() => setTab("help")}><span><HelpIcon /></span>Help</button>
  </nav>;
}
