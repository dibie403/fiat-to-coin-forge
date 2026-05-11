import { Link } from "@tanstack/react-router";

type Props = {
  size?: "sm" | "md" | "lg";
  showWordmark?: boolean;
  asLink?: boolean;
  className?: string;
};

const sizes = {
  sm: { box: "h-8 w-8", glyph: "text-[15px]", title: "text-base", sub: "text-[9px] tracking-[0.22em]" },
  md: { box: "h-10 w-10", glyph: "text-lg", title: "text-lg", sub: "text-[10px] tracking-[0.28em]" },
  lg: { box: "h-14 w-14", glyph: "text-2xl", title: "text-2xl", sub: "text-[11px] tracking-[0.32em]" },
};

export function Logo({ size = "md", showWordmark = true, asLink = true, className = "" }: Props) {
  const s = sizes[size];

  const mark = (
    <span className={`relative inline-flex ${s.box} shrink-0 items-center justify-center`}>
      {/* gradient backdrop */}
      <span className="absolute inset-0 rounded-xl bg-gradient-to-br from-primary via-emerald-400 to-amber-300 shadow-[0_8px_24px_-10px_oklch(0.72_0.18_150/0.55)]" />
      {/* inner panel */}
      <span className="absolute inset-[2px] rounded-[10px] bg-background/85 backdrop-blur-sm" />
      {/* diagonal accent */}
      <span className="absolute -left-1 top-1/2 h-[1px] w-3 -rotate-45 bg-gradient-to-r from-transparent to-primary" />
      <span className="absolute -right-1 top-1/2 h-[1px] w-3 -rotate-45 bg-gradient-to-l from-transparent to-amber-300" />
      {/* monogram */}
      <span
        className={`relative font-black ${s.glyph} bg-gradient-to-br from-primary via-emerald-400 to-amber-300 bg-clip-text text-transparent`}
        style={{ fontFamily: "ui-serif, Georgia, 'Times New Roman', serif", fontStyle: "italic", letterSpacing: "-0.04em" }}
      >
        Oƒ
      </span>
    </span>
  );

  const wordmark = (
    <span className="flex flex-col leading-none">
      <span className={`font-semibold tracking-tight ${s.title}`}>
        <span className="bg-gradient-to-r from-foreground to-foreground/70 bg-clip-text text-transparent">
          Orji
        </span>{" "}
        <span className="italic font-light text-muted-foreground">funds</span>{" "}
        <span className="bg-gradient-to-r from-primary to-emerald-400 bg-clip-text text-transparent">
          Exchange
        </span>
      </span>
      <span className={`mt-1 ${s.sub} uppercase text-muted-foreground/70`}>
        Naira · Crypto · Settled
      </span>
    </span>
  );

  const content = (
    <span className={`inline-flex items-center gap-3 ${className}`}>
      {mark}
      {showWordmark && wordmark}
    </span>
  );

  if (!asLink) return content;
  return (
    <Link to="/" className="inline-flex items-center gap-3 group">
      {content}
    </Link>
  );
}
