import { motion } from "framer-motion";
import { arrowUp as SendIcon, messagesSVG as MessagesIcon } from "../svg";
import { useMessenger } from "./MessengerContext";
import { WindowControls } from "./WindowControls";

export function MessagesEmptyView() {
  const { reduceMotion, startConversation } = useMessenger();
  return <motion.div className="messenger-page messages-empty" initial={reduceMotion ? { opacity: 0 } : { opacity: 0, x: 18 }} animate={{ opacity: 1, x: 0 }} exit={reduceMotion ? { opacity: 0 } : { opacity: 0, x: 14 }} transition={{ duration: reduceMotion ? 0.01 : 0.2, ease: "easeOut" }}>
    <header><h2>Messages</h2><WindowControls /></header>
    <div className="messages-empty-content"><MessagesIcon /><h3>No messages</h3><p>Messages from the team will be shown here</p></div>
    <button className="start-message" onClick={() => startConversation()}>Send us a message <SendIcon /></button>
  </motion.div>;
}
