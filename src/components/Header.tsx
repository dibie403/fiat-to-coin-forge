import { Link, useRouter } from "@tanstack/react-router";
import { Moon, Sun, LogOut, LayoutDashboard, Shield } from "lucide-react";
import { useEffect, useState } from "react";
import { useAuth } from "@/context/AuthContext";
import { Button } from "@/components/ui/button";

export function Header() {
  const { isAuthenticated, isAdmin, user, logout } = useAuth();
  const router = useRouter();
  const [dark, setDark] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem("brokr.theme");
    const isDark = saved ? saved === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    setDark(isDark);
    document.documentElement.classList.toggle("dark", isDark);
  }, []);

  const toggleTheme = () => {
    const next = !dark;
    setDark(next);
    document.documentElement.classList.toggle("dark", next);
    localStorage.setItem("brokr.theme", next ? "dark" : "light");
  };

  const handleLogout = () => {
    logout();
    router.navigate({ to: "/" });
  };

  return (
    <header className="sticky top-0 z-40 w-full border-b border-border/60 bg-background/80 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-4">
        <Link to="/" className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-primary-foreground font-bold">
            B
          </div>
          <span className="text-lg font-semibold tracking-tight">Brokr</span>
        </Link>

        <nav className="hidden md:flex items-center gap-1 text-sm">
          {isAuthenticated && (
            <>
              <Link
                to="/dashboard"
                className="px-3 py-2 rounded-md text-muted-foreground hover:text-foreground hover:bg-accent"
                activeProps={{ className: "px-3 py-2 rounded-md text-foreground bg-accent" }}
              >
                Dashboard
              </Link>
              <Link
                to="/buy"
                className="px-3 py-2 rounded-md text-muted-foreground hover:text-foreground hover:bg-accent"
                activeProps={{ className: "px-3 py-2 rounded-md text-foreground bg-accent" }}
              >
                Buy
              </Link>
              <Link
                to="/sell"
                className="px-3 py-2 rounded-md text-muted-foreground hover:text-foreground hover:bg-accent"
                activeProps={{ className: "px-3 py-2 rounded-md text-foreground bg-accent" }}
              >
                Sell
              </Link>
              {isAdmin && (
                <Link
                  to="/admin"
                  className="px-3 py-2 rounded-md text-muted-foreground hover:text-foreground hover:bg-accent flex items-center gap-1"
                  activeProps={{ className: "px-3 py-2 rounded-md text-foreground bg-accent flex items-center gap-1" }}
                >
                  <Shield className="h-3.5 w-3.5" /> Admin
                </Link>
              )}
            </>
          )}
        </nav>

        <div className="flex items-center gap-2">
          <Button variant="ghost" size="icon" onClick={toggleTheme} aria-label="Toggle theme">
            {dark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </Button>
          {isAuthenticated ? (
            <>
              <span className="hidden sm:inline text-sm text-muted-foreground">
                {user?.name}
              </span>
              <Button variant="outline" size="sm" onClick={handleLogout}>
                <LogOut className="h-4 w-4 mr-1" /> Logout
              </Button>
            </>
          ) : (
            <>
              <Link to="/login">
                <Button variant="ghost" size="sm">Login</Button>
              </Link>
              <Link to="/register">
                <Button size="sm">
                  <LayoutDashboard className="h-4 w-4 mr-1" /> Get started
                </Button>
              </Link>
            </>
          )}
        </div>
      </div>
    </header>
  );
}
