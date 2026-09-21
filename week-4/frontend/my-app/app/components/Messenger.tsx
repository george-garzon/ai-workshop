"use client";

import { AnimatePresence, motion } from "framer-motion";
import { ConversationView } from "./messenger/ConversationView";
import { HelpView } from "./messenger/HelpView";
import { HomeView } from "./messenger/HomeView";
import { Launcher } from "./messenger/Launcher";
import { MessengerNav } from "./messenger/MessengerNav";
import { MessengerProvider, useMessenger } from "./messenger/MessengerContext";
import { MessagesEmptyView } from "./messenger/MessagesEmptyView";

function MessengerWindow() {
  const { conversationStarted, expanded, messengerRoot, messengerWidth, open, reduceMotion, tab } = useMessenger();

  return <div className={`messenger-root ${open ? "is-open" : ""}`} ref={messengerRoot}>
    <AnimatePresence>
      {open && <motion.section
        className={`messenger open ${expanded ? "expanded" : ""}`}
        initial={reduceMotion ? { opacity: 0 } : { opacity: 0, y: 22, scale: 0.96 }}
        animate={{ opacity: 1, y: 0, scale: 1, width: messengerWidth }}
        exit={reduceMotion ? { opacity: 0 } : { opacity: 0, y: 16, scale: 0.97 }}
        transition={reduceMotion ? { duration: 0.01 } : { type: "spring", stiffness: 360, damping: 32, mass: 0.85 }}
      >
        <AnimatePresence mode="wait" initial={false}>
          {tab === "home" && <HomeView key="home" />}
          {tab === "messages" && (conversationStarted ? <ConversationView key="conversation" /> : <MessagesEmptyView key="messages-empty" />)}
          {tab === "help" && <HelpView key="help" />}
        </AnimatePresence>
        <MessengerNav />
      </motion.section>}
    </AnimatePresence>
    <Launcher />
  </div>;
}

export function Messenger() {
  return <MessengerProvider><MessengerWindow /></MessengerProvider>;
}
