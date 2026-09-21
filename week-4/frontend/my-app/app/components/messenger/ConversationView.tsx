import { type ChangeEvent, type FormEvent, useEffect, useRef, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Logo } from "../icons";
import { arrowUp as SendIcon, caretLeft as CaretLeftIcon, microphone as MicrophoneIcon, paperclipAttach as PaperclipIcon } from "../svg";
import { useMessenger } from "./MessengerContext";
import { WindowControls } from "./WindowControls";

type SpeechResultEvent = Event & { results: { [index: number]: { [index: number]: { transcript: string } }; length: number } };
type SpeechRecognitionInstance = {
  continuous: boolean; interimResults: boolean; lang: string;
  start: () => void; stop: () => void;
  onresult: ((event: SpeechResultEvent) => void) | null;
  onend: (() => void) | null; onerror: (() => void) | null;
};
type SpeechRecognitionWindow = Window & {
  SpeechRecognition?: new () => SpeechRecognitionInstance;
  webkitSpeechRecognition?: new () => SpeechRecognitionInstance;
};

function fileSize(bytes: number) {
  if (bytes < 1024 * 1024) return `${Math.max(1, Math.round(bytes / 1024))} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

export function ConversationView() {
  const { documentName, draft, error, hasDocument, messages, reduceMotion, sendMessage, setDraft, setTab, typing } = useMessenger();
  const end = useRef<HTMLDivElement>(null);
  const fileInput = useRef<HTMLInputElement>(null);
  const recognition = useRef<SpeechRecognitionInstance | null>(null);
  const [attachment, setAttachment] = useState<File | null>(null);
  const [listening, setListening] = useState(false);
  const [voiceStatus, setVoiceStatus] = useState("");

  useEffect(() => {
    end.current?.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth" });
  }, [messages, reduceMotion, typing]);

  useEffect(() => () => recognition.current?.stop(), []);

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    const sent = await sendMessage(attachment ?? undefined);
    if (sent) {
      setAttachment(null);
      if (fileInput.current) fileInput.current.value = "";
    }
  };

  const chooseFile = (event: ChangeEvent<HTMLInputElement>) => {
    const selected = event.target.files?.[0] ?? null;
    if (selected && (selected.type !== "application/pdf" || !selected.name.toLowerCase().endsWith(".pdf"))) {
      setVoiceStatus("Please choose a PDF document.");
      event.target.value = "";
      return;
    }
    setVoiceStatus("");
    setAttachment(selected);
  };

  const toggleMicrophone = () => {
    if (listening) {
      recognition.current?.stop();
      return;
    }
    const speechWindow = window as SpeechRecognitionWindow;
    const Recognition = speechWindow.SpeechRecognition ?? speechWindow.webkitSpeechRecognition;
    if (!Recognition) {
      setVoiceStatus("Voice input isn’t supported in this browser.");
      return;
    }
    const next = new Recognition();
    next.continuous = false;
    next.interimResults = false;
    next.lang = navigator.language || "en-US";
    next.onresult = (event) => {
      const transcript = event.results[event.results.length - 1][0].transcript.trim();
      setDraft([draft.trim(), transcript].filter(Boolean).join(" "));
      setVoiceStatus("Voice added to your message.");
    };
    next.onerror = () => {
      setListening(false);
      setVoiceStatus("I couldn’t hear that. Please try again.");
    };
    next.onend = () => setListening(false);
    recognition.current = next;
    setVoiceStatus("Listening…");
    setListening(true);
    next.start();
  };
  return <motion.div className="messenger-page conversation" initial={reduceMotion ? { opacity: 0 } : { opacity: 0, x: 18 }} animate={{ opacity: 1, x: 0 }} exit={reduceMotion ? { opacity: 0 } : { opacity: 0, x: 14 }} transition={{ duration: reduceMotion ? 0.01 : 0.2, ease: "easeOut" }}>
    <header className="conversation-head"><button className="back" onClick={() => setTab("home")} aria-label="Back"><CaretLeftIcon /></button><Logo /><div><b>Capn AI</b><small><i /> {documentName || "Attach a PDF to begin"}</small></div><WindowControls /></header>
    <div className="message-list" aria-live="polite">
      <div className="chat-intro"><Logo /><b>Capn AI</b><small>Your company knowledge assistant</small></div>
      <AnimatePresence initial={false}>
        {messages.map((message, index) => <motion.div className={`message ${message.role}`} key={index} initial={reduceMotion ? { opacity: 0 } : { opacity: 0, y: 12, scale: 0.98 }} animate={{ opacity: 1, y: 0, scale: 1 }} transition={{ duration: reduceMotion ? 0.01 : 0.24, ease: "easeOut" }} layout={!reduceMotion}>{message.attachment && <span className="message-attachment"><PaperclipIcon /><span><b>{message.attachment.name}</b><small>{fileSize(message.attachment.size)}</small></span></span>}<p>{message.text}</p>{message.citation && <motion.button initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: reduceMotion ? 0 : 0.12 }}>▤ {message.citation}</motion.button>}</motion.div>)}
        {typing && <motion.span className="typing" key="typing" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, scale: 0.92 }}><i /><i /><i /></motion.span>}
      </AnimatePresence>
      <div ref={end} />
    </div>
    <form className="composer" onSubmit={submit}>
      <input ref={fileInput} className="visually-hidden" type="file" accept="application/pdf,.pdf" onChange={chooseFile} />
      {attachment && <div className="attachment-chip"><PaperclipIcon /><span><b>{attachment.name}</b><small>{fileSize(attachment.size)}</small></span><button type="button" onClick={() => { setAttachment(null); if (fileInput.current) fileInput.current.value = ""; }} aria-label={`Remove ${attachment.name}`}>×</button></div>}
      <textarea rows={1} value={draft} onChange={(event) => setDraft(event.target.value)} onKeyDown={(event) => { if (event.key === "Enter" && !event.shiftKey) { event.preventDefault(); event.currentTarget.form?.requestSubmit(); } }} placeholder="Ask a question…" aria-label="Message" />
      <div><span className="composer-tools"><button type="button" disabled={hasDocument} onClick={() => fileInput.current?.click()} aria-label={hasDocument ? `Using ${documentName}` : "Attach PDF"} title={hasDocument ? `Using ${documentName}` : "Attach PDF"}><PaperclipIcon /></button><button className={listening ? "recording" : ""} type="button" onClick={toggleMicrophone} aria-label={listening ? "Stop listening" : "Talk using microphone"} title={listening ? "Stop listening" : "Talk using microphone"} aria-pressed={listening}><MicrophoneIcon /></button></span><small className={(error || voiceStatus) ? "composer-status error" : ""} aria-live="polite">{error || voiceStatus || (!hasDocument && !attachment ? "Attach a PDF to begin" : "AI answers may make mistakes")}</small><button className="send" disabled={!draft.trim() || (!hasDocument && !attachment) || typing} aria-label="Send"><SendIcon /></button></div>
    </form>
  </motion.div>;
}
