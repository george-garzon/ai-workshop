import { motion } from "framer-motion";
import { WorkshopHelp } from "../WorkshopHelp";
import { useMessenger } from "./MessengerContext";
import { WindowControls } from "./WindowControls";

export function HelpView() {
  const { reduceMotion, setExpanded, setTab } = useMessenger();
  return <motion.div className="messenger-page-transition" initial={reduceMotion ? { opacity: 0 } : { opacity: 0, x: 18 }} animate={{ opacity: 1, x: 0 }} exit={reduceMotion ? { opacity: 0 } : { opacity: 0, x: 14 }} transition={{ duration: reduceMotion ? 0.01 : 0.2, ease: "easeOut" }}>
    <WorkshopHelp onBack={() => setTab("home")} onArticleOpen={() => setExpanded(true)} onArticleBack={() => setExpanded(false)} windowControls={<WindowControls />} />
  </motion.div>;
}
