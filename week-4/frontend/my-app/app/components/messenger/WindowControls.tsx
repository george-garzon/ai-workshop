import { expand as ExpandIcon, shrink as ShrinkIcon } from "../svg";
import { useMessenger } from "./MessengerContext";

export function WindowControls() {
  const { close, expanded, isMobile, toggleExpanded } = useMessenger();
  return <div className="window-controls">
    {!isMobile && <button className="expand-button" onClick={toggleExpanded} aria-label={expanded ? "Collapse window" : "Expand window"} title={expanded ? "Collapse window" : "Expand window"}>{expanded ? <ShrinkIcon /> : <ExpandIcon />}</button>}
    <button onClick={close} aria-label="Close">×</button>
  </div>;
}
