import { useEffect, useState } from "react";

/** Returns true once the component has mounted on the client.
 *  Prevents pre-hydration form submits doing a native GET. */
export function useHydrated() {
  const [hydrated, setHydrated] = useState(false);
  useEffect(() => setHydrated(true), []);
  return hydrated;
}
