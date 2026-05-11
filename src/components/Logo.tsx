import { Link } from "@tanstack/react-router";
import { useAuth } from "@/context/AuthContext";

type Props = {
  size?: "sm" | "md" | "lg";
  showWordmark?: boolean;
  asLink?: boolean;
  className?: string;
};

const sizes = {
  sm: { box: 32, title: "text-[15px]", sub: "text-[8px] tracking-[0.28em]", stacked: "text-[10px]" },
  md: { box: 40, title: "text-lg", sub: "text-[9px] tracking-[0.3em]", stacked: "text-[11px]" },
  lg: { box: 56, title: "text-2xl", sub: "text-[10px] tracking-[0.34em]", stacked: "text-[13px]" },
};

/**
 * Orji Funds Exchange — logomark.
 * A circular badge with an interlocking ₦ / ₿ exchange glyph and rotating
 * orbital ring. Designed to read clearly at 24px on mobile.
 */
function Mark({ px }: { px: number }) {
  return (
    <span
      className="relative inline-block shrink-0"
      style={{ width: px, height: px }}
      aria-hidden
    >
      <svg viewBox="0 0 64 64" width={px} height={px} className="block">
        <defs>
          <linearGradient id="ofx-g" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor="oklch(0.78 0.18 150)" />
            <stop offset="55%" stopColor="oklch(0.72 0.14 165)" />
            <stop offset="100%" stopColor="oklch(0.82 0.14 85)" />
          </linearGradient>
          <linearGradient id="ofx-g2" x1="0" y1="1" x2="1" y2="0">
            <stop offset="0%" stopColor="oklch(0.82 0.14 85)" />
            <stop offset="100%" stopColor="oklch(0.78 0.18 150)" />
          </linearGradient>
        </defs>

        {/* outer dashed orbit */}
        <circle
          cx="32" cy="32" r="29"
          fill="none"
          stroke="url(#ofx-g)"
          strokeWidth="1"
          strokeDasharray="2 3"
          opacity="0.55"
          className="origin-center [animation:ofx-spin_18s_linear_infinite]"
        />

        {/* solid ring */}
        <circle
          cx="32" cy="32" r="25"
          fill="none"
          stroke="url(#ofx-g)"
          strokeWidth="2.25"
        />

        {/* exchange arrows arc — top */}
        <path
          d="M20 22 Q32 14 44 22"
          fill="none"
          stroke="url(#ofx-g2)"
          strokeWidth="1.6"
          strokeLinecap="round"
        />
        <path d="M43 19 L45 22 L42 24" fill="none" stroke="url(#ofx-g2)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />

        {/* exchange arrows arc — bottom */}
        <path
          d="M44 42 Q32 50 20 42"
          fill="none"
          stroke="url(#ofx-g2)"
          strokeWidth="1.6"
          strokeLinecap="round"
        />
        <path d="M21 45 L19 42 L22 40" fill="none" stroke="url(#ofx-g2)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />

        {/* monogram: O with a slash forming an F */}
        <g>
          {/* the O */}
          <circle cx="32" cy="32" r="9.5" fill="none" stroke="url(#ofx-g)" strokeWidth="2.4" />
          {/* horizontal bar of F across the O */}
          <line x1="26.5" y1="30" x2="38" y2="30" stroke="url(#ofx-g2)" strokeWidth="2" strokeLinecap="round" />
          {/* short tick — second F bar */}
          <line x1="29" y1="33.5" x2="34" y2="33.5" stroke="url(#ofx-g2)" strokeWidth="1.6" strokeLinecap="round" />
        </g>

        {/* diagonal exchange slash */}
        <line
          x1="14" y1="50" x2="50" y2="14"
          stroke="url(#ofx-g)"
          strokeWidth="1"
          opacity="0.35"
          strokeDasharray="1.5 2.5"
        />
      </svg>
    </span>
  );
}

export function Logo({ size = "md", showWordmark = true, asLink = true, className = "" }: Props) {
  const s = sizes[size];

  const wordmark = (
    <>
      {/* Mobile / compact: stacked, tightly engineered */}
      <span className="flex flex-col leading-[0.95] sm:hidden">
        <span className={`font-black tracking-[-0.02em] ${s.title}`}>
          <span className="bg-gradient-to-r from-primary via-emerald-400 to-amber-300 bg-clip-text text-transparent">
            Orji
          </span>
          <span className="text-foreground">/FX</span>
        </span>
        <span className={`mt-0.5 ${s.sub} uppercase text-muted-foreground/70`}>
          Funds · Exchange
        </span>
      </span>

      {/* Desktop: full wordmark */}
      <span className="hidden sm:flex flex-col leading-none">
        <span className={`font-semibold tracking-tight ${s.title}`}>
          <span className="bg-gradient-to-r from-foreground to-foreground/70 bg-clip-text text-transparent">
            Orji
          </span>{" "}
          <span className="italic font-light text-muted-foreground">funds</span>{" "}
          <span className="bg-gradient-to-r from-primary via-emerald-400 to-amber-300 bg-clip-text text-transparent">
            Exchange
          </span>
        </span>
        <span className={`mt-1 ${s.sub} uppercase text-muted-foreground/70`}>
          Naira · Crypto · Settled
        </span>
      </span>
    </>
  );

  const inner = (
    <>
      <Mark px={s.box} />
      {showWordmark && wordmark}
    </>
  );

  if (!asLink) {
    return (
      <span className={`inline-flex items-center gap-2.5 ${className}`}>
        {inner}
      </span>
    );
  }

  return (
    <Link
      to="/"
      className={`inline-flex items-center gap-2.5 group ${className}`}
      aria-label="Orji Funds Exchange — home"
    >
      {inner}
    </Link>
  );
}
