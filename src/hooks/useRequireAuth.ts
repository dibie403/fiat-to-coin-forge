import { useEffect } from "react";
import { useNavigate } from "@tanstack/react-router";
import { useAuth } from "@/context/AuthContext";

export function useRequireAuth(opts: { adminOnly?: boolean } = {}) {
  const { isAuthenticated, isAdmin, loading } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (loading) return;
    if (!isAuthenticated) {
      navigate({ to: "/login" });
      return;
    }
    if (opts.adminOnly && !isAdmin) {
      navigate({ to: "/dashboard" });
    }
  }, [isAuthenticated, isAdmin, loading, opts.adminOnly, navigate]);

  return { ready: !loading && isAuthenticated && (!opts.adminOnly || isAdmin) };
}
