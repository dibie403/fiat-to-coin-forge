import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from "react";
import {
  getSession,
  loginUser as apiLogin,
  logout as apiLogout,
  registerUser as apiRegister,
} from "@/services/api";
import type { User } from "@/services/mockData";

type SafeUser = Omit<User, "password">;

interface AuthState {
  user: SafeUser | null;
  token: string | null;
  isAuthenticated: boolean;
  isAdmin: boolean;
  loading: boolean;
  login: (email: string, password: string) => Promise<SafeUser>;
  register: (name: string, email: string, password: string) => Promise<SafeUser>;
  logout: () => void;
}

const AuthContext = createContext<AuthState | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<SafeUser | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const s = getSession();
    if (s) {
      setUser(s.user);
      setToken(s.token);
    }
    setLoading(false);
  }, []);

  const login = useCallback(async (email: string, password: string) => {
    const r = await apiLogin({ email, password });
    setUser(r.user);
    setToken(r.token);
    return r.user;
  }, []);

  const register = useCallback(async (name: string, email: string, password: string) => {
    const r = await apiRegister({ name, email, password });
    setUser(r.user);
    setToken(r.token);
    return r.user;
  }, []);

  const logout = useCallback(() => {
    apiLogout();
    setUser(null);
    setToken(null);
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        isAuthenticated: !!user,
        isAdmin: user?.role === "admin",
        loading,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}
