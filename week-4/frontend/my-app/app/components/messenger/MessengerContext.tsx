"use client";

import { createContext, type ReactNode, type RefObject, useCallback, useContext, useEffect, useMemo, useRef, useState } from "react";
import { useReducedMotion } from "framer-motion";
import { OPEN_MESSENGER_EVENT } from "../SiteHeader";

export type MessengerTab = "home" | "messages" | "help";
export type Attachment = { name: string; size: number; type: string };
export type Message = { role: "assistant" | "user"; text: string; citation?: string; attachment?: Attachment };

type ApiMessage = { role: "assistant" | "user"; text: string; citation?: string | null };
type ApiConversation = {
  id: string;
  document: { filename: string; size: number };
  messages: ApiMessage[];
};

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
const CONVERSATION_STORAGE_KEY = "capn-conversation-id";

type MessengerContextValue = {
  conversationStarted: boolean; draft: string; expanded: boolean; isMobile: boolean;
  messages: Message[]; messengerRoot: RefObject<HTMLDivElement | null>; messengerWidth: number;
  open: boolean; reduceMotion: boolean; tab: MessengerTab; typing: boolean;
  documentName: string; error: string; hasDocument: boolean;
  close: () => void; sendMessage: (attachment?: File) => Promise<boolean>; setDraft: (draft: string) => void;
  setExpanded: (expanded: boolean) => void; setTab: (tab: MessengerTab) => void;
  startConversation: (question?: string) => void; toggleExpanded: () => void; toggleOpen: () => void;
};

const MessengerContext = createContext<MessengerContextValue | null>(null);
const initialMessages: Message[] = [{ role: "assistant", text: "Hi! I’m Capn, your knowledge assistant. Ask me anything about your company docs." }];

