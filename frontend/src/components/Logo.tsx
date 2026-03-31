type LogoSize = "xs" | "sm" | "md" | "lg";

const sizeClassMap: Record<LogoSize, string> = {
  xs: "logo-xs",
  sm: "logo-sm",
  md: "logo-md",
  lg: "logo-lg",
};

interface LogoProps {
  size?: LogoSize;
  markOnly?: boolean;
}

export function Logo({ size = "md", markOnly = false }: LogoProps) {
  const src = markOnly ? "/logos/arllyai-icon.svg" : "/logos/arllyai-logo.svg";
  const alt = markOnly ? "Arlly.ai icon" : "Arlly.ai logo";

  return <img className={sizeClassMap[size]} src={src} alt={alt} />;
}
