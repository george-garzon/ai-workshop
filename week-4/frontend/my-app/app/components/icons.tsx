import Image from "next/image";

export function Logo({ light = false, full = false }: { light?: boolean; full?: boolean }) {
  return (
    <Image
      className={`capn-logo ${full ? "full" : "mark"} ${light ? "light" : ""}`}
      src={full ? "/CapnLogo.svg" : "/CapnLogoSQ.svg"}
      width={full ? 130 : 32}
      height={full ? 40 : 32}
      alt={full ? "Capn" : ""}
      aria-hidden={!full}
    />
  );
}

export function Arrow() {
  return (
    <svg viewBox="0 0 20 20" aria-hidden="true">
      <path d="M4 10h12M11 5l5 5-5 5" />
    </svg>
  );
}