export function MessengerProvider({ children }: { children: ReactNode }) {
  const reducedMotion = useReducedMotion();
  const [open, setOpen] = useState(false);
  const [tab, setTab] = useState<MessengerTab>("home");
  const [draft, setDraft] = useState("");
  const [typing, setTyping] = useState(false);
  const [conversationStarted, setConversationStarted] = useState(false);
  const [expanded, setExpanded] = useState(false);
  const [viewportWidth, setViewportWidth] = useState(1024);
  const [messages, setMessages] = useState<Message[]>(initialMessages);
  const [conversationId, setConversationId] = useState("");
  const [documentName, setDocumentName] = useState("");
  const [error, setError] = useState("");
  const messengerRoot = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const updateViewport = () => setViewportWidth(window.innerWidth);
    updateViewport();
    window.addEventListener("resize", updateViewport);
    return () => window.removeEventListener("resize", updateViewport);
  }, []);

  useEffect(() => {
    const savedId = window.localStorage.getItem(CONVERSATION_STORAGE_KEY);
    if (!savedId) return;

    const controller = new AbortController();
    fetch(`${API_URL}/api/conversations/${savedId}`, { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error("Saved conversation is unavailable");
        return response.json() as Promise<ApiConversation>;
      })
      .then((conversation) => {
        setConversationId(conversation.id);
        setDocumentName(conversation.document.filename);
        setConversationStarted(true);
        setMessages([
          initialMessages[0],
          ...conversation.messages.map((message) => ({
            role: message.role,
            text: message.text,
            citation: message.citation ?? undefined,
          })),
        ]);
      })
      .catch((loadError: unknown) => {
        if (loadError instanceof DOMException && loadError.name === "AbortError") return;
        window.localStorage.removeItem(CONVERSATION_STORAGE_KEY);
      });
    return () => controller.abort();
  }, []);

  useEffect(() => {
    const openMessenger = () => setOpen(true);
    window.addEventListener(OPEN_MESSENGER_EVENT, openMessenger);
    return () => window.removeEventListener(OPEN_MESSENGER_EVENT, openMessenger);
  }, []);

  useEffect(() => {
    if (!open) return;
    const closeOnOutsideClick = (event: PointerEvent) => {
      if (!messengerRoot.current?.contains(event.target as Node)) setOpen(false);
    };
    document.addEventListener("pointerdown", closeOnOutsideClick);
    return () => document.removeEventListener("pointerdown", closeOnOutsideClick);
  }, [open]);

  useEffect(() => {
    if (!open || viewportWidth > 600) return;
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => { document.body.style.overflow = previousOverflow; };
  }, [open, viewportWidth]);

  const startConversation = useCallback((question = "") => {
    setConversationStarted(true); setTab("messages"); setDraft(question);
  }, []);

  const sendMessage = useCallback(async (attachment?: File) => {
    const text = draft.trim();
    if (!text || typing) return false;
    if (!conversationId && !attachment) {
      setError("Attach a PDF before sending your first message.");
      return false;
    }
    if (attachment && (attachment.type !== "application/pdf" || !attachment.name.toLowerCase().endsWith(".pdf"))) {
      setError("Only PDF documents are supported.");
      return false;
    }

    setError("");
    setTyping(true);
    try {
      let activeConversationId = conversationId;
      let activeDocumentName = documentName;

      if (!activeConversationId && attachment) {
        const form = new FormData();
        form.append("file", attachment);
        const uploadResponse = await fetch(`${API_URL}/api/conversations`, { method: "POST", body: form });
        if (!uploadResponse.ok) {
          const payload = await uploadResponse.json().catch(() => null) as { detail?: string } | null;
          throw new Error(payload?.detail ?? "The PDF could not be uploaded.");
        }
        const conversation = await uploadResponse.json() as ApiConversation;
        activeConversationId = conversation.id;
        activeDocumentName = conversation.document.filename;
        setConversationId(conversation.id);
        setDocumentName(activeDocumentName);
        window.localStorage.setItem(CONVERSATION_STORAGE_KEY, conversation.id);
      }

      const response = await fetch(`${API_URL}/api/conversations/${activeConversationId}/messages`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      if (!response.ok) {
        const payload = await response.json().catch(() => null) as { detail?: string } | null;
        throw new Error(payload?.detail ?? "Capn could not answer right now.");
      }
      const payload = await response.json() as { message: ApiMessage };
      const uploadedAttachment = attachment ? { name: attachment.name, size: attachment.size, type: attachment.type } : undefined;
      setMessages((all) => [
        ...all,
        { role: "user", text, attachment: uploadedAttachment },
        { role: "assistant", text: payload.message.text, citation: payload.message.citation ?? activeDocumentName },
      ]);
      setDraft("");
      return true;
    } catch (sendError) {
      setError(sendError instanceof Error ? sendError.message : "Capn could not answer right now.");
      return false;
    } finally {
      setTyping(false);
    }
  }, [conversationId, documentName, draft, typing]);

  const isMobile = viewportWidth <= 600;
  const messengerWidth = isMobile ? viewportWidth : expanded ? Math.min(690, viewportWidth - 48) : 380;
  const value = useMemo<MessengerContextValue>(() => ({
    conversationStarted, draft, expanded, isMobile, messages, messengerRoot, messengerWidth,
    open, reduceMotion: Boolean(reducedMotion), tab, typing, documentName, error,
    hasDocument: Boolean(conversationId),
    close: () => setOpen(false), sendMessage, setDraft, setExpanded, setTab, startConversation,
    toggleExpanded: () => setExpanded((value) => !value), toggleOpen: () => setOpen((value) => !value),
  }), [conversationId, conversationStarted, documentName, draft, error, expanded, isMobile, messages, messengerWidth, open, reducedMotion, sendMessage, startConversation, tab, typing]);

  return <MessengerContext.Provider value={value}>{children}</MessengerContext.Provider>;
}

export function useMessenger() {
  const context = useContext(MessengerContext);
  if (!context) throw new Error("useMessenger must be used within MessengerProvider");
  return context;
}
