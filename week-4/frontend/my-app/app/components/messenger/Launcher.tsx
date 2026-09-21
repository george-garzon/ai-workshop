import { AnimatePresence, motion } from "framer-motion";
import { caretDown as CaretDownIcon, messageSend as MessageSendIcon } from "../svg";
import { useMessenger } from "./MessengerContext";

export function Launcher() {
  const { open, reduceMotion, toggleOpen } = useMessenger();
  return <motion.button className="launcher" onClick={toggleOpen} aria-label={open ? "Close support messenger" : "Open support messenger"} aria-expanded={open} whileHover={reduceMotion ? undefined : { scale: 1.06 }} whileTap={reduceMotion ? undefined : { scale: 0.92 }} transition={{ type: "spring", stiffness: 500, damping: 28 }}>
    <AnimatePresence mode="wait" initial={false}>
      <motion.span className="launcher-icon" key={open ? "close" : "open"} initial={reduceMotion ? { opacity: 0 } : { opacity: 0, rotate: -35, scale: 0.7 }} animate={{ opacity: 1, rotate: 0, scale: 1 }} exit={reduceMotion ? { opacity: 0 } : { opacity: 0, rotate: 35, scale: 0.7 }} transition={{ duration: reduceMotion ? 0.01 : 0.16 }}>{open ? <CaretDownIcon /> : <MessageSendIcon />}</motion.span>
    </AnimatePresence>
  </motion.button>;
}
